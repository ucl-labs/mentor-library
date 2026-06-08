# Fix Canonicalization Issues

Source: https://developers.google.com/search/docs/crawling-indexing/canonicalization-troubleshooting

## Overview

Google Search Central recommends using the URL Inspection tool to verify which page Google designates as canonical. The platform notes that "Google might choose a different canonical for various reasons, such as the quality of the content," even when you explicitly specify a preferred canonical URL.

## Common Canonicalization Issues

### Language Variants Without Localized Annotations

Sites serving the same content to different regions should implement `hreflang` annotations. This helps ensure "the right pages surface for users in different regions."

### Incorrect Canonical Elements

Content management systems may misuse canonicalization techniques. The documentation advises checking your HTML via browser developer tools for unexpected canonical URL preferences through improper `rel="canonical"` tags or redirects.

### Misconfigured Servers

Server misconfigurations can cause cross-domain URL selection problems, such as:
- Returning content from one domain in response to requests for another
- Multiple servers returning identical soft 404 pages that Google fails to recognize as errors

### Malicious Hacking

Attacks may inject HTTP redirects or cross-domain `rel="canonical"` links pointing to malicious content, causing Google to select compromised URLs instead of legitimate ones.

### Syndicated Content

The canonical link element isn't recommended for syndication scenarios. The documentation suggests partners block indexing of your content instead.

### Copycat Websites

External sites occasionally duplicate content without permission. You can contact the hosting provider or file a Digital Millennium Copyright Act request for removal.
