import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";
import { Agent, BedrockModel, McpClient, tool } from "@strands-agents/sdk";
import z from "zod";

const model = new BedrockModel({
    modelId: "us.amazon.nova-2-lite-v1:0",
    maxTokens: 4096,
});

// const awsKnowledgeTools = new McpClient({
//     transport: new StreamableHTTPClientTransport(new URL("https://knowledge-mcp.global.api.aws")),
// });

const agent = new Agent({
    model,
    // tools: [awsKnowledgeTools],
});

const response = await agent.invoke("眠気を覚ます方法を教えて");

console.log(response.lastMessage);
