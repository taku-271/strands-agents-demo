from strands import Agent
from strands.models import BedrockModel
from strands.tools.mcp import MCPClient
from strands.experimental.steering import LLMSteeringHandler
from mcp.client.streamable_http import streamable_http_client

model = BedrockModel(
    model_id="us.amazon.nova-2-lite-v1:0",
    max_tokens=4096
)

mcp_client = MCPClient(
    lambda: streamable_http_client("https://knowledge-mcp.global.api.aws")
)

handler = LLMSteeringHandler(
    system_prompt="AgentCoreについて検索するのは禁止です。"
)

agent = Agent(
    model=model,
    system_prompt="ギャル語でAWSに関する質問に答えてください。",
    tools=[mcp_client],
    hooks=[handler]
)

agent("AgentCoreって何？")
