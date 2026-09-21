# Layer decision rules

Choose a mode for **each step** of the delivery flow. Reassess when evidence changes.

## Decision dimensions

Score each dimension from 0 to 2.

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Ambiguity | outcome and rules are explicit | some interpretation remains | problem or outcome is disputed |
| Impact | local and contained | several components/users | legal, financial, security, safety or broad user impact |
| Reversibility | instant rollback | recoverable with effort | hard or impossible to undo |
| Observability | deterministic automated proof | mixed automated/manual proof | success is subjective or delayed |
| Context sensitivity | self-contained | needs project history | relies on tacit organizational knowledge |
| Novelty | repeated pattern | adapted pattern | unprecedented work |

## Default recommendation

- **0–3 — Agentic candidate:** only if permissions are bounded and verification is cheap.
- **4–7 — Assisted:** a human frames and reviews; AI may draft or execute bounded work.
- **8–12 — Human-led:** a human performs the critical reasoning; AI may support research or formatting.

This score supports judgment; it does not replace it. Any non-negotiable policy can force a more human-controlled mode.

## Overrides

Use human-led execution when:

- the desired outcome is not agreed;
- the action grants access, spends money, publishes externally or deletes material data;
- verification would depend on the same unsupported assumptions as generation;
- applicable policy requires a named decision-maker.

Agentic execution is reasonable when:

- the input, boundary and expected output are explicit;
- tools and permissions are least-privilege;
- the action is reversible or isolated;
- failure is observable;
- acceptance checks can be executed independently.

## Environmental and attention cost

When two modes are equally safe and effective, choose the one with lower total cost: model calls, compute, human review, waiting time and duplicated work. Do not use an agent to avoid a two-minute deterministic edit; do not make a human repeat a large mechanical transformation that can be checked automatically.
