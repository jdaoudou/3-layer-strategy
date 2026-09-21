# Three-Layer Strategy

An open framework for AI-driven development that decides **how work should be done before asking an AI to do it**.

The framework uses the same delivery flow for every change:

```text
INTENT -> ASSESS -> SPEC -> PLAN -> BUILD -> VERIFY
```

At each step, the team chooses one execution mode:

| Mode | Who does the work? | Who is accountable? |
| --- | --- | --- |
| **Human** | A human | A human |
| **Assisted** | AI drafts, a human pilots and edits | A human |
| **Agentic** | An agent executes within explicit boundaries | A human |

The layers are not maturity levels. Agentic is not automatically better. The right layer depends on ambiguity, risk, reversibility, verification cost and environmental cost.

## Why this exists

AI has made producing code faster. It has not made deciding what should exist, managing product truth or proving that a change is correct disappear. Three-Layer Strategy keeps those responsibilities visible and makes Git the shared memory of the product.

The framework borrows four useful ideas from the current ecosystem:

- specs and proposed changes are separated;
- principles, specification, planning and implementation are distinct;
- capabilities are packaged as small composable skills;
- `AGENTS.md` is the portable entry point for coding agents.

## Repository map

```text
framework/          Canonical principles, workflows, skills and templates
adapters/           Entry points for Claude Code, Codex, Cursor and Copilot
project-template/   Minimal files installed in a product repository
examples/           Worked examples
cli/                Zero-dependency initializer and validation commands
tests/              CLI and structure tests
```

## Quick start

From a clone of this repository:

```bash
python cli/three_layer.py init ../my-project --adapter codex
cd ../my-project
```

Create a proposed change:

```bash
python ../three-layer-strategy/cli/three_layer.py new-change improve-search \
  --project . \
  --title "Improve editorial search"
```

Check that the project memory is coherent:

```bash
python ../three-layer-strategy/cli/three_layer.py doctor .
```

Then ask the agent to read `AGENTS.md` and work on the change. The detailed method lives in [`framework/workflows/idea-to-delivery.md`](framework/workflows/idea-to-delivery.md).

## Project memory model

An initialized product contains:

```text
.aidd/
├── config.yaml
├── principles.md
├── specs/                 # Current product truth
├── changes/               # Proposed or active deltas
│   └── <change>/
│       ├── intent.md
│       ├── assessment.md
│       ├── spec.md
│       ├── plan.md
│       ├── tasks.md
│       └── verification.md
└── decisions/             # Durable architectural/product decisions
```

When a change is accepted, its validated behavior is merged into `.aidd/specs/`. The change folder remains a trace of why and how the product moved.

## Core rules

1. Start from an outcome, not a solution.
2. Select a layer for each workflow step, not for the whole project.
3. Keep current truth separate from proposed change.
4. Give an agent only the context and permissions it needs.
5. Prefer reversible actions and small batches.
6. Verification must be independent from generation whenever risk justifies it.
7. Human accountability does not disappear in agentic mode.
8. Every token, tool call and review minute has a cost.

## Status

This is an opinionated MVP: enough to test the method on real changes, deliberately small enough to evolve from evidence. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the proposal process.

## License

MIT. See [`LICENSE`](LICENSE).
