# Habits And Followup

## Sleep

- Aim for at least 7 hours.
- 7.5 hours is preferred.
- Target falling asleep by 24:00.
- Keep wake time stable.

Evening routine:

- Stop caffeine after early afternoon.
- Dim screens 30-60 minutes before bed.
- Keep the bedroom cool and dark.
- Use a consistent wind-down sequence.

## Morning Habits

- Drink one glass of water after waking.
- Aim for a daily water baseline of body weight in kg multiplied by 30-50 ml.
- Move for a few minutes or expose yourself to daylight.
- Record weight and sleep.

## Daily Check-In

Use `assets/daily_check_in.md`. Ask for:

- Morning weight and optional body-fat reading.
- Sleep hours and recovery score.
- Water intake.
- Fasting window adherence.
- Movement completed.
- Hunger, energy, mood, and pain.
- One action taken toward the long-term goal.

Interpret the 7-day trend, not a single day. Explain that weight changes from water, salt, glycogen, digestion, and stress.

## Structured Tracking

Use `assets/tracking-schema.json` as the canonical data shape. Each record stores:

- Date and required weight.
- Optional body-fat percentage, waist, and neck measurements.
- Sleep, water, fasting window, steps, and training minutes.
- Optional protein and calorie intake.
- Energy, hunger, mood, and pain scores.

Use `scripts/track.py` to initialize, append, summarize, and export CSV. Use `assets/dashboard.html` for a local browser dashboard with weight and body-fat trend charts. The dashboard can import and export the same JSON schema without a backend.

## Motivation Style

Each morning message should include:

- One realistic fat-loss tip.
- One short useful reminder or quote.
- One concrete daily task.

Keep it brief, specific, and non-exaggerated.

## Plateau And Rebound Rules

When progress stalls:

1. Check the 7-day average before changing the plan.
2. Verify sleep, water, protein, and movement.
3. Reduce carbohydrates slightly only if tracking is accurate and sleep is stable.
4. Avoid crash-cutting calories.

For plateau management and any liquid reset, read `references/plateau-and-liquid-reset.md`.

For maintenance:

- Keep protein and movement high.
- Add food back gradually.
- Continue weighing and tracking for at least a few weeks.
- Plan for high-risk situations such as travel, social meals, and stress.

When the user asks to review direction, update `assets/goal_profile.md` using `references/goals-and-motivation.md`.
