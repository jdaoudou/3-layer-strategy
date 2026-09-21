# Instructions for agents working on this framework

## Purpose

This repository defines Three-Layer Strategy. Preserve its central idea: human, assisted and agentic are execution modes selected per workflow step, never a hierarchy of maturity.

## Before editing

1. Read `framework/principles/manifesto.md`.
2. Read the workflow or skill directly affected by the request.
3. Inspect existing tests and examples before creating a new convention.
4. State the intended outcome and the verification method.

## Working rules

- Keep normative rules in `framework/`; adapters only translate them for a tool.
- Keep project state in `.aidd/`; never hide product truth in chat history.
- Prefer one small skill to a large general-purpose prompt.
- Do not implement an ambiguous or high-impact change without an explicit spec.
- Never claim completion without running the relevant checks.
- Do not overwrite user-authored project files unless `--force` was explicitly chosen.
- Avoid vendor-specific language in canonical framework files.

## Validation

Run:

```bash
python -m unittest discover -s tests -v
python cli/three_layer.py doctor project-template
```

Documentation-only changes must still preserve relative links, file names and the expected change bundle described in `framework/templates/README.md`.

## Definition of done

- the change follows the manifesto and decision rules;
- canonical content and adapters do not contradict each other;
- examples are updated when a public convention changes;
- tests pass;
- the result and any remaining uncertainty are reported plainly.
