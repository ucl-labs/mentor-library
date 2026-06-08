# Share Your Product Data With Google

Source: https://developers.google.com/search/docs/specialty/ecommerce/share-your-product-data-with-google

To increase visibility across Google's services, ecommerce sites should share product information through two primary methods:

## Key Recommendations

1. **Add structured data to product pages** - Enables richer search appearances and helps Google better understand pricing, discounts, and shipping information.

2. **Upload feeds to Google Merchant Center** - While not mandatory for basic search results, this service provides "a deeper understanding of commerce data" and is required for Google Shopping tab listings.

## Adding Structured Data

Benefits include:
- Eligibility for Product rich results
- Improved accuracy in price, discount, and shipping cost interpretation
- Better verification of product feeds against website content

Sites can use a `data-nosnippet` attribute if they want to prevent Google from extracting specific content.

## Google Merchant Center Advantages

For smaller sites, automated feeds can extract data from structured markup. Larger sites benefit from periodic uploads or the Content API for:

- **Guaranteed coverage** - "Web crawling is not guaranteed to find all products on your site"
- **Timing control** - Weekly, daily, or hourly updates versus relying on crawl frequency
- **Hidden data sharing** - Information like store inventory can be shared without appearing on the public website

## Data Synchronization

When combining website and Merchant Center data, timing mismatches can occur. Google recommends configuring Merchant Center to automatically update based on website content when discrepancies appear, particularly for pricing and availability changes.
