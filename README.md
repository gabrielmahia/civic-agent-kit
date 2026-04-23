# 🛠️ CivicAgentKit — East African Civic AI SDK

> The unified Python toolkit for building civic AI tools in East Africa. One install gives you access to Kenya's parliament records, county budgets, NDMA drought data, M-Pesa payments, and both MCP and A2A protocol integrations.

[![PyPI](https://img.shields.io/pypi/v/civic-agent-kit)](https://pypi.org/project/civic-agent-kit/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![MCP](https://img.shields.io/badge/MCP-Compatible-green)](https://modelcontextprotocol.io)
[![A2A](https://img.shields.io/badge/A2A-Protocol%200.3-blue)](https://github.com/a2aproject/A2A)

## Install

```bash
pip install civic-agent-kit
```

## What's included

```python
from civic_agent_kit import (
    # Data loaders — Kenya's public civic datasets
    KenyaBudgetData,       # Controller of Budget — 47 counties
    KenyaParliamentData,   # MPs, bills, CDF — 13th Parliament
    KenyaSACCOData,        # SASRA SACCO registry
    KenyaDroughtData,      # NDMA drought phases

    # Agents
    BudgetAgent,           # County budget analysis (CrewAI)
    RightsAgent,           # Constitutional rights Q&A (EN/SW)
    DroughtAgent,          # Drought + SMS alert agent

    # Protocols
    KenyaMCPServer,        # MCP server — wraps all Kenya data as MCP tools
    KenyaA2AServer,        # A2A server — Kenya civic skills for agent-to-agent

    # Utils
    KenyaCounties,         # All 47 county codes + names
    KiswahiliTranslator,   # Simple civic term translations EN↔SW
)
```

## Quick examples

**Load county budget data:**
```python
from civic_agent_kit import KenyaBudgetData

budgets = KenyaBudgetData.load()
low_absorption = budgets[budgets['absorption_rate'] < 0.5]
print(low_absorption[['county', 'allocation_kes_m', 'absorption_rate']])
```

**Serve Kenya civic data as an A2A agent:**
```python
from civic_agent_kit import KenyaA2AServer

server = KenyaA2AServer(host="http://localhost:8000")
server.run()  # exposes /.well-known/agent.json + JSON-RPC endpoint
```

**Serve as an MCP server:**
```python
from civic_agent_kit import KenyaMCPServer

# Run alongside mpesa-mcp for full East African AI stack
server = KenyaMCPServer()
server.run()
```

**Ask a rights question in Kiswahili:**
```python
from civic_agent_kit import RightsAgent

agent = RightsAgent(language="sw")
answer = agent.ask("Haki yangu ya ardhi ni nini?")
print(answer)
# → "Kifungu 40: Kila mtu ana haki ya kupata na kumiliki mali..."
```

## The East African AI Stack

```
                    ┌─────────────────────────────────────┐
                    │         Your AI Agent                │
                    └─────────────┬───────────────────────┘
                                  │
               ┌──────────────────┴──────────────────────┐
               │                                          │
        ┌──────▼──────┐                          ┌───────▼──────┐
        │   MCP Layer  │                          │  A2A Layer   │
        │  (tools)     │                          │  (agents)    │
        └──────┬───────┘                          └───────┬──────┘
               │                                          │
     ┌─────────┴──────────┐                   ┌──────────┴─────────┐
     │                    │                   │                     │
┌────▼────┐        ┌──────▼─────┐     ┌───────▼────┐       ┌──────▼──────┐
│mpesa-mcp│        │KenyaMCP    │     │kenya-a2a   │       │CivicAgent   │
│payments │        │civic data  │     │parliament  │       │Kit agents   │
│SMS      │        │budgets     │     │budgets     │       │budget/rights│
│airtime  │        │parliament  │     │drought     │       │drought      │
└─────────┘        └────────────┘     │rights EN/SW│       └─────────────┘
                                      └────────────┘
```

## Data

All data from the Kenya Civic Datasets (CC BY-SA 4.0):
- **Kaggle**: [gmahia/kenya-civic-data](https://kaggle.com/datasets/gmahia/kenya-civic-data-parliament-budget-saccos) — DOI: `10.34740/kaggle/dsv/15473045`
- **HuggingFace**: [gmahia/kenya-civic-data](https://huggingface.co/datasets/gmahia/kenya-civic-data) — DOI: `10.57967/hf/8223`

## Related packages

| Package | Description | PyPI |
|---------|-------------|------|
| `mpesa-mcp` | M-Pesa + Africa's Talking MCP server | [![PyPI](https://img.shields.io/pypi/v/mpesa-mcp)](https://pypi.org/project/mpesa-mcp/) |
| `civic-agent-kit` | This package | [![PyPI](https://img.shields.io/pypi/v/civic-agent-kit)](https://pypi.org/project/civic-agent-kit/) |

## Full portfolio

13 deployed civic apps: [gabrielmahia.github.io](https://gabrielmahia.github.io)

## IP & Collaboration

© 2026 Gabriel Mahia · [contact@aikungfu.dev](mailto:contact@aikungfu.dev)
License: MIT
