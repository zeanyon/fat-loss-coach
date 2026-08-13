#!/usr/bin/env python3
"""Calculate a conservative metabolic and fat-loss starting plan."""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import asdict, dataclass


@dataclass
class MetabolicPlan:
    bmr: float
    tdee: float
    bmi: float
    target_intake: float
    carbs_g: float
    protein_g: float
    fat_g: float
    body_fat_pct: float | None
    lean_body_mass_kg: float | None
    protein_basis: str
    weekly_loss_kg: float | None
    estimated_weeks: float | None
    warnings: list[str]


def calculate_bmr(
    sex: str,
    weight_kg: float,
    height_cm: float,
    age: int,
    formula: str,
) -> float:
    if formula == "mifflin":
        if sex == "male":
            return 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
        return 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    if sex == "male":
        return 66 + 13.7 * weight_kg + 5 * height_cm - 6.8 * age
    return 655 + 9.6 * weight_kg + 1.8 * height_cm - 4.7 * age


def estimate_body_fat_pct(
    sex: str,
    height_cm: float,
    waist_cm: float | None,
    neck_cm: float | None,
    hip_cm: float | None,
) -> float | None:
    if not height_cm or not waist_cm or not neck_cm:
        return None
    if sex == "male":
        denominator = 1.0324 - 0.19077 * math.log10(waist_cm - neck_cm) + 0.15456 * math.log10(height_cm)
        body_fat = 495 / denominator - 450
    else:
        if not hip_cm:
            return None
        denominator = 1.29579 - 0.35004 * math.log10(waist_cm + hip_cm - neck_cm) + 0.22100 * math.log10(height_cm)
        body_fat = 495 / denominator - 450
    return min(60.0, max(3.0, body_fat))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sex", choices=["male", "female"], required=True)
    parser.add_argument("--age", type=int, required=True)
    parser.add_argument("--height-cm", type=float, required=True)
    parser.add_argument("--weight-kg", type=float, required=True)
    parser.add_argument("--activity", type=float, default=1.375)
    parser.add_argument("--extra-activity", type=float, default=0.0)
    parser.add_argument("--goal", choices=["fat_loss", "maintain"], default="fat_loss")
    parser.add_argument("--target-kg", type=float)
    parser.add_argument("--formula", choices=["harris", "mifflin"], default="harris")
    parser.add_argument("--body-fat-pct", type=float)
    parser.add_argument("--waist-cm", type=float)
    parser.add_argument("--neck-cm", type=float)
    parser.add_argument("--hip-cm", type=float)
    parser.add_argument("--deficit", type=float, default=500.0)
    parser.add_argument("--carb-ratio", type=float, default=0.4)
    parser.add_argument("--protein-ratio", type=float, default=0.3)
    parser.add_argument("--fat-ratio", type=float, default=0.3)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    warnings: list[str] = []

    if args.age < 18:
        warnings.append("Age under 18 requires professional supervision.")

    if args.weight_kg <= 0 or args.height_cm <= 0:
        print("Weight and height must be positive.", file=sys.stderr)
        return 2

    ratio_sum = args.carb_ratio + args.protein_ratio + args.fat_ratio
    if abs(ratio_sum - 1.0) > 0.001:
        warnings.append(f"Macro ratios sum to {ratio_sum:.3f}, not 1.0.")

    bmr = calculate_bmr(
        args.sex,
        args.weight_kg,
        args.height_cm,
        args.age,
        args.formula,
    )
    tdee = bmr * args.activity + args.extra_activity
    bmi = args.weight_kg / args.height_cm / args.height_cm * 10000

    if args.goal == "fat_loss":
        target_intake = max(tdee - args.deficit, bmr)
    else:
        target_intake = tdee

    body_fat_pct = args.body_fat_pct
    if body_fat_pct is None:
        body_fat_pct = estimate_body_fat_pct(
            args.sex,
            args.height_cm,
            args.waist_cm,
            args.neck_cm,
            args.hip_cm,
        )
        if body_fat_pct is not None:
            warnings.append("Body-fat percentage was estimated from circumference measurements.")

    lean_body_mass_kg: float | None = None
    protein_basis = "ratio"

    if body_fat_pct is not None:
        body_fat_pct = min(60.0, max(3.0, body_fat_pct))
        lean_body_mass_kg = args.weight_kg * (1 - body_fat_pct / 100)
        lbm_protein = 2.0 * lean_body_mass_kg
        lbm_fat = 0.75 * lean_body_mass_kg
        ratio_protein = target_intake * args.protein_ratio / 4
        ratio_fat = target_intake * args.fat_ratio / 9
        protein_g = max(ratio_protein, lbm_protein)
        fat_g = max(ratio_fat, lbm_fat)
        protein_calories = protein_g * 4
        fat_calories = fat_g * 9
        if protein_calories + fat_calories > target_intake:
            scale = target_intake / (protein_calories + fat_calories)
            protein_g *= scale
            fat_g *= scale
        carbs_g = max(0.0, (target_intake - protein_g * 4 - fat_g * 9) / 4)
        protein_basis = "lean_body_mass"
    else:
        carbs_g = target_intake * args.carb_ratio / 4
        protein_g = target_intake * args.protein_ratio / 4
        fat_g = target_intake * args.fat_ratio / 9

    weekly_loss_kg: float | None = None
    estimated_weeks: float | None = None

    if args.goal == "fat_loss" and args.target_kg:
        if args.target_kg >= args.weight_kg:
            warnings.append("Target weight is not below current weight.")
        else:
            weekly_loss_kg = args.weight_kg * 0.0075
            estimated_weeks = (args.weight_kg - args.target_kg) / weekly_loss_kg
            if weekly_loss_kg / args.weight_kg > 0.01:
                warnings.append("Weekly pace exceeds 1% of body weight.")

    if bmi < 18.5:
        warnings.append("BMI is below 18.5; weight loss is not appropriate.")
    if args.deficit > 1000:
        warnings.append("Deficit exceeds 1000 kcal; consider a more conservative plan.")
    if args.target_kg and bmi >= 30:
        warnings.append("Large-body aerobic work should start with low-impact movement.")

    plan = MetabolicPlan(
        bmr=round(bmr, 1),
        tdee=round(tdee, 1),
        bmi=round(bmi, 2),
        target_intake=round(target_intake, 1),
        carbs_g=round(carbs_g, 1),
        protein_g=round(protein_g, 1),
        fat_g=round(fat_g, 1),
        body_fat_pct=round(body_fat_pct, 1) if body_fat_pct is not None else None,
        lean_body_mass_kg=round(lean_body_mass_kg, 1) if lean_body_mass_kg is not None else None,
        protein_basis=protein_basis,
        weekly_loss_kg=round(weekly_loss_kg, 3) if weekly_loss_kg is not None else None,
        estimated_weeks=round(estimated_weeks, 1) if estimated_weeks is not None else None,
        warnings=warnings,
    )

    print(json.dumps(asdict(plan), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
