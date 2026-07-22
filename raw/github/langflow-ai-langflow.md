# langflow-ai/langflow

## Metadata
- Stars: 152186
- Primary language: Python
- Default branch: main
- Latest release: v1.10.2 (2026-07-07)
- License: MIT License
- Homepage: http://www.langflow.org
- Fetched: 2026-07-22
- Final URL: https://github.com/langflow-ai/langflow

## Description
Langflow is a powerful tool for building and deploying AI-powered agents and workflows.

## README
<!-- markdownlint-disable MD030 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./docs/static/img/langflow-logo-color-blue-bg.svg">
  <img src="./docs/static/img/langflow-logo-color-black-solid.svg" alt="Langflow logo">
</picture>

[![Release Notes](https://img.shields.io/github/release/langflow-ai/langflow?style=flat-square)](https://github.com/langflow-ai/langflow/releases)
[![PyPI - License](https://img.shields.io/badge/license-MIT-orange)](https://opensource.org/licenses/MIT)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/langflow?style=flat-square)](https://pypistats.org/packages/langflow)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/langflow-ai.svg?style=social&label=Follow%20%40Langflow)](https://twitter.com/langflow_ai)
[![YouTube Channel](https://img.shields.io/youtube/channel/subscribers/UCn2bInQrjdDYKEEmbpwblLQ?label=Subscribe)](https://www.youtube.com/@Langflow)
[![Discord Server](https://img.shields.io/discord/1116803230643527710?logo=discord&style=social&label=Join)](https://discord.gg/EqksyE2EX9)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/langflow-ai/langflow)

[Langflow](https://langflow.org) is a powerful platform for building and deploying AI-powered agents and workflows. It provides developers with both a visual authoring experience and built-in API and MCP servers that turn every workflow into a tool that can be integrated into applications built on any framework or stack. Langflow comes with batteries included and supports all major LLMs, vector databases and a growing library of AI tools.

## ✨ Highlight features

- **Visual builder interface** to quickly get started and iterate.
- **Source code access** lets you customize any component using Python.
- **Interactive playground** to immediately test and refine your flows with step-by-step control.
- **Multi-agent orchestration** with conversation management and retrieval.
- **Deploy as an API** or export as JSON for Python apps.
- **Deploy as an MCP server** and turn your flows into tools for MCP clients.
- **Observability** with LangSmith, LangFuse and other integrations.
- **Enterprise-ready** security and scalability.

## 🖥️  Langflow Desktop

Langflow Desktop is the easiest way to get started with Langflow. All dependencies are included, so you don't need to manage Python environments or install packages manually.
Available for Windows and macOS.

[📥 Download Langflow Desktop](https://www.langflow.org/desktop)

## ⚡️ Quickstart

### Install locally (recommended)

Requires Python 3.10–3.14 and [uv](https://docs.astral.sh/uv/getting-started/installation/) (recommended package manager).

#### Install

From a fresh directory, run:
```shell
uv pip install langflow -U
```

The latest Langflow package is installed.
For more information, see [Install and run the Langflow OSS Python package](https://docs.langflow.org/get-started-installation#install-and-run-the-langflow-oss-python-package).

#### Run

To start Langflow, run:
```shell
uv run langflow run
```

Langflow starts at http://127.0.0.1:7860.

That's it! You're ready to build with Langflow! 🎉

## 📦 Other install options

### Run from source
If you've cloned this repository and want to contribute, run this command from the repository root:
```shell
make run_cli
```
For more information, see [DEVELOPMENT.md](./DEVELOPMENT.md).

### Docker
Start a Langflow container with default settings:
```shell
docker run -p 7860:7860 langflowai/langflow:latest
```
Langflow is available at http://localhost:7860/.
For configuration options, see the [Docker deployment guide](https://docs.langflow.org/deployment-docker).

## 🛡️ Security

For security information, see our [Security Policy](./SECURITY.md).

## 🚀 Deployment

Langflow is completely open source and you can deploy it to all major deployment clouds. To learn how to deploy Langflow, see our [Langflow deployment guides](https://docs.langflow.org/deployment-overview).

## ⭐ Stay up-to-date

Star Langflow on GitHub to be instantly notified of new releases.

![Star Langflow](https://github.com/user-attachments/assets/03168b17-a11d-4b2a-b0f7-c1cce69e5a2c)

## 👋 Contribute

We welcome contributions from developers of all levels. If you'd like to contribute, please check our [contributing guidelines](./CONTRIBUTING.md) and help make Langflow more accessible.

---

[![Star History Chart](https://api.star-history.com/svg?repos=langflow-ai/langflow&type=Timeline)](https://star-history.com/#langflow-ai/langflow&Date)

## ❤️ Contributors

[![langflow contributors](https://contrib.rocks/image?repo=langflow-ai/langflow)](https://github.com/langflow-ai/langflow/graphs/contributors)

## Docs

### docs/README.md

# Website

This website is built using [Docusaurus 3](https://docusaurus.io/), a modern static website generator.

### Installation

```
$ npm install
```

### Local Development

```
$ npm run start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

### Build

```
$ npm run build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service, including `npm run serve`.

### Import code snippets from the repo with a line range

To pull a slice of a file into the docs, source the content with `raw-loader` and present the code with the `CodeSnippet` component.
For a working example, see the [Components overview](/concepts-components#component-code).

```mdx
import CodeSnippet from "@site/src/components/CodeSnippet";
import customComponent from "!!raw-loader!@langflow/src/lfx/src/lfx/custom/custom_component/custom_component.py";

<CodeSnippet
  source={customComponent}
  startLine={41}
  endLine={74}
  language="python"
  title="CustomComponent metadata (from codebase)"
  showLineNumbers
/>
```

## Docusaurus Versioning

The versioning configuration is found in `docusaurus.config.js`.

Versioning example for release version `1.9.x` on top of `1.8.x`:

1. Before release, the docs in the active release branch should already be set to `1.8.x`, the current version.
2. When ready to release `1.9.x`, create a branch and run `npm run docs:version -- 1.9.0` to snapshot the current docs.
3. After creating a new version, update `docusaurus.config.js` to include the 1.9.0 release:

```javascript
docs: {
  lastVersion: '1.9.0',
  versions: {
    '1.9.0': {
      label: '1.9.x',
      path: '1.9.0',
    },
    '1.8.0': {
      label: '1.8.x',
      path: '1.8.0',
    },
  },
},
```

4. Test the deployment locally:

```bash
npm run build
npm run serve
```

5. Create a pull request to main, and merge to create your new release.
6. To create version 2.0.x, repeat the process: update the active release branch docs to `2.0.x` when you begin working on it, then when ready to release, run `npm run docs:version -- 2.0.0`, update `docusaurus.config.js` with labels using `.x` notation, and merge to main.

- `lastVersion` = the most recent released version (shown as "latest" in the UI).

See the [Docusaurus docs](https://docusaurus.io/docs/versioning) for more info.

### Disable versioning

1. Remove the versions configuration from `docusaurus.config.js`.
2. Delete the `docs/versioned_docs/` and `docs/versioned_sidebars/` directories.
3. Delete `docs/versions.json`.

### References

- [Official Docusaurus Versioning Documentation](https://docusaurus.io/docs/versioning)
- [Docusaurus Versioning Best Practices](https://docusaurus.io/docs/versioning#versioning-best-practices)

### Deployment

Using SSH:

```
$ USE_SSH=true npm run deploy
```

Not using SSH:

```
$ GIT_USER=<Your GitHub username> npm run deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.

### docs/docs/Agents/agents.mdx

---
title: Use Langflow agents
slug: /agents
---

import Icon from "@site/src/components/icon";
import PartialParams from '@site/docs/_partial-hidden-params.mdx';
import PartialAgentsWork from '@site/docs/_partial-agents-work.mdx';
import PartialGlobalModelProviders from '@site/docs/_partial-global-model-providers.mdx';

Langflow's [**Agent** component](/components-agents) is critical for building agent flows.
This component provides everything you need to create an agent, including multiple Large Language Model (LLM) providers, tool calling, and custom instructions.
It simplifies agent configuration so you can focus on application development.

<PartialAgentsWork />

## Use the Agent component in a flow

The following steps explain how to create an agent flow in Langflow from a blank flow.
For a prebuilt example, use the **Simple Agent** template or the [Langflow quickstart](/get-started-quickstart).

1. Click **New Flow**, and then click **Blank Flow**.
2. Add an **Agent** component to your flow.
3. <PartialGlobalModelProviders />
4. Select the model that you want to use from the **Language Model** dropdown.
If your preferred model isn't listed, make sure it's enabled in the **Models** configuration.
For more information, see [Agent component parameters](#agent-component-parameters).
5. Add [**Chat Input** and **Chat Output** components](/chat-input-and-output) to your flow, and then connect them to the **Agent** component.

    At this point, you have created a basic LLM-based chat flow that you can test in the <Icon name="Play" aria-hidden="true"/> **Playground**.
    However, this flow only chats with the LLM.
    To enhance this flow and make it truly agentic, add some tools, as explained in the next steps.

    ![A basic agent chat flow with Chat Input, Agent, and Chat Output components.](/img/agent-example-add-chat.png)

6. Add **Web Search**, **URL**, and **Calculator** components to your flow.
7. Enable **Tool Mode** in the **Web Search**, **URL**, and **Calculator** components:

    1. Click the **Web Search** component to expose the [component's header menu](/concepts-components#component-menus), and then enable **Tool Mode**.
    2. Repeat for the **URL** and **Calculator** components.
    3. Connect the **Toolset** port for each tool component to the **Tools** port on the **Agent** component.

    **Tool Mode** makes a component into a tool by modifying the component's inputs.
    With **Tool Mode** enabled, a component can accept requests from an **Agent** component to use the component's available actions as tools.

    When in **Tool Mode**, a component has a **Toolset** port that you must connect to an **Agent** component's **Tools** port if you want to allow the agent to use that component's actions as tools.

    For more information, see [Configure tools for agents](/agents-tools).

    ![A more complex agent chat flow where three components are connected to the Agent component as tools](/img/agent-example-add-tools.png)

8. Open the <Icon name="Play" aria-hidden="true"/> **Playground**, and then ask the agent, `What tools are you using to answer my questions?`

    The agent should respond with a list of the connected tools.
    It may also include built-in tools.

    ```text
    I use a combination of my built-in knowledge (up to June 2024) and a set of external tools to answer your questions. Here are the main types of tools I can use:
    Web Search & Content Fetching: I can fetch and summarize content from web pages, including crawling links recursively.
    News Search: I can search for recent news articles using Google News via RSS feeds.
    Calculator: I can perform arithmetic calculations and evaluate mathematical expressions.
    Date & Time: I can provide the current date and time in various time zones.
    These tools help me provide up-to-date information, perform calculations, and retrieve specific data from the internet when needed. If you have a specific question, let me know, and I'll use the most appropriate tool(s) to help!
    ```

9. To test a specific tool, ask the agent a question that uses one of the tools, such as `Summarize today's tech news`.

    To help you debug and test your flows, the **Playground** displays the agent's tool calls, the provided input, and the raw output the agent received before generating the summary.
    With the given example, the agent should call the **Web Search** component with **Search Mode** set to **News**.

You've successfully created a basic agent flow that uses some generic tools.

To continue building on this tutorial, try connecting other tool components or [use Langflow as an MCP client](/mcp-client) to support more complex and specialized tasks.

For a multi-agent example, see [Use an agent as a tool](/agents-tools#use-an-agent-as-a-tool).

## Agent component parameters

You can configure the **Agent** component to use your preferred provider and model, custom instructions, and tools.

<PartialParams />

### Provider and model

Use the **Language Model** (`agent_llm`) setting to select the LLM that you want the agent to use.

<PartialGlobalModelProviders />

To use a model with the **Agent** component, select the model in the **Agent** component's **Language Model** field.

The **Language Model** field lists all language models that you've configured globally. If a provider doesn't have any language models available, they aren't listed.
For example, if a provider offers only embeddings models, those models aren't listed on the **Agent** component.

To access other providers or models, you can do either of the following:

* Connect any [language model component](/components-models) to the **Agent** component's **Language Model** port. This option allows you to connect a custom language model component to use models that aren't available in the global model providers list.
* Configure additional providers in the **Models** pane, and then select the model from the **Language Model** dropdown.

If you need to generate embeddings in your flow, use an [embedding model component](/components-embedding-models).

### Agent instructions and input

In the **Agent Instructions** (`system_prompt`) field, you can provide custom instructions that you want the **Agent** component to use for every conversation.

These instructions are applied in addition to the **Input** (`input_value`), which can be entered directly or provided through another component, such as a **Chat Input** component.

### Tools

Agents are most useful when they have the appropriate tools available to complete requests.

An **Agent** component can use any Langflow component as a tool, including other agents and MCP servers.

To attach a component as a tool, you must enable **Tool Mode** on the component that you want to attach, and then attach it to the **Agent** component's **Tools** port.
For more information, see [Configure tools for agents](/agents-tools).

:::tip
To allow agents to use tools from MCP servers, use the [**MCP Tools** component](/mcp-tools).
:::

### Agent memory

Langflow agents have built-in chat memory that is enabled by default.
This memory allows them to retrieve and reference messages from previous conversations, maintaining a rolling context window for each chat session ID.

Chat memories are grouped by [session ID (`session_id`)](/session-id).
It is recommended to use custom session IDs if you need to segregate chat memory for different users or applications that run the same flow.

By default, the **Agent** component uses your Langflow installation's storage, and it retrieves a limited number of chat messages, which you can configure with the **Number of Chat History Messages** parameter.

The **Message History** component isn't required for default chat memory, but it is required if you want to use external chat memory like Mem0.
Additionally, the **Message History** component provides more options for sorting, filtering, and limiting memories. Although, most of these options are built-in to the **Agent** component with default values.

Langflow sends events to the Playground during each agent run: the input message, each tool call with its input and result, streaming tokens as they arrive, and the final answer.
Langflow writes the completed message to chat history when the run finishes.
When using the **Structured Response** output, Langflow does not send events to the Playground and does not write to chat history.

For more information, see [Store chat memory](/memory#store-chat-memory) and [**Message History** component](/message-history).

### Additional parameters

With the **Agent** component, the available parameters can change depending on the selected provider and model, including support for additional modes, arguments, or features like chat memory and temperature.
For example:

* **Current Date** (`add_current_date_tool`): When enabled (`true`), this setting adds a tool to the agent that can retrieve the current date.
* **Handle Parse Errors** (`handle_parsing_errors`): When enabled (`true`), this setting allows the agent to fix errors, like typos, when analyzing user input.
* **Verbose** (`verbose`): When enabled (`true`), this setting records detailed logging output for debugging and analysis.

<PartialParams />

## Agent component output

The **Agent** component has two outputs:

* **Response** (`response`): The agent's reply as [`Message`](/data-types#message) data, which is typically connected to a **Chat Output** component.
* **Structured Response** (`structured_response`): The agent's reply formatted as structured [`Data`](/data-types#data) according to the **Output Schema** you define.

    To configure the agent's **Structured Response** output:

    1. In the **Agent** component, click the output label near the component's output port and select **Structured Response**.
    2. Select the **Agent** component to open the [component inspection panel](/concepts-components#component-inspection-panel), and then click <Icon name="Table" aria-hidden="true"/> **Open table**.
    3. Click <Icon name="Plus" aria-hidden="true"/> **+** to add a row for each field you want to extract. For each row, enter a **Name**, **Type**, and optionally a **Description** and **As List** toggle.
    4. Connect the **Structured Response** port to a downstream component that accepts [`Data`](/data-types#data) input, such as a **Parser** or **JSON Operations** component.

    The **Agent** component uses the connected LLM to extract structured data, and the extraction behavior is configured in the **Output Format Instructions** field.
    Modify the prompt in the **Output Format Instructions** field to change extraction behavior.
    This does not modify the schema defined in **Output Schema**.

    Both outputs can be connected at the same time, but each output produces a separate LLM call. If you only need structured data, connect **Structured Response** only.

## See also

* [**Agent** and **MCP Tools** components](/components-agents)
* [Configure tools for agents](/agents-tools)

### docs/docs/Agents/mcp-server.mdx

---
title: Use Langflow as an MCP server
slug: /mcp-server
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import Icon from "@site/src/components/icon";

Langflow integrates with the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) as both an MCP server and an MCP client.

This page describes how to use Langflow as an MCP server that exposes your flows as [tools](https://modelcontextprotocol.io/docs/concepts/tools) that [MCP clients](https://modelcontextprotocol.io/clients) can use when generating responses.

Langflow MCP servers support both the **streamable HTTP** transport and **Server-Sent Events (SSE)** as a fallback.
The default project MCP server configuration uses streamable HTTP transport at the URL path `/streamable`.

For information about using Langflow as an MCP client and managing MCP server connections within flows, see [Use Langflow as an MCP client](/mcp-client).

## Prerequisites

* A [Langflow project](/concepts-flows#projects) with at least one flow that has a [**Chat Output** component](/chat-input-and-output).

    The **Chat Output** component is required to use a flow as an MCP tool.

* Any LTS version of [Node.js](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) installed on your computer if you want to use MCP Inspector to [test and debug flows](#test-and-debug-flows).

* [ngrok installed](https://ngrok.com/docs/getting-started/#1-install-ngrok) and an [ngrok authtoken](https://dashboard.ngrok.com/get-started/your-authtoken) if you want to [deploy a public Langflow server](/deployment-public-server).

## Serve flows as MCP tools {#select-flows-to-serve}

When you create a [Langflow project](/concepts-flows#projects), Langflow automatically adds the project to your MCP server's configuration and makes the project's flows available as MCP tools.

If your Langflow server has authentication enabled (`AUTO_LOGIN=false`), the project's MCP server is automatically configured with API key authentication, and a new API key is generated specifically for accessing the new project's flows.
For more information, see [MCP server authentication](#authentication).


### Prevent automatic MCP server configuration for Langflow projects

To disable automatic MCP server configuration for new projects, set the `LANGFLOW_ADD_PROJECTS_TO_MCP_SERVERS` environment variable to `false`.
For more information, see [MCP server environment variables](#mcp-server-environment-variables).

### Selectively enable and disable MCP servers for Langflow projects

With or without automatic MCP server configuration enabled, you can selectively enable and disable the projects that are exposed as MCP tools:

1. Click the **MCP Server** tab on the [**Projects** page](/concepts-flows#projects), or, when editing a flow, click **Share**, and then select **MCP Server**.

    ![MCP server projects page](/img/mcp-server.png)

    The **Flows/Tools** section lists the flows that are currently being served as tools on this MCP server.

2. To toggle exposed flows, click <Icon name="Wrench" aria-hidden="true"/> **Edit Tools**, and then select the flows that you want exposed as tools.
To prevent a flow from being used as a tool, clear the checkbox in the first column.

3. Close the **MCP Server Tools** dialog to save your changes.

    ![MCP Server Tools](/img/mcp-server-tools.png)

### Edit flow tool names and descriptions

Tool names and descriptions help MCP clients determine which actions your flows provide and when to use those actions.
It is recommended to provide clear, descriptive names and descriptions for all tools that you serve to MCP clients.

To edit the names and descriptions of flow tools on a Langflow MCP server, do the following:

1. Click the **MCP Server** tab on the [**Projects** page](/concepts-flows#projects), or, when editing a flow, click **Share**, and then select **MCP Server**.

2. Click <Icon name="Wrench" aria-hidden="true"/> **Edit Tools**.

3. Click the **Description** or **Tool** that you want to edit:

    - **Tool name**: Enter a name that makes it clear what the flow does when used as a tool by an agent.

    - **Tool description**: Enter a description that completely and accurately describes the specific actions the flow performs.

4. Close the **MCP Server Tools** dialog to save your changes.

#### Importance of tool names and descriptions

MCP clients use tool names and descriptions to determine which actions to use when generating responses.

Because MCP clients treat your Langflow project as a single MCP server with all of your enabled flows listed as tools, unclear names and descriptions can cause the agent to select tools incorrectly or inconsistently.

For example, a flow's default tool name is the flow ID, such as `adbbf8c7-0a34-493b-90ea-5e8b42f78b66`.
This provides no information to an agent about the type of flow or its purpose.

To provide more context about your flows, make sure to name and describe your flows clearly when configuring your Langflow project's MCP server.

Think of these names and descriptions as function names and code comments.
Use clear statements to describe the problems your flows solve.

<details>
<summary>Example: Tool name and description usage</summary>

For example, assume you create a flow based on the **Document Q&A** template that uses an LLM to chat about resumes, and then you give the flow the following name and description:

- **Tool name**: `document_qa_for_resume`

- **Tool description**: `A flow for analyzing Emily's resume.`

After connecting your Langflow MCP server to Cursor, you can ask Cursor about the resume, such as `What job experience does Emily have?`.
Using the context provided by your tool name and description, the agent can decide to use the `document_qa_for_resume` MCP tool to create a response about Emily's resume.
If necessary, the agent asks permission to use the flow tool before generating the response.

If you ask about a different resume, such as `What job experience does Alex have?`, the agent can decide that `document_qa_for_resume` isn't relevant to this request, because the tool description specifies that the flow is for Emily's resume.
In this case, the agent might use another available tool, or it can inform you that it doesn't have access to information about Alex's.
For example:

```
I notice you're asking about Alex's job experience.
Based on the available tools, I can see there is a Document QA for Resume flow that's designed for analyzing resumes.
However, the description mentions it's for "Emily's resume" not Alex's. I don't have access to Alex's resume or job experience information.
```

</details>

### Configure tool execution timeouts

There are three ways to set tool execution timeouts: the MCP Tools component timeout setting, a global environment variable, and Langflow's default fallback. How you configure these determines their effect in resolving the actual timeout limit for each tool call.

Langflow times are evaluated in the following order:

1. Per-component timeout is set directly on an MCP Tools component in your flow. To configure per-component timeout in the [**MCP Tools** component](/mcp-tools), open the advanced settings tab and enter a value in the **Tool Execution Timeout (seconds)** field. A value of `0` disables the per-component override and falls back to the global setting.

2. Global timeout is set with the `LANGFLOW_MCP_TOOL_EXECUTION_TIMEOUT` environment variable. The default is 180 seconds.

3. If neither `LANGFLOW_MCP_TOOL_EXECUTION_TIMEOUT` or `LANGFLOW_MCP_SERVER_TIMEOUT` is configured, Langflow defaults to 180 seconds.

To support tool calls that take longer than 180 seconds, set `LANGFLOW_MCP_TOOL_EXECUTION_TIMEOUT` to a value greater than `180` to raise the global limit, or set the **Tool Execution Timeout (seconds)** field on a specific MCP Tools component to a value greater than `180` to raise the limit for that component only.

If `LANGFLOW_MCP_SERVER_TIMEOUT` is set to a value greater than `LANGFLOW_MCP_TOOL_EXECUTION_TIMEOUT`, the server timeout takes precedence and becomes the actual limit for tool calls.

{/* The anchor on this section (connect-clients-to-use-the-servers-actions) is currently a link target in the Langflow UI. Do not change. */}
## Connect clients to your Langflow MCP server {#connect-clients-to-use-the-servers-actions}

Langflow provides automatic installation and code snippets to help you deploy your Langflow MCP servers to your local MCP clients.

<Tabs>
<TabItem value="JSON" label="JSON" default>

The JSON option allows you to connect a Langflow MCP server to any local or remote MCP client.
You can modify this process for any [MCP-compatible client](https://modelcontextprotocol.io/clients).

1. Install any [MCP-compatible client](https://modelcontextprotocol.io/clients).

    These steps use Cursor as an example, but the process is generally the same for all clients, with slight differences in client-specific details like file names.

2. In your client, add a new MCP server using the client's UI or configuration file.

    For example, in Cursor, go to **Cursor Settings**, select **MCP**, and then click **Add New Global MCP Server** to open Cursor's global `mcp.json` configuration file.

3. Recommended: Configure [authentication](#authentication) for your MCP server.

4. In Langflow, on the **Projects** page, click the **MCP Server** tab.

5. Click the **JSON** tab, copy the code snippet for your operating system, and then paste it into your client's MCP configuration file.
For example:

    ```json
    {
      "mcpServers": {
        "PROJECT_NAME": {
          "command": "uvx",
          "args": [
            "mcp-proxy",
            "--transport",
            "streamablehttp",
            "http://LANGFLOW_SERVER_ADDRESS/api/v1/mcp/project/PROJECT_ID/streamable"
          ]
        }
      }
    }
    ```

    The **MCP Server** tab automatically populates the `LANGFLOW_SERVER_ADDRESS` and `PROJECT_ID` values.

    The default Langflow server address is `http://localhost:7860`.
    If you are using a [public Langflow server](/deployment-public-server), the server address is automatically included.

    If your Langflow server requires authentication, you must include your Langflow API key or OAuth settings in the configuration.
    For more information, see [MCP server authentication](#authentication).

6. To include other environment variables with your MCP server command, add an `env` object with key-value pairs of environment variables. For example:

    ```json
    {
      "mcpServers": {
        "PROJECT_NAME": {
          "command": "uvx",
          "args": [
            "mcp-proxy",
            "--transport",
            "streamablehttp",
            "http://LANGFLOW_SERVER_ADDRESS/api/v1/mcp/project/PROJECT_ID/streamable"
          ],
          "env": {
            "KEY": "VALUE"
          }
        }
      }
    }
    ```

    Don't add API keys in the `env` object, as these variables are specifically for the `mcp-proxy` process.
    Instead, add API keys under `args`.
    For an example, see [MCP server authentication](#authentication).

7. Save and close your client's MCP configuration file.

8. Confirm that your Langflow MCP server is on the client's list of MCP servers.
If necessary, restart your client to apply the modified configuration file.

</TabItem>
<TabItem value="auto" label="Auto install">

:::info
The auto install option is available only for specific MCP clients.
Auto install requires the client to be installed locally so Langflow can write to the client's configuration file.
If your client isn't supported, is installed remotely, or you need to pass additional environment variables, use the **JSON** option.
:::

1. Install [Cursor](https://docs.cursor.com/get-started/installation), [Claude](https://claude.ai/download), or [Windsurf](https://windsurf.com/download/editor) on the same computer where your Langflow server is running.

2. Recommended: Configure [authentication](#authentication) for your MCP server.

3. In Langflow, on the **Projects** page, click the **MCP Server** tab.

4. On the **Auto install** tab, find your MCP client provider, and then click <Icon name="Plus" aria-hidden="true"/> **Add**.

    Your Langflow project's MCP server is automatically added to the configuration file for your local Cursor, Claude, or Windsurf client.
    For example, with Cursor, the server configuration is added to the `mcp.json` configuration file.

    Langflow attempts to add this configuration even if the selected client isn't installed.
    To verify the installation, check the available MCP servers in your client.

</TabItem>
</Tabs>

Once your MCP client is connected to your Langflow project's MCP server, your flows are registered as tools.
Cursor determines when to use tools based on your queries, and requests permissions when necessary.
For more information, see the MCP documentation for your client, such as [Cursor's MCP documentation](https://docs.cursor.com/context/model-context-protocol).

## MCP server authentication {#authentication}

Each [Langflow project](/concepts-flows#projects) has its own MCP server with its own MCP server authentication settings.

When you create a new project, Langflow automatically configures authentication for the project's MCP server based on your Langflow server's authentication settings. If authentication is enabled (`AUTO_LOGIN=false`), the project is automatically configured with API key authentication, and a new API key is generated for accessing the project's flows.

To configure authentication for a Langflow MCP server, go to the **Projects** page in Langflow, click the **MCP Server** tab, click <Icon name="Fingerprint" aria-hidden="true"/> **Edit Auth**, and then select your preferred authentication method:

<Tabs groupId="auth-type">
<TabItem value="API key" label="API key">

When authenticating your MCP server with a Langflow API key, your project's MCP server **JSON** code snippets and **Auto install** configuration automatically include the `--headers` and `x-api-key` arguments in the **args** array (for streamable transport).

Click <Icon name="key" aria-hidden="true"/> **Generate API key** to automatically insert a new Langflow API key into the code template.
Alternatively, you can replace `YOUR_API_KEY` with an existing Langflow API key.

To add your API key to the configuration, use three separate entries in `args`: `"--headers"`, `"x-api-key"`, and your key value. For example:

```json
{
  "mcpServers": {
    "PROJECT_NAME": {
      "command": "uvx",
      "args": [
        "mcp-proxy",
        "--transport",
        "streamablehttp",
        "--headers",
        "x-api-key",
        "YOUR_API_KEY",
        "http://LANGFLOW_SERVER_ADDRESS/api/v1/mcp/project/PROJECT_ID/streamable"
      ]
    }
  }
}
```

</TabItem>
<TabItem value="OAuth" label="OAuth">

When OAuth is enabled, Langflow automatically starts an [MCP Composer](https://pypi.org/project/mcp-composer) instance for your project, creating a secure client-side proxy between MCP clients and the `mcp-proxy` on your server.

OAuth integration allows your Langflow MCP server to authenticate users and applications through any OAuth 2.0 compliant service. When users or applications connect to your MCP server, they are redirected to your chosen OAuth provider to authenticate. Upon successful authentication, they are granted access to your flows as MCP tools.

Before configuring OAuth in Langflow, you must first set up an OAuth application with an external OAuth 2.0 service provider.
You must register your Langflow server as an OAuth client, and then obtain the required values to complete the configuration in Langflow.

The following table describes the required values.
[GitHub OAuth](https://github.com/settings/developers) is used for example purposes.
Be sure to use the actual values from your own deployment.
For more information, see your OAuth provider's documentation.

| Field | Description | Source | Example |
|-------|-------------|--------|---------|
| **Host** | OAuth server host | MCP Composer default. | `localhost` |
| **Port** | OAuth server port | MCP Composer default. | `9000` |
| **Server URL** | Full OAuth server URL | Combines the MCP Composer default OAuth host and port. | `http://localhost:9000` |
| **Callback URL** | OAuth callback URL on your server | You define this full URL during OAuth app registration. This must match exactly what you register with your OAuth provider. | `http://localhost:9000/auth/idaas/callback` |
| **Client ID** | Your OAuth client identifier | From your OAuth provider. | `Ov23li9vx2grVL61qjb` |
| **Client Secret** | Your OAuth client secret | From your OAuth provider. | `1234567890abcdef1234567890abcdef12345678` |
| **Authorization URL** | OAuth authorization endpoint | From your OAuth provider. | `https://github.com/login/oauth/authorize` |
| **Token URL** | OAuth token endpoint for getting refresh tokens | From your OAuth provider. | `https://github.com/login/oauth/access_token` |
| **MCP Scope** | Scope for MCP operations | You define this. As of Langflow 1.6, `user` is the only available value. | `user` |
| **Provider Scope** | OAuth provider scope | You define this. As of Langflow 1.6, `openid` is the only available value. | `openid` |

To configure OAuth authentication:

1. Select **OAuth** as the authentication type.
2. Configure the OAuth settings with the values from your OAuth deployment.
    All values are required.

    The OAuth credentials are encrypted and stored securely in your Langflow database.

3. Click **Save**.

    Your MCP server's **JSON** code snippets and **Auto install** configuration are automatically updated with OAuth values. These are automatically used for new installations after enabling OAuth. However, you must manually update any existing installations, as explained in the next step.

4. If you already installed your Langflow MCP server in your MCP client, you must update your MCP client configuration to use the new OAuth settings after enabling OAuth on your MCP server.
The client update method depends on how you installed the server on the client:

    - **Auto install**: Manually update your client's config file using the updated JSON snippet from the **JSON** tab, or repeat the steps in [Auto-install](#connect-clients-to-use-the-servers-actions) to re-install the client with the updated settings.
    - **JSON option**: Copy the updated JSON snippet from the **JSON** tab and replace your existing configuration.
    - **New connections**: Use either the **Auto install** or **JSON** option. The OAuth settings are included automatically.

After you enable OAuth and update your client configuration, an OAuth callback window opens each time your MCP client attempts to authenticate with the server.
A successful authentication returns `Authentication complete. You may close this window.`
If your client doesn't open the OAuth window, try restarting the client to retrieve the updated configuration.

</TabItem>
<TabItem value="None" label="None">

When no authentication is configured, your MCP server becomes a public endpoint that anyone can access without providing credentials.
Only use this option when Langflow is running in a trusted environment.

</TabItem>
</Tabs>



{/* The anchor on this section (deploy-your-server-externally) is currently a link target in the Langflow UI. Do not change. */}
## Deploy your Langflow MCP server externally {#deploy-your-server-externally}

To deploy your Langflow MCP server externally, see [Deploy a public Langflow server](/deployment-public-server).

## Use MCP Inspector to test and debug flows {#test-and-debug-flows}

:::info Node prerequisite
MCP Inspector requires any LTS version of [Node.js](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) installed on your computer.
:::
[MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) is a common tool for testing and debugging MCP servers.
You can use MCP Inspector to monitor your flows and get insights into how they are being consumed by the MCP server.

1. Install MCP Inspector:

    ```bash
    npx @modelcontextprotocol/inspector
    ```

    For more information about configuring MCP Inspector, including specifying a proxy port, see the [MCP Inspector GitHub project](https://github.com/modelcontextprotocol/inspector).

2. Open a web browser and navigate to the MCP Inspector UI.
The default address is `http://localhost:6274`.

3. In the MCP Inspector UI, enter the connection details for your Langflow project's MCP server.
    The field values depend on your server's method of [authentication](#authentication).
    <Tabs groupId="auth-type">
      <TabItem value="API key" label="API key" default>

        - **Transport Type**: Select **STDIO**.
        - **Command**: `uvx`
        - **Arguments**: Enter the following list of arguments, separated by spaces. Replace the values for `YOUR_API_KEY`, `LANGFLOW_SERVER_ADDRESS`, and `PROJECT_ID` with the values from your Langflow MCP server. For example:
            ```bash
            mcp-proxy --headers x-api-key YOUR_API_KEY http://LANGFLOW_SERVER_ADDRESS/api/v1/mcp/project/PROJECT_ID/streamable
            ```

      </TabItem>
      <TabItem value="OAuth" label="OAuth">

        - **Transport Type**: Select **STDIO**.
        - **Command**: `uvx`
        - **Arguments**: Enter the following list of arguments, separated by spaces. Replace the value for `OAUTH_SERVER_URL` with the URL of your OAuth server. For example:
            ```bash
            mcp-composer --mode stdio --sse-url http://localhost:9000/sse --disable-composer-tools --client_auth_type oauth
            ```

      </TabItem>
      <TabItem value="None" label="None">

        - **Transport Type**: Select **SSE**.
        - **URL**: Enter the Langflow MCP server's endpoint. For example:
            ```bash
            http://localhost:7860/api/v1/mcp/project/d359cbd4-6fa2-4002-9d53-fa05c645319c/streamable
            ```

      </TabItem>
    </Tabs>

4. Click **Connect**.

    If the connection was successful, you should see your project's flows in the **Tools** tab.
    From this tab, you can monitor how your flows are being registered as tools by MCP, as well as test the tools with custom input values.

5. To quit MCP Inspector, press <kbd>Control+C</kbd> in the same terminal window where you started it.

## Restrict MCP server management to superusers {#restrict-mcp-server-management}

To prevent non-superusers from editing MCP server connections, set `LANGFLOW_MCP_SERVERS_LOCKED=true`.

When set to `true`, non-superusers can use existing MCP servers that are already configured, but they cannot configure MCP server connections in the UI or API.
Superusers retain full access to MCP server configuration.

Locking the MCP server configuration for users does not disable Langflow's built-in MCP server for serving flows as MCP tools.

## MCP server environment variables

The following environment variables set behaviors related to your Langflow projects' MCP servers:

| Variable | Format | Default | Description |
|----------|--------|---------|-------------|
| `LANGFLOW_MCP_SERVER_ENABLED` | Boolean | `True` | Whether to initialize an MCP server for each of your Langflow projects. If `false`, Langflow doesn't initialize MCP servers. |
| `LANGFLOW_MCP_SERVER_ENABLE_PROGRESS_NOTIFICATIONS` | Boolean | `False` | If `true`, Langflow MCP servers send progress notifications. |
| `LANGFLOW_MCP_SERVER_TIMEOUT` | Integer | `20` | Timeout in seconds for MCP connection setup and tool execution. See [Configure tool execution timeouts](#configure-tool-execution-timeouts). |
| `LANGFLOW_MCP_TOOL_EXECUTION_TIMEOUT` | Integer | `180` | Global timeout in seconds for MCP tool calls. See [Configure tool execution timeouts](#configure-tool-execution-timeouts). |
| `LANGFLOW_MCP_MAX_SESSIONS_PER_SERVER` | Integer | `10` | Maximum number of MCP sessions to keep per unique server. |
| `LANGFLOW_ADD_PROJECTS_TO_MCP_SERVERS` | Boolean | `True` | Whether to automatically add newly created projects to the user's MCP servers configuration. If `false`, projects must be manually added to MCP servers. |
| `LANGFLOW_MCP_SERVERS_LOCKED` | Boolean | `False` | If `true`, non-superusers cannot add, edit, or remove MCP server connections through the UI or API. Superusers retain full access. For more information, see [Restrict MCP server management to superusers](#restrict-mcp-server-management). |

## Troubleshoot Langflow MCP servers {#troubleshooting-mcp-server}

For troubleshooting advice for MCP servers and clients, see [Troubleshoot Langflow: MCP issues](/troubleshoot#mcp).

## See also

* [Use Langflow as an MCP client](/mcp-client)
* [Use a DataStax Astra DB MCP server](/mcp-component-astra)
* [MCP server environment variables](/environment-variables#mcp)

### docs/docs/Agents/mcp-client.mdx

---
title: Use Langflow as an MCP client
slug: /mcp-client
---

import Icon from "@site/src/components/icon";
import McpIcon from '@site/static/logos/mcp-icon.svg';
import PartialMcpNodeTip from '@site/docs/_partial-mcp-node-tip.mdx';
import PartialMcpToolsAddSteps from '@site/docs/_partial-mcp-tools-add-steps.mdx';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Langflow integrates with the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) as both an MCP server and an MCP client.

This page describes how to use Langflow as an MCP client with the [**MCP Tools** component](#use-the-mcp-tools-component) and connected [MCP servers](#manage-connected-mcp-servers).

For information about using Langflow as an MCP server, see [Use Langflow as an MCP server](/mcp-server).

## Use the MCP tools component {#use-the-mcp-tools-component}

The **MCP Tools** component connects to an MCP server so that a [Langflow agent](/agents) can use the server's tools when responding to user queries.

Register MCP servers, and then add **MCP Tools** from the <McpIcon /> **MCP** sidebar as described in [Connect to a non-Langflow MCP server](#mcp-stdio-mode).

This component has two modes, depending on the type of server you want to access:

* [Connect to a non-Langflow MCP server](#mcp-stdio-mode) with a JSON configuration file, server start command, or HTTP/SSE URL to access tools provided by external, non-Langflow MCP servers.
* [Connect to a Langflow MCP server](#mcp-http-mode) to use flows from your [Langflow projects](/concepts-flows#projects) as MCP tools.

### Connect to a non-Langflow MCP server {#mcp-stdio-mode}

<PartialMcpNodeTip />

<PartialMcpToolsAddSteps />

4. In the **MCP Server** field on the **MCP Tools** component, select the server you registered.

    New servers are registered in **Settings** > **MCP Servers**, or in the <McpIcon /> **MCP** sidebar > <Icon name="Plus" aria-hidden="true"/> **Add MCP Server**, using one of the following connection types:

    * **JSON**: Paste the MCP server's JSON configuration object into the field, including required and optional parameters that you want to use, and then click **Add Server**.
    * **STDIO**: Enter the MCP server's **Name**, **Command**, and any **Arguments** and **Environment Variables** the server uses, and then click **Add Server**.
    For example, to start a [Fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) server, the **Command** is `uvx mcp-server-fetch`.
    * **HTTP/SSE**: Enter your MCP server's **Name**, **URL**, and any **Headers** and **Environment Variables** the server uses, and then click **Add Server**.
    The default **URL** for Langflow MCP servers is `http://localhost:7860/api/v1/mcp/project/PROJECT_ID/streamable` or `http://localhost:7860/api/v1/mcp/streamable`. For more information, see [Connect to a Langflow MCP server](#mcp-http-mode).

5. To configure headers for your MCP server, enter each header in the **Headers** fields as key-value pairs.
    You can use [global variables](/configuration-global-variables) in header values by entering the global variable name as the header value.
    For more information, see [Use global variables in MCP server headers](#use-global-variables-in-mcp-server-headers).

    If this server is nested inside a Langflow flow that runs as an MCP server, you can propagate the incoming request's `x-api-key` or `Authorization` header directly to this server at runtime.
    For more information, see [Propagate x-api-key to nested MCP servers](#propagate-x-api-key).

6. To use environment variables in your server command, enter each variable in the **Env** fields as key-value pairs.

7. In the **Tool** field, select a tool that you want this component to use, or leave the field blank to allow access to all tools provided by the MCP server.

    If you select a specific tool, you might need to configure additional tool-specific fields. For information about tool-specific fields, see your MCP server's documentation.

    At this point, the **MCP Tools** component is serving a tool from the connected server, but nothing is using the tool. The next steps explain how to make the tool available to an [**Agent** component](/components-agents) so that the agent can use the tool in its responses.

8. In the [component's header menu](/concepts-components#component-menus), enable **Tool mode** so you can use the component with an agent.

9. Connect the **MCP Tools** component's **Toolset** port to an **Agent** component's **Tools** port.

    If not already present in your flow, make sure you also attach **Chat Input** and **Chat Output** components to the **Agent** component.

    ![MCP Tools component in STDIO mode](/img/component-mcp-stdio.png)

10. Test your flow to make sure the MCP server is connected and the selected tool is used by the agent. Open the **Playground**, and then enter a prompt that uses the tool you connected through the **MCP Tools** component.

    For example, if you use `mcp-server-fetch` with the `fetch` tool, you could ask the agent to summarize recent tech news. The agent calls the MCP server function `fetch`, and then returns the response.

11. If you want the agent to be able to use more tools, repeat these steps to add more tools components with different servers or tools.

### Connect a Langflow MCP server {#mcp-http-mode}

Every Langflow project runs a separate MCP server that exposes the project's flows as MCP tools.
For more information about your projects' MCP servers, including exposing flows as MCP tools, see [Use Langflow as an MCP server](/mcp-server).

Langflow MCP servers support both the **streamable HTTP** transport and **Server-Sent Events (SSE)** as a fallback.

To leverage flows-as-tools, register your Langflow MCP endpoint as a server first, and then add the **MCP Tools** component from the <McpIcon /> **MCP** sidebar.

1. Register the Langflow MCP server.
 Open **Settings** > **MCP Servers** or the <McpIcon /> **MCP** section in the flow sidebar, click <Icon name="Plus" aria-hidden="true"/> **Add MCP Server**, and select **HTTP/SSE** mode.

2. In the **MCP URL** field, enter your Langflow server's MCP endpoint.
   - For project-specific servers: `http://localhost:7860/api/v1/mcp/project/PROJECT_ID/streamable`
   - For global MCP server: `http://localhost:7860/api/v1/mcp/streamable`
   - Default for Langflow Desktop: `http://localhost:7868/`

   All flows available from the targeted server are treated as tools. For authentication and project URLs, see [Use Langflow as an MCP server](/mcp-server).

3. Save the server. When the connection succeeds, the server is stored and appears as a tile in the **MCP** sidebar.

4. Add the **MCP Tools** component to the flow.

5. In the [component's header menu](/concepts-components#component-menus), enable **Tool Mode** so you can use the component with an agent.

6. Connect the **MCP Tools** component's **Toolset** port to an **Agent** component's **Tools** port.

7. If not already present in your flow, make sure you also attach **Chat Input** and **Chat Output** components to the **Agent** component.

    ![MCP component with HTTP/SSE mode enabled](/img/component-mcp-sse-mode.png)

8. Test your flow to make sure the agent uses your flows to respond to queries. Open the **Playground**, and then enter a prompt that uses a flow that you connected through the **MCP Tools** component.

9. If you want the agent to be able to use more tools, repeat these steps to add more tools components with different servers or tools.

## MCP Tools parameters

| Name | Type | Description |
|------|------|-------------|
| mcp_server | String | Input parameter. The MCP server to connect to. |
| tool | String | Input parameter. The specific tool to execute from the connected MCP server. Leave blank to allow access to all tools. |
| use_cache | Boolean | Input parameter. Enable caching of MCP server and tools to improve performance. Default: `false`. |
| verify_ssl | Boolean | Input parameter. Enable SSL certificate verification for HTTPS connections. Default: `true`. |
| response | Table | Output parameter. [`Table`](/data-types#table) containing the response from the executed tool. |

## Manage connected MCP servers

To manage MCP server connections for use in flows, open the <McpIcon /> **MCP** section in the visual editor, and then click <Icon name="ArrowUpRight" aria-hidden="true"/> **Manage Servers**, or click your profile icon, select **Settings**, and then click **MCP Servers**.

To add a new MCP server, click <Icon name="Plus" aria-hidden="true"/> **Add MCP Server**, register the server, and then select the server on the **MCP Tools** component as described in [Connect to a non-Langflow MCP server](#mcp-stdio-mode).

Click <Icon name="Ellipsis" aria-hidden="true"/> **More** to edit or delete an MCP server connection.

If your Langflow server administrator has locked MCP server management, you will receive a locked message when you try to add or modify servers. For more information, see [Lock MCP server management](/mcp-server#restrict-mcp-server-management).

## Modify MCP server environment variables with the API {#mcp-api-tweaks}

You can modify MCP server environment variables at runtime when running flows through the [Langflow API](/api-reference-api-examples) by tweaking the **MCP Tools** component.

You can include tweaks with any Langflow API request that supports the `tweaks` parameter, such as POST requests to the `/run` or `/webhook` endpoints.
For more information, see [Input schema (tweaks)](/concepts-publish#input-schema).

To modify the **MCP Tools** component's environment variables with tweaks, do the following:

1. Open the flow that contains your **MCP Tools** component.
2. To find the **MCP Tools** component's unique ID, in your **MCP Tools** component, click <Icon name="SlidersHorizontal" aria-hidden="true"/> **Controls**.
The component's ID is displayed in the **Controls** pane, such as `MCPTools-Bzahc`.
3. Send a POST request to the Langflow server's `/run` endpoint, and include tweaks to the **MCP Tools** component.

    The following examples demonstrate a request structure with the `env` object nested under `mcp_server` in the `tweaks` payload:

    <Tabs groupId="language">
    <TabItem value="python" label="Python" default>

    ```python
    import requests
    import os

    LANGFLOW_SERVER_ADDRESS = "http://localhost:7860"
    FLOW_ID = "your-flow-id"
    LANGFLOW_API_KEY = os.getenv("LANGFLOW_API_KEY")
    MCP_TOOLS_COMPONENT_ID = "MCPTools-Bzahc"

    url = f"{LANGFLOW_SERVER_ADDRESS}/api/v1/run/{FLOW_ID}?stream=false"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": LANGFLOW_API_KEY
    }
    payload = {
        "output_type": "chat",
        "input_type": "chat",
        "input_value": "What sales data is available to me?",
        "tweaks": {
            MCP_TOOLS_COMPONENT_ID: {
                "mcp_server": {
                    "env": {
                        "API_URL": "https://api.example.com",
                        "API_KEY": "your-mcp-server-api-key",
                        "ENVIRONMENT": "production"
                    }
                }
            }
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.json())
    ```

    </TabItem>
    <TabItem value="typescript" label="TypeScript">

    ```typescript
    const LANGFLOW_SERVER_ADDRESS = "http://localhost:7860";
    const FLOW_ID = "your-flow-id";
    const LANGFLOW_API_KEY = process.env.LANGFLOW_API_KEY || "";
    const MCP_TOOLS_COMPONENT_ID = "MCPTools-Bzahc";

    const url = `${LANGFLOW_SERVER_ADDRESS}/api/v1/run/${FLOW_ID}?stream=false`;

    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "x-api-key": LANGFLOW_API_KEY,
      },
      body: JSON.stringify({
        output_type: "chat",
        input_type: "chat",
        input_value: "What sales data is available to me?",
        tweaks: {
          [MCP_TOOLS_COMPONENT_ID]: {
            mcp_server: {
              env: {
                API_URL: "https://api.example.com",
                API_KEY: "your-mcp-server-api-key",
                ENVIRONMENT: "production",
              },
            },
          },
        },
      }),
    });

    const data = await response.json();
    console.log(data);
    ```

    </TabItem>
    <TabItem value="curl" label="cURL">

    ```bash
    curl --request POST \
      --url "http://LANGFLOW_SERVER_ADDRESS/api/v1/run/FLOW_ID?stream=false" \
      --header "Content-Type: application/json" \
      --header "x-api-key: LANGFLOW_API_KEY" \
      --data '{
        "output_type": "chat",
        "input_type": "chat",
        "input_value": "What sales data is available to me?",
        "tweaks": {
          "MCP_TOOLS_COMPONENT_ID": {
            "mcp_server": {
              "env": {
                "API_URL": "https://api.example.com",
                "API_KEY": "your-mcp-server-api-key",
                "ENVIRONMENT": "production"
              }
            }
          }
        }
      }'
    ```

    </TabItem>
    </Tabs>

    Replace `MCP_TOOLS_COMPONENT_ID`, `LANGFLOW_API_KEY`, `LANGFLOW_SERVER_ADDRESS`, and `FLOW_ID` with the actual values from your Langflow deployment.

    Langflow doesn't automatically discover or expose which environment variables your MCP server accepts from the **MCP Tools** component.
    To determine which environment variables your MCP server accepts, see the MCP server's documentation. For example, the [Astra DB MCP server](https://github.com/datastax/astra-db-mcp) requires `ASTRA_DB_APPLICATION_TOKEN` and `ASTRA_DB_API_ENDPOINT`, with an optional variable for `ASTRA_DB_KEYSPACE`, as documented in its repository.

## Use global variables in MCP server headers {#use-global-variables-in-mcp-server-headers}

You can use [global variables](/configuration-global-variables) in MCP server header values to securely store and reference API keys, authentication tokens, and other sensitive values. This is particularly useful for deployment scenarios where you need to pass user-specific credentials at runtime.

Enter a global variable name as the header value, and Langflow resolves the global variable name to its actual value before making the MCP server request. Langflow only passes the token value to your server; it doesn't validate tokens on behalf of your MCP server.

For example, to create a global variable named `TEST_BEARER_TOKEN` for MCP server bearer authentication, do the following:

1. To open the **Global Variables** pane, click your profile icon, select **Settings**, and then click <Icon name="Globe" aria-hidden="true"/> **Global Variables**.
2. Create a **Credential** global variable named `TEST_BEARER_TOKEN`.
3. In the **Value** field, enter your MCP server's bearer token value. The value must include the `Bearer` prefix with a space, for example: `Bearer eyJhbG...`.
4. Click **Save Variable**.
5. To manage MCP server connections for your Langflow client, click <McpIcon /> **MCP servers**, and then click <Icon name="ArrowUpRight" aria-hidden="true"/> **Manage Servers**, or click your profile icon, select **Settings**, and then click **MCP Servers**.
6. Click <Icon name="Plus" aria-hidden="true"/> **Add MCP Server**.
7. Select the following:
    * **Name**: test-mcp-server
    * **Streamable HTTP/SSE URL**: Your MCP server's URL, such as `http://127.0.0.1:8000/mcp`.
    * **Headers**: In the key field, enter the literal string `Authorization`. For the key's value, enter `TEST_BEARER_TOKEN`, or the exact name of your global variable.
8. Click **Create Server**.

   If the connection succeeds, Langflow shows the number of tools exposed by the server.

   After creating the server and global variable, you can connect to the server with the **MCP Tools** component, as explained in the next steps.

9. Add the **MCP Tools** component to a flow.
10. In the **MCP Tools** component, confirm the **MCP Server** is set to the server you created.
The MCP server configuration already includes the headers you configured earlier, so no further configuration is needed in the component. The global variable `TEST_BEARER_TOKEN` is automatically resolved when the component makes requests to the MCP server.

11. Optional: To override headers or add additional headers to the **MCP Tools** component, click the component to view the **Headers** parameter in the [component inspection panel](/concepts-components#component-menus), and then add header key values. Headers configured in the component take precedence over the headers configured in the MCP server settings.

12. Test your flow to make sure the agent uses your server to respond to queries. Open the **Playground**, and then enter a prompt that uses a tool that you connected through the **MCP Tools** component.

    Langflow automatically resolves `TEST_BEARER_TOKEN` to its actual value before sending the request to the MCP server. When your MCP server receives the request, the `Authorization` header contains the resolved token value.

## Propagate `x-api-key` to nested MCP servers {#propagate-x-api-key}

When Langflow runs as an MCP server and a flow contains an [**MCP Tools** component](/mcp-tools) that calls an external server, you can forward the outer client's `x-api-key` or `Authorization` header at runtime.

In the nested server's **Headers** config, set the key and value to the same header name, such as `x-api-key` and `x-api-key`.
Langflow reads the matching header from the incoming request and substitutes it before calling the nested server.

If the incoming request does not include the configured header, the literal string is passed through unchanged.

## See also

- [Langflow MCP Client](./langflow-mcp-client.mdx)
- [Use Langflow as an MCP server](/mcp-server)
- [Use a DataStax Astra DB MCP server with the MCP Tools component](/mcp-component-astra)

### docs/docs/Components/components-agents.mdx

---
title: Agents
slug: /components-agents
---

import PartialAgentsWork from '@site/docs/_partial-agents-work.mdx';

Langflow's **Agent** component is critical for building agent flows.
This component defines the behavior and capabilities of AI agents in your flows.

<PartialAgentsWork />

## Examples of agent flows

For examples of flows using the **Agent** component, see the following:

* [Langflow quickstart](/get-started-quickstart): Start with the **Simple Agent** template, modify its tools, and then learn how to use an agent flow in an application.

    The **Simple Agent** template creates a basic agent flow with an **Agent** component that can use two other Langflow components as tools.
    The LLM specified in the **Agent** component's settings can use its own built-in functionality as well as the functionality provided by the connected tools when generating responses.

* [Use an agent as a tool](/agents-tools#use-an-agent-as-a-tool): Create a multi-agent flow.

* [Use Langflow as an MCP client](/mcp-client) and [Use Langflow as an MCP server](/mcp-server): Use the **Agent** and [**MCP Tools** component](/mcp-tools) to implement the Model Context Protocol (MCP) in your flows.

## Agent component {#agent-component}

The **Agent** component is the primary agent actor in your agent flows.
This component uses an LLM integration to respond to input, such as a chat message or file upload.

The agent can use the tools already available in the base LLM as well as additional tools that you connect to the **Agent** component's **Tools** port.
You can connect any Langflow component as a tool, including other **Agent** components and MCP servers through the [**MCP Tools** component](/mcp-tools).

For more information about using this component, see [Use Langflow agents](/agents).

## See also

* [**MCP Tools** component](/mcp-tools)
* [**Message History** component](/message-history)
* [Store chat memory](/memory#store-chat-memory)
* [Bundles](/components-bundle-components)
* [Legacy LangChain components](/bundles-langchain#legacy-langchain-components)

### docs/docs/Components/components-bundles.mdx

---
title: About bundles
slug: /components-bundle-components
---

import Icon from "@site/src/components/icon";
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Bundles contain custom components that support specific third-party integrations with Langflow.
You add them to your flows and configure them in the same way as Langflow's core components.

To browse bundles, click <Icon name="Blocks" aria-hidden="true" /> **Bundles** in the visual editor.

## Bundle maintenance and documentation

Many bundled components are developed by third-party contributors to the Langflow codebase.

Some providers contribute documentation with their bundles, whereas others document their bundles in their own documentation.
Some bundles have no documentation.

To find documentation for a specific bundled component, browse the Langflow docs and your provider's documentation.
If available, you can also find links to relevant documentation, such as API endpoints, through the component itself:

1. Click the component to expose the [component inspection panel](/concepts-components#component-menus).
2. Click <Icon name="Ellipsis" aria-hidden="true" /> **More**.
3. Select **Docs**.

The Langflow documentation focuses on using bundles within flows.
For that reason, it focuses on the Langflow-specific configuration steps for bundled components.
For information about provider-specific features or APIs, see the provider's documentation.

## Component parameters

import PartialParams from '@site/docs/_partial-hidden-params.mdx';

<PartialParams />

## Core components and bundles

:::tip
The Langflow documentation doesn't list all bundles or components in bundles.
For the most accurate and up-to-date list of bundles and components for your version of Langflow, check <Icon name="Blocks" aria-hidden="true" /> **Bundles** in the visual editor.

If you can't find a component that you used in an earlier version of Langflow, it may have been removed or marked as a [legacy component](#legacy-bundles).
:::

Langflow offers generic <Icon name="Component" aria-hidden="true" /> **Core components** in addition to third-party, provider-specific bundles.

If you are looking for a specific service or integration, you can <Icon name="Search" aria-hidden="true" /> **Search** components in the visual editor.

If all else fails, you can always create your own [custom components](/components-custom-components).

## Legacy bundles

import PartialLegacy from '@site/docs/_partial-legacy.mdx';

<PartialLegacy />

The following bundles include only legacy components.

### CrewAI bundle

Replace the following legacy CrewAI components with other agentic components, such as the [**Agent** component](/components-agents).

<details>
<summary>CrewAI Agent</summary>

This component represents CrewAI agents, allowing for the creation of specialized AI agents with defined roles goals and capabilities within a crew.
For more information, see the [CrewAI agents documentation](https://docs.crewai.com/core-concepts/Agents/).

This component accepts the following parameters:

| Name | Display Name | Info |
|------|--------------|------|
| role | Role | Input parameter. The role of the agent. |
| goal | Goal | Input parameter. The objective of the agent. |
| backstory | Backstory | Input parameter. The backstory of the agent. |
| tools | Tools | Input parameter. The tools at the agent's disposal. |
| llm | Language Model | Input parameter. The language model that runs the agent. |
| memory | Memory | Input parameter. This determines whether the agent should have memory or not. |
| verbose | Verbose | Input parameter. This enables verbose output. |
| allow_delegation | Allow Delegation | Input parameter. This determines whether the agent is allowed to delegate tasks to other agents. |
| allow_code_execution | Allow Code Execution | Input parameter. This determines whether the agent is allowed to execute code. |
| kwargs | kwargs | Input parameter. Additional keyword arguments for the agent. |
| output | Agent | Output parameter. The constructed CrewAI Agent object. |

</details>

<details>
<summary>CrewAI Hierarchical Crew, CrewAI Hierarchical Task</summary>

The **CrewAI Hierarchical Crew** component represents a group of agents managing how they should collaborate and the tasks they should perform in a hierarchical structure. This component allows for the creation of a crew with a manager overseeing the task execution.
For more information, see the [CrewAI hierarchical crew documentation](https://docs.crewai.com/how-to/Hierarchical/).

It accepts the following parameters:

| Name | Display Name | Info |
|------|--------------|------|
| agents | Agents | Input parameter. The list of Agent objects representing the crew members. |
| tasks | Tasks | Input parameter. The list of HierarchicalTask objects representing the tasks to be executed. |
| manager_llm | Manager LLM | Input parameter. The language model for the manager agent. |
| manager_agent | Manager Agent | Input parameter. The specific agent to act as the manager. |
| verbose | Verbose | Input parameter. This enables verbose output for detailed logging. |
| memory | Memory | Input parameter. The memory configuration for the crew. |
| use_cache | Use Cache | Input parameter. This enables caching of results. |
| max_rpm | Max RPM | Input parameter. This sets the maximum requests per minute. |
| share_crew | Share Crew | Input parameter. This determines if the crew information is shared among agents. |
| function_calling_llm | Function Calling LLM | Input parameter. The language model for function calling. |
| crew | Crew | Output parameter. The constructed Crew object with hierarchical task execution. |

</details>

<details>
<summary>CrewAI Sequential Crew, CrewAI Sequential Task</summary>

The **CrewAI Sequential Crew** component represents a group of agents with tasks that are executed sequentially. This component allows for the creation of a crew that performs tasks in a specific order.
For more information, see the [CrewAI sequential crew documentation](https://docs.crewai.com/how-to/Sequential/).

It accepts the following parameters:

| Name | Display Name | Info |
|------|--------------|------|
| tasks | Tasks | Input parameter. The list of SequentialTask objects representing the tasks to be executed. |
| verbose | Verbose | Input parameter. This enables verbose output for detailed logging. |
| memory | Memory | Input parameter. The memory configuration for the crew. |
| use_cache | Use Cache | Input parameter. This enables caching of results. |
| max_rpm | Max RPM | Input parameter. This sets the maximum requests per minute. |
| share_crew | Share Crew | Input parameter. This determines if the crew information is shared among agents. |
| function_calling_llm | Function Calling LLM | Input parameter. The language model for function calling. |
| crew | Crew | Output parameter. The constructed Crew object with sequential task execution. |

</details>

<details>
<summary>CrewAI Sequential Task Agent</summary>

This component creates a CrewAI Task and its associated agent allowing for the definition of sequential tasks with specific agent roles and capabilities.
For more information, see the [CrewAI sequential agents documentation](https://docs.crewai.com/how-to/Sequential/).

It accepts the following parameters:

| Name | Display Name | Info |
|------|--------------|------|
| role | Role | Input parameter. The role of the agent. |
| goal | Goal | Input parameter. The objective of the agent. |
| backstory | Backstory | Input parameter. The backstory of the agent. |
| tools | Tools | Input parameter. The tools at the agent's disposal. |
| llm | Language Model | Input parameter. The language model that runs the agent. |
| memory | Memory | Input parameter. This determines whether the agent should have memory or not. |
| verbose | Verbose | Input parameter. This enables verbose output. |
| allow_delegation | Allow Delegation | Input parameter. This determines whether the agent is allowed to delegate tasks to other agents. |
| allow_code_execution | Allow Code Execution | Input parameter. This determines whether the agent is allowed to execute code. |
| agent_kwargs | Agent kwargs | Input parameter. The additional kwargs for the agent. |
| task_description | Task Description | Input parameter. The descriptive text detailing the task's purpose and execution. |
| expected_output | Expected Task Output | Input parameter. The clear definition of the expected task outcome. |
| async_execution | Async Execution | Input parameter. Boolean flag indicating asynchronous task execution. |
| previous_task | Previous Task | Input parameter. The previous task in the sequence for chaining. |
| task_output | Sequential Task | Output parameter. The list of SequentialTask objects representing the created tasks. |

</details>

### Embeddings bundle

* **Embedding Similarity**: Replaced by built-in similarity search functionality in vector store components.
* **Text Embedder**: Replaced by the embedding model components.

### Vector Stores bundle

This bundle contains only the legacy **Local DB** component.
All other vector store components can be found within their respective provider-specific bundles, such as the [**DataStax** bundle](/bundles-datastax).

<details>
<summary>Local DB</summary>

Replace the **Local DB** component with the **Chroma DB** vector store component (in the **Chroma** bundle) or another vector store component.

The **Local DB** component reads and writes to a persistent, in-memory Chroma DB instance intended for use with Langflow.
It has separate modes for reads and writes, automatic collection management, and default persistence in your Langflow cache directory.

Set the **Mode** parameter to reflect the operation you want the component to perform, and then configure the other parameters accordingly.
Some parameters are only available for one mode.

<Tabs>
<TabItem value="ingest" label="Ingest">

To create or write to your local Chroma vector store, use **Ingest** mode.

The following parameters are available in **Ingest** mode:

| Name | Type | Description |
|------|------|-------------|
| **Name Your Collection** (`collection_name`) | String | Input parameter. The name for your Chroma vector store collection. Default: `langflow`. Only available in **Ingest** mode. |
| **Persist Directory** (`persist_directory`) | String | Input parameter. The base directory where you want to create and persist the vector store. If you use the **Local DB** component in multiple flows or to create multiple collections, collections are stored at `$PERSISTENT_DIRECTORY/vector_stores/$COLLECTION_NAME`. If not specified, the default location is your Langflow configuration directory. For more information, see [Memory management options](/memory). |
| **Embedding** (`embedding`) | Embeddings | Input parameter. The embedding function to use for the vector store. |
| **Allow Duplicates** (`allow_duplicates`) | Boolean | Input parameter. If `true` (default), writes don't check for existing duplicates in the collection, allowing you to store multiple copies of the same content. If `false`, writes won't add documents that match existing documents already present in the collection. If `false`, it can strictly enforce deduplication by searching the entire collection or only search the number of records, specified in `limit`. Only available in **Ingest** mode. |
| **Ingest Data** (`ingest_data`) | JSON or Table | Input parameter. The records to write to the collection. Records are embedded and indexed for semantic search. Only available in **Ingest** mode. |
| **Limit** (`limit`) | Integer | Input parameter. Limit the number of records to compare when **Allow Duplicates** is `false`. This can help improve performance when writing to large collections, but it can result in some duplicate records. Only available in **Ingest** mode. |

</TabItem>
<TabItem value="retrieve" label="Retrieve">

To read from your local Chroma vector store, use **Retrieve** mode.

The following parameters are available in **Retrieve** mode:

| Name | Type | Description |
|------|------|-------------|
| **Persist Directory** (`persist_directory`) | String | Input parameter. The base directory where you want to create and persist the vector store. If you use the **Local DB** component in multiple flows or to create multiple collections, collections are stored at `$PERSISTENT_DIRECTORY/vector_stores/$COLLECTION_NAME`. If not specified, the default location is your Langflow configuration directory. For more information, see [Memory management options](/memory). |
| **Existing Collections** (`existing_collections`) | String | Input parameter. Select a previously-created collection to search. Only available in **Retrieve** mode. |
| **Embedding** (`embedding`) | Embeddings | Input parameter. The embedding function to use for the vector store. |
| **Search Type** (`search_type`) | String | Input parameter. The type of search to perform, either `Similarity` or `MMR`. Only available in **Retrieve** mode. |
| **Search Query** (`search_query`) | String | Input parameter. Enter a query for similarity search. Only available in **Retrieve** mode. |
| **Number of Results** (`number_of_results`) | Integer | Input parameter. Number of search results to return. Default: 10. Only available in **Retrieve** mode. |

</TabItem>
</Tabs>

</details>

### Zep bundle

<details>
<summary>Zep Chat Memory</summary>

The **Zep Chat Memory** component is a legacy component.
Replace this component with the [**Message History** component](/message-history).

This component creates a `ZepChatMessageHistory` instance, enabling storage and retrieval of chat messages using Zep, a memory server for LLMs.

It accepts the following parameters:

| Name          | Type          | Description                                               |
|---------------|---------------|-----------------------------------------------------------|
| url           | MessageText   | Input parameter. The URL of the Zep instance. Required. |
| api_key       | SecretString  | Input parameter. The API Key for authentication with the Zep instance. |
| api_base_path | Dropdown      | Input parameter. The API version to use. Options include api/v1 or api/v2. |
| session_id    | MessageText   | Input parameter. The unique identifier for the chat session. Optional. |
| message_history | BaseChatMessageHistory  | Output parameter. An instance of ZepChatMessageHistory for the session. |

</details>

## See also

* [LangWatch observability and evaluation](/integrations-langwatch)



<!-- Not documented but in Langflow as of 1.5.11 -->
<!--
* AgentQL
* Confluence
* Git
* Home Assistant
* Jigsawstack
* LangWatch (Mentioned on integrations-langwatch.mdx)
* Needle
* Not Diamond
* Olivya
* Scrape Graph AI
* SerpApi (Mentioned on components-tools.mdx)
* Tavily (Mentioned on components-tools.mdx)
* Twelve Labs (Mentioned on concepts-file-management.mdx and components-data.mdx)
* Unstructured
* WolframAlpha
* yfinance/Yahoo! Search (Mentioned on components-tools.mdx)
* YouTube (Mentioned on concepts-file-management.mdx and components-data.mdx)
-->

### docs/docs/API-Reference/workflows-api.mdx

---
title: Workflow API (Beta)
slug: /workflow-api
---
import CodeSnippet from '@site/src/components/CodeSnippet';
import exampleWorkflowsApiExampleSynchronousRequest from '!!raw-loader!@site/docs/API-Reference/curl-examples/workflows-api/example-synchronous-request.sh';
import exampleWorkflowsApiExampleAsynchronousRequest from '!!raw-loader!@site/docs/API-Reference/curl-examples/workflows-api/example-asynchronous-request.sh';
import exampleWorkflowsApiExampleRequest from '!!raw-loader!@site/docs/API-Reference/curl-examples/workflows-api/example-request.sh';
import exampleWorkflowsApiExampleRequest2 from '!!raw-loader!@site/docs/API-Reference/curl-examples/workflows-api/example-request-2.sh';
import examplePythonWorkflowsApiExampleSynchronousRequest from '!!raw-loader!@site/docs/API-Reference/python-examples/workflows-api/example-synchronous-request.py';
import examplePythonWorkflowsApiExampleAsynchronousRequest from '!!raw-loader!@site/docs/API-Reference/python-examples/workflows-api/example-asynchronous-request.py';
import examplePythonWorkflowsApiExampleRequest from '!!raw-loader!@site/docs/API-Reference/python-examples/workflows-api/example-request.py';
import examplePythonWorkflowsApiExampleRequest2 from '!!raw-loader!@site/docs/API-Reference/python-examples/workflows-api/example-request-2.py';
import exampleJavascriptWorkflowsApiExampleSynchronousRequest from '!!raw-loader!@site/docs/API-Reference/javascript-examples/workflows-api/example-synchronous-request.js';
import exampleJavascriptWorkflowsApiExampleAsynchronousRequest from '!!raw-loader!@site/docs/API-Reference/javascript-examples/workflows-api/example-asynchronous-request.js';
import exampleJavascriptWorkflowsApiExampleRequest from '!!raw-loader!@site/docs/API-Reference/javascript-examples/workflows-api/example-request.js';
import exampleJavascriptWorkflowsApiExampleRequest2 from '!!raw-loader!@site/docs/API-Reference/javascript-examples/workflows-api/example-request-2.js';




import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import PartialAPISetup from '@site/docs/_partial-api-setup.mdx';

:::warning Beta Feature
The Workflow API is currently in **Beta**.
The API endpoints and response formats may change in future releases.
:::

The Workflow API provides programmatic access to execute Langflow workflows synchronously or asynchronously.
Synchronous requests receive complete results immediately upon completion.
Asynchronous requests are queued in the background and will run until complete, or a request is issued to the [Stop Workflow endpoint](#stop-workflow-endpoint).

The Workflow API is part of the Langflow Developer v2 API and offers enhanced workflow execution capabilities compared to the v1 `/run` endpoint.

<PartialAPISetup />

## Execute workflows endpoint (synchronous or asynchronous)

**Endpoint:**

```
POST /api/v2/workflows
```

**Description:** Execute a workflow synchronously and receive complete results immediately upon completion.
Set `background=false` to make the request synchronous.

### Example synchronous request

Execute a workflow synchronously and receive complete results immediately:

<Tabs>
<TabItem value="Python" label="Python" default>

<CodeSnippet source={examplePythonWorkflowsApiExampleSynchronousRequest} language="python" />

</TabItem>
<TabItem value="JavaScript" label="JavaScript">

<CodeSnippet source={exampleJavascriptWorkflowsApiExampleSynchronousRequest} language="javascript" />

</TabItem>
<TabItem value="curl" label="curl">

<CodeSnippet source={exampleWorkflowsApiExampleSynchronousRequest} language="bash" />

</TabItem>
</Tabs>

### Example asynchronous request

For long-running workflows, set `background=true` to get a `job_id` immediately, and then poll the status [using the GET endpoint](#get-workflow-status-endpoint) until the job is complete.

To stop a job, send a POST request to the [Stop workflow endpoint](#stop-workflow-endpoint).

:::tip
The asynchronous request contains `stream` parameter, but streaming is not yet supported. The parameter is included for future compatibility.
:::

**Example request:**

<Tabs>
<TabItem value="Python" label="Python" default>

<CodeSnippet source={examplePythonWorkflowsApiExampleAsynchronousRequest} language="python" />

</TabItem>
<TabItem value="JavaScript" label="JavaScript">

<CodeSnippet source={exampleJavascriptWorkflowsApiExampleAsynchronousRequest} language="javascript" />

</TabItem>
<TabItem value="curl" label="curl">

<CodeSnippet source={exampleWorkflowsApiExampleAsynchronousRequest} language="bash" />

</TabItem>
</Tabs>

**Response:**

```json
{
  "job_id": "job_id_1234567890",
  "created_timestamp": "2025-01-15T10:30:00Z",
  "status": "queued",
  "errors": []
}
```

### Request body

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `flow_id` | `string` | Yes | - | The ID or endpoint name of the flow to execute. |
| `flow_version` | `string` | No | - | Optional version hash to pin to a specific flow version. |
| `background` | `boolean` | No | `false` | Must be `false` for synchronous execution. |
| `inputs` | `object` | No | `{}` | Inputs for the workflow execution. Uses component identifiers with dot notation (e.g., `ChatInput-abc.input_value`). See [Component identifiers and input structure](#component-identifiers-and-input-structure) for detailed information. |
| `globals` | `object` | No | `{}` | Request-level global variables available to workflow components. Use this body field for arbitrary strings, including Unicode values. Keys are limited to 256 characters and values to 64 KB. See [Migrating from `X-LANGFLOW-GLOBAL-VAR-*` headers](#migrating-from-x-langflow-global-var--headers). |

### Example response

```json
{
  "flow_id": "flow_67ccd2be17f0819081ff3bb2cf6508e60bb6a6b452d3795b",
  "job_id": "job_id_1234567890",
  "object": "response",
  "created_at": 1741476542,
  "status": "completed",
  "errors": [],
  "inputs": {
    "ChatInput-abc.input_type": "chat",
    "ChatInput-abc.input_value": "what is 2+2",
    "ChatInput-abc.session_id": "session-123"
  },
  "globals": {
    "FILENAME": "relatório—final.pdf",
    "OWNER_NAME": "José"
  },
  "outputs": {
    "ChatOutput-xyz": {
      "type": "message",
      "component_id": "ChatOutput-xyz",
      "status": "completed",
      "content": "2 + 2 equals 4."
    }
  },
  "metadata": {}
}
```

### Response body

The response includes an `outputs` field containing component-level results. Each output has a `type` field indicating the type of content:

| Type | Description | Example |
|------|-------------|---------|
| `message` | Text message content. | Chat responses, summaries |
| `image` | Image URL or data. | Generated images, processed images |
| `sql` | SQL query results. | Database query outputs |
| `data` | Structured data. | JSON objects, arrays |
| `file` | File reference. | Generated documents, reports |

## Get workflow status endpoint

**Endpoint:** `GET /api/v2/workflows`

**Description:** Retrieve the status and results of a workflow execution by job ID.

### Example request

<Tabs>
<TabItem value="Python" label="Python" default>

<CodeSnippet source={examplePythonWorkflowsApiExampleRequest} language="python" />

</TabItem>
<TabItem value="JavaScript" label="JavaScript">

<CodeSnippet source={exampleJavascriptWorkflowsApiExampleRequest} language="javascript" />

</TabItem>
<TabItem value="curl" label="curl">

<CodeSnippet source={exampleWorkflowsApiExampleRequest} language="bash" />

</TabItem>
</Tabs>

### Query parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `job_id` | `string` | Yes | The job ID returned from a workflow execution. |
| `stream` | `boolean` | No | If `true`, returns server-sent events stream. Default: `false`. |
| `sequence_id` | `integer` | No | Optional sequence ID to resume streaming from a specific point. |

### Example response

```json
{
  "flow_id": "flow_67ccd2be17f0819081ff3bb2cf6508e60bb6a6b452d3795b",
  "job_id": "job_id_1234567890",
  "object": "response",
  "created_at": 1741476542,
  "status": "completed",
  "errors": [],
  "outputs": {
    "ChatOutput-xyz": {
      "type": "message",
      "component_id": "ChatOutput-xyz",
      "status": "completed",
      "content": "Processing complete..."
    }
  },
  "input": [
    {
      "type": "text",
      "data": "Input text prompt for the workflow execution",
      "role": "User"
    }
  ],
  "metadata": {}
}
```

### Response body

The response includes a `status` field that indicates the current state of the workflow execution:

| Status | Description |
|--------|-------------|
| `queued` | Job is queued and waiting to start. |
| `in_progress` | Job is currently executing. |
| `completed` | Job completed successfully. |
| `failed` | Job failed during execution. |
| `error` | Job encountered an error. |

## Stop workflow endpoint

**Endpoint:** `POST /api/v2/workflows/stop`

**Description:** Stop a running workflow execution by job ID.

### Example request

<Tabs>
<TabItem value="Python" label="Python" default>

<CodeSnippet source={examplePythonWorkflowsApiExampleRequest2} language="python" />

</TabItem>
<TabItem value="JavaScript" label="JavaScript">

<CodeSnippet source={exampleJavascriptWorkflowsApiExampleRequest2} language="javascript" />

</TabItem>
<TabItem value="curl" label="curl">

<CodeSnippet source={exampleWorkflowsApiExampleRequest2} language="bash" />

</TabItem>
</Tabs>

### Request body

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `job_id` | `string` | Yes | - | The job ID of the workflow to stop. |

### Example response

```json
{
  "job_id": "job_id_1234567890",
  "message": "Job job_id_1234567890 cancelled successfully."
}
```

## Migrating from `X-LANGFLOW-GLOBAL-VAR-*` headers

Earlier preview releases of the Workflow API accepted request-level global variables via `X-LANGFLOW-GLOBAL-VAR-*` HTTP headers. HTTP headers cannot reliably carry arbitrary Unicode values, so the v2 Workflow API now accepts globals as a typed `globals` field in the JSON request body.

For backwards compatibility, the previous header transport is still honored for one release:

- Body globals always win when the same key is sent both ways.
- A deprecation warning is logged on every request that carries `X-LANGFLOW-GLOBAL-VAR-*` headers.
- Header-based globals will be **removed in a future Langflow release**. Migrate to the `globals` body field at your earliest convenience.

**Before (deprecated):**

```bash
curl -X POST "$LANGFLOW_URL/api/v2/workflows" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-LANGFLOW-GLOBAL-VAR-FILENAME: relatorio-final.pdf" \
  -H "X-LANGFLOW-GLOBAL-VAR-OWNER_NAME: Jose" \
  --data '{"flow_id": "..."}'
```

**After:**

```bash
curl -X POST "$LANGFLOW_URL/api/v2/workflows" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -H "Content-Type: application/json" \
  --data '{
    "flow_id": "...",
    "globals": {
      "FILENAME": "relatório—final.pdf",
      "OWNER_NAME": "José"
    }
  }'
```

Keys may use the same characters supported by the global variables panel in the Langflow UI; they are bounded to 256 characters, and values are bounded to 64 KB.

## Component identifiers and input structure

The Workflows API uses component identifiers with dot notation to specify inputs for individual components in your workflow. This allows you to pass values to specific components and override component parameters.

Component identifiers use the format `{component_id}.{parameter_name}`.
When making requests to the Workflows API, include component identifiers in the `inputs` object.
For example, this demonstrates targeting multiple components and their parameters in a single request.

```json
{
  "flow_id": "your-flow-id",
  "inputs": {
    "ChatInput-abc.input_type": "chat",
    "ChatInput-abc.input_value": "what is 2+2",
    "ChatInput-abc.session_id": "session-123",
    "OpenSearchComponent-xyz.opensearch_url": "https://opensearch:9200",
    "LLMComponent-123.temperature": 0.7,
    "LLMComponent-123.max_tokens": 100
  }
}
```

To find the component ID in the Langflow UI, open your flow in Langflow, click the component, and then click **Controls**. The component ID is at the top of the **Controls** pane.

You can override any component's parameters.

## Error handling

The API uses standard HTTP status codes to indicate success or failure:

| Status Code | Description |
|-------------|-------------|
| `200 OK` | Request successful. |
| `400 Bad Request` | Invalid request parameters. |
| `401 Unauthorized` | Invalid or missing API key. |
| `404 Not Found` | Flow not found or developer API disabled. |
| `500 Internal Server Error` | Server error during execution. |
| `501 Not Implemented` | Endpoint not yet implemented. |

### Error response format

```json
{
  "detail": "Error message describing what went wrong"
}
```

### docs/docs/API-Reference/api-build.mdx

---
title: Build endpoints
slug: /api-build
---
import CodeSnippet from '@site/src/components/CodeSnippet';
import exampleApiBuildBuildFlowAndStreamEvents from '!!raw-loader!@site/docs/API-Reference/curl-examples/api-build/build-flow-and-stream-events.sh';
import resultApiBuildResultBuildFlowAndStreamEvents from '!!raw-loader!@site/docs/API-Reference/curl-examples/api-build/result-build-flow-and-stream-events.json';
import exampleApiBuildBuildFlowAndStreamEvents2 from '!!raw-loader!@site/docs/API-Reference/curl-examples/api-build/build-flow-and-stream-events-2.sh';
import resultApiBuildResultBuildFlowAndStreamEvents2 from '!!raw-loader!@site/docs/API-Reference/curl-examples/api-build/result-build-flow-and-stream-events-2.json';
import exampleApiBuildBuildFlowAndStreamEvents3 from '!!raw-loader!@site/docs/API-Reference/curl-examples/api-build/build-flow-and-stream-events-3.sh';
import exampleApiBuildSetStartAndStopPoints from '!!raw-loader!@site/docs/API-Reference/curl-examples/api-build/set-start-and-stop-points.sh';
import exampleApiBuildOverrideFlowParameters from '!!raw-loader!@site/docs/API-Reference/curl-examples/api-build/override-flow-parameters.sh';
import resultApiBuildResultOverrideFlowParameters from '!!raw-loader!@site/docs/API-Reference/curl-examples/api-build/result-override-flow-parameters.json';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import examplePythonApiBuildBuildFlowAndStreamEvents from '!!raw-loader!@site/docs/API-Reference/python-examples/api-build/build-flow-and-stream-events.py';
import exampleJavascriptApiBuildBuildFlowAndStreamEvents from '!!raw-loader!@site/docs/API-Reference/javascript-examples/api-build/build-flow-and-stream-events.js';
import examplePythonApiBuildBuildFlowAndStreamEvents2 from '!!raw-loader!@site/docs/API-Reference/python-examples/api-build/build-flow-and-stream-events-2.py';
import exampleJavascriptApiBuildBuildFlowAndStreamEvents2 from '!!raw-loader!@site/docs/API-Reference/javascript-examples/api-build/build-flow-and-stream-events-2.js';
import examplePythonApiBuildBuildFlowAndStreamEvents3 from '!!raw-loader!@site/docs/API-Reference/python-examples/api-build/build-flow-and-stream-events-3.py';
import exampleJavascriptApiBuildBuildFlowAndStreamEvents3 from '!!raw-loader!@site/docs/API-Reference/javascript-examples/api-build/build-flow-and-stream-events-3.js';
import examplePythonApiBuildSetStartAndStopPoints from '!!raw-loader!@site/docs/API-Reference/python-examples/api-build/set-start-and-stop-points.py';
import exampleJavascriptApiBuildSetStartAndStopPoints from '!!raw-loader!@site/docs/API-Reference/javascript-examples/api-build/set-start-and-stop-points.js';
import examplePythonApiBuildOverrideFlowParameters from '!!raw-loader!@site/docs/API-Reference/python-examples/api-build/override-flow-parameters.py';
import exampleJavascriptApiBuildOverrideFlowParameters from '!!raw-loader!@site/docs/API-Reference/javascript-examples/api-build/override-flow-parameters.js';



:::info
The `/build` endpoints are used by Langflow's frontend visual editor code.
These endpoints are part of the internal Langflow codebase.

Don't use these endpoints to run flows in applications that use your Langflow flows.
To run flows in your apps, see [Flow trigger endpoints](/api-flows-run).
:::

The `/build` endpoints support Langflow's frontend code for building flows in the Langflow visual editor.
You can use these endpoints to build vertices and flows, as well as execute flows with streaming event responses.
You might need to use or understand these endpoints when contributing to the Langflow codebase.

## Build flow and stream events

This endpoint builds and executes a flow, returning a job ID that can be used to stream execution events.

1. Send a POST request to the `/build/$FLOW_ID/flow` endpoint:

    <Tabs>
    <TabItem value="Python" label="Python" default>

    <CodeSnippet source={examplePythonApiBuildBuildFlowAndStreamEvents} language="python" />

    </TabItem>
    <TabItem value="JavaScript" label="JavaScript">

    <CodeSnippet source={exampleJavascriptApiBuildBuildFlowAndStreamEvents} language="javascript" />

    </TabItem>
    <TabItem value="curl" label="curl">

    <CodeSnippet source={exampleApiBuildBuildFlowAndStreamEvents} language="bash" />

    </TabItem>
    </Tabs>

    <details>
    <summary>Result</summary>

    <CodeSnippet source={resultApiBuildResultBuildFlowAndStreamEvents} language="json" />

    </details>

2. After receiving a job ID from the build endpoint, use the `/build/$JOB_ID/events` endpoint to stream the execution results:

    <Tabs>
    <TabItem value="Python" label="Python" default>

    <CodeSnippet source={examplePythonApiBuildBuildFlowAndStreamEvents2} language="python" />

    </TabItem>
    <TabItem value="JavaScript" label="JavaScript">

    <CodeSnippet source={exampleJavascriptApiBuildBuildFlowAndStreamEvents2} language="javascript" />

    </TabItem>
    <TabItem value="curl" label="curl">

    <CodeSnippet source={exampleApiBuildBuildFlowAndStreamEvents2} language="bash" />

    </TabItem>
    </Tabs>

    <details>
    <summary>Result</summary>

    <CodeSnippet source={resultApiBuildResultBuildFlowAndStreamEvents2} language="json" />

    </details>

The `/build/$FLOW_ID/events` endpoint has a `stream` query parameter that defaults to `true`.
To disable streaming and get all events at once, set `?stream=false`.

<Tabs>
<TabItem value="Python" label="Python" default>

<CodeSnippet source={examplePythonApiBuildBuildFlowAndStreamEvents3} language="python" />

</TabItem>
<TabItem value="JavaScript" label="JavaScript">

<CodeSnippet source={exampleJavascriptApiBuildBuildFlowAndStreamEvents3} language="javascript" />

</TabItem>
<TabItem value="curl" label="curl">

<CodeSnippet source={exampleApiBuildBuildFlowAndStreamEvents3} language="bash" />

</TabItem>
</Tabs>

## Build headers

| Header | Info | Example |
|--------|------|---------|
| Content-Type | Required. Specifies the JSON format. | "application/json" |
| accept | Optional. Specifies the response format. | "application/json" |
| x-api-key | Optional. Required only if authentication is enabled. | "sk-..." |

## Build parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| inputs | object | Optional. Input values for flow components. |
| data | object | Optional. Flow data to override stored configuration. |
| files | array[string] | Optional. List of file paths to use. |
| start_component_id | string | Optional. ID of the component where the execution should start. Component `id` values can be found in [Langflow JSON files](/concepts-flows-import#langflow-json-file-contents) |
| stop_component_id | string | Optional. ID of the component where the execution should stop. Component `id` values can be found in [Langflow JSON files](/concepts-flows-import#langflow-json-file-contents).|
| log_builds | Boolean | Whether to record build logs. Default: Enabled (`true`). |

### Set start and stop points

The `/build` endpoint accepts optional values for `start_component_id` and `stop_component_id` to control where the flow run starts and stops.
Setting `stop_component_id` for a component triggers the same behavior as clicking **Run component** on that component in the visual editor: The specified component and all dependent components leading up to that component will run.

The following example stops flow execution at an **OpenAI** component:

<Tabs>
<TabItem value="Python" label="Python" default>

<CodeSnippet source={examplePythonApiBuildSetStartAndStopPoints} language="python" />

</TabItem>
<TabItem value="JavaScript" label="JavaScript">

<CodeSnippet source={exampleJavascriptApiBuildSetStartAndStopPoints} language="javascript" />

</TabItem>
<TabItem value="curl" label="curl">

<CodeSnippet source={exampleApiBuildSetStartAndStopPoints} language="bash" />

</TabItem>
</Tabs>

### Override flow parameters

The `/build` endpoint also accepts inputs for `data` directly, instead of using the values stored in the Langflow database.
This is useful for running flows without having to pass custom values through the visual editor.

<Tabs>
<TabItem value="Python" label="Python" default>

<CodeSnippet source={examplePythonApiBuildOverrideFlowParameters} language="python" />

</TabItem>
<TabItem value="JavaScript" label="JavaScript">

<CodeSnippet source={exampleJavascriptApiBuildOverrideFlowParameters} language="javascript" />

</TabItem>
<TabItem value="curl" label="curl">

<CodeSnippet source={exampleApiBuildOverrideFlowParameters} language="bash" />

</TabItem>
</Tabs>

<details>
<summary>Result</summary>

<CodeSnippet source={resultApiBuildResultOverrideFlowParameters} language="json" />

</details>

## See also

- [Get Vertex builds](/api-monitor#get-vertex-builds)
- [Delete Vertex builds](/api-monitor#delete-vertex-builds)
- [Session ID](/session-id)

### AGENTS.md

# AGENTS.md

This file provides guidance to AI coding agents when working with code in this repository.

## Project Overview

Langflow is a visual workflow builder for AI-powered agents. It has a Python/FastAPI backend, React/TypeScript frontend, and a lightweight executor CLI (lfx).

## Prerequisites

- **Python:** 3.10-3.14
- **uv:** >=0.4 (Python package manager)
- **Node.js:** >=20.19.0 (v22.12 LTS recommended)
- **npm:** v10.9+
- **make:** For build coordination

## Common Commands

### Development Setup
```bash
make init              # Install all dependencies + pre-commit hooks
make run_cli           # Build and run Langflow (http://localhost:7860)
make run_clic          # Clean build and run (use when frontend issues occur)
```

### Development Mode (Hot Reload)
```bash
make backend           # FastAPI on port 7860 (terminal 1)
make frontend          # Vite dev server on port 3000 (terminal 2)
```

For component development, enable dynamic loading:
```bash
LFX_DEV=1 make backend                    # Load all components dynamically
LFX_DEV=mistral,openai make backend       # Load only specific modules
```

### Code Quality
```bash
make format_backend    # Format Python (ruff) - run FIRST before lint
make format_frontend   # Format TypeScript (biome)
make format            # Both
make lint              # mypy type checking
```

### Testing
```bash
make unit_tests                    # Backend unit tests (pytest, parallel)
make unit_tests async=false        # Sequential tests
uv run pytest path/to/test.py      # Single test file
uv run pytest path/to/test.py::test_name  # Single test

make test_frontend                 # Jest unit tests
make tests_frontend                # Playwright e2e tests
```

### Database Migrations
```bash
make alembic-revision message="Description"  # Create migration
make alembic-upgrade                         # Apply migrations
make alembic-downgrade                       # Rollback one version
```

## Architecture

### Monorepo Structure
```
src/
├── backend/
│   ├── base/langflow/     # Core backend package (langflow-base)
│   │   ├── api/           # FastAPI routes (v1/, v2/)
│   │   ├── components/    # Built-in Langflow components
│   │   ├── services/      # Service layer (auth, database, cache, etc.)
│   │   ├── graph/         # Flow graph execution engine
│   │   └── custom/        # Custom component framework
│   └── tests/             # Backend tests
├── frontend/              # React/TypeScript UI
│   └── src/
│       ├── components/    # UI components
│       ├── stores/        # Zustand state management
│       └── icons/         # Component icons
└── lfx/                   # Lightweight executor CLI
```

### Key Packages
- **langflow**: Main package with all integrations
- **langflow-base**: Core framework (api, services, graph engine)
- **lfx**: Standalone CLI for running flows (`lfx serve`, `lfx run`)

### Service Layer
Backend services in `src/backend/base/langflow/services/`:
- `auth/` - Authentication
- `authorization/` - Authorization (RBAC) plugin layer — see below
- `database/` - SQLAlchemy models and migrations
- `cache/` - Caching layer
- `storage/` - File storage
- `tracing/` - Observability integrations

### Authorization (RBAC)

Authorization is a pluggable layer separate from authentication:

- **OSS** ships the interface (`BaseAuthorizationService` in `lfx`) + a pass-through implementation (`LangflowAuthorizationService`) + the `authz_*` and `casbin_rule` DB schema + route guards.
- Implementations register via the `lfx.services` entry point `authorization_service` in `lfx.toml` (same pattern as the SSO `auth_service`). A registered plugin reads the `authz_*` admin tables and writes compiled rules to `casbin_rule`.

Default is **off**: `LANGFLOW_AUTHZ_ENABLED=false`. When enabled with only the OSS stub registered, every check returns allow — the stub is a no-op so routes stay wired and audit rows still flow. Real allow/deny requires a registered authorization plugin.

Route guards live in `langflow.services.authorization.guards` (the legacy `langflow.services.authorization.utils` path re-exports them for backward compatibility):
- `ensure_flow_permission(user, FlowAction.*, flow_id=..., flow_user_id=..., workspace_id=..., folder_id=...)` — single-flow CRUD + execute
- `ensure_deployment_permission(user, DeploymentAction.*, deployment_id=..., deployment_user_id=..., workspace_id=..., project_id=...)`
- `ensure_project_permission(user, ProjectAction.*, project_id=..., project_user_id=..., workspace_id=...)`
- `ensure_knowledge_base_permission(user, KnowledgeBaseAction.*, kb_name=..., kb_user_id=...)`
- `ensure_variable_permission(user, VariableAction.*, variable_id=..., variable_user_id=...)`
- `ensure_file_permission(user, FileAction.*, file_id=..., file_user_id=...)`
- `ensure_share_permission(user, ShareAction.*, share_id=..., share_user_id=...)`
- `filter_visible_resources(user, resource_type=..., candidates=..., act=...)` — list-endpoint filter; safe no-op in OSS

The enforcement request shape is `(subject, domain, object, action)`:
- subject = `user:{uuid}`
- domain = `project:{uuid}` → `workspace:{uuid}` → `*` (resolved by `_resolve_flow_domain`; the more specific domain wins so project-scoped grants match directly while workspace-scoped grants still flow down via plugin-side role inheritance)
- object = `flow:{uuid}` / `deployment:{uuid}` / `project:{uuid}` / `flow:*` / etc.
- action = `read` / `write` / `create` / `delete` / `execute` / `deploy`

**Share-aware fetch (Phase 3):** route fetch helpers (`_read_flow`, `get_flow_by_id_or_endpoint_name`, `get_deployment`, project reads in `projects.py`, v2 file fetcher, variable PATCH/DELETE in `variable.py`) branch on `BaseAuthorizationService.supports_cross_user_fetch()`. The OSS pass-through reports `False` so the existing owner-scoped queries are preserved — enabling `LANGFLOW_AUTHZ_ENABLED=true` without a registered plugin cannot widen visibility. Plugins set `SUPPORTS_CROSS_USER_FETCH=True` so resources load by id alone and `ensure_*_permission` decides access; route handlers can convert a plugin-deny `HTTPException(403)` to `HTTPException(404)` via `langflow.services.authorization.fetch.deny_to_404` to preserve UUID privacy.

**Share CRUD API (Phase 3):** `/api/v1/authz/shares` provides POST / GET / PATCH / DELETE on `authz_share` rows. The handler enforces an OSS floor (resource owner or superuser may administer shares for that resource) so the OSS pass-through cannot let a non-owner mint share rows. Each write fires `BaseAuthorizationService.invalidate_user` / `invalidate_all` so a registered enforcer can drop cached policy. Audit rows are written via `audit_decision` with `share:create` / `share:update` / `share:delete` actions.

**Audit query API (Phase 4):** `GET /api/v1/authz/audit` (superuser-only) exposes a paginated, filterable view of `authz_audit_log`. Supports `user_id`, `resource_type`, `resource_id`, `action`, `result`, `since`, `until` filters; page size capped at 200.

**Default role catalog (Phase 4):** the consolidated foundations migration `7c8d9e0f1a2b_authz_foundations` seeds the three built-in `is_system=True` roles (viewer / developer / admin) with `"{resource}:{action}"` permission slugs. OSS does not interpret these — they exist so a registered plugin's policy sync has a stable bootstrap source.

## Component Development

Components live in `src/backend/base/langflow/components/`. To add a new component:

1. Create component class inheriting from `Component`
2. Define `display_name`, `description`, `icon`, `inputs`, `outputs`
3. Add to `__init__.py` (alphabetical order)
4. Run with `LFX_DEV=1 make backend` for hot reload

**IMPORTANT:** Changing a component's class name is a breaking change and should never be done. The class name serves as an identifier used to match components in saved flows and to flag them for updates in the UI. Renaming it will break existing flows that use that component.

### Component Structure
```python
from langflow.custom import Component
from langflow.io import MessageTextInput, Output

class MyComponent(Component):
    display_name = "My Component"
    description = "What it does"
    icon = "component-icon"  # Lucide icon name or custom

    inputs = [
        MessageTextInput(name="input_value", display_name="Input"),
    ]
    outputs = [
        Output(display_name="Output", name="output", method="process"),
    ]

    def process(self) -> Message:
        # Component logic
        return Message(text=self.input_value)
```

### Component Testing
Tests go in `src/backend/tests/unit/components/`. Use base classes:
- `ComponentTestBaseWithClient` - Components needing API access
- `ComponentTestBaseWithoutClient` - Pure logic components

Required fixtures: `component_class`, `default_kwargs`, `file_names_mapping`

## Frontend Development

- **React 19** + TypeScript + Vite
- **Zustand** for state management
- **@xyflow/react** for graph visualization
- **Tailwind CSS** for styling

### Custom Icons
1. Create SVG component in `src/frontend/src/icons/YourIcon/`
2. Export with `forwardRef` and `isDark` prop support
3. Add to `lazyIconImports.ts`
4. Set `icon = "YourIcon"` in Python component

## Testing Notes

- `@pytest.mark.api_key_required` - Tests requiring external API keys
- `@pytest.mark.no_blockbuster` - Skip blockbuster plugin
- Database tests may fail in batch but pass individually
- Pre-commit hooks require `uv run git commit`
- Always use `uv run` when running Python commands
- When running tests inside a sub-package (e.g. `langflow-base`, `lfx`), sync that package's dev group first: `uv sync --group dev --package langflow-base`. The default `uv sync` only resolves the top-level workspace and may leave dev-only test deps (e.g. `fakeredis`) uninstalled.

### Graph Testing Pattern

Proper Graph tests follow this pattern:
1. Build graph with connected components
2. Connect them via `.set()` calls
3. Call `async_start` and iterate over the results
4. Validate the results

### Testing Best Practices

- Avoid mocking in tests when possible
- Prefer real integrations for more reliable tests

## Version Management
```bash
make patch v=1.5.0  # Update version across all packages
```

This updates: `pyproject.toml`, `src/backend/base/pyproject.toml`, `src/frontend/package.json`

## Pre-commit Workflow

Pre-commit hooks run ruff and biome automatically on `git commit`, so manual
formatting is not required. To avoid an extra commit cycle when you have many
changes:

1. Run `make format_backend` once before staging - fixes most ruff issues up front.
2. Run `uv run git commit` (the `uv run` ensures pre-commit finds the right Python).
3. If you touched backend code, run `make unit_tests` locally for faster feedback than CI.

## Pull Request Guidelines

- Follow [semantic commit conventions](https://www.conventionalcommits.org/)
- Reference any issues fixed (e.g., `Fixes #1234`)
- Ensure all tests pass before submitting

## Documentation

Documentation uses Docusaurus and lives in `docs/`:
```bash
cd docs
yarn install
yarn start        # Dev server on port 3000 (prompts for 3001 if 3000 is in use)
```

### CLAUDE.md

# CLAUDE.md

@AGENTS.md
@.claude/CLAUDE.md

This project uses [AGENTS.md](https://agents.md/) as the standard for providing context to AI coding agents. The `@AGENTS.md` import above tells Claude Code to load `AGENTS.md` automatically; other tools that natively support `AGENTS.md` will pick it up directly. The `@.claude/CLAUDE.md` import loads the local hard-rules file (gitignored) that mirrors the PostToolUse hook policy.

### DEVELOPMENT.md

# Setting up a Development Environment

This document details how to set up a local development environment that will allow you to contribute changes to the project!

## Base Requirements

- The project is hosted on GitHub, so you need an account there (and if you are reading this, you likely do!)
- An IDE such as Microsoft VS Code IDE https://code.visualstudio.com/

## Set up Git Repository Fork

You will push changes to a fork of the Langflow repository, and from there create a Pull Request into the project repository.

Fork the [Langflow GitHub repository](https://github.com/langflow-ai/langflow/fork), and follow the instructions to create a new fork.

On your new fork, click the "<> Code" button to get a URL to [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) using your preferred method, and clone the repository; for example using `https`:

```bash
git clone https://github.com/<your username>/langflow.git
```

Finally, add the Project repository as `upstream`:

```bash
cd langflow
git remote add upstream https://github.com/langflow-ai/langflow.git
git remote set-url --push upstream no_push
```

> [!TIP] > **Windows/WSL Users**: You may find that files "change", specifically the file mode e.g. "changed file mode 100755 → 100644". You can workaround this problem with `git config core.filemode false`.

## Set up Environment

There are two options available to you: use your local environment with `make` commands (recommended for macOS and Linux), or use a Development Container ("[Dev Container](https://containers.dev/)") which is recommended for Windows users.

### Option 1 (Recommended): Use Your Local Environment

Install Pre-Requisites:

- **Operating System**: macOS or Linux; Windows users should use WSL or consider Option 2 (Dev Container).
- **`git`**: The project uses the ubiquitous `git` tool for change control.
- **`make`**: The project uses `make` to coordinate packaging.
- **`uv`**: This project uses `uv` (`>=0.4`), a Python package and project manager from Astral. Install instructions at https://docs.astral.sh/uv/getting-started/installation/.
- **`npm`**: The frontend files are built with Node.js (`v22.12 LTS`) and `npm` (`v10.9`). Install instructions at https://nodejs.org/en/download/package-manager.
  - Windows (WSL) users: ensure `npm` is installed within WSL environment; `which npm` should resolve to a Linux location, not a Windows location.

### Option 2: Use a Dev Container (Recommended for Windows)

Open this repository as a Dev Container per your IDEs instructions.

A preconfigured `.devcontainer` is included in this repository and is auto-detected by supported IDEs.

#### Microsoft VS Code

To start the preconfigured `.devcontainer` with the VS Code Dev Containers extension, from the Command Palette, run the Dev Containers: Reopen in Container command.

- See [Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers)
- You may also find it helpful to [share `git` credentials](https://code.visualstudio.com/remote/advancedcontainers/sharing-git-credentials) with the container

### Initial Environment Validation

To setup and validate the initial environment, run:

```bash
make init
```

This sets up the development environment by installing backend and frontend dependencies and installing pre-commit hooks. It runs `make install_backend`, `make install_frontend`, and `uvx pre-commit install`.

> [!TIP]
> If you want to quickly run Langflow from source without setting up the full development environment, you can use `make run_cli` instead. This command installs dependencies, builds the frontend, and starts the application in one step.

After running `make init`, you have two options for running Langflow:

- Use `make run_cli` to build and run the application immediately.
- Continue to the next section to run Langflow in Development mode.

### Troubleshooting frontend build issues

If you encounter frontend build problems or are upgrading from an older version of Langflow, run `make run_clic` once.

```bash
make run_clic
```

This command cleans the build cache and rebuilds everything from scratch, which resolves most frontend-related issues when switching between versions.

## Complete development environment setup

There are some other steps to consider before you are ready to begin development.

### Optional pre-commit hooks

Pre-commit hooks will help keep your changes clean and well-formatted.

> [!NOTE]
> With these installed, the `git commit` command needs to run within the Python environment; your syntax needs to change to `uv run git commit`.

Install pre-commit hooks by running the following commands:

```bash
uv sync
uv run pre-commit install
```

## Run Langflow in Development mode

With the above validation, you can now run the backend (FastAPI) and frontend (Node) services in a way that will "hot-reload" your changes. In this mode, the FastAPI server requires a Node.js server to serve the frontend pages rather than serving them directly.

> [!NOTE]
> You will likely have multiple terminal sessions active in the normal development workflow. These will be annotated as _Backend Terminal_, _Frontend Terminal_, _Documentation Terminal_, and _Build Terminal_.

### Debug Mode

A debug configuration is provided for VS Code users: this can be launched from the Debug tab (the backend debug mode can be launched directly via the F5 key). You may prefer to start services in this mode. You may still want to read the following subsections to understand expected console output and service readiness.

### Start the Backend Service

The backend service runs as a FastAPI service on Python, and is responsible for servicing API requests. In the _Backend Terminal_, start the backend service:

```bash
make backend
```

> [!TIP]
> **Component Development Mode**: By default, Langflow uses a prebuilt component index for fast startup (~10ms). If you're actively developing or modifying components, enable dynamic component loading with `LFX_DEV`:
>
> ```bash
> # Load all components dynamically
> LFX_DEV=1 make backend
>
> # Load only specific component modules (faster dev workflow)
> LFX_DEV=mistral,openai,anthropic make backend
> ```
>
> The list mode is particularly useful when working on specific integrations, as it significantly speeds up startup time by only loading the components you need.
>
> Without `LFX_DEV`, component changes require rebuilding the index:
>
> ```bash
> uv run python scripts/build_component_index.py
> ```

You will get output similar to:

```
INFO:     Will watch for changes in these directories: ['/home/phil/git/langflow']
INFO:     Loading environment from '.env'
INFO:     Uvicorn running on http://0.0.0.0:7860 (Press CTRL+C to quit)
INFO:     Started reloader process [22330] using WatchFiles
Starting Langflow ...
```

At which point you can check http://localhost:7860/health in a browser; when the backend service is ready it will return a document like:

```json
{ "status": "ok" }
```

### Start the Frontend Service

The frontend (User Interface) is, in shipped code (i.e. via `langflow run`), statically-compiled files that the backend FastAPI service provides to clients via port `7860`. In development mode, these are served by a Node.js service on port `3000`. In the _Frontend Terminal_, start the frontend service:

```bash
make frontend
```

You will get output similar to:

```
  VITE v5.4.11  ready in 552 ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help
```

At this point, you can navigate to http://localhost:3000/ in a browser and access the Langflow User Interface.

### Build and display documentation

> [!IMPORTANT]
> If you're using a dev container, run the documentation build from outside the container in your host terminal, not from within the dev container workspace. The documentation build may not work properly when run inside the dev container.

If you are contributing changes to documentation (always welcome!), these are built using [Docusaurus](https://docusaurus.io/) and served separately, also using Node.js.

In the terminal, from the project root directory, run the following:

```bash
cd docs
npm install
npm run start
```

If the frontend service is running on port `3000` you might be prompted `Would you like to run the app on another port instead?`, in which case answer "yes". You will get output similar to:

```
[SUCCESS] Docusaurus website is running at: http://localhost:3001/
```

Navigate to http://localhost:3001/ in a browser and view the documentation. Documentation updates will be visible as they are saved, though sometimes the browser page will also need to be refreshed.

## Adding or Modifying a Component

Components reside in folders under `src/backend/base/langflow`, and their unit tests under `src/backend/base/tests/unit/components`.

> [!IMPORTANT]
> **Component Development Mode**: When actively developing components, make sure to run the backend with `LFX_DEV=1` to enable live reloading:
>
> ```bash
> LFX_DEV=1 make backend
> ```
>
> This ensures your component changes are immediately reflected without needing to rebuild the component index.

### Adding a Component

Add the component to the appropriate subdirectory, and add the component to the `__init__.py` file (alphabetical ordering on the `import` and the `__all__` list). Assuming the backend and frontend services are running **with `LFX_DEV=1`**, the backend service will restart as these files are changed. The new component will be visible after the backend is restarted, _*and*_ after you hit "refresh" in the browser.

> [!TIP]
> It is faster to copy-paste the component code from your editor into the UI _without_ saving in the source code in the editor, and once you are satisfied it is working you can save (restarting the backend) and refresh the browser to confirm it is present.

You should try to add a unit test for your component, though templates and best practices for this is a work in progress. At the very least, please create a Markdown file in the unit test subdirectory associated with your component (create the directory if not present), with the same filename as the component but with a `.md` extension. Within this should be the steps you have taken to manually test the component.

### Modifying a Component

Modifying a component is much the same as adding a component: it is generally easier to make changes in the UI and then save the file in the repository. Please be sure to review and modify unit tests; if there is not a unit test for the component, the addition of one that at least covers your changes would be much appreciated!

> [!NOTE]
> If you have an old version of the component on the canvas when changes are saved and the backend service restarts, that component should show "Updates Available" when the canvas is reloaded (i.e. a browser refresh). [Issue 5179](https://github.com/langflow-ai/langflow/issues/5179) indicates this behavior is not consistent, at least in a development setting.

### Component Index

When you're done modifying components and ready to commit, the component index will be automatically updated by CI when you create a pull request. The GitHub Actions workflow will detect changes to components and rebuild the index, committing it to your PR branch if needed.

If you want to manually rebuild the index locally for testing:

```bash
uv run python scripts/build_component_index.py
```

## Building and Testing Changes

When you are ready to commit, and before you commit, you should consider the following:

- `make lint`
- `make format_backend` and `make format_frontend` will run code formatters on their respective codebases
- `make unit_tests` runs the (backend) unit tests (see "Quirks" below for more about testing).

Once these changes are ready, it is helpful to rebase your changes on top of `upstream`'s `main` branch, to ensure you have the latest code version! Of course if you have had to merge changes into your component you may want to re-lint/format/unit_test.

As a final validation, stop the backend and frontend services and run `make init`; this will do a clean build and the UI should be available in port `7860` (as it has invoked `langflow run`). Open a **new** browser tab to this service and do a final check of your changes by adding your new/modified component onto the canvas from the Components list.

## Committing, Pushing, and Pull Requests

Once you are happy your changes are complete, commit them and push the changes to your own fork (this will be `origin` if you followed the above instructions). You can then raise a Pull Request into the Project repository on the GitHub interface or within your IDE.

> [!TIP]
> Remember that if you have pre-commit hooks enabled, you need to run the `git` command as `uv run git` to activate the necessary Python environment!

## Some Quirks!

You may observe some quirky things:

### Testing

- Backend test `src/backend/tests/unit/test_database.py` can fail when running with `make tests` but passes when running manually
  - You can validate this by running the test cases sequentially: `uv run pytest src/backend/tests/unit/test_database.py`
- There are some other test targets: `integration_tests`, `coverage`, `tests_frontend` but these require additional setup not covered in this document.

### Files That Change

There are some files that change without you having made changes:

- Files in `src/backend/base/langflow/initial_setup/starter_projects` modify after `langflow run`; these are formatting changes. Feel free to commit (or ignore) them.
- `uv.lock` and `src/frontend/package-lock.json` files can be modified by `make` targets; changes should not be committed by individual contributors.
  - You can exclude these from consideration in git: `git update-index --assume-unchanged uv.lock src/frontend/package-lock.json`
  - You can re-include these from consideration in git: `git update-index --no-assume-unchanged uv.lock src/frontend/package-lock.json`

### BUNDLE_API.md

# Bundle API

Stable surface that Langflow Extension Bundles consume.  Every public symbol
listed below is part of the contract: changes to its name, signature, semantics,
or visibility require a coordinated version bump and a `## Changelog` entry.

This document is paired with the integer **`BUNDLE_API_VERSION`** declared in
[`lfx.extension.manifest`](src/lfx/src/lfx/extension/manifest.py).  Manifests
declare the contract versions they support via `lfx.compat: ["1"]`; a bundle
that does not list `str(BUNDLE_API_VERSION)` is rejected at install time with
`version-constraint-unsatisfied`.

> **CI gate:** any PR that modifies a file containing an in-scope surface MUST
> add a `## Changelog` entry describing the change.  The CI guard
> [`scripts/migrate/check_bundle_api_changelog.py`](scripts/migrate/check_bundle_api_changelog.py)
> enforces this.  Pure-internal refactors that preserve every public symbol's
> name and signature do not require a changelog entry, but reviewers should be
> skeptical.

---

## Surface (v0)

### Component base class

| Symbol | Source |
| --- | --- |
| `Component` | `lfx.custom.custom_component.component.Component` |
| `Component.build()` (declared on subclasses) | call site of every loaded bundle module |
| `Component.inputs` | declarative input list |
| `Component.outputs` | declarative output list |
| `Component.display_name` / `Component.description` / `Component.icon` / `Component.documentation` | metadata read by the palette |
| `Component.name` | optional override of the registry class name |

### Inputs

| Symbol | Source |
| --- | --- |
| `Input` (base) | `lfx.io` |
| `MessageTextInput` / `MultilineInput` / `SecretStrInput` | `lfx.io` |
| `IntInput` / `FloatInput` / `BoolInput` | `lfx.io` |
| `DropdownInput` / `TabInput` | `lfx.io` |
| `DictInput` / `NestedDictInput` | `lfx.io` |
| `FileInput` / `LinkInput` | `lfx.io` |
| `HandleInput` | `lfx.io` |

### Outputs

| Symbol | Source |
| --- | --- |
| `Output` | `lfx.io` |

### Schema types

| Symbol | Source |
| --- | --- |
| `Data` | `lfx.schema.data` |
| `DataFrame` | `lfx.schema.dataframe` |
| `Message` | `lfx.schema.message` |

### Manifest contract (consumed by the loader)

| Symbol | Source |
| --- | --- |
| Manifest schema (`extension.json` / `[tool.langflow.extension]`) | `lfx.extension.manifest.ExtensionManifest` |
| `BundleRef` (one entry in `bundles[]`) | `lfx.extension.manifest.BundleRef` |
| `LfxCompat` (declared as `manifest.lfx`) | `lfx.extension.manifest.LfxCompat` |
| `BUNDLE_API_VERSION` (the integer this lfx ships) | `lfx.extension.manifest` |
| `EXTENSION_SCHEMA_URL` / `SCHEMA_VERSION` | `lfx.extension.manifest` |

Slot vocabulary: `official` (installed pip distributions and seed
directories) and `extra` (paths declared in `LANGFLOW_COMPONENTS_PATH`).
Component IDs at runtime are `ext:<bundle>:<Class>@<slot>`.

### Discovery + loading entry points

| Symbol | Source |
| --- | --- |
| `load_extension(root)` | `lfx.extension.loader` |
| `load_installed_extensions()` | `lfx.extension.loader` |
| `discover_inline_bundles()` | `lfx.extension.loader` |
| `discover_installed_extensions()` / `discover_seed_extensions()` / `discover_all_extensions()` | `lfx.extension.discovery` |
| `LoadedComponent` | `lfx.extension.loader` (frozen dataclass; what the registry stores) |
| `LoadResult` | `lfx.extension.loader` |
| `SLOT_OFFICIAL` / `SLOT_EXTRA` | `lfx.extension.loader` |

### Reload pipeline

| Symbol | Source |
| --- | --- |
| `reload_bundle(registry, bundle_name)` | `lfx.extension.reload` |
| `BundleRegistry` | `lfx.extension.bundle_registry` |
| `BundleRecord` | `lfx.extension.bundle_registry` |
| `ReloadInProgressError` | `lfx.extension.bundle_registry` |
| `POST /api/v1/extensions/{id}/bundles/{name}/reload` | `langflow.api.v1.extensions` |

### Errors

| Symbol | Source |
| --- | --- |
| `ExtensionError` | `lfx.extension.errors` |
| `ExtensionErrorCollection` | `lfx.extension.errors` |
| `format_extension_error(error)` | `lfx.extension.errors` |
| `ERROR_CODES` (frozenset of every typed code) | `lfx.extension.errors` |

The full kebab-case discriminant set is the contract — adding a code is
backward-compatible; removing or renaming a code is a breaking change and
requires a `BUNDLE_API_VERSION` bump.

### Validate / authoring CLI

| Symbol | Source |
| --- | --- |
| `validate_extension(root, *, execute_imports=False)` | `lfx.extension.validate` |
| `ValidateReport` | `lfx.extension.validate` |
| `lfx extension validate` (CLI) | `lfx.cli._extension_commands` |
| `lfx extension schema` (CLI) | `lfx.cli._extension_commands` |
| `lfx extension init` (CLI) | `lfx.cli._extension_commands` |
| `lfx extension dev` (CLI -- registers a local path and execs `langflow run`) | `lfx.cli._extension_commands` |
| `lfx extension list` (CLI) | `lfx.cli._extension_commands` |
| `lfx extension reload` (CLI) | `lfx.cli._extension_commands` |
| `register_dev_extension` / `unregister_dev_extension` (Python API) | `lfx.extension.dev_registry` |

### Migration

| Symbol | Source |
| --- | --- |
| Migration-table file | `src/lfx/src/lfx/extension/migration/migration_table.json` |
| `MigrationEntry` | `lfx.extension.migration.schema` |
| `MigrationTable` | `lfx.extension.migration.schema` |
| `migrate_flow_payload(payload, table)` | `lfx.extension.migration.rewrite` |
| `MIGRATION_SCHEMA_VERSION` | `lfx.extension.migration.schema` |

---

## Out of scope (v0)

These are reserved in the manifest schema and produce a typed
`field-deferred-in-this-milestone` error if set; they are NOT part of the
v0 contract:

- `services` — bundle-declared service factories
- `routes` — bundle-mounted HTTP routes
- `hooks` — bundle-declared lifecycle hooks
- `starter_projects` — bundle-shipped starter flows
- `userConfig` — bundle-declared user-config schema
- Multi-bundle manifests (`bundles` list with length > 1)

---

## Pilot bundle: `lfx-duckduckgo`

The shipped LE-1023 pilot is **`duckduckgo`**, extracted into the
standalone distribution
[`lfx-duckduckgo`](src/bundles/duckduckgo/) under `src/bundles/duckduckgo/`
with its own `pyproject.toml`.  `langflow`'s own `pyproject.toml`
declares `lfx-duckduckgo>=0.1.0` as a regular dependency so a flat
`pip install langflow` continues to ship the bundle as before.

Why this bundle:

- Single component (`DuckDuckGoSearchComponent`) in a single file
  (`duck_duck_go_search_run.py`).
- Zero git churn over the last six months.
- Modern `Component` base class (no `LCToolComponent` legacy).
- No authentication required — failure mode is a single failed request, not a
  paid-API outage.
- Class name is globally unique across `src/lfx/src/lfx/components/**`, so the
  bare-name migration entry is allowed by `check_bare_names.py`.

The runtime half of the M1 proof-of-delivery gate (save a flow on
pre-migration Langflow, upgrade, confirm it loads AND runs identically)
lives in the dogfood checklist at
[`src/bundles/duckduckgo/M1_DOGFOOD_CHECKLIST.md`](src/bundles/duckduckgo/M1_DOGFOOD_CHECKLIST.md);
the deserialize half is covered by
`src/lfx/tests/integration/extension/test_pilot_duckduckgo_upgrade.py`.

---

## Changelog

### v0 (this release)

- Initial surface enumerated above.  Frozen as `BUNDLE_API_VERSION = 1`.
- `BundleRegistry.write_locked()` exposed as a public context manager so the
  reload pipeline can hold the registry write lock across both the
  `sys.modules` swap and the `BundleRecord` install.  Concurrent readers
  can no longer observe new modules paired with the old record.  No change
  to the addressable component contract.
- HTTP reload endpoint (`POST /api/v1/extensions/{id}/bundles/{name}/reload`)
  returns `422 Unprocessable Entity` for structural failures (broken
  bundle, missing source path, name mismatch) instead of `200 OK` with
  `ok=false`.  Body is `{...primaryError, result: ReloadResult}` so the
  full typed result is preserved under the FastAPI `detail` envelope.
  `409 Conflict` for `reload-in-progress` is unchanged.
- CLI table updated to remove the obsolete `dev register` / `dev unregister`
  / `dev list` subcommands; the actual surface is `extension dev <path>`
  plus the Python helpers `register_dev_extension` / `unregister_dev_extension`.
- `MigrationTable.ambiguous_bare_names` added.  Each entry is
  `{name, candidates: [list of canonical IDs]}` and registers a bare
  class name that exists in 2+ bundles.  The deserializer now surfaces
  `component-name-ambiguous` (with the candidate targets) for any bare
  name listed here, instead of falling through to the generic
  `component-not-found-with-hint`.  Seeded with the canonical regression
  cases (`MergeDataComponent`, `SplitTextComponent`, `SubFlowComponent`).
  `check_bare_names.py` now verifies every Component class found in
  2+ bundle folders has a matching marker, so a future bundle move that
  introduces a new ambiguity is caught at PR time.
- Router-trust CI guard broadened to scan every `.py` under
  `src/backend/base/langflow/api/**` and `src/lfx/src/lfx/**`; a new file
  that mounts an `APIRouter(prefix=".../extensions...")` is auto-detected
  and checked for forbidden install/uninstall/registry-mutation handlers.
  Authors of files with non-literal prefixes can opt in via a
  `# router-trust: in-scope` marker.
- Router-trust guard rewritten to use AST-based cross-file resolution.
  A forbidden handler in module A is now caught when module B mounts A's
  router via `parent.include_router(child, prefix=".../extensions...")`,
  and the same applies transitively across multi-hop include_router
  chains.  An imported router that cannot be statically resolved is
  ignored (the guard never flags routes it cannot prove reachable from
  `/extensions`); routes co-located with an in-scope router ARE flagged.
- `check_migration_append_only.py` now compares
  `ambiguous_bare_names` alongside `entries`.  A marker may not be
  removed once published, and its `candidates` list may only grow --
  shrinking it would silently regress flows from
  `component-name-ambiguous` to `component-not-found-with-hint`.
- Router-trust guard now resolves dotted attribute references in
  `include_router` and decorators.  ``include_router(child.api.router,
  prefix="/extensions")`` after ``import child.api`` (and the
  ``import child.api as alias; alias.router`` shape) are caught -- not
  just ``from child.api import router as child_router``.  The parser
  flattens any ``Name``/``Attribute`` chain, and the resolver walks
  imports of either kind (``from M import N`` and ``import M``,
  with or without an asname) back to the source file.
- Router-trust guard's relative-import resolver is now
  ``__init__.py``-aware.  Inside a package, ``from .child import Y``
  anchors at the package itself (level=1 -> ``pkg``); inside a regular
  module ``pkg.foo`` it anchors at the parent package (level=1 ->
  ``pkg``).  The arithmetic differs because ``__init__.py``'s file
  module IS the package, while ``pkg/foo.py``'s file module is
  ``pkg.foo``.  The resolver tracks ``is_package`` and decrements
  ``level`` by one for ``__init__.py`` files so both shapes resolve
  correctly.
- Code-review hardening pass across the extension subsystem.  No public
  symbol's name or signature changed; this entry covers behavioural
  tightening that bundle authors and operators should be aware of:
  - **Path-safety contract honored on every discovery path.**
    ``DiscoveredExtension`` records emitted from
    ``discover_installed_extensions`` / ``discover_seed_extensions``
    now run the same resolve-and-``relative_to`` containment check that
    ``validate_extension`` performs.  A symlinked ``bundles[0].path``
    or a symlinked seed subdirectory that escapes the extension root
    is now rejected with ``path-escape`` *before* reaching the loader,
    instead of slipping through to ``exec_module()``.  The shared
    primitive lives at ``lfx.extension._paths.is_within``; every
    walker (loader, validator, seed discovery, inline-bundle discovery)
    uses the same function and the same ``SKIP_DIR_NAMES``.
  - **``--execute-imports`` env allowlist.** The validator's
    ``--execute-imports`` subprocess now inherits an explicit allowlist
    (``PATH``, ``LANG``, ``LC_*``, ``SYSTEMROOT``, ``TMPDIR``, ``TZ``,
    Python locale + encoding vars) instead of denylisting only
    ``LANGFLOW_*``/``LFX_*``.  Cloud / CI credentials
    (``AWS_*``, ``OPENAI_API_KEY``, ``GITHUB_TOKEN``, ...) no longer
    propagate into untrusted bundle import.  The CLI / module docs
    re-frame this pass as best-effort hygiene lint, not a sandbox.
  - **AST hygiene lint widened.** ``_find_top_level_io`` now flags
    ``exec``, ``eval``, ``__import__``, ``compile`` as top-level
    primitives and ``importlib.import_module`` /
    ``importlib.__import__`` as dotted-name primitives.  Still
    best-effort literal-name matching; trivially bypassable by
    obfuscation, and documented as such.
  - **Reload swap is non-destructive.** ``_swap_sys_modules`` now
    builds the staging->prod rename map **before** any ``sys.modules``
    mutation, snapshots popped old modules into a recovery map, and
    restores them on any mid-swap exception.  The length-mismatch
    tripwire on ``zip(strict=True)`` no longer leaves the prod
    namespace shredded.  A new typed code,
    ``reload-class-retag-failed``, is appended to
    ``ReloadResult.warnings`` when ``cls.__module__`` cannot be
    retagged so the empty-palette-after-reload regression leaves a
    trail instead of silently failing.
  - **Cross-source bundle-name collision.**
    ``load_installed_extensions`` now detects two distributions with
    different canonical names but identical ``bundle.name`` (which
    would silently clobber each other at
    ``_lfx_ext.official.<name>.*``) and emits a typed
    ``duplicate-bundle-name`` error on the loser, dropping its
    components.  ``BundleRegistry.install_bundle`` additionally logs a
    WARNING when an existing record is replaced by a record from a
    different ``source_path`` (catches collisions the upstream
    precedence resolver missed).
  - **Reload endpoint off event loop.**
    ``POST /api/v1/extensions/{id}/bundles/{name}/reload`` now invokes
    ``reload_bundle`` via ``asyncio.to_thread`` so slow or large
    bundle imports do not freeze the worker for other in-flight
    requests.  The wire contract (status codes, body shape) is
    unchanged.
  - **Stable typed-error code rename.**
    ``multi-bundle-deferred-in-this-milestone`` is renamed to the
    stable ``multi-bundle-unsupported``.  The old code is retained in
    ``ERROR_CODES`` as a deprecated alias for one milestone for log
    scrapers.  Three new codes are added to
    ``ERROR_CODES``: ``duplicate-bundle-name`` (see above),
    ``reload-class-retag-failed`` (see above), and
    ``reload-transport-error`` (CLI-side connectivity failure,
    previously misreported as ``reload-source-missing``).
  - **Discovery preserves "unreadable" vs "absent" distinction.**
    ``_pyproject_declares_extension`` now propagates ``OSError`` so a
    permission failure on a pyproject that *might* declare an
    extension surfaces as ``manifest-unreadable`` instead of being
    silently dropped as "no extension here".
  - **Dev registry corruption is logged.** ``_read_state`` now
    distinguishes file absent (silent, legitimate empty registry),
    file present but unreadable (WARNING), and file present but
    corrupt JSON / wrong shape (WARNING with detail).  The state
    file is written with mode 0600 so a hostile third-party process
    cannot inject an extension path into the developer's next
    ``langflow run``.
  - **Entry-point predicate avoids module-level side effects.**
    ``_entry_point_loads_to_component`` now consults
    ``importlib.util.find_spec`` first and only falls through to
    ``ep.load()`` when the spec lookup is insufficient.  The
    ``except BaseException`` was narrowed to ``except Exception`` so
    ``SystemExit`` / ``KeyboardInterrupt`` are no longer swallowed at
    filter time.
  - **Frontend reload-success warnings surfaced.**  The reload route's
    ``ReloadResult.warnings`` (non-empty on success) now reach the
    user via a notice toast in addition to the green success toast.
    Wire shape unchanged; this is a UI fix that consumes existing
    payload fields.
  - **Internal-only file split.** ``sys.modules`` surgery primitives
    moved to ``lfx.extension.reload_swap``; ``load_installed_extensions``
    / ``load_seed_extensions`` moved to
    ``lfx.extension.loader._startup``.  Both are re-exported from
    their previous import paths so external imports are unchanged.
  - **Editable installs are discovered via the entry-point fallback.**
    ``_distribution_manifest_path`` now falls back to the
    ``langflow.extensions`` entry-point group when ``dist.files`` only
    surfaces ``dist-info/`` entries (the ``pip install -e`` /
    ``uv pip install -e`` case).  The entry-point value is resolved
    via ``importlib.util.find_spec`` -- which runs import-system
    finders but never executes the module body -- and the resulting
    package directory is scanned for ``extension.json`` or a
    ``[tool.langflow.extension]`` pyproject.  Wheel installs are
    unaffected: the fallback only fires when the primary ``dist.files``
    scan finds no manifest.  Previously, editable-installed bundles
    were silently dropped by ``lfx extension list`` and the registry,
    even though the bundle pyproject already declared the
    entry-point.
  - **Reload CLI: ``--bundle`` is optional; ``--all`` is implemented.**
    ``lfx extension reload <ext_id>`` now resolves the bundle name
    from local ``discover_all_extensions`` when ``--bundle`` is
    omitted; explicit ``--bundle`` still wins for cases where the
    local install is not visible to the running server.
    ``lfx extension reload --all`` iterates every locally-discovered
    bundle, POSTs reload to each, and exits non-zero if any reload
    fails (previously hard-errored as "not yet wired").  ``--all`` is
    mutually exclusive with a positional id / ``--bundle`` (exit 2).
    The HTTP wire contract (``POST /api/v1/extensions/{id}/bundles/
    {name}/reload`` per-bundle) is unchanged; this is a CLI-only
    surface change.
- **User-scoped extension events.**  Bundle lifecycle events
  (``bundle_reloaded``, ``bundle_reload_failed``, ``flow_migrated``,
  ``extension_error``) now publish to a per-user keyspace
  (``user:<user_id>``) instead of the shared ``"global"`` bucket so
  flow-migration and reload payloads cannot leak across users via the
  poll endpoint.
  - ``reload_bundle`` gains an optional keyword-only ``user_id: str |
    None = None`` argument.  When supplied, ``bundle_reloaded`` /
    ``bundle_reload_failed`` events are emitted to keyspace
    ``user:<user_id>``; ``None`` (CLI / authless dev) keeps the legacy
    ``"global"`` emission.  Existing positional callers are unaffected.
  - ``POST /api/v1/extensions/{id}/bundles/{name}/reload`` now resolves
    the authenticated user and threads its id into ``reload_bundle``, so
    every reload triggered via HTTP is published to that user's
    keyspace.  Wire contract (status codes, body shape) unchanged.
  - ``GET /api/v1/extensions/events`` drops its client-supplied
    ``keyspace`` query parameter.  The endpoint derives the keyspace
    from the authenticated user server-side, so an authenticated client
    can no longer poll another user's keyspace.  Frontends that polled
    without ``keyspace`` (the in-tree consumer) are unaffected;
    third-party callers that explicitly passed ``keyspace=...`` will
    now receive ``422`` from FastAPI's strict parameter validation.
- **Reload event payload aligned with ``ReloadResult``.**  Both
  ``bundle_reloaded`` and ``bundle_reload_failed`` events now carry the
  full ``ReloadResult.to_dict()`` envelope (``ok``, ``bundle``,
  ``reload_id``, ``components_added``, ``components_removed``,
  ``components_changed``, ``warnings``, ``errors``) instead of a
  hand-rolled subset.  Polling clients can now (a) detect body-only
  edits via ``components_changed`` instead of mis-reporting them as
  "no source changes detected", and (b) surface a failed reload's
  ``errors[0].message`` instead of degrading to a generic
  "check server logs" fallback.  HTTP response shape unchanged.
- **``GET /api/v1/extensions/events`` rejects ``keyspace`` explicitly.**
  Previously the endpoint accepted but silently ignored any
  client-supplied ``keyspace`` query parameter (server-derived from the
  authenticated user since the prior entry).  Silent drop masked client
  bugs that assumed the value had effect.  The route now returns ``422
  Unprocessable Entity`` with a typed
  ``extension-events-keyspace-forbidden`` error envelope when the
  parameter is present.  ``extension-events-keyspace-forbidden`` is
  added to ``ERROR_CODES`` (additive; codes-as-contract semantics
  preserved).  In-tree polling clients that never sent the parameter
  are unaffected.

## Top-level structure
- `.agents` (dir)
- `.cursor` (dir) — tooling/automation config
- `.devcontainer` (dir) — tooling/automation config
- `.github` (dir) — tooling/automation config
- `.vscode` (dir) — tooling/automation config
- `deploy` (dir) — deployment manifests and scripts
- `docker` (dir) — container build and local run assets
- `docker_example` (dir) — container build and local run assets
- `docs` (dir) — Docusaurus docs site and API/reference docs
- `regressions` (dir) — regression assets and checks
- `scripts` (dir) — developer and release scripts
- `src` (dir) — application source (backend, frontend, graph/runtime, components)
- `test-results` (dir)
- `.coderabbit.yaml` (file)
- `.composio.lock` (file)
- `.dockerignore` (file)
- `.env.example` (file)
- `.eslintrc.json` (file)
- `.gitattributes` (file)
- `.gitignore` (file)
- `.pre-commit-config.yaml` (file)
- `.secrets.baseline` (file)
- `.whitesource` (file)
- `AGENTS-example.md` (file)
- `AGENTS.md` (file) — agent instruction file
- `BUNDLE_API.md` (file) — project documentation
- `ci-skip-analysis.md` (file)
- `CLAUDE.md` (file) — agent instruction file
- `CODE_OF_CONDUCT.md` (file)
- `codecov.yml` (file)
- `CONTRIBUTING.md` (file) — project documentation
- `DESIGN.md` (file)
- `DEVELOPMENT.md` (file) — project documentation
- `LICENSE` (file)
- `Makefile` (file)
- `Makefile.frontend` (file)
- `package-lock.json` (file)
- `package.json` (file) — backend/frontend dependency and tooling manifest
- `pyproject.toml` (file) — backend/frontend dependency and tooling manifest
- `README.md` (file) — project documentation
- `RELEASE.md` (file)
- `render.yaml` (file)
- `SECURITY.md` (file) — project documentation
- `uv.lock` (file)
