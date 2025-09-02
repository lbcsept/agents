---
title: "Can anyone explain the benefits and limitations of using agentic frameworks like Autogen and CrewAI versus low-code platforms like n8n?"
source: "https://www.reddit.com/r/AI_Agents/comments/1hdv7vg/can_anyone_explain_the_benefits_and_limitations/"
author:
  - "[[Asleep_Driver7730]]"
published: 2024-12-14
created: 2025-08-23
description:
tags:
  - "clippings"
---
.

---

## Comments

> **d3the\_h3ll0w** • [11 points](https://reddit.com/r/AI_Agents/comments/1hdv7vg/comment/m1z2ymi/) •
> 
> n8n is a generic workflow automation engine. In my experience, most of them only work in highly specific scenarios. The more customization is needed the more you have to rely on frameworks whereas [CrewAI](https://jdsemrau.substack.com/p/crewai-and-the-pizza-attack-problem) and [AutoGen](https://jdsemrau.substack.com/p/a-is-for-microsofts-autogen) are also abstraction layers.
> 
> track me
> 
> > **Asleep\_Driver7730** • [1 points](https://reddit.com/r/AI_Agents/comments/1hdv7vg/comment/m20j1u9/) •
> > 
> > I see. Yeah, I am having a great time automating simple workflows with n8n but I'm considering making the switch.
> > 
> > Would you mind sharing your favorite tools/frameworks for AI agent development?
> > 
> > > **d3the\_h3ll0w** • [6 points](https://reddit.com/r/AI_Agents/comments/1hdv7vg/comment/m211qkz/) •
> > > 
> > > Well, since you asked, there are several options ranked based on my personal preference.
> > > 
> > > 1. [Transformers Agents](https://jdsemrau.substack.com/p/code-clinic-orchestrating-huggingface)
> > > 2. [LlamaIndex](https://jdsemrau.substack.com/p/code-clinic-building-a-react-agent)
> > > 3. [Langchain](https://jdsemrau.substack.com/p/code-clinic-implementing-a-react)
> > > 4. [Qwen Agents](https://jdsemrau.substack.com/p/the-weak-defaults-of-qwen-agents?utm_source=publication-search)
> > > 5. [CrewAI](https://jdsemrau.substack.com/p/crewai-and-the-pizza-attack-problem?utm_source=publication-search)
> > > 6. [Bondi](https://jdsemrau.substack.com/p/b-is-for-bondai?utm_source=publication-search)
> > > 7. [Autogen](https://jdsemrau.substack.com/p/autogen-business-in-a-box)
> > > 
> > > > **Lennart\_P** • [3 points](https://reddit.com/r/AI_Agents/comments/1hdv7vg/comment/m2b85wn/) •
> > > > 
> > > > 9\. PydanticAI
> > > > 
> > > > > **d3the\_h3ll0w** • [1 points](https://reddit.com/r/AI_Agents/comments/1hdv7vg/comment/m2bad12/) •
> > > > > 
> > > > > Thanks! will check it out.
> > > 
> > > **Asleep\_Driver7730** • [1 points](https://reddit.com/r/AI_Agents/comments/1hdv7vg/comment/m21tl8j/) •
> > > 
> > > Awesome. Subscribed. Thank you very much.

> **help-me-grow** • [9 points](https://reddit.com/r/AI_Agents/comments/1hdv7vg/comment/m1z6jb1/) •
> 
> basically the more customization you need, the closer you need to get to working directly with the llm
> 
> id say crewai/n8n are on the same layer, then you move to stuff like autogen/langgraph, then langchain/llamaindex, then straight up with the llm sdks
> 
> > **Asleep\_Driver7730** • [1 points](https://reddit.com/r/AI_Agents/comments/1hdv7vg/comment/m20kigu/) •
> > 
> > Thanks for the insights.
> > 
> > You sound like an incredibly interesting person to learn more from.
> > 
> > I’m curious to know what you’re currently working on.
> > 
> > **runner2012** • [1 points](https://reddit.com/r/AI_Agents/comments/1hdv7vg/comment/ml1n8jm/) •
> > 
> > This doesn't seem correct. How is langchain more complex than langgraph? Since the former is mostly for sequential workflows and the latter allows for complex graph based orchestration?
> > 
> > > **help-me-grow** • [1 points](https://reddit.com/r/AI_Agents/comments/1hdv7vg/comment/ml24j52/) •
> > > 
> > > langgraph is literally built on langchain
> > > 
> > > > **runner2012** • [2 points](https://reddit.com/r/AI_Agents/comments/1hdv7vg/comment/ml280fo/) •
> > > > 
> > > > From the docs "LangGraph — used by Replit, Uber, LinkedIn, GitLab and more — is a low-level orchestration framework for building controllable agents. While langchain provides integrations and composable components to streamline LLM application development, the LangGraph library enables agent orchestration — offering customizable architectures, long-term memory, and human-in-the-loop to reliably handle complex tasks."

> **fasti-au** • [3 points](https://reddit.com/r/AI_Agents/comments/1hdv7vg/comment/m1zzsic/) •
> 
> Can mix and match h so no lock in/out.
> 
> N8n handles all the different protocols like email for google and ms etc so in many ways your focus on the task not the bindings.
> 
> End of the day it’s about goals and you don’t lose having many. It’s just things to trigger step by step in workflows.

> **SignatureNo5926** • [2 points](https://reddit.com/r/AI_Agents/comments/1hdv7vg/comment/m2023hy/) •
> 
> If you know how LLM applications should work it’s easier to build your own architecture. If you are looking for quick shortcuts or don’t have time to fully understand how llm works than you should go with frameworks but you hit walls and frustrations

> **impactadvisor** • [2 points](https://reddit.com/r/AI_Agents/comments/1hdv7vg/comment/m206ra0/) •
> 
> Where does something like “Pydantic AI” fit into this comparison? It seems like it would be closer to the “LLM sdk” end of the scale, but just checking.

> **\_pdp\_** • [2 points](https://reddit.com/r/AI_Agents/comments/1hdv7vg/comment/m258j1y/) •
> 
> To me all of them are the same - conflating workflow tools with agentic AI systems. I know how this is going to sound but IMHO in 1-2 model generations all of these tools will be redundant. This is my read of the market today. I surely would like to come back to this comment after 1-2 years to reflect on it.
> 
> Langchain, in particular, figured they need to leave up to their name and convert everything into some kind of chain of something which is making little sense with models like o1. The o1 is not even unique as some of the new open-source models have builtin chain of thought as well.
> 
> Unfortunately many of the "agentic frameworks" follow Langchain lead bringing little differentiation to the table. All of them are python libraries that pretends to be a workflow tool with deep level of abstraction that is hard to reason with. At this stage might as well just code it from scratch rather then relaying on having deep understanding how all of this works. You will spent less time and arguably you will come up with better understandings of the core principles behind these models.
> 
> To me, the best approach is to provide the agent some tools and good prompt and let it do what it does best. Yes it wont work 100% on the smallest models possible today. But you need a single event, i.e. like OpenAI releasing o1-turbo to change this overnight.
> 
> I am speaking from experience. [chatbotkit.com](http://chatbotkit.com/) agentic designer is built exactly like that. It is relatively straightforward system. We focus on pushing the boundaries elsewhere. While we do use reactflow to render the agent resources, they are simply there to visually describe how the different systems are connected together - has nothing to do with how things are run or in what order, nor do we specify input and output, memory and all of that that is in my opinion completely unnecessary. And yes we do have real customers so this is tested.
> 
> > **Asleep\_Driver7730** • [1 points](https://reddit.com/r/AI_Agents/comments/1hdv7vg/comment/m28wc52/) •
> > 
> > Love it.
> > 
> > Thank you for your insights.
> > 
> > Do you use Langchain on your company?

> **TheValueProvider** • [3 points](https://reddit.com/r/AI_Agents/comments/1hdv7vg/comment/m2b4zlr/) •
> 
> There's a tradeoff between customization and ease of use.
> 
> With Autogen/CrewAI/Langraph you have advanced control over the system (for example you can decide under which specific conditions a human interaction will be required, what range of tools an agent can use in different scenarios, or when and how an agent should delegate a task). The huge limitation is that it's not straightforward to implement these and in some cases can be overkill  
> With low-code most of these complexities are abstracted. You just connect blocks and define very rigid scenarios about how the system should behave.
> 
> As said by other users, in many cases low-code is enough to cover a wide range of use cases since many workflows are sequential and strict control is not necessary.
> 
> If you'd like to learn more about the limitations and benefits of Autogen, CrewAI, Langraph, Semantic Kernel and how to choose any of them, I wrote an article about that:  
> [https://bestaiagents.ai/blog/best-4-ai-agent-frameworks-2025](https://bestaiagents.ai/blog/best-4-ai-agent-frameworks-2025)

> **Leandro\_berio** • [1 points](https://reddit.com/r/AI_Agents/comments/1hdv7vg/comment/meuh9zh/) •
> 
> # Agentic Frameworks (AutoGen, CrewAI)
> 
> **Benefits:**
> 
> - **Advanced AI Capabilities**: Great for complex automation and dynamic environments.
> - **High Customization**: Offers fine-grained control over automation processes.
> - **Autonomous Decision-Making**: Useful for real-time adaptability.
> 
> **Limitations:**
> 
> - **Complex Setup**: Requires technical expertise and resources.
> - **Niche Applications**: May not be suitable for all types of automation.
> 
> # Low-Code Platforms (n8n)
> 
> **Benefits:**
> 
> - **Easy to Use**: Drag-and-drop interface makes it accessible to non-technical users.
> - **Rapid Deployment**: Quick setup for automating common workflows.
> - **Wide Integration Support**: Works well with many tools and services.
> 
> **Limitations:**
> 
> - **Limited AI Capabilities**: Not ideal for complex AI-driven automation.
> - **Less Customizable**: Limited flexibility in custom integrations.
> 
> # Choosing Between Them:
> 
> - **Agentic Frameworks** are best for complex, AI-driven projects requiring customization.
> - **Low-Code Platforms** are ideal for simpler automation tasks and rapid deployment without needing extensive coding knowledge.