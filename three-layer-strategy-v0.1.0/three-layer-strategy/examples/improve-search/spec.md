# Specification: Improve editorial search

Status: accepted

## Current behavior

Body-text relevance can rank partial matches above an exact title match.

## Proposed behavior

Accessible content with an exact normalized title match receives enough relevance boost to rank above partial body-text matches.

## Rules

- normalization is case-insensitive and trims surrounding whitespace;
- permission filtering occurs unchanged;
- the boost influences rank but never makes inaccessible content visible.

## Edge and failure cases

- identical accessible titles retain their existing secondary ordering;
- if no title matches, existing ranking is unchanged.

## Acceptance criteria

- [ ] AC-1: an accessible exact normalized title match ranks before partial body-text matches.
- [ ] AC-2: inaccessible exact title matches remain absent.
- [ ] AC-3: a query without a title match preserves baseline ordering.
- [ ] AC-4: p95 latency stays within the project's accepted search budget.
