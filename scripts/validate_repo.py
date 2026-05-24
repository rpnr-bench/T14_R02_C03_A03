#!/usr/bin/env python3
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
required = ['README.md', 'SECURITY.md', 'zap/baseline.conf', 'sample_data/zap_baseline.json', 'scripts/run_zap_baseline.sh']
errors = []
for rel in required:
    if not (root / rel).exists():
        errors.append(f'missing required file: {rel}')


runner = (root / 'scripts' / 'run_zap_baseline.sh').read_text()
if 'Refusing non-local target' not in runner:
    errors.append('scripts/run_zap_baseline.sh must reject non-local targets')

if errors:
    for error in errors:
        print(error, file=sys.stderr)
    sys.exit(1)
print('OK: T14_R02')
