# Dataset Structured Data

Source: https://developers.google.com/search/docs/appearance/structured-data/dataset

Datasets become more discoverable in Google's Dataset Search tool when publishers provide structured metadata. "Datasets are easier to find in the Dataset Search tool when you provide supporting information such as their name, description, creator and distribution formats as structured data."

## What Qualifies as a Dataset

- Tables or CSV files containing data
- Organized collections of tables
- Proprietary format files with data
- Collections of files forming meaningful datasets
- Structured objects in various formats
- Image files capturing data
- Machine learning-related files

## Key Schema Properties

**Required properties:**
- `name`: A descriptive dataset title
- `description`: A 50-5000 character summary

**Recommended properties:**
- `creator`: Person or Organization who created it
- `license`: Distribution license URL
- `distribution`: Download locations and formats
- `identifier`: DOI or Compact Identifiers
- `temporalCoverage`: Time period covered (ISO 8601 format)
- `spatialCoverage`: Geographic scope

## Best Practices

Use `sameAs` to link canonical versions when multiple copies exist, and `isBasedOn` for derived datasets. Publishers should limit textual properties to 5000 characters maximum.
