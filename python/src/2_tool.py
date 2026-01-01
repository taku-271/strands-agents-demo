from strands import Agent
from strands.models import BedrockModel
from strands.tools.mcp import MCPClient
from mcp.client.streamable_http import streamablehttp_client

model = BedrockModel(
    model_id="us.amazon.nova-2-lite-v1:0",
    max_tokens=4096
)

mcp_client = MCPClient(
    lambda: streamablehttp_client(
        "https://knowledge-mcp.global.api.aws"
    )
)

agent = Agent(
    model=model,
    tools=[mcp_client]
)

agent(
    input("質問：")
)
