# Managing Multi-Regional and Multilingual Sites

Source: https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites

## Key Distinctions

**Multilingual sites** offer content in multiple languages. For example, "a Canadian business with English and French versions of its site."

**Multi-regional sites** explicitly target different countries. Some sites are both multi-regional and multilingual.

## Key Recommendations for Multilingual Sites

Google recommends using "different URLs for each language version of a page rather than using cookies or browser settings to adjust the content language."

"Google uses the visible content of your page to determine its language," not code-level indicators like lang attributes.

Sites should avoid automatically redirecting users between language versions and instead "consider adding hyperlinks to other language versions of a page."

## Geotargeting Strategies

For locale-specific targeting, Google identifies four URL structure options:

- **Country-specific domains** (example.de) - clear geotargeting but are expensive
- **Subdomains** (de.example.com) - easy to set up
- **Subdirectories** (example.com/de/) - require low maintenance
- **URL parameters** - not recommended

"Don't use IP analysis to adapt your content. IP location analysis is difficult and generally not reliable."

## Determining Target Locale

Google uses multiple signals including ccTLDs, hreflang statements, server location, local addresses, language, currency, and local site links.
