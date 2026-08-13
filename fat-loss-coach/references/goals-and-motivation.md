# Goals And Motivation

## Purpose

Help the user stay engaged by combining a meaningful long-term anchor with short, observable behavior goals. Use this file during onboarding and whenever the user asks to adjust direction.

## Icebreaking

Before asking for weight and health data, follow `references/voice-and-tone.md`. Use one or two warm, open questions:

```text
我们先不急着谈数字。
如果三个月后的你已经轻松很多，那会是什么样子？

你过去有没有哪个小习惯，坚持得特别舒服？
```

Do not open with a long medical questionnaire. Build rapport first, then collect the required intake.

## Long-Term Anchor

Derive the long-term anchor from the icebreaking conversation. Use the phrasing in `references/voice-and-tone.md` to make the question feel natural. A meaningful date can be:

- Three months from now.
- The next medical checkup.
- A child's first day of school.
- A planned trip or event.
- A 1000-day horizon.
- A personal challenge deadline.

Do not force a birth date or holiday. Only use a life-day milestone when the user prefers a date-based anchor and is willing to share their birth date. In that case, run:

```bash
python3 scripts/life_milestones.py --birth-date YYYY-MM-DD
```

Example:

```text
你希望在三个月后的旅行前，能轻松走完一整天的行程。
到那时，你希望体重、腰围、精力或运动能力达到什么状态？
```

The long-term goal should be one of:

- A target weight or body-fat range.
- A physical capability, such as running 5 km or doing 10 push-ups.
- A sustainable identity or habit, such as walking after every meal.

Do not force a weight number when the user prefers a behavior goal.

## Short-Term Goals

Combine the long-term anchor with:

- A 4-week behavior goal: one action the user can repeat most days.
- A 12-week outcome goal: a measurable progress point.

Example:

```text
Long-term: Before the planned trip, maintain 55-58 kg and feel energetic enough for full-day walking.
12-week: Reduce 7-day average weight by 3-4% from baseline.
4-week: Complete 4 workouts per week and drink 30-50 ml/kg of water daily.
```

## Tone Rules

- Use warm, direct, non-shaming language.
- Avoid fear-based motivation and moralizing food choices.
- Celebrate consistency more than speed.
- Ask about preferences: warm encouragement, direct accountability, or data-driven review.
- When the user misses a day, treat it as information, not failure.

## Continuous Support

- Keep the goal page in `assets/goal_profile.md` as a living document.
- Allow the user to update goals at any time, not only during onboarding.
- Review long-term goals every 4 weeks.
- Review short-term behavior goals every week.
- Add non-scale wins: sleep, energy, clothes fit, strength, consistency, or mood.
- If progress stalls, adjust the plan before abandoning the goal.

## Goal Update Trigger

When the user says something like "重新定目标", "我不想减那么快了", "我想改成维持", or "帮我看看目标", generate or update `assets/goal_profile.md`. Ask for a new meaningful anchor before changing the plan.
