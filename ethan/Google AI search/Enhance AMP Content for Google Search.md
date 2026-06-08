# Enhance AMP Content for Google Search

Source: https://developers.google.com/search/docs/crawling-indexing/amp/enhance-amp

## Overview

Google's documentation guides developers in optimizing Accelerated Mobile Pages (AMP) for search visibility through structured implementation and monitoring.

## Key Sections

### Creating Basic AMP Pages

The guide recommends five foundational steps: creating your initial AMP page, adhering to Google Search guidelines, ensuring discoverability through proper linking, maintaining feature parity between AMP and canonical versions, and validating with the AMP Test Tool.

**Important linkage requirement:** "Google Search requires that an AMP page links to a canonical page" which may be either a non-AMP version or the AMP page itself.

### Structured Data Implementation

Developers should apply identical structured data markup across both canonical and AMP pages, then verify correctness using the Rich Results Test tool.

### CMS-Based Development

For content management systems, two recommended URL schemes are:
- `https://www.example.com/myarticle/amp`
- `https://www.example.com/myarticle.amp.html`

### Monitoring Tools

Google provides two essential reports:
- AMP status report (identifies templating issues)
- Rich result status reports (reveals structured data problems)

### Learning Resources

The documentation includes links to four codelabs covering foundational concepts, advanced features, interactive canonical pages, and Progressive Web App integration.

### Additional Integrations

Resources cover ad units, monetization, Google Tag Manager implementation, and analytics integration.
