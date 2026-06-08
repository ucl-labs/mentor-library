# Book Actions Structured Data

Source: https://developers.google.com/search/docs/appearance/structured-data/book

## Overview

This Google Search Central documentation provides guidance for implementing Book actions structured data, enabling book providers to display purchase and borrowing options directly in Search results. Book actions allow users to "quickly buy or borrow the books that they find directly from Search results." The feature supports two action types: `ReadAction` for purchases and `BorrowAction` for borrowing.

## Critical Requirements

### Participation

"This feature is currently limited to book providers with a wide selection of available books." Interested providers must complete an interest form, though registration doesn't guarantee participation.

### Identifiers

ISBN-13 is the primary reconciliation signal. The documentation notes that "Google Search doesn't accept ISBN-10" and recommends converting to ISBN-13 using conversion tools. Alternative identifiers accepted include OCLC Numbers, LCCN, and JP e-codes.

### Feed Specifications

- Maximum uncompressed file size: less than 1 GB
- Format: JSON with `.json` extension
- Supported compression: zip, gz, tar, tar.gz, JAR, ar, arj, cpio, or dump
- Must use production URLs only (no QA or development links)
- All URLs must be canonical

## Core Concepts

### Works vs. Editions

The schema distinguishes between:
- **Work**: Abstract concept (title, author, original language)
- **Edition**: Concrete copy (publication year, ISBN, specific format)

One work can have multiple editions grouped together to leverage comprehensive book information.

### Library Structure

For lending features, the system uses three tiers:
- `LibrarySystem`: Abstract network of affiliated libraries
- `Library (member)`: Physical library branches with addresses
- Each member must belong to at least one system

## Implementation Steps

1. Build feed according to structured data type definitions
2. Review guidelines covering works/editions, library systems, identifiers, and links
3. Test using the Data Feed validation tool
4. Host at secure location (supports Google Cloud Storage, HTTPS, SFTP, AWS S3)
5. Submit for quality review by Google support team
6. Update feeds as needed (daily updates recommended)

## Required Properties (Book Work Level)

- `@context`: "https://schema.org"
- `@id`: Globally unique URL identifier
- `@type`: "Book"
- `author`: Person or Organization entity
- `name`: Book title
- `url`: Website page describing the book
- `workExample`: At least one edition required

## Required Properties (Book Edition Level)

- `@id`: Unique edition identifier
- `@type`: "Book"
- `bookFormat`: AudiobookFormat, EBook, Hardcover, or Paperback
- `inLanguage`: ISO 639-1 two-letter code
- `isbn`: ISBN-13 number
- `potentialAction`: ReadAction or BorrowAction object

## Action Types

### ReadAction Properties

Enables purchases with properties including:
- `target`: EntryPoint with `urlTemplate` and `actionPlatform`
- `expectsAcceptanceOf`: Offer defining purchase terms
- Supported categories: nologinrequired, free, subscription, purchase, rental

### BorrowAction Properties

Enables borrowing with:
- `lender`: LibrarySystem reference
- `target`: EntryPoint specifications
- No offer categories required

## Content Guidelines

- Remove stale entities (expired `availabilityEnds` dates)
- Use canonical URLs only
- Direct action links must lead to purchase/borrowing pages, not intermediate landing pages
- Each entity requires unique `@id`, `url`, and `urlTemplate`

## Feed Management

Update frequency depends on catalog changes. The documentation notes that "Google Search fetches your feed once a day and typically indexes the content within two days." Use `availabilityStarts` and `availabilityEnds` properties to manage availability windows.
