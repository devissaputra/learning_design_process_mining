# Research design

## Project aim

Learning design is usually documented as a final artifact, which hides the design process. This repo treats instructional design work as an event log so researchers can study iteration, bottlenecks, rework, and human–AI handoffs across the design lifecycle.

## Research questions

1. Which design paths occur most often from objective-setting to release?
2. Where do designers loop back or stall?
3. How does AI assistance change iteration patterns without assuming that fewer steps are automatically better?

## Baseline analytic pipeline

1. Design event log
2. Trace extraction
3. Transition graph
4. Variant analysis
5. Bottleneck analysis

## Construct-to-measure discipline

The repository intentionally distinguishes **constructs** from **proxies**. A behavioral feature may be consistent with a construct without proving that construct exists. A real study should establish content validity, reliability, sensitivity to context, and convergent/discriminant evidence before attaching strong interpretations.

## Minimum empirical extension

1. Pre-register the main research question and analysis plan.
2. Recruit a context-appropriate sample with consent and a documented data-governance plan.
3. Establish annotation reliability or measurement reliability before model comparison.
4. Split exploratory analysis from confirmatory evaluation.
5. Report uncertainty, subgroup performance, missing-data patterns, and negative findings.
6. Evaluate whether the output is understandable and useful to the people expected to act on it.

## Threats to validity

- Process efficiency is not the same as design quality.
- The synthetic event taxonomy is intentionally small and should be adapted to the local design process.
- AI handoffs are logged as events; this repo does not claim they improve outcomes.

## Next experiments

- Import xAPI or workflow logs from real authoring environments.
- Add conformance checking against a chosen instructional-design model.
- Link process variants to expert review of final learning-design quality.
