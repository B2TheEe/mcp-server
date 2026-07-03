# mcp-server

Demo MCP (Model Context Protocol) server built with `fastmcp`. Exposes simple tools over stdio.

## Tools

- `add(a, b)` — sum two integers
- `get_time()` — current date/time (ISO format)
- `greet(name)` — greet by name

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install mcp
```

## Run

```bash
python server.py
```

Runs over stdio transport — connect from an MCP client (e.g. Claude Desktop) rather than invoking directly.
