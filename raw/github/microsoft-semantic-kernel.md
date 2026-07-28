# microsoft/semantic-kernel

## Metadata
- Stars: 28378
- Primary language: C#
- Default branch: main
- Latest release: dotnet-1.78.0 (2026-07-07)
- License: MIT License
- Homepage: https://aka.ms/semantic-kernel
- Fetched: 2026-07-28
- Final URL: https://github.com/microsoft/semantic-kernel

## Description
Integrate cutting-edge LLM technology quickly and easily into your apps

> **Deprecation notice (from README):** Semantic Kernel is now [Microsoft Agent Framework](https://github.com/microsoft/agent-framework). Microsoft Agent Framework (MAF) is the enterprise-ready successor to Semantic Kernel, available at version 1.0 as a production-ready release with stable APIs and long-term support commitment. See the [migration guide](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel).

## README
# Semantic Kernel

> [!IMPORTANT]
> Semantic Kernel is now [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)! Microsoft Agent Framework (MAF) is the enterprise‑ready successor to Semantic Kernel. Microsoft Agent Framework is now available at version 1.0 as a production-ready release: stable APIs, and a commitment to long-term support. Whether you're building a single assistant or orchestrating a fleet of specialized agents, Microsoft Agent Framework 1.0 gives you enterprise-grade multi-agent orchestration, multi-provider model support, and cross-runtime interoperability via A2A and MCP.
>
> Learn more about Semantic Kernel and Agent Framework here: [Semantic Kernel and Microsoft Agent Framework on the Agent Framework blog](https://devblogs.microsoft.com/agent-framework/semantic-kernel-and-microsoft-agent-framework/), and try out the [Semantic Kernel migration guide](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel).

**Build intelligent AI agents and multi-agent systems with this enterprise-ready orchestration framework**

[![License: MIT](https://img.shields.io/github/license/microsoft/semantic-kernel)](https://github.com/microsoft/semantic-kernel/blob/main/LICENSE)
[![Python package](https://img.shields.io/pypi/v/semantic-kernel)](https://pypi.org/project/semantic-kernel/)
[![Nuget package](https://img.shields.io/nuget/vpre/Microsoft.SemanticKernel)](https://www.nuget.org/packages/Microsoft.SemanticKernel/)
[![Discord](https://img.shields.io/discord/1063152441819942922?label=Discord&logo=discord&logoColor=white&color=d82679)](https://aka.ms/SKDiscord)

## What is Semantic Kernel?

Semantic Kernel is a model-agnostic SDK that empowers developers to build, orchestrate, and deploy AI agents and multi-agent systems. Whether you're building a simple chatbot or a complex multi-agent workflow, Semantic Kernel provides the tools you need with enterprise-grade reliability and flexibility.

## System Requirements

- **Python**: 3.10+
- **.NET**: .NET 10.0+
- **Java**: JDK 17+
- **OS Support**: Windows, macOS, Linux

## Key Features

- **Model Flexibility**: Connect to any LLM with built-in support for [OpenAI](https://platform.openai.com/docs/introduction), [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service), [Hugging Face](https://huggingface.co/), [NVidia](https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/) and more
- **Agent Framework**: Build modular AI agents with access to tools/plugins, memory, and planning capabilities
- **Multi-Agent Systems**: Orchestrate complex workflows with collaborating specialist agents
- **Plugin Ecosystem**: Extend with native code functions, prompt templates, OpenAPI specs, or Model Context Protocol (MCP)
- **Vector DB Support**: Seamless integration with [Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search), [Elasticsearch](https://www.elastic.co/), [Chroma](https://docs.trychroma.com/docs/overview/getting-started), and more
- **Multimodal Support**: Process text, vision, and audio inputs
- **Local Deployment**: Run with [Ollama](https://ollama.com/), [LMStudio](https://lmstudio.ai/), or [ONNX](https://onnx.ai/)
- **Process Framework**: Model complex business processes with a structured workflow approach
- **Enterprise Ready**: Built for observability, security, and stable APIs

## Installation

First, set the environment variable for your AI Services:

**Azure OpenAI:**
```bash
export AZURE_OPENAI_API_KEY=AAA....
```

**or OpenAI directly:**
```bash
export OPENAI_API_KEY=sk-...
```

### Python

```bash
pip install semantic-kernel
```

### .NET

```bash
dotnet add package Microsoft.SemanticKernel
dotnet add package Microsoft.SemanticKernel.Agents.Core
```

### Java

See [semantic-kernel-java build](https://github.com/microsoft/semantic-kernel-java/blob/main/BUILD.md) for instructions.

## Quickstart

### Basic Agent - Python

Create a simple assistant that responds to user prompts:

```python
import asyncio
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

async def main():
    # Initialize a chat agent with basic instructions
    agent = ChatCompletionAgent(
        service=AzureChatCompletion(),
        name="SK-Assistant",
        instructions="You are a helpful assistant.",
    )

    # Get a response to a user message
    response = await agent.get_response(messages="Write a haiku about Semantic Kernel.")
    print(response.content)

asyncio.run(main())

# Output:
# Language's essence,
# Semantic threads intertwine,
# Meaning's core revealed.
```

### Basic Agent - .NET

```csharp
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Agents;

var builder = Kernel.CreateBuilder();
builder.AddAzureOpenAIChatCompletion(
                Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT"),
                Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT"),
                Environment.GetEnvironmentVariable("AZURE_OPENAI_API_KEY")
                );
var kernel = builder.Build();

ChatCompletionAgent agent =
    new()
    {
        Name = "SK-Agent",
        Instructions = "You are a helpful assistant.",
        Kernel = kernel,
    };

await foreach (AgentResponseItem<ChatMessageContent> response
    in agent.InvokeAsync("Write a haiku about Semantic Kernel."))
{
    Console.WriteLine(response.Message);
}

// Output:
// Language's essence,
// Semantic threads intertwine,
// Meaning's core revealed.
```

### Agent with Plugins - Python

Enhance your agent with custom tools (plugins) and structured output:

```python
import asyncio
from typing import Annotated
from pydantic import BaseModel
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, OpenAIChatPromptExecutionSettings
from semantic_kernel.functions import kernel_function, KernelArguments

class MenuPlugin:
    @kernel_function(description="Provides a list of specials from the menu.")
    def get_specials(self) -> Annotated[str, "Returns the specials from the menu."]:
        return """
        Special Soup: Clam Chowder
        Special Salad: Cobb Salad
        Special Drink: Chai Tea
        """

    @kernel_function(description="Provides the price of the requested menu item.")
    def get_item_price(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns the price of the menu item."]:
        return "$9.99"

class MenuItem(BaseModel):
    price: float
    name: str

async def main():
    # Configure structured output format
    settings = OpenAIChatPromptExecutionSettings()
    settings.response_format = MenuItem

    # Create agent with plugin and settings
    agent = ChatCompletionAgent(
        service=AzureChatCompletion(),
        name="SK-Assistant",
        instructions="You are a helpful assistant.",
        plugins=[MenuPlugin()],
        arguments=KernelArguments(settings)
    )

    response = await agent.get_response(messages="What is the price of the soup special?")
    print(response.content)

    # Output:
    # The price of the Clam Chowder, which is the soup special, is $9.99.

asyncio.run(main())
```

### Agent with Plugin - .NET

```csharp
using System.ComponentModel;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Agents;
using Microsoft.SemanticKernel.ChatCompletion;

var builder = Kernel.CreateBuilder();
builder.AddAzureOpenAIChatCompletion(
                Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT"),
                Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT"),
                Environment.GetEnvironmentVariable("AZURE_OPENAI_API_KEY")
                );
var kernel = builder.Build();

kernel.Plugins.Add(KernelPluginFactory.CreateFromType<MenuPlugin>());

ChatCompletionAgent agent =
    new()
    {
        Name = "SK-Assistant",
        Instructions = "You are a helpful assistant.",
        Kernel = kernel,
        Arguments = new KernelArguments(new PromptExecutionSettings() { FunctionChoiceBehavior = FunctionChoiceBehavior.Auto() })

    };

await foreach (AgentResponseItem<ChatMessageContent> response
    in agent.InvokeAsync("What is the price of the soup special?"))
{
    Console.WriteLine(response.Message);
}

sealed class MenuPlugin
{
    [KernelFunction, Description("Provides a list of specials from the menu.")]
    public string GetSpecials() =>
        """
        Special Soup: Clam Chowder
        Special Salad: Cobb Salad
        Special Drink: Chai Tea
        """;

    [KernelFunction, Description("Provides the price of the requested menu item.")]
    public string GetItemPrice(
        [Description("The name of the menu item.")]
        string menuItem) =>
        "$9.99";
}
```

### Multi-Agent System - Python

Build a system of specialized agents that can collaborate:

```python
import asyncio
from semantic_kernel.agents import ChatCompletionAgent, ChatHistoryAgentThread
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, OpenAIChatCompletion

billing_agent = ChatCompletionAgent(
    service=AzureChatCompletion(),
    name="BillingAgent",
    instructions="You handle billing issues like charges, payment methods, cycles, fees, discrepancies, and payment failures."
)

refund_agent = ChatCompletionAgent(
    service=AzureChatCompletion(),
    name="RefundAgent",
    instructions="Assist users with refund inquiries, including eligibility, policies, processing, and status updates.",
)

triage_agent = ChatCompletionAgent(
    service=OpenAIChatCompletion(),
    name="TriageAgent",
    instructions="Evaluate user requests and forward them to BillingAgent or RefundAgent for targeted assistance."
    " Provide the full answer to the user containing any information from the agents",
    plugins=[billing_agent, refund_agent],
)

thread: ChatHistoryAgentThread = None

async def main() -> None:
    print("Welcome to the chat bot!\n  Type 'exit' to exit.\n  Try to get some billing or refund help.")
    while True:
        user_input = input("User:> ")

        if user_input.lower().strip() == "exit":
            print("\n\nExiting chat...")
            return False

        response = await triage_agent.get_response(
            messages=user_input,
            thread=thread,
        )

        if response:
            print(f"Agent :> {response}")

# Agent :> I understand that you were charged twice for your subscription last month, and I'm here to assist you with resolving this issue. Here's what we need to do next:

# 1. **Billing Inquiry**:
#    - Please provide the email address or account number associated with your subscription, the date(s) of the charges, and the amount charged. This will allow the billing team to investigate the discrepancy in the charges.

# 2. **Refund Process**:
#    - For the refund, please confirm your subscription type and the email address associated with your account.
#    - Provide the dates and transaction IDs for the charges you believe were duplicated.

# Once we have these details, we will be able to:

# - Check your billing history for any discrepancies.
# - Confirm any duplicate charges.
# - Initiate a refund for the duplicate payment if it qualifies. The refund process usually takes 5-10 business days after approval.

# Please provide the necessary details so we can proceed with resolving this issue for you.


if __name__ == "__main__":
    asyncio.run(main())
```

## Where to Go Next

1. 📖 Try our [Getting Started Guide](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide) or learn about [Building Agents](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/)
2. 🔌 Explore over 100 [Detailed Samples](https://learn.microsoft.com/en-us/semantic-kernel/get-started/detailed-samples)
3. 💡 Learn about core Semantic Kernel [Concepts](https://learn.microsoft.com/en-us/semantic-kernel/concepts/kernel)

### API References

- [C# API reference](https://learn.microsoft.com/en-us/dotnet/api/microsoft.semantickernel?view=semantic-kernel-dotnet)
- [Python API reference](https://learn.microsoft.com/en-us/python/api/semantic-kernel/semantic_kernel?view=semantic-kernel-python)

## Troubleshooting

### Common Issues

- **Authentication Errors**: Check that your API key environment variables are correctly set
- **Model Availability**: Verify your Azure OpenAI deployment or OpenAI model access

### Getting Help

- Check our [GitHub issues](https://github.com/microsoft/semantic-kernel/issues) for known problems
- Search the [Discord community](https://aka.ms/SKDiscord) for solutions
- Include your SDK version and full error messages when asking for help

## Join the community

We welcome your contributions and suggestions to the SK community! One of the easiest ways to participate is to engage in discussions in the GitHub repository. Bug reports and fixes are welcome!

For new features, components, or extensions, please open an issue and discuss with us before sending a PR. This is to avoid rejection as we might be taking the core in a different direction, but also to consider the impact on the larger ecosystem.

To learn more and get started:

- Read the [documentation](https://aka.ms/sk/learn)
- Learn how to [contribute](https://learn.microsoft.com/en-us/semantic-kernel/support/contributing) to the project
- Ask questions in the [GitHub discussions](https://github.com/microsoft/semantic-kernel/discussions)
- Ask questions in the [Discord community](https://aka.ms/SKDiscord)

- Attend [regular office hours and SK community events](COMMUNITY.md)
- Follow the team on our [blog](https://aka.ms/sk/blog)

## Contributor Wall of Fame

[![semantic-kernel contributors](https://contrib.rocks/image?repo=microsoft/semantic-kernel)](https://github.com/microsoft/semantic-kernel/graphs/contributors)

## Code of Conduct

This project has adopted the
[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information, see the
[Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
or contact [opencode@microsoft.com](mailto:opencode@microsoft.com)
with any additional questions or comments.

## License

Copyright (c) Microsoft Corporation. All rights reserved.

Licensed under the [MIT](LICENSE) license.

## Docs

Note: `docs/PLUGINS.md`, `docs/PLANNERS.md`, and top-level `FEATURE_MATRIX.md` are stub redirects to the Microsoft Learn documentation site (content has moved off-repo). `docs/GLOSSARY.md` and `docs/FAQS.md` retain in-repo content and are included below.

### docs/GLOSSARY.md
# Glossary ✍

To wrap your mind around the concepts we present throughout the kernel, here is a glossary of
commonly used terms

**Semantic Kernel (SK)** - The orchestrator that fulfills a user's ASK with SK's available [PLUGINS](PLUGINS.md).

**Ask** - What a user requests to the Semantic Kernel to help achieve the user's goal.

- "We make ASKs to the SK"

**Plugins** - A domain-specific collection made available to the SK as a group of finely-tuned functions.

- "We have a PLUGIN for using Office better"

**Function** - A computational machine comprised of Semantic AI and/or native code that's available in a [PLUGIN](PLUGINS.md).

- "The Office PLUGIN has many FUNCTIONS"

**Native Function** - expressed with traditional computing language (C#, Python, Typescript)
and easily integrates with SK

**Semantic Function** - expressed in natural language in a text file "*skprompt.txt*" using SK's
[Prompt Template language](PROMPT_TEMPLATE_LANGUAGE.md).
Each semantic function is defined by a unique prompt template file, developed using modern
**prompt engineering** techniques.

**Memory** - a collection of semantic knowledge, based on facts, events, documents, indexed with **[embeddings](EMBEDDINGS.md)**.

The kernel is designed to encourage **function composition**, allowing users to combine multiple functions
(native and semantic) into a single pipeline.

### docs/FAQS.md
# Frequently Asked Questions

### How do I get access to nightly builds?

Nightly builds of the Semantic Kernel are available [here](https://github.com/orgs/microsoft/packages?repo_name=semantic-kernel).

To download nightly builds follow the following steps:

1. You will need a GitHub account to complete these steps.
1. Create a GitHub Personal Access Token with the `read:packages` scope using these [instructions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic).
1. If you account is part of the Microsoft organization then you must authorize the `Microsoft` organization as a single sign-on organization.
1. Use the following command to add the Microsoft GitHub Packages source to your NuGet configuration (see repo for full XML/PowerShell snippets).
1. You can now add packages from the nightly build to your project.

For more information see: <https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-nuget-registry>

Other files present under `docs/`: COSINE_SIMILARITY.md, DOT_PRODUCT.md, EMBEDDINGS.md, EUCLIDEAN_DISTANCE.md, PROMPT_TEMPLATE_LANGUAGE.md, plus `docs/code_maps/`, `docs/decisions/` (ADR log), and `docs/images/`.

## Top-level structure

- `dotnet/` — .NET SDK source (`src/`), samples (`samples/`), notebooks, docs, and build tooling. Primary/most actively maintained language implementation (matches `primaryLanguage: C#`).
- `python/` — Python SDK source (`semantic_kernel/`), samples (`samples/`), tests (`tests/`), packaged via `pyproject.toml`/`uv.lock`.
- `java/` — Java SDK; this repo's `java/` only contains a `README.md` pointing to the separate [`microsoft/semantic-kernel-java`](https://github.com/microsoft/semantic-kernel-java) repo for the actual Java implementation and build instructions.
- `docs/` — Design notes, glossary, embeddings/similarity math references, architecture decision records (`decisions/`), and code maps; most conceptual/how-to docs have been migrated to learn.microsoft.com (stub redirect files remain).
- `prompt_template_samples/` — Example semantic-function plugin folders (`CalendarPlugin`, `ChatPlugin`, `ChildrensBookPlugin`, `ClassificationPlugin`, `CodingPlugin`, `FunPlugin`, `GroundingPlugin`, `IntentDetectionPlugin`, `MiscPlugin`, `QAPlugin`, `SummarizePlugin`, `WriterPlugin`) — prompt-template-language demos, not native code.
- `CONTRIBUTING.md`, `COMMUNITY.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `TRANSPARENCY_FAQS.md` — standard Microsoft OSS governance files.
- `FEATURE_MATRIX.md` — stub redirecting to the Learn docs "Supported Languages" page (per-language feature parity table now lives off-repo).
- Boilerplate skipped: `.github/`, `.devcontainer/`, `.vscode/`, `.editorconfig`, `.gitattributes`, `.gitignore`.
