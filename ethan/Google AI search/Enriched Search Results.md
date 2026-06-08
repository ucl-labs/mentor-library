# Enriched and Interactive Search Results

Source: https://developers.google.com/search/docs/appearance/enriched-search-results

## Overview

Enriched search results represent an enhanced category of rich results supported by Google Search. These results feature immersive experiences and advanced interactive capabilities beyond standard rich results. For instance, a Jobs enriched result might allow users to filter opportunities by location within the United States.

## Key Capabilities

"Enriched search enables the user to search across the various properties of a structured data item; for example, a user might search for chicken soup recipes under 200 calories, or recipes that take less than 1 hour of preparation time."

## Implementation Requirements

Enriched search relies on structured data implementation. Implementation requires:

- Correct structured data markup on pages
- Adherence to quality guidelines including structured data policies, Search Essentials, and enriched search-specific guidelines

## Supported Types

Three primary content types support enriched search experiences:

- Job Posting
- Recipe
- Event

## Quality Guidelines

Sites must maintain standards across several dimensions:

- **Required Properties**: Each enriched type specifies mandatory properties; items lacking these are ineligible
- **Completeness**: Additional recommended properties improve ranking, particularly salary information for jobs or genuine reviews for recipes
- **Relevance**: Marked-up data must align with the enriched search category
- **Leaf Content**: Only detailed item pages qualify, excluding category or listing pages
- **Content Policies**: Type-specific policies apply; violations may reduce ranking or remove eligibility

The system notes: "Structured data is typically duplicated across many pages within a site, and for good reason."
