# Google Image SEO Best Practices

Source: https://developers.google.com/search/docs/appearance/google-images

Google provides several search features for visual discovery, including text result images, Google Discover, and Google Images.

## Help Google Discover and Index Your Images

### Use HTML image elements to embed images

Standard HTML image elements help crawlers find and process images. Google can locate images in the `src` attribute of `<img>` elements (including when nested in other elements like `<picture>`). CSS background images are not indexed.

**Recommended:**
```html
<img src="puppy.jpg" alt="A golden retriever puppy" />
```

**Not recommended:**
```html
<div style="background-image:url(puppy.jpg)">A golden retriever puppy</div>
```

### Use an image sitemap

Submitting an image sitemap helps Google discover images that might otherwise be missed. Unlike regular sitemaps, you can include URLs from other domains in image sitemap `<image:loc>` elements, enabling CDN usage.

### Responsive images

Use the `<picture>` element or `srcset` attribute for responsive design. Always specify a fallback `src` attribute.

### Use supported image formats

Google Search supports: BMP, GIF, JPEG, PNG, WebP, SVG, and AVIF.

## Optimize the Image Landing Pages

### Specify a preferred image with metadata

Influence image selection using:
- `schema.org primaryImageOfPage`
- `schema.org mainEntity`
- `og:image` meta tag

**Best practices for chosen images:**
- Select relevant, representative images
- Avoid generic images (logos) with text
- Avoid extreme aspect ratios
- Use high resolution when possible

### Use descriptive filenames, titles, and alt text

- Use short, descriptive filenames (e.g., `my-new-black-kitten.jpg` rather than `IMG00023.JPG`)
- Avoid generic names like `image1.jpg`
- Alt text describes images for accessibility and helps Google understand content

**Poor:** Missing alt text or keyword stuffing

**Best:** `<img src="puppy.jpg" alt="Dalmatian puppy playing fetch"/>`

For inline SVG elements, use the `<title>` element.

### Add structured data

Structured data enables rich results in Google Images with prominent badges. Ensure image attributes are included as required fields.

## Opt out of Google Images inline linking

To prevent full-sized images from appearing in Google Images:
1. Examine the HTTP referrer header when your image is requested
2. If from a Google domain, reply with HTTP `200` or `204` status code with no content

This doesn't constitute cloaking.
