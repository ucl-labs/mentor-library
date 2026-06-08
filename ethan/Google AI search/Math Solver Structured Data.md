# Math Solver (MathSolver) Structured Data

Source: https://developers.google.com/search/docs/appearance/structured-data/math-solvers

## Overview

This Google Search Central documentation explains how to implement structured data for math solvers - tools that help students and educators by providing step-by-step solutions to mathematical problems.

## Key Implementation Steps

1. **Add required properties** using standardized structured data format
2. **Follow content and technical guidelines**
3. **Validate** using the Rich Results Test tool
4. **Deploy and test** with the URL Inspection tool
5. **Submit sitemap** for ongoing updates

## Required Properties

The core implementation requires:

- **potentialAction**: A `SolveMathAction` that processes mathematical expressions
- **mathExpression-input**: A placeholder for the math problem being solved
- **url**: Your math solver's website address
- **usageInfo**: Link to your privacy policy
- **potentialAction.target**: The endpoint URL that solves problems

## Problem Type Support

The documentation lists 60+ problem types including:

- Polynomial equations and expressions
- Derivatives and integrals
- Linear and quadratic equations
- Trigonometric problems
- Matrix operations
- Statistics and geometry

For complex types like derivatives and integrals, Google sends specially formatted strings (e.g., `(x^2+x)'` for derivatives or `\int x^2+x` for integrals).

## Content Guidelines

Solvers must meet these standards:

- No promotional or affiliate content disguised as math tools
- Accurate problem-type declarations
- Correct solutions for declared problem types
- Public access to initial solutions (additional content may require login)

## Technical Requirements

- Add markup to your site's homepage
- Ensure efficient crawlability
- Use canonical URLs for duplicate copies
- Don't hide behind complete paywalls initially
