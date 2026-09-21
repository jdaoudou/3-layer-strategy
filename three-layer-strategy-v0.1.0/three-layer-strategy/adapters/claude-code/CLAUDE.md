# Three-Layer Strategy — Claude Code adapter

Read `AGENTS.md`, `.aidd/principles.md` and `.aidd/config.yaml` before change work.

- Treat `.aidd/specs/` as current product truth.
- Treat `.aidd/changes/<slug>/` as a proposed delta.
- Select human, assisted or agentic mode per workflow step.
- In agentic mode, obey the explicit boundaries and stop conditions in `assessment.md`.
- Never infer acceptance from successful code generation; write evidence to `verification.md`.

Use the skill matching the current step. Canonical framework rules override this adapter.
