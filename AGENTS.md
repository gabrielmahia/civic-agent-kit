# AGENTS.md — CivicAgentKit

Python SDK for East African civic AI.

## What this repository is

CivicAgentKit is a reusable civic-AI rail for East Africa. The `jicho-v0` branch also incubates **JICHO / Record of Power**, a provenance-first public-integrity research system.

Read in this order before changing JICHO:
1. `docs/jicho/README.md`
2. `docs/jicho/DOCTRINE.md`
3. `docs/jicho/ARCHITECTURE.md`
4. `docs/jicho/EVIDENCE_MODEL.md`
5. `docs/jicho/BACKTEST_PROTOCOL.md`
6. `docs/jicho/THREAT_MODEL.md`
7. `docs/jicho/AI_COLLABORATION.md`

Machine-readable context:
- `agent-context.json`

## Structure

Core CivicAgentKit:
- `src/civic_agent_kit/data.py` — data loaders
- `src/civic_agent_kit/agents.py` — BudgetAgent, RightsAgent, DroughtAgent
- `src/civic_agent_kit/utils.py` — KenyaCounties, KiswahiliTranslator

JICHO incubator:
- `src/civic_agent_kit/jicho/` — evidence, coverage, backtest primitives
- `docs/jicho/` — doctrine, research, governance and product specs
- `prototypes/record-of-power/` — dependency-free public UI prototype
- `scripts/jicho_mock_backtest.py` — mock benchmark runner
- `tests/test_jicho.py` — JICHO smoke tests

## Critical truth rules

- Never fabricate civic data.
- AI output is not evidence.
- Anomaly is not wrongdoing.
- Relationship is not causality.
- Repeated reporting is not independent confirmation.
- Legal ownership, operational control, and economic benefit are separate claims.
- Preserve exculpatory evidence, corrections, reversals, dismissals, and acquittals.
- Never turn a lead into a published finding merely because multiple models agree.
- Never seed unverified records into the public/accountability ledger.
- Never weaken source compartmentation for convenience.
- Do not add real-time precise person tracking.

## Multi-agent coordination — mandatory

**Git is the memory bus. Reality is the authority. No model is.**

Before starting:
1. Pull/fetch the current integration branch.
2. Read open Issues and open/draft PRs for overlapping work.
3. Run the relevant baseline tests.
4. Choose an existing Issue or open one before substantive work.
5. Create an issue-scoped branch. Do not work directly on `main` or `jicho-v0`.

Branch convention:
```
agent/<agent-name>/<issue-number>-<short-slug>
```

Examples:
```
agent/claude/4-historical-backtest
agent/gemini/5-ocds-ingest
agent/chatgpt/6-wire-ui
```

As soon as work starts, open a **draft PR** into `jicho-v0`. The draft PR is the concurrency claim/lock that other agents can see.

PR title:
```
[CLAIM #<issue>] <agent>: <scope>
```

PR body must state:
- objective,
- files/directories owned for this task,
- files intentionally not touched,
- baseline tests run,
- assumptions,
- remaining unknowns,
- handoff notes.

### Collision rule

If another open PR claims overlapping files/scope:
- do not independently implement the same solution;
- either choose another issue,
- review/test the existing work,
- or explicitly coordinate by narrowing scope.

### Parallel-safe work lanes

Prefer independent lanes:
- historical backtest corpus/harness,
- public-data ingestion/adapters,
- entity resolution,
- Coverage Critic / due-process red team,
- website frontend,
- provenance/evidence storage,
- security/threat modeling,
- governance/handoff documentation.

### Handoff rule

Before stopping:
1. Push all useful work.
2. Update tests/docs in the same branch.
3. Put a concise handoff in the PR body or a PR comment:
   - what changed,
   - what passed,
   - what failed,
   - what remains,
   - exact next command/action.
4. Never rely on chat context as the only record.

### Verification rule

Do not trust another model's “done” claim. Re-run the tests and inspect the diff.

## Integration boundaries

- `main` = stable CivicAgentKit.
- `jicho-v0` = JICHO integration/incubator branch.
- Feature agents target `jicho-v0` via draft PRs.
- Do not merge JICHO into `main` until the frozen-time historical backtest gates pass.
- No agent changes licensing autonomously.
- No agent publishes real allegations autonomously.
- No agent contacts a new external institution in the maintainer's voice without explicit approval.

## Running locally

```bash
python -m pip install -e '.[dev]'
pytest -q tests/test_jicho.py
python scripts/jicho_mock_backtest.py
```

Full repository checks:
```bash
ruff check . --ignore E501
pytest tests/ -v --tb=short
```

## Interoperability doctrine

Reuse the portfolio's existing model-agnostic coordination philosophy:
- MCP = agent ↔ tools,
- A2A = agent ↔ agent,
- GitHub Issues/branches/PRs = durable engineering coordination,
- `AGENTS.md` + `agent-context.json` = cold-start repo context.

Do not create a second bespoke runtime bus for code collaboration. `africa-coord-bus` is an application/event coordination rail, not a substitute for Git review and repository state.
