# Nutrition And Fasting

## Eating Principles

- Use a table to track daily intake. Track calories, protein, and one subjective hunger/satiety score.
- Build meals around meat, eggs, vegetables, and dairy.
- Strictly limit fried staples, pastries, sugary sauces, instant noodles with fried toppings, and other high-fat plus refined-carb combinations.
- Do not phrase foods as morally bad. Give replacements and portion anchors.

## 18:6 Fasting

Default to an 18-hour fast and a 6-hour eating window when the user is a healthy adult and wants fasting.

Offer these time-restricted variants only after screening:

| Method | Fasting | Eating window | Notes |
|---|---|---|---|
| 16:8 | 16 hours | 8 hours | Gentler starting point |
| 18:6 | 18 hours | 6 hours | Founder preference and default |
| 20:4 | 20 hours | 4 hours | Advanced; use with caution |
| 5:2 | Two low-calorie days per week | Normal eating on other days | Not for everyone |

Do not push 20:4 or 5:2 on beginners, people with a history of disordered eating, pregnancy, diabetes, or high physical job demands without professional clearance.

Example:

```text
Wake: 07:00
First meal: 12:00
Last meal: 18:00
Sleep: 23:30
```

In the eating window:

- Prioritize protein at the first meal.
- Include vegetables and a protein source at the last meal.
- Keep the window consistent.

During the fast:

- Water, black coffee, and unsweetened tea are acceptable.
- If genuinely hungry, use one protein bar or a small high-protein snack instead of breaking the plan with refined carbs.

### Protein Bar Criteria

Choose only when needed:

- Protein >= 15 g.
- Added sugar as low as possible, preferably <= 5 g.
- Not a meal replacement.
- Does not contain a long list of oils and syrups as the first ingredients.

## Meal Construction

Each main meal should include:

- Protein: palm-sized portion or about 25-40 g protein.
- Vegetables: 1-2 handfuls.
- Carb: a fist-sized portion when appropriate.
- Fat: 1 thumb-sized portion.

Use budget-friendly staples first:

| Category | Examples |
|---|---|
| Protein | Eggs, chicken breast, chicken thigh, lean pork, fish, tofu, milk, yogurt |
| Carbohydrates | Rice, oats, sweet potato, potato, whole-grain bread |
| Healthy fats | Olive oil, nuts, seeds, avocado |
| Vegetables and fruit | Cabbage, broccoli, leafy greens, tomato, cucumber, seasonal fruit |
| Snacks | Unsweetened yogurt, fruit, small nuts, protein bar if needed |

## Budget Shopping List

When generating a list:

1. Ask for weekly budget.
2. Choose whole foods over branded diet products.
3. Include frozen vegetables and canned fish only when fresh food is less accessible.
4. Separate the list into protein, carbohydrate, healthy fat, vegetables/fruit, and snacks.
5. Add portion guidance beside each category.

For canteen, takeout, and recipe generation from an allowed food range, read `references/meal-planning.md`.

## Water

Treat water as a required daily baseline, not an optional suggestion.

```text
daily_water_ml = body_weight_kg * 30 to 50
```

For example, a 60 kg person should target about 1800-3000 ml per day.

- Drink one glass on waking.
- Spread intake across the day instead of drinking a large amount at once.
- Increase the upper end when training, sweating heavily, or in hot weather.
- Do not apply extreme water targets to people with kidney or heart concerns; use professional guidance.

## Typical Day Pattern

Use this only as a flexible scaffold:

```text
12:00 First meal: protein + vegetables + moderate carb
15:00 Optional snack: fruit or yogurt
17:30 Last meal: protein + vegetables + small carb
18:00 Begin fasting
```
