# AGENTS.md — CivicAgentKit

Python SDK for East African civic AI.

## Structure
- `src/civic_agent_kit/data.py` — data loaders
- `src/civic_agent_kit/agents.py` — BudgetAgent, RightsAgent, DroughtAgent
- `src/civic_agent_kit/utils.py` — KenyaCounties, KiswahiliTranslator

## Rules
- Never fabricate civic data
- All data must cite sources with DOIs
- MCP/A2A extras are optional installs

<!-- coverage-adaptive-reasoning:v2 -->

## Coverage-Adaptive Reasoning v2

For consequential research, recommendations, investigations, analogy searches, forecasting, opportunity discovery, and canon building:

- A correct ranking inside an incomplete universe is still a failed answer.
- Separate candidate generation from candidate ranking.
- Materiality-gate the search: use the minimum useful set of orthogonal retrieval routes that could change the answer.
- Before closure ask what correct answer the current search method would be structurally incapable of finding.
- Treat aliases, language/geography, era, source class, format, genealogy, taxonomy, legal identity vs operational control/economic benefit, intermediaries, schema categories, null/failure cases, and negative space as potential blind spots when material.
- Maintain leading + competing + null explanations.
- Distinguish answer confidence from coverage confidence.
- “Nothing found” is not evidence of absence when coverage is low.
- Stop when additional independent search routes no longer materially change the candidate universe, hypotheses, decision, or next test.
- When an important miss occurs, repair the retrieval architecture via MISS → SENSOR REDESIGN; do not merely append the missed example.

<!-- v2 section appended 2026-10-28 from https://github.com/gabrielmahia/nairobi-stack/blob/main/docs/COVERAGE_ADAPTIVE_REASONING.md; the rest of this file is unchanged. -->
