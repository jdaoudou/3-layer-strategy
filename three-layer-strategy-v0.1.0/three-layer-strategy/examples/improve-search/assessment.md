# Assessment: Improve editorial search

## Scores

| Dimension | Score | Evidence |
| --- | ---: | --- |
| Ambiguity | 0 | Expected ranking behavior is explicit. |
| Impact | 1 | Search ordering changes for all editorial users. |
| Reversibility | 0 | The boost can be reverted independently. |
| Observability | 0 | Ranking and latency can be tested deterministically. |
| Context sensitivity | 1 | Current query and permissions pipeline must be understood. |
| Novelty | 0 | Title boosting is an established search pattern. |

Total: 2

## Execution modes

| Step | Mode | Human control point | Agent boundaries / checks |
| --- | --- | --- | --- |
| Spec | Assisted | Product validates ranking examples. | Draft only from supplied evidence. |
| Plan | Assisted | Tech lead validates query path. | Read-only inspection. |
| Build | Agentic | Engineer approves diff. | Search module only; no permission changes. |
| Verify | Assisted | QA validates dataset and result. | Run ranking, permission and latency checks. |

## Policy overrides and approvals

None.

## Reassessment triggers

Any required schema reindex, latency regression or permission-filter change.
