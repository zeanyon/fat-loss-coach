# Assessment And Planning

## Required Intake

Collect at least:

- Sex.
- Age in years.
- Height in centimeters.
- Current weight in kilograms.
- Activity level.
- Goal: fat loss, maintenance, or muscle gain.
- Target weight if relevant.
- Training environment: home, gym, or both.
- Daily available exercise minutes.
- Eating preferences, cooking ability, budget, and food access.
- Sleep and wake times.
- Medical red flags from `safety-and-boundaries.md`.

## Activity Factors

| Level | Description | Factor |
|---|---|---|
| Sedentary | Mostly sitting, little structured exercise | 1.2 |
| Lightly active | Light exercise 1-3 days per week | 1.375 |
| Moderately active | Moderate exercise 3-5 days per week | 1.55 |
| Very active | Hard exercise 6-7 days per week | 1.725 |

## Core Formulas

Use the script `scripts/metabolic_plan.py` for arithmetic. Keep the formulas visible when explaining a plan.

### BMR

```text
Male:   BMR = 66 + 13.7 * weight_kg + 5 * height_cm - 6.8 * age
Female: BMR = 655 + 9.6 * weight_kg + 1.8 * height_cm - 4.7 * age
```

### Formula Variants

Support `harris` by default and allow `mifflin` when the user prefers a more recent estimate:

```text
Mifflin-St Jeor male:   BMR = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
Mifflin-St Jeor female: BMR = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
```

If body-fat percentage is available, consider lean body mass later for protein and fat targets:

```text
lean_body_mass = weight_kg * (1 - body_fat_pct)
```

Do not ask for body-fat percentage as a hard requirement. Treat it as optional context.

`scripts/metabolic_plan.py` supports three ways to provide body composition:

```bash
--body-fat-pct 22
--waist-cm 78 --neck-cm 38
--waist-cm 75 --neck-cm 34 --hip-cm 95
```

When body-fat percentage is available, protein and fat are anchored to lean body mass:

```text
protein_g = max(ratio_protein, 2.0 * lean_body_mass_kg)
fat_g = max(ratio_fat, 0.75 * lean_body_mass_kg)
remaining calories -> carbohydrates
```

This avoids underfeeding protein for a muscular person or overfeeding fat for someone with higher body fat.

### BMI

```text
BMI = weight_kg / height_cm / height_cm * 10000
```

### TDEE

```text
TDEE = BMR * activity_factor + extra_activity_calories
```

The uploaded metabolic template does not use activity factor. Correct that behavior when producing a plan.

### Target Intake

```text
target_intake = TDEE - deficit
default_deficit = 300 to 500 kcal
```

Do not use BMR as the default intake. Keep intake above BMR unless a qualified professional has directed otherwise.

## Macro Ratios

Use these defaults:

| Goal | Carb | Protein | Fat |
|---|---|---|---|
| Fat loss | 40% | 30% | 30% |
| Balanced maintenance | 40% | 30% | 30% |
| Higher-carb performance | 50% | 30% | 20% |

The founder's original template uses `5:3:2` or `4:4:2`. Use the 30% protein default for most fat-loss plans, then adjust protein by body weight.

## Weight-Loss Pace

```text
monthly_loss = weight_kg * 0.03  # safe example, not a universal rule
weekly_loss = monthly_loss / 4
```

Default to `0.5%` to `1%` per week. The original `3%` per month calculation is acceptable for many people but is not a universal target.

## Plan Output

Generate:

1. A one-paragraph assessment summary.
2. BMR, TDEE, target intake, and macro ranges.
3. A 7-day food and fasting pattern.
4. A weekly movement schedule.
5. Sleep, water, and daily tracking defaults, including optional waist, neck, and body-fat fields.
6. A safety note.

Use `assets/weekly_plan.md` as the output skeleton.
