#!/usr/bin/env python3
"""Manage a cross-agent JSON tracking file for fat-loss daily check-ins."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import date
from pathlib import Path


FIELDS = [
    "weight_kg",
    "body_fat_pct",
    "waist_cm",
    "neck_cm",
    "sleep_hours",
    "water_ml",
    "fasting_window_hours",
    "steps",
    "training_minutes",
    "protein_g",
    "calories",
    "energy",
    "hunger",
    "mood",
    "pain",
]


def load(path: Path) -> dict:
    if path.exists():
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
        if not isinstance(data, dict):
            raise ValueError("Tracking file must contain a JSON object.")
        data.setdefault("records", [])
        data.setdefault("user", {})
        return data
    return {"schema_version": "1.0", "user": {}, "records": []}


def save(path: Path, data: dict) -> None:
    data["records"].sort(key=lambda record: record.get("date", ""))
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def init_tracking(args: argparse.Namespace) -> int:
    path = Path(args.path)
    if path.exists() and path.stat().st_size > 0:
        print(f"Already exists: {path}")
        return 1
    user = {}
    for key, value in {
        "age": args.age,
        "sex": args.sex,
        "height_cm": args.height_cm,
        "initial_weight_kg": args.initial_weight_kg,
        "target_weight_kg": args.target_weight_kg,
    }.items():
        if value is not None:
            user[key] = value
    data = {"schema_version": "1.0", "user": user, "records": []}
    save(path, data)
    print(json.dumps(data, ensure_ascii=False, indent=2))
    return 0


def append_record(args: argparse.Namespace) -> int:
    path = Path(args.path)
    data = load(path)
    record_date = args.date or date.today().isoformat()
    if args.weight_kg is None:
        print("--weight-kg is required.", file=sys.stderr)
        return 2

    record = {"date": record_date, "weight_kg": args.weight_kg, "notes": args.notes or ""}
    for field in FIELDS:
        value = getattr(args, field.replace("-", "_"))
        if value is not None:
            record[field] = value

    data["records"] = [item for item in data["records"] if item.get("date") != record_date]
    data["records"].append(record)
    save(path, data)
    print(json.dumps(record, ensure_ascii=False, indent=2))
    return 0


def summary(path: Path) -> int:
    data = load(path)
    records = sorted(data["records"], key=lambda item: item.get("date", ""))
    if not records:
        print("No records.")
        return 0

    latest = records[-1]
    first = records[0]
    weights = [record.get("weight_kg") for record in records if record.get("weight_kg") is not None]
    last_seven = [record.get("weight_kg") for record in records[-7:] if record.get("weight_kg") is not None]
    avg = sum(last_seven) / len(last_seven) if last_seven else None
    change = (latest.get("weight_kg") or 0) - (first.get("weight_kg") or 0) if weights else None

    print(json.dumps(
        {
            "records": len(records),
            "latest": latest,
            "change_kg": round(change, 1) if change is not None else None,
            "seven_day_avg_kg": round(avg, 1) if avg is not None else None,
        },
        ensure_ascii=False,
        indent=2,
    ))
    return 0


def export_csv(args: argparse.Namespace) -> int:
    source = Path(args.path)
    destination = Path(args.output)
    data = load(source)
    headers = ["date", *FIELDS, "notes"]
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        for record in sorted(data["records"], key=lambda item: item.get("date", "")):
            writer.writerow({field: record.get(field, "") for field in headers})
    print(destination)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Create a new tracking file.")
    init_parser.add_argument("path")
    init_parser.add_argument("--age", type=int)
    init_parser.add_argument("--sex", choices=["male", "female"])
    init_parser.add_argument("--height-cm", type=float)
    init_parser.add_argument("--initial-weight-kg", type=float)
    init_parser.add_argument("--target-weight-kg", type=float)
    init_parser.set_defaults(func=init_tracking)

    append_parser = subparsers.add_parser("append", help="Append or replace a daily record.")
    append_parser.add_argument("path")
    append_parser.add_argument("--date")
    append_parser.add_argument("--weight-kg", type=float)
    append_parser.add_argument("--body-fat-pct", type=float)
    append_parser.add_argument("--waist-cm", type=float)
    append_parser.add_argument("--neck-cm", type=float)
    append_parser.add_argument("--sleep-hours", type=float)
    append_parser.add_argument("--water-ml", type=float)
    append_parser.add_argument("--fasting-window-hours", type=float)
    append_parser.add_argument("--steps", type=float)
    append_parser.add_argument("--training-minutes", type=float)
    append_parser.add_argument("--protein-g", type=float)
    append_parser.add_argument("--calories", type=float)
    append_parser.add_argument("--energy", type=float)
    append_parser.add_argument("--hunger", type=float)
    append_parser.add_argument("--mood", type=float)
    append_parser.add_argument("--pain", type=float)
    append_parser.add_argument("--notes")
    append_parser.set_defaults(func=append_record)

    summary_parser = subparsers.add_parser("summary", help="Print a compact summary.")
    summary_parser.add_argument("path")
    summary_parser.set_defaults(func=lambda args: summary(Path(args.path)))

    export_parser = subparsers.add_parser("export-csv", help="Export records to CSV.")
    export_parser.add_argument("path")
    export_parser.add_argument("output")
    export_parser.set_defaults(func=export_csv)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
