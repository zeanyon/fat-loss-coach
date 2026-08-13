# Automation And Daily Scheduling

## Goal

Run one daily check-in around the user's normal wake time. The check-in should read existing tracking data, ask for the latest values, append them with `scripts/track.py`, and return a short trend summary plus one realistic action.

## Trigger

Use the host agent's native scheduler. For Codex, use its automation mechanism. For other agents, use a cron job or platform scheduler that can execute:

```bash
python3 scripts/track.py summary tracking.json
```

Then ask the user to provide today's values and append them.

## Daily Prompt

Use this prompt shape:

```text
Good morning. Reply with today's:

- Weight (kg)
- Body-fat percentage (optional)
- Waist (cm, optional)
- Neck (cm, optional)
- Sleep hours
- Water intake (ml)
- Fasting window followed
- Steps and training minutes
- Energy, hunger, mood, and pain scores

Keep it short. After I reply, summarize the 7-day trend and give one specific action for today.
```

## Append Command

After collecting values, run:

```bash
python3 scripts/track.py append tracking.json \
  --date YYYY-MM-DD \
  --weight-kg 59.2 \
  --body-fat-pct 21.6 \
  --sleep-hours 7.5 \
  --training-minutes 45 \
  --notes "today note"
```

## Response Rules

- Compare the latest record with the 7-day average.
- Ignore single-day swings under about 0.5-2 kg.
- If weight stalls for 7-14 days, check sleep, water, protein, and tracking accuracy before recommending fewer calories.
- Celebrate behavior consistency, not only scale change.
- If pain, dizziness, fainting, or severe fatigue appears, stop coaching and recommend professional care.

## Cross-Agent Cron Example

For a generic Unix cron:

```cron
30 7 * * * /usr/bin/env python3 /path/to/fat-loss-coach/scripts/track.py summary /path/to/tracking.json
```

The host agent can then use the output as context for its morning prompt.
