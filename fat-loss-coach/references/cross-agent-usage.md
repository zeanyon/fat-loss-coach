# Cross-Agent Usage

This skill is written as platform-neutral Markdown, JSON, Python, and HTML. Any agent that can read local files and run Python can use it.

## Generic System Prompt

```text
You are a sustainable fat-loss coach. Read /absolute/path/to/fat-loss-coach/SKILL.md first.
Before generating a plan, read references/safety-and-boundaries.md and apply its decision tree.
Read references/voice-and-tone.md and use a warm, conversational, non-judgmental style.
Use scripts/metabolic_plan.py for calculations and scripts/track.py for daily tracking.
Keep output practical, budget-aware, and non-medical.
```

## Codex

Reference the skill by name or path:

```text
Use $fat-loss-coach to create my personalized sustainable fat-loss plan.
```

For scheduled follow-up, follow `references/automation.md` and use the host's native automation mechanism.

## ChatGPT Or Claude

Upload or point the agent at the skill folder, then say:

```text
Read the fat-loss-coach skill in this folder.
My age is 30, height 170 cm, weight 80 kg, and I want a home fat-loss plan.
Ask me the required onboarding questions, then generate a first plan.
```

## Cursor Or Local CLI

Ask the agent to run:

```bash
python3 scripts/metabolic_plan.py \
  --sex male \
  --age 30 \
  --height-cm 170 \
  --weight-kg 80 \
  --activity 1.375 \
  --goal fat_loss
```

Then use the JSON output as plan input.

## Shared Tracking Contract

All agents should use `assets/tracking-schema.json`. Append records with:

```bash
python3 scripts/track.py append tracking.json --date 2026-08-14 --weight-kg 79.4
```

Open `assets/dashboard.html` in a browser to view the same records without an API.
