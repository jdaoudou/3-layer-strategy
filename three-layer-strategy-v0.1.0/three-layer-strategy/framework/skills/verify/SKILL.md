---
name: verify
description: Test a change against its acceptance criteria and risk profile, then report evidence without hiding failures.
---

# Verify a change

## Method

1. Read the spec and assessment before inspecting implementation claims.
2. Run the project's required automated checks.
3. Map evidence to each acceptance criterion.
4. Test risk-specific failure paths and regressions.
5. Distinguish observed facts, inferences and untested assumptions.
6. Record failures and residual risk; never soften them to declare success.

## Output

Write `.aidd/changes/<slug>/verification.md` with one status: `accepted`, `accepted-with-exceptions` or `rejected`.

Where risk justifies it, verification should be performed by a different human, agent or deterministic system than the one that generated the change.
