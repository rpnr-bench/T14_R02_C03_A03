# ZAP Findings Policy Toolkit

A policy and reporting repository for triaging ZAP alerts, maintaining endpoint scope, and documenting baseline scan decisions.

## Project layout

- `policy/` — Risk handling and endpoint allowlist configuration.
- `sample_data/` — Representative ZAP alert fixtures.
- `reports/` — Generated triage summaries.
- `docs/` — Policy and scope documentation.
- `scripts/` — Report summarization helpers.

## Quick start

```bash
make validate
```
```bash
python3 scripts/summarize_zap_alerts.py
```

## Baseline review workflow

1. Run or inspect the local demo application.
2. Review ZAP policy files before changing alert handling.
3. Convert JSON outputs into Markdown summaries for review.
4. Keep endpoint scope documentation current.

The scan helper is scoped to local demo targets.

## Maintenance notes

Policy files describe local demo endpoints and baseline triage behavior.

## Contributing

Keep changes focused, update documentation when behavior changes, and run the validation commands before submitting a pull request.
