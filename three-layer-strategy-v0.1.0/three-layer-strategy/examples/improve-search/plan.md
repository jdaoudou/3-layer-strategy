# Plan: Improve editorial search

Status: accepted

## Affected components

Search query builder and relevance integration tests.

## Approach

Add an exact-match title clause with an explicit boost inside the existing permission-filtered query. Preserve current fallback ranking.

## Risks and mitigations

- over-boosted short titles: add representative fixtures;
- performance regression: compare query latency on the reference dataset;
- permission leakage: retain and test filtering independently.

## Rollout

Release behind a configurable boost value and observe zero-result rate, click position and latency.

## Rollback

Set the boost to zero or revert the isolated query clause.

## Verification mapping

| Acceptance criterion | Check | Owner/tool |
| --- | --- | --- |
| AC-1 | ranking fixture | automated test |
| AC-2 | restricted-content fixture | automated test + QA |
| AC-3 | baseline snapshot | automated test |
| AC-4 | reference latency comparison | performance check |
