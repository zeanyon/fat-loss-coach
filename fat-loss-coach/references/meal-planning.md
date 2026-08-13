# Meal Planning

## Canteen And Takeout Selection

Use this selection order:

1. Choose a protein source: lean meat, fish, eggs, tofu, or unsweetened dairy.
2. Add at least one vegetable.
3. Choose a plain staple: rice, potato, or whole grain.
4. Ask for sauce on the side or choose clear soups instead of thick sauces.
5. Avoid deep-fried meat, fried rice, fried noodles, sweet-and-sour sauces, and sugar-heavy drinks.

If only a mixed dish is available, remove or reduce the oily sauce and add an extra vegetable or protein when possible.

## Food Range To Recipe Suggestions

When the user provides an allowed food range, generate 3-5 recipe suggestions that:

- Use only foods from the allowed list.
- Match the user's macro targets.
- Use simple cooking methods: steam, boil, stir-fry with a small amount of oil, bake, or cold mix.
- Reuse ingredients across meals to reduce cost and waste.
- Include approximate portions, not only ingredient names.

Ask for these inputs before generating:

```text
Available proteins:
Available vegetables:
Available carbs:
Available fats and seasonings:
Cooking tools:
Meal budget:
```

## Recipe Template

For each suggestion:

```text
Meal:
Main ingredients and portions:
Cooking method:
Estimated protein:
Estimated carbohydrate:
Estimated fat:
Suitable for:
```

## Example

Given chicken breast, eggs, broccoli, tomato, rice, potato, olive oil, and salt:

1. Tomato egg stir-fry with rice.
2. Chicken breast and broccoli with rice.
3. Potato, egg, and vegetable soup.

Estimate portions by the palm, fist, and thumb method when exact scales are unavailable.
