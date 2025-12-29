import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";
import { Agent, BedrockModel, McpClient, tool } from "@strands-agents/sdk";
import z from "zod";

const model = new BedrockModel({
    region: "us-east-1",
    maxTokens: 4096,
    temperature: 0.7,
});

const currentTempertureTool = tool({
    name: "current_temperture",
    description: "Get the current temperature of a city",
    inputSchema: z.object({
        city: z.string().describe("The name of the city to get the temperature for"),
    }),
    callback: (input) => {
        return 20.0;
    }
});

const awsKnowledgeTools = new McpClient({
    transport: new StreamableHTTPClientTransport(new URL("https://knowledge-mcp.global.api.aws")),
});

const agent = new Agent({
    model,
    tools: [currentTempertureTool, awsKnowledgeTools],
});

const response = await agent.invoke("DynamoDBについて日本語で教えてください。");

console.log(response.lastMessage);
