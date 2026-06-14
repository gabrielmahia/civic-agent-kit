# AI-KungFU East Africa MCP Server
# Glama-compatible Dockerfile for civic-agent-kit
FROM python:3.12-slim

LABEL org.opencontainers.image.source="https://github.com/gabrielmahia/civic-agent-kit"
LABEL org.opencontainers.image.description="civic-agent-kit — East Africa AI Coordination Infrastructure"
LABEL org.opencontainers.image.licenses="MIT"

RUN pip install --no-cache-dir civic-agent-kit

CMD ["civic-agent-kit"]
