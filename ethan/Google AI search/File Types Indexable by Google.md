# File Types Indexable by Google

Source: https://developers.google.com/search/docs/crawling-indexing/indexable-file-types

## Overview

Google indexes content from most text-based files and certain encoded document formats. The determination of file type relies primarily on the `Content-Type` HTTP header, though Google may use file extensions or re-parse files if the header is missing or incorrect.

## Supported Flat File Types

These files contain plain, unencoded text (potentially with markup):

- Comma-Separated Values (.csv)
- Google Earth (.kml, .kmz)
- GPS eXchange Format (.gpx)
- HTML (.htm, .html, other extensions)
- Scalable Vector Graphics (.svg)
- TeX/LaTeX (.tex)
- Text files (.txt, .text, other extensions), including source code:
  - Basic (.bas)
  - C/C++ (.c, .cc, .cpp, .cxx, .h, .hpp)
  - C# (.cs)
  - Java (.java)
  - Perl (.pl)
  - Python (.py)
- Wireless Markup Language (.wml, .wap)
- XML (.xml)

## Supported Encoded File Types

Binary files or complex containers requiring specific parsers:

- Adobe Portable Document Format (.pdf)
- Adobe PostScript (.ps)
- Electronic Publication (.epub)
- Hancom Hanword (.hwp)
- Microsoft Excel (.xls, .xlsx)
- Microsoft PowerPoint (.ppt, .pptx)
- Microsoft Word (.doc, .docx)
- OpenOffice presentation (.odp)
- OpenOffice spreadsheet (.ods)
- OpenOffice text (.odt)
- Rich Text Format (.rtf)

## Supported Media Formats

**Image formats:** BMP, GIF, JPEG, PNG, WebP, SVG, AVIF

**Video formats:** 3GP, 3G2, ASF, AVI, DivX, M2V, M3U, M3U8, M4V, MKV, MOV, MP4, MPEG, OGV, QVT, RAM, RM, VOB, WebM, WMV, XAP

## Search by File Type

Users can employ the `filetype:` operator to filter search results by type (e.g., `filetype:rtf galway`).
