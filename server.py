from datetime import datetime

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo-server")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Tel twee getallen op."""
    return a + b


@mcp.tool()
def get_time() -> str:
    """Geef huidige datum en tijd terug."""
    return datetime.now().isoformat()


@mcp.tool()
def greet(name: str) -> str:
    """Groet iemand bij naam."""
    return f"Hallo, {name}!"


if __name__ == "__main__":
    mcp.run(transport="stdio")
