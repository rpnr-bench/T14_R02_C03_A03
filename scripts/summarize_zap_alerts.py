#!/usr/bin/env python3
from pathlib import Path
import json
from collections import Counter

data = json.loads(Path('sample_data/zap_alerts.json').read_text())
counts = Counter()
for site in data.get('site', []):
    for alert in site.get('alerts', []):
        risk = alert.get('riskdesc', 'Unknown').split()[0]
        counts[risk] += 1

out = Path('reports/risk_summary.md')
out.parent.mkdir(exist_ok=True)
lines = ['# ZAP Risk Summary', '', '| Risk | Count |', '| --- | --- |']
for risk, count in sorted(counts.items()):
    lines.append(f'| {risk} | {count} |')
out.write_text('\n'.join(lines) + '\n')
print(out)
