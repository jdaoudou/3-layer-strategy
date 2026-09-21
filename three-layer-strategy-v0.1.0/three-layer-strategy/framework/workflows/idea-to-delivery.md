# Workflow: idea to verified delivery

## 1. Intent

Capture the user, problem, evidence, desired outcome, non-goals and constraints in `intent.md`. Do not lock onto a solution prematurely.

Exit condition: the outcome is understandable by someone who did not attend the original conversation.

## 2. Assess

Use the decision dimensions in `principles/decision-rules.md`. Choose a mode independently for spec, plan, build and verify. Record high-impact overrides and required approvals in `assessment.md`.

Exit condition: the chosen autonomy is proportionate to risk and verifiability.

## 3. Spec

Describe observable behavior, rules, edge cases, acceptance criteria and the delta from current product truth. Resolve important ambiguity before implementation.

Exit condition: acceptance criteria can fail unambiguously.

## 4. Plan

Map the affected components, dependencies, data changes, rollout, rollback and verification. Split work into independently checkable tasks.

Exit condition: another capable contributor could execute the plan without inventing product behavior.

## 5. Build

Execute tasks in small batches. Follow the selected layer and its control points. Update the plan when reality differs; do not silently rewrite the spec to match the implementation.

Exit condition: tasks are complete and evidence is attached.

## 6. Verify

Run automated checks, inspect the observable outcome and test risk-specific cases. Whenever justified, separate the generator from the verifier.

Exit condition: every acceptance criterion has evidence or an explicit exception approved by its owner.

## 7. Integrate product truth

After acceptance, update `.aidd/specs/` with the resulting current behavior and record durable decisions in `.aidd/decisions/`. Keep the change bundle as history.
