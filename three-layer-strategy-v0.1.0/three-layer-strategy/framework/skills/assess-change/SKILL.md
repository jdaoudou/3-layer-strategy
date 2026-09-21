---
name: assess-change
description: Evaluate ambiguity, impact, reversibility, observability, context sensitivity and novelty to recommend execution modes.
---

# Assess a change

## Inputs

- validated `intent.md`;
- project principles and policies;
- the layer decision rules.

## Method

1. Score the six decision dimensions and justify each score with one sentence.
2. Identify policy overrides and required named approvals.
3. Select a mode separately for spec, plan, build and verify.
4. Define controls for any agentic step: permitted files/tools, stop conditions, rollback and checks.
5. Estimate model, compute and review cost qualitatively: low, medium or high.

## Output

Write `.aidd/changes/<slug>/assessment.md` using the assessment template.

## Quality gate

The recommendation can be challenged from visible evidence; it is not based on enthusiasm for or fear of AI.
