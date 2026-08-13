# Exercise Library

## Recommended Source

Use [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) as the primary action library:

- 1,324 exercises.
- Each exercise has a 180x180 GIF and thumbnail.
- Instructions are available in 10 languages, including Chinese.
- Body-part, equipment, target, and muscle-group fields are included.
- Raw dataset: `https://raw.githubusercontent.com/hasaneyldrm/exercises-dataset/main/data/exercises.json`.

To display an image or GIF, prefix the returned `image` or `gif_url` path with:

```text
https://raw.githubusercontent.com/hasaneyldrm/exercises-dataset/main/
```

Include the media attribution required by that repository when embedding images in a user-facing product.

For a public-domain fallback without media attribution requirements, use [yuhonas/free-exercise-db](https://github.com/yuhonas/free-exercise-db).

## Filtering Rules

When selecting from the dataset:

1. Match `equipment` to `home`, `gym`, or `both`.
2. Prefer `body weight`, `dumbbell`, `band`, and `barbell` for simple programs.
3. Prefer `compound` movements for time-efficient fat-loss programs.
4. Include shoulder and back work even when a user only asks for a generic full-body plan.
5. Use the Chinese instruction field when the user is Chinese-speaking.

## Curated Split

### Push

- Home: incline push-up, push-up, pike push-up, chair dip.
- Gym: dumbbell bench press, shoulder press, cable crossover, triceps extension.

### Pull

- Home: doorway row, band row, superman, reverse snow angel.
- Gym: lat pulldown, seated row, face pull, dumbbell row, biceps curl.

### Legs

- Home: bodyweight squat, split squat, glute bridge, calf raise.
- Gym: goblet squat, leg press, Romanian deadlift, lunge, calf raise.

## Posture And Face Work

- Chin tuck.
- Wall slide.
- Band pull-apart.
- Neck and jaw relaxation.
- Tongue posture awareness.

Frame face work as supportive muscle and posture training, not a promise of skin tightening.
