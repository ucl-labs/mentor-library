# Social Engineering (Phishing and Deceptive Sites)

Source: https://developers.google.com/search/docs/monitor-debug/security/social-engineering

## Overview

Google Search Central documentation addresses how social engineering threats affect website visibility. When Google detects such content, Chrome displays a "Deceptive site ahead" warning to visitors.

## Key Definitions

**Social engineering attacks** involve tricking users into dangerous online actions. The documentation identifies three main categories:

1. **Phishing** - Sites impersonate trusted entities to steal personal information like passwords or financial data
2. **Deceptive content** - Material encouraging actions only appropriate for trusted sources (downloading software, sharing passwords)
3. **Unmarked third-party services** - Operations by one entity on behalf of another without clear disclosure

## Detection and Monitoring

Website owners can check the Security Issues Report in Search Console to identify flagged pages. The documentation notes that "deceptive content may be included via resources embedded in the page, such as images, other third-party components, or ads."

## Common Violation Examples

The guide illustrates problematic patterns:
- Fake browser or software update prompts
- Counterfeit login pages with suspicious URLs
- Ads masquerading as system notifications or media player controls

## Remediation Steps

The documentation recommends:
1. Verifying site ownership and checking for unauthorized accounts
2. Removing all deceptive content
3. Auditing third-party embedded resources
4. Requesting a security review after cleanup

Website owners should also follow third-party service guidelines requiring clear branding and explicit disclosure of relationships between first and third parties.
