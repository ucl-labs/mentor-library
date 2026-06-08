# Changing Your Web Hosting and SEO

Source: https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-changes

## Overview

Google's guide helps minimize search performance impact when switching hosting providers or CDNs without changing user-visible URLs. The process involves four main phases:

1. **Prepare new infrastructure** - Upload content, test thoroughly, verify Googlebot access
2. **Start the move** - Update DNS settings to point to new hosting
3. **Monitor traffic** - Track old/new server logs and crawling activity
4. **Shut down old hosting** - Decommission infrastructure once traffic reaches zero

## Key Preparation Steps

Before migrating, site owners should:

- Create a testing environment with restricted access to verify all functionality
- Test the site in browsers and review pages, images, forms, and downloads
- Set up temporary hostnames (like `beta.example.com`) with `noindex` rules to prevent indexing
- Use the URL Inspection Tool in Search Console to confirm Googlebot can access new servers
- Lower DNS TTL values weeks in advance to speed propagation

## Critical Considerations

Firewall and denial-of-service protection must not block Googlebot. Search Console verification methods (HTML files, meta tags, or Google Analytics) must remain intact on the new infrastructure.

## During Migration

Remove any temporary crawling blocks like robots.txt restrictions or `noindex` tags before updating DNS. Monitor server logs on both old and new infrastructure as traffic transitions. A temporary dip in Googlebot's crawl rate is normal, typically recovering within days as the system adjusts to new hosting signals.
