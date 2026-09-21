---
name: create-spec
description: Convert validated intent into observable behavior, rules, edge cases and testable acceptance criteria.
---

# Create a specification

## Method

1. Read current truth under `.aidd/specs/` and the change intent.
2. Describe only the delta required for the outcome.
3. Express behavior with actor, trigger, response and constraints.
4. Cover permissions, empty/loading/error states and relevant accessibility or localization concerns.
5. Write acceptance criteria that are independently testable.
6. Keep implementation choices out unless they constrain product behavior.

## Output

Write `.aidd/changes/<slug>/spec.md`. Mark unresolved decisions explicitly; do not proceed to autonomous implementation when they affect acceptance behavior.
