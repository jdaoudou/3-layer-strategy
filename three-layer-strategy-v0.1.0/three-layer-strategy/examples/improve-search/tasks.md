# Tasks: Improve editorial search

- [ ] T1 — Add failing ranking and permission fixtures.
  - Expected evidence: AC-1 and AC-2 fail for the expected reason.
- [ ] T2 — Add the exact-title boost in the query builder.
  - Depends on: T1.
  - Expected evidence: targeted tests pass.
- [ ] T3 — Run regression and latency checks.
  - Depends on: T2.
  - Expected evidence: AC-3 and AC-4 results recorded.
- [ ] T4 — Review diff and rollout settings.
  - Depends on: T3.
