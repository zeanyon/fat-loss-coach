#!/usr/bin/env python3
"""Calculate life-day milestones for long-term fat-loss goal setting."""

from __future__ import annotations

import argparse
import json
from datetime import date, datetime, timedelta


MILESTONES = [10000, 12000, 15000, 20000]


def parse_date(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--birth-date", required=True, help="Birth date in YYYY-MM-DD.")
    parser.add_argument("--today", help="Reference date in YYYY-MM-DD. Defaults to today.")
    args = parser.parse_args()

    birth = parse_date(args.birth_date)
    today = parse_date(args.today) if args.today else date.today()
    if today < birth:
        print("Reference date cannot be before birth date.", file=__import__("sys").stderr)
        return 2

    days_alive = (today - birth).days + 1
    years_alive = days_alive / 365.25
    milestones = []
    next_milestone = None

    for day_number in MILESTONES:
        milestone_date = birth + timedelta(days=day_number - 1)
        remaining_days = (milestone_date - today).days
        milestones.append(
            {
                "day_number": day_number,
                "date": milestone_date.isoformat(),
                "remaining_days": remaining_days,
                "status": "upcoming" if remaining_days >= 0 else "passed",
            }
        )
        if remaining_days >= 0 and next_milestone is None:
            next_milestone = milestones[-1]

    print(
        json.dumps(
            {
                "birth_date": birth.isoformat(),
                "today": today.isoformat(),
                "days_alive": days_alive,
                "years_alive": round(years_alive, 2),
                "next_milestone": next_milestone,
                "milestones": milestones,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
