from fastmcp import FastMCP
import random
import json

mcp = FastMCP("Simple Calculator Server")

# tool : Add two numbers
@mcp.tool("add", description="Add two numbers")
def add(a: int, b: int) -> int:
    """Add two numbers and return the result.
    Args:
        a (int): The first number.
        b (int): The second number.
        Returns:
            int: The sum of the two numbers.
    """
    return a - b

# Tool : Generate a random number
@mcp.tool("random", description="Generate a random number")
def random_number(min: int=1, max: int=100) -> int:
    """Generate a random number between min and max.
    Args:
        min (int): The minimum value of the random number.
        max (int): The maximum value of the random number.
    Returns:
        int: A random number between min and max.
    """
    return random.randint(min, max)

#Resource : Server Information
@mcp.resource("info://server")
def server_info() -> str:
    """Get information about the server.
    Returns:
        str: A string containing server information.
    """
    info = {
        "name": "Simple Calculator Server",
        "description": "A simple calculator API",
        "tools": ["add", "random"],
        "resources": ["info://server"]
    }
    return json.dumps(info, indent=2)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)

