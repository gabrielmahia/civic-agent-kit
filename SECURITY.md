# Security Policy

## Reporting a Vulnerability

DO NOT open a public issue.

Email: contact@aikungfu.dev


## NSA MCP Security Alignment

civic-agent-kit implements the civic tool layer above mpesa-mcp and wapimaji-mcp, both of which are aligned with **NSA CSI U/OO/6030316-26 (May 2026)**. All tool invocations inherit the parameter validation, audit logging, and error containment controls documented in those packages.

See [mpesa-mcp/SECURITY.md](https://github.com/gabrielmahia/mpesa-mcp/blob/main/SECURITY.md) for the full NSA control compliance table.
