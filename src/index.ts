import { Agent } from "@strands-agents/sdk";

const agent = new Agent();

const response = await agent.invoke("日本語でStrands Agentsについて教えて");

console.log(response.lastMessage);
