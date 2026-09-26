# Calculation guide

## Question and evidence

Where does instructional-design work repeat or branch?

Synthetic timestamped design-event logs, grouped into cases.

**Status:** SYNTHETIC / RULE-BASED PROTOTYPE | no educational validity claim.

## Design

Order events within cases; count trace variants and next-stage transitions; calculate rework and transition entropy.

## Calculation and interpretation

`P(next|stage) = transition count / outgoing count; H(stage) = -sum p log2 p.`

Entropy is averaged equally across source stages. Rework is repeated-stage events divided by events within a case, then averaged over cases. Repetition may be productive revision rather than waste.

## Evidence table

Selected recorded values (units and context shown). Full precision below is for traceability, not a claim of measurement precision.

| Quantity | Value | Unit / meaning | JSON path |
|---|---:|---|---|
| variant_count | 4 | unitless | `variant_count` |
| transition_entropy | 0.737 | unitless | `transition_entropy` |
| rework_rate | 0.129 | unitless | `rework_rate` |
| ai_handoff_rate | 0.295 | unitless | `ai_handoff_rate` |

Source: [results/demo_metrics.json](results/demo_metrics.json). Values resolve directly from this file when figures are regenerated.

This process-mining prototype reconstructs instructional-design traces from synthetic event logs. It reports common variants, stage-to-stage transition shares, entropy, and a clearly defined repetition rate, making workflow differences visible without calling every revision inefficient. The calculations support process inspection; real conclusions would require authentic logs and a defensible interpretation of stage labels.

## Verification performed in this review

The existing suite requires unavailable dependencies; no full-suite pass is claimed. The bundled demonstration executed successfully in this review.

The figure-generation check verifies agreement between the selected source values and SVGs. It does not validate the raw dataset, fitted model, identification assumptions, or external generalization.

```bash
python scripts/build_review_figures.py
python scripts/build_review_figures.py --check
```

## Implementation map

Follow these functions to inspect each transformation. Validation helpers and private functions remain visible in the linked modules.

| Function | Purpose / documented behavior |
|---|---|
| [`main`](src/learning_design_process_mining/cli.py#L5) | Inspect the explicit implementation and its callers. |
| [`trace_variants`](src/learning_design_process_mining/core.py#L9) | Inspect the explicit implementation and its callers. |
| [`transition_table`](src/learning_design_process_mining/core.py#L14) | Inspect the explicit implementation and its callers. |
| [`transition_entropy`](src/learning_design_process_mining/core.py#L18) | Inspect the explicit implementation and its callers. |
| [`rework_rate`](src/learning_design_process_mining/core.py#L25) | Inspect the explicit implementation and its callers. |
| [`make_design_log`](src/learning_design_process_mining/synthetic.py#L3) | Inspect the explicit implementation and its callers. |

## What remains before a stronger research claim

Entropy is averaged equally across source stages. Rework is repeated-stage events divided by events within a case, then averaged over cases. Repetition may be productive revision rather than waste. A successful software test is not validation of a scientific construct. New experiments should state their split unit, comparator, outcome, uncertainty procedure and failure criteria before examining final test results.
