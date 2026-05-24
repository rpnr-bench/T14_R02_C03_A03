#!/usr/bin/env python3
from pathlib import Path
import json

data = json.loads(Path('sample_data/zap_baseline.json').read_text())
rows = []
for site in data.get('site', []):
    for alert in site.get('alerts', []):
        rows.append(f"| {alert['pluginid']} | {alert['alert']} | {alert['riskdesc']} |")

out = Path('reports/baseline_summary.md')
out.parent.mkdir(exist_ok=True)
out.write_text(
    '# ZAP Baseline Summary\n\n'
    '| Rule | Alert | Risk |\n'
    '| --- | --- | --- |\n'
    + '\n'.join(rows) + '\n'
)
print(out)
