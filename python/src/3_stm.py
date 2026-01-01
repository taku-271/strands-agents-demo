from strands import Agent
from strands.models import BedrockModel
from bedrock_agentcore.memory.integrations.strands.config import AgentCoreMemoryConfig
from bedrock_agentcore.memory.integrations.strands.session_manager import AgentCoreMemorySessionManager

model = BedrockModel(
    model_id="us.amazon.nova-2-lite-v1:0",
    max_tokens=4096
)

memory_config = AgentCoreMemoryConfig(
    memory_id="strands_agents_demo_memory-C699uJ8lsm",
    session_id="handson",
    actor_id="me"
)

session_manager = AgentCoreMemorySessionManager(
    agentcore_memory_config=memory_config
)

agent = Agent(
    model=model,
    session_manager=session_manager
)

agent(
    input("質問：")
)