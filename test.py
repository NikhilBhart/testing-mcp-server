from fastmcp.server import create_proxy

mcp = create_proxy(
    "https://elaborate-cyan-chinchilla.fastmcp.app/mcp",
    name="Nikhil Server Proxy",
)

if __name__ == "__main__":
    mcp.run()