---
name: formalize-idea
description: Turn a raw idea or request into a concise outcome-focused intent without inventing unsupported requirements.
---

# Formalize an idea

## Inputs

- the raw request;
- known product context and evidence;
- `.aidd/principles.md`;
- the intent template.

## Method

1. Identify the affected user or stakeholder.
2. Separate the observed problem from the proposed solution.
3. Capture evidence and clearly label assumptions.
4. Define an observable desired outcome.
5. Write explicit non-goals and constraints.
6. Ask only questions whose answers would materially change scope, risk or behavior.

## Output

Create or update `.aidd/changes/<slug>/intent.md`. Keep unresolved items under `Open questions`; never silently fill them with plausible details.

## Quality gate

A reader unfamiliar with the discussion can explain who needs what change, why it matters and what success looks like.
