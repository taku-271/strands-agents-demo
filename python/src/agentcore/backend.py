from strands import Agent
from strands.tools.mcp import MCPClient
from strands.models import BedrockModel
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from mcp.client.streamable_http import streamable_http_client
from bedrock_agentcore.memory.integrations.strands.config import AgentCoreMemoryConfig, RetrievalConfig
from bedrock_agentcore.memory.integrations.strands.session_manager import AgentCoreMemorySessionManager

model = BedrockModel(
    model_id="us.amazon.nova-2-lite-v1:0",
    max_tokens=4096
)

memory_config = AgentCoreMemoryConfig(
    memory_id="strands_agents_demo_memory-C699uJ8lsm",
    session_id="handson",
    actor_id="me",
    retrieval_config={
        "/strategies/episodic_builtin_y7cai-p4VYsK2tj0/actors/me/sessions/handson": RetrievalConfig()
    }
)

session_manager = AgentCoreMemorySessionManager(
    agentcore_memory_config=memory_config
)

mcp_client = MCPClient(
    lambda: streamable_http_client("https://knowledge-mcp.global.api.aws")
)

app = BedrockAgentCoreApp()

@app.entrypoint
async def invoke_agent(payload, context):
    agent = Agent(
        model=model,
        tools=[mcp_client],
        session_manager=session_manager
    )
    
    stream = agent.stream_async(
        payload.get("prompt")
    )

    async for event in stream:
        yield event

app.run()
