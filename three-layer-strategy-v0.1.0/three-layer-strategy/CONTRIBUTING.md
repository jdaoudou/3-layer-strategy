# Contributing

Three-Layer Strategy should evolve from real delivery evidence, not from adding more ceremony.

## Propose a change

1. Describe the observed problem and who experiences it.
2. Provide one concrete example.
3. Explain which canonical rule, workflow, skill or template must change.
4. State how the proposal can be tested in a real project.
5. Update affected examples and adapters.

New concepts belong in the framework only when they are reusable across several projects. Local process belongs in a project's `.aidd/principles.md` or `AGENTS.md`.

## Pull request checklist

- [ ] The proposal reduces ambiguity or improves delivery safety.
- [ ] It does not assume that agentic execution is always preferable.
- [ ] It does not duplicate an existing rule in a new location.
- [ ] Examples and adapters remain consistent.
- [ ] `python -m unittest discover -s tests -v` passes.
