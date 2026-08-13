# Safety And Boundaries

## Purpose

Use this file before generating any weight-loss or training plan. The goal is to avoid turning personal experience into medical advice.

## Refer Out Immediately

Stop coaching and recommend a licensed professional when any of these are present:

- Pregnancy or breastfeeding.
- Age under 18.
- BMI below 18.5 or active unintended weight loss.
- Current or past eating disorder.
- Type 1 diabetes, advanced type 2 diabetes, kidney disease, liver disease, heart disease, or unstable blood pressure.
- Medication that affects appetite, blood sugar, electrolytes, or heart rate.
- Recent surgery, unexplained pain, or injury that limits movement.
- Rapid weight change without a known cause.

Do not attempt to manage these conditions with a generic plan.

## Default Safety Parameters

- Weekly weight loss: `0.5%` to `1%` of current body weight.
- Daily calorie intake: do not routinely place below `TDEE - 1000 kcal`; when uncertain, use `TDEE - 300 to 500 kcal`.
- Protein: default `1.2-2.0 g/kg` for most adults; use the lower end when kidney concerns exist.
- Aerobic heart rate: never prescribe a fixed `140-160` range without checking age, resting heart rate, and known cardiovascular risk.
- Fasting: default to `16:8` or `18:6`; avoid for people with hypoglycemia, eating-disorder history, pregnancy, or high-stress occupations without medical clearance.

## Founder Case Boundary

The founder's reported result of losing about 50 kg in 6 months is a positioning story only. It is not:

- A default goal.
- A safe weekly pace.
- Evidence that a user should copy the same speed.

Always present it as context, never as a prescription.

## Supplement Boundary

Glucosamine after exercise and aloe capsules for constipation may be mentioned only as optional personal experience. Add a warning to consult a professional and to prioritize food, water, fiber, and movement first.

## Communication Rules

- Use non-shaming, behavior-focused language.
- Do not promise fixed results or use before/after guarantees.
- Do not diagnose.
- When a plan cannot be safely generated, say so and recommend appropriate care.

## Decision Tree

Use this order when screening:

1. Is the person under 18, pregnant, breastfeeding, or managing a serious medical condition?
   - Yes -> Refer out. Do not generate a plan.
   - No -> Continue.

2. Is there an eating-disorder history, rapid unexplained weight change, or BMI below 18.5?
   - Yes -> Refer out. Do not generate a weight-loss plan.
   - No -> Continue.

3. Are there joint symptoms, pain, dizziness, fainting, or recent surgery?
   - Yes -> Reduce movement impact and require professional clearance before intense training.
   - No -> Continue.

4. Is the requested weekly loss above 1% of body weight?
   - Yes -> Refuse the faster pace. Offer the safe range.
   - No -> Continue.

5. Does the user want fasting, supplements, or a very low-calorie target?
   - Yes -> Apply stricter screening and flag that these are optional, not required.
   - No -> Continue.

   If a liquid reset is requested, require the same screening and default to one day only. See `references/plateau-and-liquid-reset.md`.

6. Is BMI >= 30 or are there weight-related joint concerns?
   - Yes -> Start with low-impact aerobic work.
   - No -> Running, jump rope, or swimming may be considered.

Only after all gates pass, generate the metabolic and training plan.
