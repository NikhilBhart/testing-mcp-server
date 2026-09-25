from fastmcp import FastMCP
import random
import json

mcp = FastMCP("Simple Calculator Server")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers.

    Args:
        a: First number,
        b: Second number.
        
        Returns the sum of a and b.
    """
    return a + b

# Tool: Generate a random number
@mcp.tool
def random_number(min_value: int = 1, max_value: int = 100) -> int:
    """Generate a random number between min_value and max_value.

    Args:
        min_value: Minimum value (inclusive),
        max_value: Maximum value (inclusive).
        
        Returns a random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

# Resource: Server information
@mcp.resource("info://server")
def server_info() -> str:
    """Return server information as a JSON string."""
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0",
        "description": "A simple calculator server that can add numbers and generate random numbers.",
        "tools": ["add", "random_number"],
        "author": "Your Name"
    }
    return json.dumps(info, indent=2)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)