# Recipe Schema Markup

Source: https://developers.google.com/search/docs/appearance/structured-data/recipe

Implement Recipe structured data to help your recipe content appear in search results and Google Images. By marking up recipes with schema.org `Recipe` type properties, you enable features like rich results, carousels, and enhanced search appearance.

## Required Properties

- **`image`**: "Image of the completed dish" (supports multiple high-resolution images with 16x9, 4x3, and 1x1 aspect ratios)
- **`name`**: "The name of the dish"

## Recommended Properties

- `aggregateRating` for review scores
- `author` (Person or Organization)
- `cookTime` and `prepTime` (ISO 8601 format)
- `recipeIngredient` and `recipeInstructions`
- `nutrition.calories` (requires `recipeYield`)
- `video` for instructional videos

## Recipe Instructions Structure

Three formatting options:
1. **`HowToStep`** (recommended): Individual steps with optional images and URLs
2. **`HowToSection`**: Groups of steps for complex recipes
3. **Text blocks**: Single text passages Google attempts to split

## Carousel Eligibility

To enable recipe carousels, provide `ItemList` structured data on summary pages listing multiple recipes, with required `position` and `url` properties for each item.

## Guidelines Compliance

Content must represent actual dishes (not "facial scrub" or abstract concepts), use proper time formats, and avoid mixing recipe metadata with instruction text.
