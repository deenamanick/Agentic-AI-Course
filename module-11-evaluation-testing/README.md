# Module 11 — Agent Evaluation and Testing

## Goal

Replace demo-driven development with repeatable evidence.

## Topics

- Golden datasets and scenario design
- Unit, contract, integration, and end-to-end tests
- Structured-output and tool-argument correctness
- Tool-selection and task-completion metrics
- Retrieval precision, recall, and groundedness
- Trajectory and handoff evaluation
- LLM-as-judge calibration and bias
- Regression gates, latency, and cost budgets

## Practicals

1. [Build a golden evaluation dataset](module-11-1-golden-dataset.md)
2. [Test tools and execution trajectories](module-11-2-trajectory-tests.md)
3. [Add deterministic and model-based graders](module-11-3-graders.md)
4. [Create regression and budget gates](module-11-4-regression-gates.md)

## Deliverable

An automated evaluation harness that produces a JSON and Markdown report suitable for CI.

## Completion criteria

- Critical safety cases must pass 100%.
- Quality regressions and budget overruns cause a non-zero exit.
- Model-based grading is checked against a human-reviewed sample.
