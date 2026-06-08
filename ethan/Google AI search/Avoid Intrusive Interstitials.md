# Avoid Intrusive Interstitials and Dialogs

Source: https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials

## Overview

The documentation explains that "intrusive interstitials and dialogs are page elements that obstruct users' view of the content, usually for promotional purposes." These elements can negatively impact both user experience and search engine crawlability.

## Key Problems

Intrusive overlays create several issues:
- They frustrate users and damage website trust
- They impede search engine understanding of page content
- Poor user experience leads to decreased return visits
- They may harm search performance

## Best Practices for Unintrusive Dialogs

### Use Banners Instead of Full-Page Interstitials

Rather than blocking entire pages, implement small banners that occupy minimal screen space. Examples include:
- Smart App Banners (Safari)
- In-app install experiences (Chrome)
- HTML banners similar to advertisements

These allow users and search engines immediate access to content.

### Leverage Existing Solutions

Many content management systems offer plugins for common use cases like newsletter signups. Using standardized plugins benefits Google, other search engines, and the broader web ecosystem.

### Common Mistakes to Avoid

Avoid these practices unless legally required:
- Full-page interstitials that obscure entire content
- Redirecting users to separate pages for consent or input

## Mandatory Interstitials Exception

Age gates and legally required interstitials are exempt from these guidelines. However, Google recommends:
- Overlaying interstitials on content so some material remains indexable
- Avoiding redirects that could limit search indexing
- Allowing Googlebot to bypass age verification through verification methods
