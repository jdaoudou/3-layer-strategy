---
name: create-plan
description: Produce an implementation plan and small verifiable tasks from an accepted specification.
---

# Create a plan

## Method

1. Inspect the code and runtime paths affected by each acceptance criterion.
2. Identify dependencies, migrations, permissions and operational impacts.
3. Choose the smallest coherent implementation approach.
4. Define rollout, rollback and observability.
5. Split work into ordered tasks, each with a check.
6. Map every acceptance criterion to at least one verification activity.

## Outputs

- `.aidd/changes/<slug>/plan.md`
- `.aidd/changes/<slug>/tasks.md`

Do not invent product rules to make the technical plan easier.
