# Googlebot

Source: https://developers.google.com/search/docs/crawling-indexing/googlebot

Googlebot is Google's web crawler, available in two types:

- **Googlebot Smartphone**: simulates mobile device users
- **Googlebot Desktop**: simulates desktop users

## Key Technical Details

**Crawling Frequency**: Googlebot typically accesses sites no more than once every few seconds on average, though short-term rates may appear higher due to delays.

**File Size Limits**: The crawler processes the first 2MB of supported file types and 64MB of PDF files. Resources like CSS and JavaScript follow the same 2MB limit.

**Timezone**: When crawling from US IP addresses, Googlebot operates on Pacific Time.

## Blocking and Verification

To prevent Googlebot access, webmasters have options:
- Use `robots.txt` to block crawling
- Apply `noindex` tags to prevent indexing
- Implement password protection for complete access denial

**Important Security Note**: The user-agent header is frequently spoofed. Google recommends verifying requests through reverse DNS lookup on the source IP or checking against official Googlebot IP ranges.

## Mobile-First Indexing

Google primarily indexes mobile versions of content, making Googlebot Smartphone requests the majority of crawl activity, with desktop crawler requests representing a smaller portion.
