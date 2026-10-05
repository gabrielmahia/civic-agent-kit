import json
from dataclasses import asdict

from civic_agent_kit.jicho.backtest import diagnostic, run_case
from civic_agent_kit.jicho.fixtures import all_cases

rows=[]
for case in all_cases():
    result=run_case(case)
    rows.append({**asdict(result), **diagnostic(case)})
print(json.dumps(rows, indent=2))
