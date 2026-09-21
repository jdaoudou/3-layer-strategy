# Testing policy

- Every behavior change must map acceptance criteria to evidence.
- Bug fixes should include a regression test when technically feasible.
- Tests must cover the highest-risk failure paths, not only the happy path.
- Generated tests are reviewed for false positives and tautological assertions.
- A change cannot be accepted solely because the test suite is green if the observable outcome has not been checked.
- Any skipped or unavailable check is recorded in `verification.md` with its impact.
