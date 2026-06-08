# Job Posting Schema Markup

Source: https://developers.google.com/search/docs/appearance/structured-data/job-posting

`JobPosting` structured data enhances job listings in Google Search results, enabling job seekers to discover positions more effectively while providing employers with interactive, discoverable job postings.

## Key Benefits

- "More interactive results" displaying logos, reviews, and job details
- Enhanced filtering capabilities for job seekers by location and title
- "Increased chances of discovery and conversion" through improved visibility

## Required Properties

Every valid `JobPosting` must include:

- **datePosted**: Original posting date in ISO 8601 format
- **description**: Complete HTML-formatted job details with qualifications
- **hiringOrganization**: Company name and details
- **jobLocation**: Physical work location with address components
- **title**: Job position title (not including codes, dates, or salary)

## Recommended Properties

- `baseSalary`: Actual compensation details
- `employmentType`: Position classification (full-time, contractor, etc.)
- `validThrough`: Expiration date for job postings
- `jobLocationType`: Set to "TELECOMMUTE" for remote positions
- `applicantLocationRequirements`: Geographic restrictions for remote work

## Remote Work Markup

For work-from-home positions, use three coordinated properties: `jobLocationType` set to "TELECOMMUTE," `applicantLocationRequirements` specifying eligible countries, and optionally `jobLocation` for hybrid arrangements.

## Content Policies

Google enforces strict guidelines prohibiting:
- Irrelevant markup on non-job pages
- Incomplete job descriptions
- Misrepresentation or fake positions
- Profanity and vulgar language
- Expired postings without proper removal
- Positions lacking application mechanisms
- Mandatory applicant payments

## Removing Job Postings

Expired positions must be handled through one of three methods: setting `validThrough` to a past date, removing the page entirely (returning 404/410 status), or deleting the `JobPosting` structured data.
