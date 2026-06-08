# Introduction to Structured Data Markup in Google Search

Source: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data

Structured data is a standardized format for providing explicit information about page content to Google Search. By adding structured data, website owners help Google understand their content better and enable "rich results" - more visually engaging search results that encourage user interaction.

## Why Add Structured Data?

Implementing structured data can significantly improve search performance:

- Rotten Tomatoes measured "a 25% higher click-through rate for pages enhanced with structured data"
- Food Network converted 80% of pages and saw a 35% increase in visits
- Rakuten found users spent 1.5x more time on structured data pages
- Nestlé measured "an 82% higher click through rate than non-rich result pages"

## How Structured Data Works

Google uses structured data to understand page content and gather information about entities mentioned in the markup (people, books, companies, etc.). For example, JSON-LD markup on a recipe page allows Google to display enhanced results where users can search by ingredient, calories, or cook time.

**Important guideline:** Structured data should describe visible page content only. Creating blank pages solely to hold structured data, or marking up invisible information, violates best practices.

## Supported Formats

Google supports three formats equally well:

1. **JSON-LD (Recommended)** - JavaScript notation in `<script>` tags, easiest to maintain at scale
2. **Microdata** - HTML specification using tag attributes
3. **RDFa** - HTML5 extension using tag attributes for linked data

## Getting Started

- The Rich Results Test tool for validation
- Schema.org beginner's guide for foundational concepts
- Google's feature-specific implementation guides
- URL Inspection tool to verify Google finds your markup

## Measuring Impact

1. Select established pages without structured data
2. Add structured data and confirm validity
3. Monitor performance metrics in Search Console's Performance report over several months
