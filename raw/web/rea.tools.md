# rea.tools

## Fetch log
- Inbox URL: https://rea.tools/
- Final URL: https://rea.tools/
- Fetched: 2026-10-15
- Pages: 11
- Mode: standard
- Notes: no llms.txt (404); no /docs — sitemap.xml used as the docs catalog. Sitemap lists the English site plus 18 locale mirrors (ar, de, el, es, fa, fr, id, it, ja, ko, pl, pt-BR, ru, th, tr, uk, vi, zh-CN, zh-TW) of the same pages. Pages captured via Jina Reader (r.jina.ai) as verbatim markdown.

## Sitemap (English pages) — https://rea.tools/sitemap.xml
- https://rea.tools/
- https://rea.tools/blog/
- https://rea.tools/blog/reverse-engineering-models/
- https://rea.tools/blog/touhou-reconstruction/
- https://rea.tools/contributors/
- https://rea.tools/examples/dino-lab/
- https://rea.tools/faq/
- https://rea.tools/first-investigation/
- https://rea.tools/get-started/
- https://rea.tools/guides/
- https://rea.tools/guides/browser/
- https://rea.tools/guides/javascript/
- https://rea.tools/guides/native/
- https://rea.tools/showcase/
- https://rea.tools/showcase/aegis/
- https://rea.tools/showcase/ctf/
- https://rea.tools/showcase/dx-ball/
- https://rea.tools/showcase/notion/
- https://rea.tools/showcase/th04/

## Landing page — https://rea.tools/

Reverse engineering, with your coding agent

## Find out how  
software works.

Ask your coding agent about an app, a game or a website. REA gives it the tools to inspect the code behind the answer.

[Showcases →](https://rea.tools/showcase/) — investigations and interactive demos.

[Blog →](https://rea.tools/blog/) — methods and reconstruction notes.

## Set up REA

Copy this into your coding agent:

Install REA and connect it to this coding agent using npx rea-agents@latest setup. Show me the setup plan for approval, then verify the installation.

## How it works

Reverse engineering means learning how software works by inspecting the program itself. With REA, your agent can follow the code, explain a feature and help you rebuild it.

1.   ### Ask about one feature

Give your agent a program or page and a question.

2.   ### Inspect the program

REA returns code, references and runtime observations.

3.   ### Explain it, then try a change

Your agent uses the findings to explain or rebuild the feature.

See the full Calculator investigation
Why does Calculator give 220 for 200 + 10%?

### Follow the instructions step by step

```
0x180124945: MOV EAX, dword ptr [R13 + 0x18]
0x180124949: CMP EAX, 0x5c
0x18012494c: JZ 0x180124aba
0x180124952: CMP EAX, 0x5b
0x180124955: JZ 0x180124aba
0x18012495b: MOV EDX, 0x64
0x180124960: LEA RCX, [RSP + 0x160]
0x180124968: CALL 0x180122650
0x18012496e: LEA RDX, [R13 + 0x160]
0x180124975: LEA RCX, [RSP + 0x78]
0x18012497a: CALL 0x180109720
0x18012497f: MOV RSI, RAX
0x180124982: MOV qword ptr [RSP + 0x28], RAX
0x180124987: LEA RDX, [RSP + 0x160]
0x18012498f: MOV RCX, RAX
0x180124992: CALL 0x180123190
; … value-copy instructions omitted …
0x180124a14: MOV RDX, RDI
0x180124a17: LEA RCX, [RSP + 0xf8]
0x180124a1f: CALL 0x180109720
0x180124a24: LEA R8, [RSP + 0x30]
0x180124a29: MOV RDX, RAX
0x180124a2c: LEA RCX, [RSP + 0xb8]
0x180124a34: CALL 0x180123c10
```

**You decode the instructions, follow the calls and reconstruct the calculation.**

Ask your agent the same question

Use REA to inspect Windows Calculator. Why does 200 + 10% give 220?

Example answer · based on the findings

After +, the % button takes **a percentage of the first number.**

`10% of 200 = 20`**200 + 20 = 220**

REA supplies The handler’s instructions, decompiled code and calls.

Your agent explains Which branch applies, what it calculates and how to rebuild it.

 Selected assembly from the installed Calculator DLL. The thoughts and reply illustrate the findings. [Continue with the Calculator example ↓](https://rea.tools/#calculator)

Let’s try two examples: change a game’s speed, then rebuild Calculator’s % button.

Example 01 · Chrome’s dinosaur game

## Why does the dinosaur get faster?

The game gets faster as you run. To rebuild it with a speed control, we first need to find out how the speed changes.

### 1. Ask about the speed

Use REA to inspect this dinosaur game. Why does it get faster? Show the speed rule, then build a small version with an adjustable speed.

### 2. Find the speed rule

REA lets the agent read the game’s running code. The speed starts at 6 and increases a little each update while it is below 13.

### 3. Play the result

We rebuilt that rule in the mini-game below and added a speed slider. Press Play, then choose your own speed.

Speed 6.0  Use the recovered acceleration rule

Press Play, then jump over the cactus.

 Move the slider to set your own speed. Space or Jump clears a cactus. 

[Open the speed lab →](https://rea.tools/examples/dino-lab/)

 See the script, checks and how to try the analysis 
Inspected target: [wayou’s Chromium-derived browser edition](https://wayou.github.io/t-rex-runner/).

```
if (this.currentSpeed < this.config.MAX_SPEED) {
  this.currentSpeed += this.config.ACCELERATION;
}
```

Start at 6. Add 0.001 each update without a collision, while speed is below 13.

What each part does

1.   01 · REA Read the running game’s script Return its actual code and settings to the agent.
2.   02 · Your agent Rebuild the rule, add a control Use the recovered acceleration in a small game with a speed slider.
3.   03 · You Change the speed and play Try the original acceleration, then choose your own pace.

REA inspected the HTTP browser edition through a local debugging connection and returned the loaded `index.js`, including its source and digest.

```
ACCELERATION: 0.001,
MAX_SPEED: 13,
SPEED: 6
```

We called the original game’s update function in a controlled browser check, with obstacles and automatic scheduling disabled. After 4,000 updates, speed was 10.0; after 10,000, it was 13.0, rounded to one decimal.

The new mini-game keeps that speed rule. Its drawing, jumping and collision code are a small teaching implementation. [Open the lab](https://rea.tools/examples/dino-lab/) to see the new code and run the same speed check.

To inspect the target yourself, follow the [browser connection steps](https://rea.tools/guides/browser/#prepare) using [the dinosaur page](https://wayou.github.io/t-rex-runner/). Give your agent that page URL and your local debugging endpoint, then copy the prompt above.

[Inspected speed code](https://github.com/wayou/t-rex-runner/blob/5455bfa408ec6b707c7300ff194b7390733a766d/index.js#L565-L571) · [Chromium Authors · BSD license](https://rea.tools/assets/licenses/dinosaur.txt)

Example 02 · Windows Calculator

## Rebuild Calculator’s % button.

The % button does different things after + and ×. Let’s find both rules and try them in a small calculator.

### 1. Ask about the % button

Use REA to inspect Windows Calculator’s % button. Recover the rules after + and ×, then build a small calculator that uses both.

### 2. Find both rules

REA helps the agent read the code behind the % button. It applies two different rules:

With +Take 10% of the first number.`10% of 200 = 20 → 200 + 20 = 220`

With ×Turn 10% into 0.1.`200 × 0.1 = 20`

### 3. Try the % button

We recreated both rules below. Choose + or ×, press %, then press =.

200 +**10**

Press % to see what happens to 10.

 Interactive illustration of the inspected percentage rule. 

See the real code and how the answer was checked
For this example, `previous = 200` and `current = 10`.

```
if (operation == multiply || operation == divide) {
  percent = current / 100;
} else {
  percent = current * previous / 100;
}
```

From the installed app to a working % button

1.   01 · REA reads calc.exe It launches the Calculator app The code opens `ms-calculator:`. The agent then selects the installed app’s library.
2.   02 · REA reads the library Return the % handler’s code The function checks the operator and uses the constant `100`.
3.   03 · Your agent interprets it Explain and reproduce the rules Crosscheck the branch with Microsoft’s source, then try + and × above.

```
0x180124945: MOV EAX, dword ptr [R13 + 0x18]
0x180124949: CMP EAX, 0x5c
0x18012494c: JZ 0x180124aba
0x180124952: CMP EAX, 0x5b
0x180124955: JZ 0x180124aba
0x18012495b: MOV EDX, 0x64
```

```
#define IDC_MUL 92      // 0x5c
#define IDC_DIV 91      // 0x5b
#define IDC_PERCENT 118 // 0x76

0x64 = 100
```

Inspected with REA 4.1.0: Windows Calculator 11.2508.4.0, x64. The readable summary uses names from Microsoft’s public source to explain the recovered branch.

[Percentage implementation](https://github.com/microsoft/calculator/blob/d125246a4e19842ce1332e6c7839cf0e110027d8/src/CalcManager/CEngine/scifunc.cpp#L98-L111) · [Microsoft’s test cases](https://github.com/microsoft/calculator/blob/d125246a4e19842ce1332e6c7839cf0e110027d8/src/CalculatorUnitTests/CalculatorManagerTest.cpp#L350-L370) · [Native setup guide](https://rea.tools/guides/native/)

## REA case studies.

Explore a feature in a released app or game, with code and checked results.

[Showcases →](https://rea.tools/showcase/)

Android · APK analysis

### How an authenticator generates a login code

Trace Aegis's six-digit login code through its released APK, then move a demo clock to see why it changes every 30 seconds.

[Read the Android case study](https://rea.tools/showcase/aegis/)
Electron · Feature tracing

### How Notion copies text and HTML

Follow Notion's packaged JavaScript to the system clipboard and see how a copy preserves rich block data.

[Read the Notion case study](https://rea.tools/showcase/notion/)
Native · Reconstruction

### DX-Ball's sound-pan calculation

Recover how a ball's position becomes left/right sound in a 1996 Windows game.

[Read the DX-Ball case study](https://rea.tools/showcase/dx-ball/)

Your first investigation

## Try REA on a small app.

Download our Notes example, trace its CSV export, and check one changed input.

[Try the guided example](https://rea.tools/first-investigation/)

## Choose your target.

These guides cover setup and a first investigation for each kind of software.

### Native binaries

Inspect functions, strings, references and call relationships in executables and libraries.

[Native analysis guide](https://rea.tools/guides/native/)

### JavaScript & Electron

Map modules, routes, IPC and native dependencies from an application folder or ASAR archive.

[Application workflows](https://rea.tools/guides/javascript/)

### Browser & runtime activity

Capture selected browser or process activity, then compare the results across runs.

[Browser observation guide](https://rea.tools/guides/browser/)

Try a larger project

Use REA to inspect https://rea.tools/. Clone this website for me.

Yes, this one.

Use REA to reconstruct this game from its executable. Recover the gameplay logic in C and test it against the original.

[See the DX-Ball case study →](https://rea.tools/showcase/dx-ball/)

## Get started — https://rea.tools/get-started/

## 1. Prepare your computer

Use the computer where your target files are stored. A local coding agent can read those files and run tools for you.

How do I open a terminal?
*   **Windows:** open the Start menu, type _PowerShell_ and press Enter. 
*   **macOS:** press ⌘Space, type _Terminal_ and press Enter. 
*   **Linux:** press Ctrl Alt T on most desktops. 

Paste a command with Ctrl V (macOS: ⌘V; Linux terminals: Ctrl Shift V), then press Enter.

Commands go in the terminal. Prompts labeled “Your coding agent” go in the agent's chat.

You'll need Node.js 22 (22.19+), 24 (24.11+) or 26+. npm comes with Node.js.

 Don't have Node.js, or not sure? 
Open a terminal and check:

```
node -v
npm -v
```

If `node -v` prints v22.19+, v24.11+ or v26+, you're ready. If it prints an older version or "not recognized" / "command not found", install Node.js 24 LTS:

Windows (PowerShell)

`winget install --exact --id OpenJS.NodeJS.LTS`

Type Y if asked to accept the terms. Close PowerShell, open it again, then run `node -v`.

[Download the Node.js installer](https://nodejs.org/en/download) if winget is unavailable.

If PowerShell later says _"running scripts is disabled on this system"_ when you run `npx`, use `npx.cmd` instead. For npm, use `npm.cmd`:

`npx.cmd rea-agents@latest setup`

macOS
For a first installation, download the [Node.js 24 LTS macOS installer (.pkg)](https://nodejs.org/en/download), open it and follow the installer. Then reopen Terminal.

Already use Homebrew?

`brew install node`

Linux
Install curl and unzip first if they are missing. On Debian or Ubuntu, run `sudo apt install curl unzip`; on other distributions, use your package manager.

`curl -fsSL https://fnm.vercel.app/install | bash`

Close the terminal, open it again, then:

```
fnm install 24
fnm use 24
fnm default 24
```

Your distribution's own `nodejs` package is often older than 22.19, so check `node -v` if you use it instead.

Prefer a regular installer? Download the LTS version from [nodejs.org](https://nodejs.org/en/download).

Make a working folder for your agent
In your terminal, make a folder for the exercise, then move into it:

```
mkdir rea-work
cd rea-work
```

Keep this terminal open for the next step. If you already have a working folder, open it instead.

## 2. Choose a coding agent

Your agent is the AI you talk to. REA supplies the inspection tools it uses. Pick one client below; open its instructions if you haven't used it before.

Codex · use your ChatGPT account
Install Codex using the command for your operating system:

`powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"`

`curl -fsSL https://chatgpt.com/codex/install.sh | sh`

After installation, reopen your terminal and return to the working folder. Then start Codex:

`codex`

Choose “Sign in with ChatGPT”, complete the browser sign-in, then return to the terminal. When the message box appears, continue to step 3.

[Codex installation and sign-in](https://learn.chatgpt.com/docs/codex/cli)

Cursor, Windsurf or VS Code · use an editor
1.    Install the editor for your operating system and sign in. 
2.   Open the rea-work folder you made in step 1.
3.    Open its AI chat and choose Agent mode. In Windsurf or Devin Desktop, open the agent chat; in VS Code, set up GitHub Copilot first. 

[Cursor setup](https://cursor.com/docs) · [Windsurf / Devin Desktop setup](https://docs.windsurf.com/windsurf/getting-started) · [VS Code and Copilot setup](https://code.visualstudio.com/docs/setup/copilot)

Claude Code · use your Claude account
Install using the command for your operating system:

`irm https://claude.ai/install.ps1 | iex`

`curl -fsSL https://claude.ai/install.sh | bash`

Reopen your terminal, return to your working folder and run `claude`. Follow the sign-in prompts. Access uses an eligible Claude subscription or a configured API account.

[Claude Code installation and account options](https://code.claude.com/docs/en/setup)

Claude Desktop · use a desktop chat
Install Claude Desktop on Windows or macOS and sign in. Quit it completely, then run this command in a terminal you opened outside Claude:

`npx rea-agents@latest setup --client claude_desktop`

Review and approve the plan, reopen Claude, then [check the connection in step 3](https://rea.tools/get-started#check-connection).

[Download Claude Desktop](https://claude.ai/download) · [Claude Desktop connection details](https://github.com/morluto/rea/blob/main/docs/client-configuration.md#claude-desktop)

OpenCode · choose an AI model

`npm install --global opencode-ai`

Run `opencode` in your working folder. Use `/connect` in its chat to connect your model account, then select a model.

[OpenCode installation and model setup](https://opencode.ai/docs/)

All supported clients and setup IDs
The npm 6.4.0 release supports the clients below. Use the ID with `--client` when choosing a client explicitly.

| Client | Setup ID |
| --- | --- |
| Claude Code | `claude_code` |
| Claude Desktop | `claude_desktop` |
| Codex | `codex` |
| Cursor | `cursor` |
| Gemini CLI | `gemini_cli` |
| Windsurf | `windsurf` |
| Devin | `devin` |
| OpenCode | `opencode` |
| Antigravity | `antigravity` |
| GitHub Copilot CLI | `copilot_cli` |
| Command Code | `commandcode` |
| Qwen Code | `qwen_code` |
| VS Code | `vscode` |
| Grok Build | `grok_build` |
| OMP | `omp` |
| Pi | `pi` |
| Hermes | `hermes` |

Qoder (`qoder`), Factory Droid (`droid`), Trae (`trae`), ZCode (`zcode`) and DeepSeek Harness (`dsh`) are available on repository main; use a source build or a release containing those integrations.

[Client configuration and troubleshooting](https://github.com/morluto/rea/blob/main/docs/client-configuration.md) · [Release availability](https://github.com/morluto/rea/blob/main/docs/installation.md#released-package-and-main)

Grok Bot · connect on its hosted computer
In Grok Bot's chat, ask it to add a custom MCP server named `rea` using this command on the Bot's computer:

`npx -y rea-agents@6.4.0 mcp`

[Grok Bot connector instructions](https://github.com/morluto/rea/blob/main/docs/client-configuration.md#other-client-settings)

## 3. Connect REA

Copy this into your coding agent:

Install REA and connect it to this coding agent using npx rea-agents@latest setup. Show me the setup plan for approval, then verify the installation.

Or run setup yourself

`npx rea-agents@latest setup`

For one specific client, add its setup ID:

`npx rea-agents@latest setup --client codex`

If npm asks to download the package, type `y` and press Enter. In REA's client list, use the arrow keys to move, Space to select your client and Enter to continue.

Choose your client and review the setup plan. REA adds its MCP connection and the matching investigation skill, keeping a backup of existing configuration. It asks before applying the changes.

MCP is the connection that lets your agent call REA. The skill gives it a workflow for investigating software.

For the first exercise, you can skip the optional Hopper installation. Restart your client when setup finishes.

How do I restart my client?
**Desktop apps** (Claude Desktop, Cursor, Windsurf, VS Code): quit the app completely, then open it again. Closing the window isn't enough. On macOS press ⌘Q; on Windows, also quit from the tray icon if there is one.

**Terminal agents** (Claude Code, Codex, Gemini CLI): exit the session and start it again.

`npx -y rea-agents@latest doctor --client codex --json`

Replace `codex` with your client's setup ID. A successful check reports `"healthy": true`. Then ask your agent:

> Check that REA is connected and show me which REA tools you can use.

## 4. Try your first investigation

The example is a six-file Electron app with an **Export notes** button. Your agent can inspect its code without installing or launching Electron.

Download https://rea.tools/examples/notes-example.zip into a new example folder and unpack it. Use REA to find what happens when I click Export notes. Show where notes.csv is written, which fields it contains, and the relevant files and lines.

Look for a short explanation with file and line references:

> The button sends a `notes:export` message. The main process formats the notes as CSV and writes `notes.csv` in the user’s Downloads folder. The columns are `id` and `title`.

[Check a prediction in the guided exercise →](https://rea.tools/first-investigation/#check)

 Download the example yourself, or use your own app 
[Download example ZIP](https://rea.tools/examples/notes-example.zip)

If your agent can’t download files, unzip this archive yourself. Give it the path to the `notes-example` folder and the same export question.

> Use REA to inspect the app at `/absolute/path/to/app`. Find how it exports data and show the relevant files and lines.

How do I get a folder's full path?
*   **Windows:** in File Explorer, right-click the folder and choose _Copy as path_. On Windows 10, hold Shift while right-clicking. 
*   **macOS:** in Finder, right-click the folder, hold Option and choose _Copy "…" as Pathname_. 
*   **Any system:** drag the folder into a terminal window and its path appears. 

In a terminal, put quotes around a path that contains spaces.

## Analyze another kind of software

Choose the section for your target. A provider is the local analysis tool REA uses for that kind of software.

 Native executables and libraries · Hopper, Ghidra or IDA 
Install one analysis tool on the computer running REA. The host is your operating system; the target is the program you want to inspect.

| Provider | Windows | macOS | Linux |
| --- | --- | --- | --- |
| Hopper | Unavailable | 12+ | Supported distributions |
| Ghidra | x64 · experimental | x64 / arm64 | x64 / arm64 |
| IDA | Verified profiles | Verified headless profile | See provider guide |

Hopper · let setup install or connect it
Connect Hopper on macOS or Linux. Run the setup command above; it detects an existing installation or offers an installation plan for your approval.

Choose Hopper in setup and review its separate installation plan. On macOS, choose demo mode or activate your license when Hopper first opens. On Linux, setup prepares the supported demo and its private display.

Linux hosts: Ubuntu 24.04+, Fedora 41+, Nobara 44+, Arch Linux, CachyOS or Omarchy. Hopper is commercial software; its demo has vendor-defined limits.

`npx -y rea-agents@latest doctor --provider hopper --json`

If macOS asks for Automation permission, allow the app that starts REA in System Settings → Privacy & Security → Automation, then retry.

[Hopper setup and troubleshooting](https://github.com/morluto/rea/blob/main/docs/installation.md#hopper)

 Ghidra · install the free analysis tool and Java 
1.    Install a 64-bit JDK 21 or newer, including the Java compiler. Choose the package matching your computer's architecture. 
2.    Download Ghidra 12.1.4 from the release's Assets list and extract the `ghidra_…_PUBLIC_….zip` archive. Choose the release archive, not “Source code”. 
3.    Find the extracted folder containing `ghidraRun` or `ghidraRun.bat`. Use that folder for `GHIDRA_INSTALL_DIR`. 

[Download a JDK](https://adoptium.net/temurin/releases/?version=21) · [Download Ghidra 12.1.4](https://github.com/NationalSecurityAgency/ghidra/releases/tag/Ghidra_12.1.4_build)

Check Java. The first command prints `java.home`; use that folder for `JAVA_HOME`. The second confirms the compiler is installed:

```
java -XshowSettings:properties -version
javac -version
```

Connect Ghidra on Windows
Windows x64 has experimental, read-only support for native x86 and x64 PE applications and DLLs on fixed local NTFS drives. Use an existing Ghidra 12.1.x installation and a 64-bit JDK 21 or newer:

```
$env:GHIDRA_INSTALL_DIR = "C:/tools/ghidra_12.1.4_PUBLIC"
$env:JAVA_HOME = "C:/tools/jdk-21"
npx -y rea-agents@latest doctor --provider ghidra --json
npx rea-agents@latest setup
```

Replace the two paths with your installations, then review setup's plan.

Connect your Ghidra installation

```
export GHIDRA_INSTALL_DIR="/absolute/path/to/ghidra_12.1.4_PUBLIC"
export JAVA_HOME="/absolute/path/to/jdk-21"
```

Replace both paths with your existing installations. For a fresh macOS or Linux arm64 installation, build the native decompiler for your computer before continuing.

Build Ghidra's native decompiler
On macOS, the build needs Xcode Command Line Tools, make and bison. Use the guide for your computer:

*   [macOS · Intel](https://github.com/morluto/rea/blob/main/docs/installation.md#missing-macos-native-decompiler)
*   [macOS · Apple Silicon](https://github.com/morluto/rea/blob/main/docs/installation.md#macos-arm64-native-decompiler)
*   [Linux arm64 · native build instructions](https://github.com/NationalSecurityAgency/ghidra/blob/Ghidra_12.1.4_build/GhidraDocs/GettingStarted.md#building-native-components)

Then check Ghidra and save its paths for your client:

```
npx -y rea-agents@latest doctor --provider ghidra --json
npx rea-agents@latest setup
```

Keep these commands in the same terminal session. Rerun setup after setting the paths, approve the updated client configuration, then restart your agent.

[Ghidra setup and architecture requirements](https://github.com/morluto/rea/blob/main/docs/installation.md#ghidra) · [Windows Ghidra guide](https://github.com/morluto/rea/blob/main/docs/windows-ghidra-p0.md)

IDA · connect an existing installation
Use the IDA provider guide to prepare an upstream MCP registration. Choose an attached GUI with the original binary open, or a headless supervisor that opens a private database.

Verified profiles include the Windows legacy GUI and headless supervisor, plus a macOS arm64 headless supervisor with IDA Professional 9.1. The optional native GUI bridge has its own version and platform requirements.

The macOS headless profile and native GUI bridge require a [REA source build](https://github.com/morluto/rea/blob/main/CONTRIBUTING.md#development-setup) or a release containing those changes. npm `6.4.0` does not include them.

From the built checkout, run `node scripts/rea.mjs doctor --provider ida --json` and `node scripts/rea.mjs setup` instead of the `npx` commands below.

Prepare the IDA registration file
Install and configure the upstream server using the IDA guide below. Then save its working registration as `ida-mcp.json` in a text editor. On Windows, choose “All files” when saving in Notepad so it doesn't add `.txt`.

For a headless supervisor providing `idb_open`, `idb_list` and `idb_close`, the file can look like this:

```
{
  "command": "idalib-mcp",
  "args": ["--stdio", "--max-workers", "1"],
  "mode": "headless"
}
```

For an attached legacy 1.4.0 GUI server, copy its working `command`, `args` and optional `env` into the file. Open the original binary in IDA and start its upstream plugin before asking REA to inspect it.

```
$env:REA_IDA_MCP_CONFIG = "C:/analysis/ida-mcp.json"
$env:REA_ANALYSIS_PROVIDER = "ida"
npx -y rea-agents@latest doctor --provider ida --json
npx rea-agents@latest setup
```

```
export REA_IDA_MCP_CONFIG="/absolute/path/to/ida-mcp.json"
export REA_ANALYSIS_PROVIDER="ida"
npx -y rea-agents@latest doctor --provider ida --json
npx rea-agents@latest setup
```

Use the JSON registration file you prepared with the provider guide, then rerun setup and restart your agent.

[IDA profiles, registration examples and verified platforms](https://github.com/morluto/rea/blob/main/docs/ida-provider.md)

Once connected, give your agent the original executable's full path and name your provider:

> Use REA with my configured provider to inspect `/absolute/path/to/program`. List its functions and strings, then explain the part that handles user input with references to the code.

[Follow a native analysis example](https://rea.tools/guides/native/)

 Websites, Android, .NET, firmware and other targets 
Open the guide for the target you have. Each guide gives the additional tools, supported hosts and first command.

| Target | Tools to prepare | Guide |
| --- | --- | --- |
| JavaScript / Electron | Node.js + npm | [Open guide](https://rea.tools/guides/javascript/) |
| Website | Chrome / Chromium / Edge | [Open guide](https://rea.tools/guides/browser/) |
| .NET / Flutter / packages | Node.js + npm | [Open guide](https://github.com/morluto/rea/blob/main/docs/managed-code-analysis.md) |
| Android APK | JADX + JDK 17+ | [Open guide](https://github.com/morluto/rea/blob/main/docs/android-analysis.md) |
| Android device | adb | [Open guide](https://github.com/morluto/rea/blob/main/docs/adb-device-analysis.md) |
| Android resources | Apktool + Java | [Open guide](https://github.com/morluto/rea/blob/main/docs/apktool-resource-analysis.md) |
| JEB project | JEB + MCP | [Open guide](https://github.com/morluto/rea/blob/main/docs/jeb-analysis.md) |
| Firmware | Binwalk / Unblob · Linux | [Open guide](https://github.com/morluto/rea/blob/main/docs/firmware-analysis.md) |
| WASM | WABT | [Open guide](https://github.com/morluto/rea/blob/main/docs/wasm-artifacts.md) |
| SQLite database | Node.js 24.15+ / 26+ | [Open guide](https://github.com/morluto/rea/blob/main/docs/sqlite-databases.md) |
| EVM bytecode | Node.js · Linux x64 | [Open guide](https://github.com/morluto/rea/blob/main/docs/evm-bytecode.md) |
| ELF / Linux crash | pwntools / GDB / pwndbg | [Open guide](https://github.com/morluto/rea/blob/main/docs/recorded-crashes.md) |
| HAR / SAZ / mitmproxy | Node.js / mitmdump | [Open guide](https://github.com/morluto/rea/blob/main/docs/web-network-captures.md) |
| PCAP / PCAPNG | TShark / capinfos · Linux | [Open guide](https://github.com/morluto/rea/blob/main/docs/packet-captures.md) |
| Logic signals | sigrok-cli · Linux | [Open guide](https://github.com/morluto/rea/blob/main/docs/signal-recordings.md) |
| Process behavior | PTY · Linux / macOS | [Open guide](https://github.com/morluto/rea/blob/main/docs/process-capture.md) |

[Flutter guide](https://github.com/morluto/rea/blob/main/docs/flutter-analysis.md) · [Packages and resources](https://github.com/morluto/rea/blob/main/docs/javascript-artifact-reconstruction.md) · [EVM bytecode](https://github.com/morluto/rea/blob/main/docs/evm-bytecode.md) · [All investigation guides](https://rea.tools/guides/)

## Use REA from a terminal

CLI commands, global installation and curl
Analyze a JavaScript or Electron application folder or ASAR archive without running the app:

`npx -y rea-agents@latest analyze-javascript-application "/absolute/path/to/app" --json`

Replace the path with your extracted app directory or `.asar` file. On Windows, a path such as `"D:/apps/example"` works here.

Where do I find an app's .asar file?
Electron apps usually keep it in a `resources` folder:

*   **Windows:**`C:\Users\<you>\AppData\Local\Programs\<App>\resources\app.asar`
*   **macOS:**`/Applications/<App>.app/Contents/Resources/app.asar` (right-click the app and choose _Show Package Contents_) 
*   **Linux:** often `/opt/<App>/resources/app.asar`

Some apps install elsewhere. Search the app's folder for `app.asar`.

The result identifies the app, shows connections between modules and gives their source locations. Connections REA cannot resolve are marked in the result.

If you'd like a permanent `rea` command in your shell:

`npm install --global rea-agents`

[Continue with the JavaScript application guide](https://rea.tools/guides/javascript/)

`npx -y rea-agents@latest function "/absolute/path/to/program" main --provider ghidra --json`

Replace `main` with a function name or address from the target's function list. Ghidra must be configured first.

On macOS or Linux, you can also use the curl installer after preparing Node.js:

`curl -fsSL https://raw.githubusercontent.com/morluto/rea/main/install.sh | bash`

Follow the setup prompts to connect your agent. If they don't appear, run `rea setup`.

If your shell can't find `rea`, use the executable path printed by the installer. On Linux, the default setup command is `"$HOME/.local/bin/rea" setup`.

## Getting help

If your agent doesn't see REA
Restart or reconnect the client after setup. Check its REA connection with `doctor`; for Codex:

Use the client check in step 3 with your setup ID. In editor clients, enable REA in MCP settings and allow its tools in the agent chat.

If a provider needs attention
Check the provider you're using. For Ghidra:

`npx -y rea-agents@latest doctor --provider ghidra --json`

The report gives the failed check and a suggested next step.

Windows, WSL and paths with spaces
Use Windows PowerShell for Windows clients and analysis tools. If your agent runs inside WSL, install Node.js and REA inside that Linux environment and use Linux paths there. Headless providers run on the same host as REA.

In a terminal, put quotes around a path that contains spaces.

Windows setup command:

`npx.cmd rea-agents@latest setup`

Update or remove REA
To refresh your agent connection, run the latest setup command again, review its plan and restart your client.

`npx rea-agents@latest setup`

If you installed the global CLI, update it with `rea update`. Use `npx rea-agents@latest uninstall` to remove REA's client configuration and skill.

[Update and uninstall details](https://github.com/morluto/rea/blob/main/docs/installation.md#diagnose-update-and-remove)

*   [REA FAQ](https://rea.tools/faq/)Quick answers on updates, agents and analysis.
*   [Choose an investigation guide](https://rea.tools/guides/)Worked examples for a binary, an Electron app and a browser.
*   [GitHub issues](https://github.com/morluto/rea/issues)Report a problem with the command and diagnostics.
*   [REA community](https://discord.gg/GkcryMnJDM)Questions, investigations and work in progress.

## Your first investigation — https://rea.tools/first-investigation/

## 1. Connect your agent to REA

Use a coding agent such as Claude Code, Codex or Cursor. You’ll need Node.js and npm; the [setup guide lists supported versions](https://rea.tools/get-started/).

Install REA and connect it to this coding agent using npx rea-agents@latest setup. Show me the setup plan for approval, then verify the installation.

Or run this command in your terminal:

`npx rea-agents@latest setup`

Review the plan, approve the setup, then restart your agent. Already connected? Continue below.

## 2. Ask where the CSV is written

The example is a six-file Electron app with an **Export notes** button. Your agent can inspect its code without installing or launching Electron.

Download https://rea.tools/examples/notes-example.zip into a new example folder and unpack it. Use REA to find what happens when I click Export notes. Show where notes.csv is written, which fields it contains, and the relevant files and lines.

Your agent downloads the files and gives the unpacked folder to REA for inspection.

[Download example ZIP](https://rea.tools/examples/notes-example.zip)

If your agent can’t download files, unzip this archive yourself. Give it the path to the `notes-example` folder and the same export question.

## 3. Follow the answer back to the code

Look for a short explanation with file and line references:

> The button sends a `notes:export` message. The main process formats the notes as CSV and writes `notes.csv` in the user’s Downloads folder. The columns are `id` and `title`.

From the button to the file writer

1.   Page · renderer.js Export notes Calls `notes.exportCsv()`.
2.   Bridge · preload.js`notes:export`Sends a named message to the main process.
3.   Handler · main.js Write notes.csv Calls the formatter in `csv.js` and writes the file.

 REA’s static analysis pairs the message with its handler. The destination is read from code. 

```
ipcMain.handle("notes:export", () => {
  const destination = path.join(app.getPath("downloads"), "notes.csv");
  writeFileSync(destination, toCsv(notes), "utf8");
  return destination;
});
```

The file path, formatter and write call are together in this handler. Ask your agent to show these lines if its answer leaves them out.

[See the full code trace and recorded REA result](https://rea.tools/guides/javascript/#follow).

## 4. Check a prediction

A comma separates CSV columns. What happens when a note title itself contains a comma or quotation marks?

Predict the CSV for a note with id 1 and title Hello, "REA". Then run the example’s toCsv formatter with Node.js to check it. Show the prediction and actual output.

```
id,title
1,"Hello, ""REA"""
```

The title stays in one quoted field; each quotation mark is doubled. This checks the formatter directly with Node.js.

Run the check yourself
Open a terminal in the unpacked `notes-example` folder:

```
node <<'JS'
const { toCsv } = require('./csv.js');
process.stdout.write(toCsv([{ id: 1, title: 'Hello, "REA"' }]));
JS
```

```
@'
const { toCsv } = require('./csv.js');
process.stdout.write(toCsv([{ id: 1, title: 'Hello, "REA"' }]));
'@ | node
```

## 5. Ask another question

Try a follow-up in the same conversation:

> What happens if the file can’t be written? Follow the error back to the page.

Or give your agent an app of your own and ask about one button, file or behavior.

*   [How Notion copies text and HTML](https://rea.tools/showcase/notion/)Follow a clipboard feature in a packaged Electron app.
*   [How DX-Ball calculates sound panning](https://rea.tools/showcase/dx-ball/)Read the original instructions and the reconstruction’s checks.
*   [Troubleshoot setup or analysis](https://rea.tools/faq/#troubleshooting)Update REA and check the connection if you get stuck.

## Guides — https://rea.tools/guides/

[Home](https://rea.tools/) / Guides

Analyze a native function, an Electron export or a browser request. Each guide includes a prompt, code and results.

First investigation

Native binaries

## Recover a sound-pan calculation

Start with a Windows game executable. Inspect instructions, follow a caller, read numeric constants and check the recovered C.

Instructions Caller Constants C function

[Native analysis guide](https://rea.tools/native/)

JavaScript & Electron

## Follow a CSV export

A small Notes app spreads one feature across the renderer, preload and main process. Use REA to connect the API, IPC channel and file writer.

Button Preload API IPC CSV file

[JavaScript & Electron guide](https://rea.tools/javascript/)

For a larger packaged app, follow [Notion's clipboard bridge](https://rea.tools/showcase/notion/).

Browser behavior

## Observe a click

Open a working Notes example, capture an export request and find the code that turns its response into a download.

Your click Captured request Export script

[Browser observation guide](https://rea.tools/browser/)

## Native binary analysis guide — https://rea.tools/guides/native/

## Calculate left/right sound panning

In DX-Ball, a brick hit supplies a horizontal screen position. The sound code turns it into a left/right panning value.

The starting function, `0x00406400`, has a short decompiler result: a call to `__ftol()`. REA also returns its instructions and callers, which give the agent a way to investigate the missing arithmetic.

New to these terms?
*   **Instructions:** the steps the processor runs, shown in readable form such as `MOV` or `ADD`. 
*   **Decompiler result / pseudocode:** an analysis tool's attempt to turn instructions back into C-like code. It can miss parts, as in this example. 
*   **Caller:** a function that calls this one. It shows which values are passed in. 
*   **Address:** a location in the program, written in hexadecimal, such as `0x00406400`. 
*   **Constants:** fixed numbers stored in the program, read as raw bytes and decoded. 

Three pieces of evidence, one calculation

1.   01 · Instructions An integer input A stack read supplies the value used by the floating-point instructions.
2.   02 · Caller A screen coordinate The brick-hit caller passes `20 + 30 × tile_x`.
3.   03 · Data bytes The numeric constants Referenced bytes decode to `1.5625`, `500.0` and a scale value.

`pan = (x × 1.5625 − 500.0) × scale`

 REA supplies the instructions, call relationship and bytes. The agent interprets them together. 

## Ask about the behavior

After [connecting REA to your agent](https://rea.tools/get-started/#agent) and [setting up a native analysis tool](https://rea.tools/get-started/#native), provide the local executable and a question:

Which analysis tool should I use?
REA needs one of these to read native programs:

*   **Hopper** (macOS or Linux): REA's setup detects it or offers to install it. On macOS, open Hopper once and choose demo mode or activate a license before your first analysis. 
*   **Ghidra** (macOS or Linux; experimental on Windows): free, but needs an existing Ghidra 12.1.x installation and a 64-bit JDK 21 or newer. 
*   **IDA** (Windows): for an existing IDA setup with an MCP registration. 

See [Set up native analysis](https://rea.tools/get-started/#native) for the steps.

Use REA to find how DX-Ball calculates sound panning. Explain the calculation and show the code.

Example prompt. Give your agent the path to your local DX-Ball 1.07 executable. REA doesn't include DX-Ball, so use your own copy, or ask the same kind of question about another small Windows program you have.

How do I get a file's full path?
*   **Windows:** in File Explorer, right-click the file and choose _Copy as path_. On Windows 10, hold Shift while right-clicking. 
*   **macOS:** in Finder, right-click the file, hold Option and choose _Copy "…" as Pathname_. 
*   **Any system:** drag the file into a terminal window and its path appears. 

## Read the REA results

### Read the input

```
MOV EAX, dword ptr [EBP + 0x8]
MOV dword ptr [EBP + -0xc], EAX
FILD dword ptr [EBP + -0xc]
```

The instructions load an integer argument and convert it for floating-point arithmetic. This is the input absent from the first pseudocode view.

### Follow the caller

```
ADD EAX, 0x14
PUSH EAX
CALL 0x00406400
```

REA identifies the brick-hit caller. Its earlier instructions multiply the tile coordinate by 30; adding `0x14` (20) gives the brick's screen position.

### Read the referenced constants

```
0x420068  000000000000f93f  → 1.5625
0x420070  0000000000407f40  → 500.0
0x4210a0  000000000000f03f  → 1.0
```

The arithmetic references these addresses. Reading the bytes supplies the actual values; the instruction order tells the agent how they are used.

## Write and check the recovered function

```
pan = (double)x;
pan = pan * 1.5625;
pan = pan - 500.0;
pan = pan * dxball_pan_scale;
return (DxBallInt)pan;
```

With a scale of 1.0, screen positions 0, 320 and 640 map to −500, 0 and 500 before integer conversion. The calculation puts the center of the screen at the center of the stereo field.

The agent used REA's findings to write the C. Separate checks compared 3,205 inputs against the original x86 function and reproduced all 63 compiled bytes of the complete function.

[See the full investigation and assembly-to-C comparison](https://rea.tools/showcase/dx-ball/#sound-pan)

## Try it with your own binary

[Connect a native analysis provider](https://rea.tools/get-started/#native), then give your agent a local executable or library and a feature to investigate. Useful starting questions include “How is this file parsed?” or “Which function handles this menu action?”

If you already know a function name or address, you can query it from the terminal. For a configured Ghidra installation:

```
npx -y rea-agents@latest function /absolute/path/to/program main \
  --provider ghidra --json
```

Replace the target path and `main` with your own function name or address. Each CLI invocation imports and analyzes the binary, then closes its session. Your agent's MCP queries reuse the imported binary while that session is open.

Read the pseudocode alongside instructions and references. When a result leaves a call or value unresolved, use that location as the next question.

## JavaScript and Electron guide — https://rea.tools/guides/javascript/

## Where does “Export notes” go?

This guide uses a small Electron app. Clicking **Export notes** calls an API in the page, crosses into the main process, and writes a CSV. The behavior is spread across several files.

The CSV export across Electron processes

1.   Renderer → preload`notes.exportCsv()``renderer.js` calls the API exposed by `preload.js`.
2.   Between processes`notes:export`The preload invokes an IPC channel: a named message to the main process.
3.   Main process An export handler`main.js` handles that channel and calls the CSV writer.

`csv.js` formats the notes → `main.js` writes `downloads/notes.csv`.

 REA matches the literal IPC call to its handler and identifies the exposed API. The path is inferred from code; a runtime capture can check what executes. 

## Ask about the CSV export

[Connect your agent to REA](https://rea.tools/get-started/#agent) and give it the app directory or ASAR file:

Use REA to find what happens when I export notes in this app. Where is the CSV created?

Example prompt. Include the absolute path to the application folder or `app.asar`.

REA reads the application files and builds a map of entrypoints, modules and process boundaries. Your agent uses that map to narrow the investigation to the export feature.

## Trace the export code

### The page calls a small API

```
document.querySelector("#export").addEventListener("click", async () => {
  const destination = await window.notes.exportCsv();
  document.querySelector("#status").textContent = `Saved to ${destination}`;
});
```

The page knows the method name. The implementation lives in the preload, which exposes it to the renderer.

```
contextBridge.exposeInMainWorld("notes", {
  exportCsv: () => ipcRenderer.invoke("notes:export"),
});
```

REA records `notes.exportCsv` and the literal channel `notes:export`. It pairs that invocation with the single matching handler in the main process.

```
ipcMain.handle("notes:export", () => {
  const destination = path.join(app.getPath("downloads"), "notes.csv");
  writeFileSync(destination, toCsv(notes), "utf8");
  return destination;
});
```

Reading the handler answers the original question: `csv.js` formats the notes, and the main process writes `notes.csv` into the user's Downloads folder.

```
{
  "literal_channels": 1,
  "renderer_transmissions": 1,
  "main_handlers": 1,
  "paired_renderer_transmissions": 1,
  "ambiguous_renderer_transmissions": 0
}
```

Recorded by REA 4.1.0 on the downloadable example below. Source locations accompany the API, channel and handler findings.

## Analyze the example yourself

Download the example and unzip it. The archive contains the complete `notes-example` folder. Analyze it with Node.js and npm; Electron is not needed for this example.

[Download example ZIP](https://rea.tools/examples/notes-example.zip)

Browse the six source files
*   [package.json](https://rea.tools/examples/notes-electron/package.json)
*   [main.js](https://rea.tools/examples/notes-electron/main.js)
*   [preload.js](https://rea.tools/examples/notes-electron/preload.js)
*   [renderer.js](https://rea.tools/examples/notes-electron/renderer.js)
*   [csv.js](https://rea.tools/examples/notes-electron/csv.js)
*   [index.html](https://rea.tools/examples/notes-electron/index.html)

```
npx -y rea-agents@latest analyze-javascript-application \
  /absolute/path/to/notes-example --json
```

Replace the path with the folder you unzipped. You should find one IPC channel and one matching handler in `normalized_result.summary.ipc`. Source locations are in `normalized_result.graph`.

For your own app, use the same command with its directory or ASAR path. An agent can follow a literal string, API name or IPC channel with REA's feature tracing tools.

## Inspect the CSV writer

> Follow `notes:export` to its handler. Which inputs reach the CSV writer, and what happens if writing the file fails?

Use the source locations to inspect those details. Computed channel names and ambiguous handlers can remain unresolved; runtime observations give you another way to investigate them.

*   [Follow Notion's clipboard bridge](https://rea.tools/showcase/notion/)Apply the same approach to a packaged Electron app.
*   [Observe a browser export](https://rea.tools/browser/)Capture a real click and see which request it makes.
*   [Follow a native function](https://rea.tools/native/)Continue into a binary when a feature depends on native code.

## Browser and network guide — https://rea.tools/guides/browser/

## What happens when you click Export?

The [Notes browser example](https://rea.tools/examples/notes-web/) has an **Export notes** button. Clicking it loads `notes.json`, formats the two notes as CSV, and starts a download.

From the click to the CSV download

1.   01 · You Click Export notes Perform the action in your browser while the capture is running.
2.   02 · REA Record the request Capture the request URL, response status and JSON structure from the selected page.
3.   03 · Your agent Read the export code Connect the observed request to `fetch("./notes.json")` in `export.js`.

`GET notes.json → 200 → notes[] → CSV`

 Start the capture before clicking Export notes. 

## Open Chrome with remote debugging

Open the hosted Notes example with a separate browser profile and a local debugging port. On Linux:

```
google-chrome \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/rea-notes-browser \
  https://rea.tools/examples/notes-web/
```

Use your installed browser's executable path on macOS or Windows. You can replace the page URL with another page you want to inspect.

REA connects to this existing browser. You keep control of the page, perform the action, and close the browser when finished.

## Ask your agent to watch one action

Use REA to inspect this page while I click Export notes. What request does it make, and how is the CSV built?

Example prompt. Give your agent the debugging endpoint, `http://127.0.0.1:9222`, and the page URL. Let it start the capture before you click.

Your agent discovers the page target, starts an observation window, and reads the resulting evidence. It can then inspect the script behind the export.

## Or capture from the terminal

Find the page's target ID:

```
npx -y rea-agents@latest list-browser-targets \
  http://127.0.0.1:9222 --json
```

Choose the target with the Notes example URL. Replace `TARGET_ID` below with its ID, then run:

```
npx -y rea-agents@latest inspect-web-page \
  http://127.0.0.1:9222 TARGET_ID \
  --observation-ms 10000 \
  --include-accessibility-text \
  --include-json-body-shapes --json
```

Let the command connect for a few seconds, then click **Export notes** in that browser. The result arrives after the observation window ends.

The captured result includes the selected page, network activity during that window, and the shape of the JSON response. Earlier requests are outside this capture.

## Read the request and export script

 Recorded with REA 4.1.0 on the local Notes example 
| Captured fact | Value |
| --- | --- |
| Request | `GET /examples/notes-web/notes.json` |
| Response | `200 · application/json` |
| Request initiator | `export.js` · script |
| Response structure | `notes[]` with `id` and `title` fields |

```
npx -y rea-agents@latest inspect-web-page \
  http://127.0.0.1:9222 TARGET_ID \
  --include-script-sources --json
```

The request identifies the data source, and REA records `export.js` as its initiator. Read the captured script source to see how the data is used:

```
const response = await fetch("./notes.json");
const { notes } = await response.json();
// Format each note as a CSV row.
const url = URL.createObjectURL(new Blob([csv], { type: "text/csv" }));
link.href = url;
link.download = "notes.csv";
link.click();
```

The download is constructed in the page using the JSON response. The CSV formatting step comes from the script; the network capture establishes that this click requested `notes.json`.

[Open the example](https://rea.tools/examples/notes-web/) · [Download export.js](https://rea.tools/examples/notes-web/export.js) · [Download notes.json](https://rea.tools/examples/notes-web/notes.json)

> Find the script that requests `notes.json`. How does it escape titles containing commas or quotation marks?

For an installed JavaScript or Electron app, continue with the [application workflow](https://rea.tools/javascript/) to follow files and process boundaries.

For HTTP request and response bodies, use [Fiddler Everywhere: SAZ captures, MCP and public skills](https://github.com/morluto/rea/blob/main/docs/web-network-captures.md). Export SAZ or HAR 1.2 for offline REA capture Evidence, or connect Everywhere's MCP server to inspect captured traffic with your agent.

## FAQ — https://rea.tools/faq/

## Setup and updates

How do I install REA?
With Node.js and npm available, run setup, choose your coding agent and review the proposed changes.

`npx rea-agents@latest setup`

Setup registers REA's MCP connection and installs the matching investigation skill. Restart your agent when it finishes, then give it a target path and a question. [Follow the setup guide](https://rea.tools/get-started/) for prerequisites and your first analysis.

Which coding agents can use REA?
Any agent that supports local MCP servers. Setup includes Claude Code, Claude Desktop, Codex, Cursor, Gemini CLI, Windsurf, Devin, OpenCode, Antigravity, GitHub Copilot CLI, Command Code, Grok Build, OMP, and VS Code. Grok Bot's connector is added from its chat.

[Connect your coding agent](https://rea.tools/get-started/#agent).

How do I update REA?
REA releases frequently, including bug fixes. If you installed the CLI with npm:

`rea update`

Follow the setup refresh command printed by the update. If you set up your agent through `npx`, run:

`npx rea-agents@latest setup`

Review the changes and restart your agent. Its REA connection pins a package version, so refreshing setup makes it use the new release. For one-off CLI commands, use `npx -y rea-agents@latest` followed by the command.

 Is installing the skill from skills.sh enough? 
The skill gives your agent investigation instructions. Run [REA setup](https://rea.tools/faq#install) to connect the MCP server and install the matching skill, then restart your agent so it can call the tools.

## Analysis

What can I analyze with REA?
Start with the kind of software you have:

*   [Native executables and libraries](https://rea.tools/guides/native/): functions, assembly, pseudocode and references. 
*   [JavaScript and Electron apps](https://rea.tools/guides/javascript/): modules, imports, IPC and source locations. 
*   [Browser pages](https://rea.tools/guides/browser/): scripts, requests and runtime observations. 

REA also has workflows for managed assemblies, Android APKs, firmware and packaged resources. [See the case studies](https://rea.tools/showcase/) for worked investigations.

Do I need Hopper, Ghidra or IDA?
Deep native analysis uses one of them. Static JavaScript and .NET inspection work with the supplied files and do not need a native analysis engine.

Connect your existing Ghidra or IDA installation, or let setup detect Hopper and propose an installation. Your host and target determine which provider can be used. [Set up native analysis](https://rea.tools/get-started/#native).

Can I use REA without a coding agent?
Yes. The CLI uses the same analysis workflows. For a local JavaScript or Electron app:

```
npx -y rea-agents@latest analyze-javascript-application \
  /absolute/path/to/app --json
```

Replace the path with an extracted application folder or ASAR file. [Use the CLI](https://rea.tools/get-started/#terminal) for installation options.

What code does REA return?
Native analysis returns assembly and pseudocode, with calls, references and relevant constants. JavaScript analysis returns modules, their relationships and source locations.

Your agent uses these findings to explain the behavior or write and test an implementation. The [DX-Ball calculation](https://rea.tools/showcase/dx-ball/#sound-pan) and [CTF flag checker](https://rea.tools/showcase/ctf/) show how that process works.

What should I ask my agent?
Give it a local target and one behavior to investigate. For a JavaScript or Electron app:

Use REA to analyze /absolute/path/to/app and explain how it exports data. Show the relevant code and source locations.

Replace the path with your target. The [guides](https://rea.tools/guides/) provide prompts for native, Electron and browser examples.

## Troubleshooting

Why can't my agent see the REA tools?
Restart or reconnect your agent after setup. Check its REA registration with `doctor`; for Codex:

`npx -y rea-agents@latest doctor --client codex --json`

Replace `codex` with your client ID, such as `claude_code` or `cursor`. If the report shows a missing or stale registration, run setup for that client:

`npx rea-agents@latest setup --client codex`

Review its plan and restart the client. If registration is healthy but tools remain absent, check the client's MCP connection error. [More setup diagnostics](https://rea.tools/get-started/#help).

Do I need to start Hopper first?
REA starts Hopper when an operation needs it. On macOS, complete the first-run choice of demo mode or license activation before unattended analysis. [See native provider setup](https://rea.tools/get-started/#native).

What should I do if I hit a bug?
[Update REA](https://rea.tools/faq#update), restart your agent and retry the same task. A recent release may already fix the problem.

If it persists, [open an issue](https://github.com/morluto/rea/issues/new/choose) with your REA version, operating system, target type, steps to reproduce and error output. Include the provider name when the problem involves native analysis.

## Data and sharing

Does REA upload my app?
REA analyzes targets on your machine. Your agent receives the results, and its model provider's data policy applies to those results.

How can I share an example or contribute?
Have a useful REA example? We'd love to see it. Share the target, your question, the findings and how you checked them in an [issue](https://github.com/morluto/rea/issues/new/choose) or [pull request](https://github.com/morluto/rea/pulls). Short code excerpts and figures help others follow the investigation.

Bug reports, feature requests, documentation and code improvements are welcome too. You can also discuss an example in the [community](https://discord.gg/GkcryMnJDM).

## Showcases — https://rea.tools/showcase/

[Home](https://rea.tools/) / Showcases

Android, games, Electron and a CTF challenge, with code, figures and checked results.

Android · APK analysis

## How an authenticator generates a login code

Find Aegis's six-digit code calculation in its released APK. Trace the generating methods with REA, then move a demo clock to see why the code changes every 30 seconds.

APK Generating code Recovered rule Adjustable clock

[Read the Android case study](https://rea.tools/aegis/)

CTF · Native analysis

## Solve a CTF flag checker

Inspect an easy DownUnderCTF challenge with REA. Find its checking functions, turn masks and sums into equations, then verify the solved flag with the original program.

Binary Checking code Equations Correct!

[Read the CTF case study](https://rea.tools/ctf/)

Native · Reconstruction

## DX-Ball's sound-pan calculation

Recover a sound-pan calculation from a 1996 Windows game. REA's instructions, caller references and numeric constants lead to a small C function, checked against the original behavior and all 63 compiled bytes.

Executable REA findings Recovered C Validation

[Read the DX-Ball case study](https://rea.tools/dx-ball/)

Electron · Feature tracing

## How Notion copies text and HTML

Trace a page-facing API through Notion's packaged JavaScript. Follow its IPC wrappers to the system clipboard, then see how a small HTML marker keeps rich block data connected to a copy.

Packaged app Exposed API IPC wrappers Clipboard

[Read the Notion case study](https://rea.tools/notion/)

PC-98 DOS · Reconstruction

## How TH04 aims a ring of bullets

Inspect the original 16-bit angle helper with REA. Match its multiply, divide and coordinate operations to readable C++, then see how they produce a ring aimed at the player.

Original DOS code REA instructions Angle calculation Bullet ring

[Read the TH04 case study](https://rea.tools/th04/)

## Step-by-step guides

The guides walk through a native calculation, an Electron export and a browser request. Each starts with a prompt and a concrete target.

[Read the guides](https://rea.tools/guides/)

## Blog: Does reverse engineering need a bigger model? — https://rea.tools/blog/reverse-engineering-models/

## What better models changed

Since August 2026, I have been exploring how much reverse engineering an agent can carry out with access to a program and a way to check its work. Most of my experience comes from reconstructing games, especially Touhou. As I have changed models, the repositories have kept a record of what each session managed to recover.

Much of that work aims at exact reconstruction: we compile the maintained source under a pinned historical toolchain and check whether it reproduces the target function. When a later model succeeds where earlier work stalled, the source changes show what made that progress possible.

### The temporary values had to stay alive together

Much of a TH09 attack function's logic had already been reconstructed, but the compiler still stored temporary results differently from the original. The remaining problem was how long those results needed to stay alive and when their storage could be reused.

A [GPT-6-Sol checkpoint](https://github.com/N0zoM1z0/th09/commit/de63c0f9121963f3a6b1ab5471c4878625fd3425) recorded this mismatch after testing several ordinary source arrangements. When [GPT-6.1-Sol returned to the problem](https://github.com/N0zoM1z0/th09/commit/52929ed7c299f1a5f29cc13964e22510145fd616), it found a useful hypothesis about how long those temporary values needed to stay alive.

The function produced temporary results and copied them into animation positions. In C++, a temporary result stays alive until the expression using it finishes. Grouping the real operations into one expression kept those results alive together, so the compiler could no longer reuse the same storage for all of them.

One result still shared storage with a value used later for collision checks. Giving that value its own lifetime resolved the remaining overlap. After several targeted experiments, **a clean rebuild confirmed that the full function matched**.

What interests me is how the discovery and the tests worked together. The lifetime hypothesis gave the agent a new direction; compiler feedback helped it refine that hypothesis into a source arrangement that matched.

### A different control-flow graph

A second TH09 function shows why that new direction can matter. Here, the obstacle was how several branches shared their final work. [GPT-6.1-Sol's earlier work](https://github.com/N0zoM1z0/th09/commit/f8d12d72aaf02212ee1b585a8f3f86d7ed000269) got parts of the function to match, but the branches still joined up differently from the original.

[GPT-6-Astra changed the surrounding control-flow graph](https://github.com/N0zoM1z0/th09/commit/da33a646221198ceb7f3df2b96e2ca0e9b2f705f). The main paths now led to a shared final update and return. In that source structure, the compiler combined the branches in the same way as the original. The complete function matched, and a [separate rebuild check confirmed it](https://github.com/N0zoM1z0/th09/commit/5f825b28a862f8e1a6d4aea2f78a42f04c09a1c0).

**Changing the representation opened a more productive search space.** Both cases give me a reason to take general model capability seriously: an agent can keep trying local variations for a long time before finding a better way to express the surrounding work.

At the same time, the later sessions started with earlier source and recorded failures. That accumulated work was part of their advantage. The history lets us inspect the discoveries and their checks; a controlled comparison would help separate the effect of the model from the experience it inherited.

This is where the question becomes interesting to me. Some of the progress came from finding a new representation, while much of the remaining work involved testing source forms against a familiar compiler. How much needs broad reasoning ability, and how much could a model learn through repeated experience with that compiler and code?

## Why might a specialist do well?

Touhou gives us a concrete reason to expect that experience to help. Much of the game code comes from the same author, ZUN, so recurring habits are a reasonable starting assumption. The repositories back that up with useful examples: related loops and helper arrangements have supplied hypotheses across games.

Those source patterns become more specific when we include the compiler. Under a particular version and set of options, small changes in source can produce repeatable differences in machine code. Some of those differences are surprisingly obscure.

In TH095, for example, **even the name used for a local variable could change where VC7.1 stored it**. Moving the declaration alone did not solve the layout, but an earlier background function had revealed a naming pattern that affected the compiler's choice. That gave us a more promising hypothesis for [the reconstruction of `Supervisor::LoadDat`](https://github.com/N0zoM1z0/th095/commit/26bb64bdb093a13f73abd0ee8ae7ce199ee4658f).

Reusing that pattern for the file-size variable produced the required layout without adding storage. The full function then matched.

This is the sort of narrow detail a general model may not know when it arrives. A specialist trained on this compiler could encounter many such cases and learn which source variations are worth testing first.

The opportunity is especially clear in final matching problems where we already understand the behavior. We are then asking which ordinary source form this compiler turns into the observed instructions. Specialization could help the model propose those forms more efficiently, while the target still determines which hypotheses survive.

The useful patterns would have to retain their context, though. TH08 uses an earlier Visual C++ version than TH095 and TH09. TH04 uses a different DOS-era compiler, and its [player reconstruction](https://github.com/N0zoM1z0/th04/commit/6dce0a79d5b931f0e2a08475b90e0c33d2321b98) needed different hypotheses about source patterns and how the compiled code was combined into an executable. Shared authorship gives us a prior, but each target tells us whether it applies. Distinguishing those contexts is part of what a specialist would need to learn.

## Where should that experience live?

Before deciding to teach those patterns through model training, I would look at the knowledge we already keep in the repository. In the [previous essay](https://rea.tools/touhou-reconstruction/), I wrote about it becoming the project's working memory. That memory includes compiler lessons, along with the source and failed experiments that made them useful.

By retrieving that record, an agent can start with a known result and inspect how we reached it. It can also avoid alternatives that have already failed in the same context. The starting point improves without changing the model's weights.

When reconstructing TH09's enemy-spawn function, a [GPT-6-Luna-max session](https://github.com/N0zoM1z0/th09/commit/1eb843383941d00065622a9e353146c4bb96979e) drew a hypothesis from TH08's corresponding source family. That earlier source suggested how to structure the loop and handle failures within it. TH09's own evidence supplied the game-specific details, and clean rebuilds confirmed the complete match.

**"The model did not know that compiler quirk" and "the model could not use it" are different problems.** Retrieval may solve the first, but turning that fact into a useful candidate still takes work. And if the candidate fails, the model must decide what the result means for its next attempt. Knowing the relevant pattern is only the beginning of that process.

For that reason, I would include a smaller general model with good retrieval in any comparison. Giving it the same library of experience would help us identify what training adds: better candidate generation, better decisions after feedback, or both.

## Learning the next useful experiment

Those decisions after feedback are what I would most like to study. In agentic reconstruction, the model proposes an explanation and tests it against the program. Even when the candidate fails, the result can narrow the remaining possibilities and suggest a more useful next experiment.

Consider the temporary-results example again. Its final source shows the arrangement that worked, but the route to that source contains more information. Each of the following experiments helped identify what still needed to change.

| Experiment | What its result taught us |
| --- | --- |
| Try a different way to copy the results | The copy code changes, but the function still differs. |
| Use the returned values directly | Copying follows the original pattern, but temporary storage still differs. |
| Keep the temporary results alive together | They get separate storage, but one still overlaps a value used later for collision checks. |
| Keep the collision-check value separate | A clean rebuild confirms the complete match. |

Selected experiments from the attack-function reconstruction above, grouped by what they taught us.

A training record that keeps this sequence can teach more than the final source alone. It connects each proposed change to an observed result and the next decision. Keeping ineffective variations matters too: they tell a later agent which hypotheses have already been tested in that context.

**I would want the model to learn how to use feedback.** A neutral result is a reason to reconsider the variation; a changed mismatch may point to another cause. When local edits stop being informative, the agent should be able to revisit the source representation or inspect the evidence again.

Learning to make those choices requires autonomy. Sometimes the useful next step is inspecting another caller rather than compiling another edit. A rigid sequence of required rewrites would remove that choice, along with part of the behavior we want the model to learn.

## Why RE is interesting for reinforcement learning

Bounded reconstruction gives us a practical environment for studying these choices. Once the target and compiler are pinned, many source experiments produce quick, repeatable feedback. The agent can compile a candidate, inspect the mismatch and use that observation to choose its next step.

Reinforcement learning could train that decision-making process through the feedback it receives. A candidate accepted by a defined check gives us a concrete outcome, while the sequence of attempts lets us observe how much work it took to reach it.

There is already research supporting this direction. [LLM4Decompile](https://aclanthology.org/2024.emnlp-main.203/) studies models specialized for decompilation. [AutoDecompiler](https://arxiv.org/html/2606.16162v1) trains multi-turn refinement using compiler and execution feedback. Their studies focus on functional recovery. For this work, I would use them as a starting point for the related task of finding source that matches a historical compiler's output.

To reach such a well-defined task, though, we may first need to establish what a function owns or devise a new runtime measurement. In TH08, for example, a [collision difference led back to how the original program handled floating-point calculations](https://github.com/N0zoM1z0/th08/commit/af9cb1d3e839b15a78b47ac1701506083cc82847). Before the agent could test a useful correction, it had to work out what to measure.

This suggests another role for a broadly capable model: helping make the problem checkable in the first place. Once that check exists, we can investigate how far a learned search policy can get with it.

## When the oracle is wrong

Once we train against that check, its coverage becomes part of what the model learns. I call the reference or checker an oracle. Even if it gives a repeatable answer, we still need to understand what that answer covers.

TH08 showed how much can hide outside that coverage. Some reconstructed functions passed their exact comparisons with wrong floating constants. The comparator adjusted relocated addresses before checking instructions, but it checked the values behind those addresses only when they had been explicitly recorded for verification. Other literal references could pass without their values being examined.

To close that gap, a [wider audit](https://github.com/N0zoM1z0/th08/commit/a393f400786e4cc6cbb1000af0dad3276da12c78) found incorrect constants in functions that had already been accepted. In one calculation, the reconstructed source added `1.0f` where the original added `32.0f`.

**A learner rewarded by the old check could learn to produce the wrong reconstruction.** We had not trained an RL model against this oracle; the observed failure was in the check itself. But using that check as a reward would have made the same blind spot part of the learning environment.

A functional test can have a similar blind spot. [Differential-fuzzing research on LLM decompilers](https://arxiv.org/html/2609.05370v1) has found behavior differences beyond the supplied tests. Passing those tests therefore needs to be read in terms of the cases they exercise, just as an instruction match needs to be read in terms of the bytes and data it checks.

Before using either kind of check as a reward, I would test it with deliberate failures. I would also keep final acceptance outside the candidate's editable source, so the model has to satisfy the check through its reconstruction. Otherwise, something like a byte array copied from the target could satisfy a naive score without recovering useful source.

**Improving the learner and improving its oracle belong to the same research problem.** As the learner gets better at optimizing the feedback we give it, understanding that feedback becomes more important too.

## A comparison worth running

With those checks in place, I would start the comparison on a fixed VC7.1 task family. First, I would establish baselines for a strong general model and a smaller one. Adding repository knowledge to the smaller model would show what retrieval changes. From there, supervised specialization and an RL-trained version would let us examine what training adds.

To make those comparisons informative, each model would receive the same target evidence and tools. For the training-specific comparisons, I would keep the base model and available knowledge fixed as well. Repeated trials would help distinguish a reliable search strategy from a lucky candidate.

I would then separate two starting conditions: reconstructing a function from its instructions, and closing the last few differences in maintained source. A specialist might be excellent at the second task while a general model does much of the work needed to reach it. Measuring them separately would reveal that division of work.

Both tasks need genuinely held-out examples. Because related Touhou games share engine code, holding out a game's name would still allow nearly identical functions to appear in training. I would instead hold out source families and keep their accepted answers out of both training and retrieval.

On those examples, the outcome would be complete, independently validated matches. Giving each model the same candidate or compile budget would help compare search quality. Measuring elapsed time and total cost, including compilation, would tell us whether that quality produces an efficient workflow. Training costs would need their own accounting too.

Both views matter because a cheaper proposal can become an expensive workflow if it causes more uninformative compiles. Conversely, a slower model may pay for itself by finding a useful experiment sooner. The comparison should capture those costs.

Counting accepted results also keeps intermediate progress in perspective. One TH09 [replay-save candidate](https://github.com/N0zoM1z0/th09/commit/ab72fd77728293fc0beacfc656ca701b0e266016) looked promising because the compiled function had the expected size, but a full comparison still found substantial differences. Changes in how the compiler arranges instructions can also make a candidate look closer without resolving the underlying problem. Such diagnostics can guide the next experiment, but I would validate any reward for "getting closer" against the full acceptance check.

I would be interested in the pattern across these results. If a specialist does well within a familiar compiler family, does that advantage survive a toolchain change? And once both models have good retrieval, how much does training still add? The answers would help us decide where each kind of model is most useful.

## What kind of agent does this suggest?

If the models turn out to help at different stages, a useful arrangement might be a broad agent with access to a specialist. Once a task becomes a familiar compiler search, it could ask the specialist for candidates. If the results stop making sense, the broader agent could return to the target evidence or investigate the measurement itself.

In that arrangement, specialization becomes a tool the agent can choose as the investigation develops. The agent keeps the freedom to change direction that made the earlier breakthroughs possible.

This follows naturally from the industrial shift I described in the previous essay. Being able to run many more experiments changes how we organize the work. It also gives us a reason to ask which decisions need broad judgment and which improve through repeated experience with a particular craft.

For now, the strongest general model has earned its place in my workflow by opening problems I had left unresolved. Those successes are what make me want to examine the work more closely: how much depended on the model's breadth, and how much could be handled by a model trained in this particular kind of reconstruction?

**The repositories give us a way to test the question.** I would like to use that record to build the comparison and see what we learn.

Evidence and model attribution
[Detailed evidence notes](https://github.com/morluto/rea/blob/main/website/evidence/reverse-engineering-models.md) include the recorded comparisons and experiment context.

The examples describe historical function-level comparisons recorded in the linked commits. Whole-game runtime checks are separate milestones. Source and matching records were reviewed on 13 October 2026.

The TH09 label `gpt-dots` identifies GPT-6-Astra. `gpt-web` changed with the model used at the time, so that label alone does not identify an individual run. Explicit model names in the other cited commits establish their recorded attribution; the histories do not contain uniform per-run cost or effort measurements.

*   **TH09 temporary lifetimes:** the [earlier context review](https://github.com/N0zoM1z0/th09/commit/de63c0f9121963f3a6b1ab5471c4878625fd3425) and [complete cold reconstruction](https://github.com/N0zoM1z0/th09/commit/52929ed7c299f1a5f29cc13964e22510145fd616). 
*   **TH09 Front callback:**[non-exact diagnostic regions](https://github.com/N0zoM1z0/th09/commit/f8d12d72aaf02212ee1b585a8f3f86d7ed000269), [Astra's new graph](https://github.com/N0zoM1z0/th09/commit/da33a646221198ceb7f3df2b96e2ca0e9b2f705f) and its [accepted recompile replay](https://github.com/N0zoM1z0/th09/commit/5f825b28a862f8e1a6d4aea2f78a42f04c09a1c0). 
*   **Compiler knowledge:**[TH095 identifier-bucket reuse](https://github.com/N0zoM1z0/th095/commit/26bb64bdb093a13f73abd0ee8ae7ce199ee4658f), [TH04 player source and linker order](https://github.com/N0zoM1z0/th04/commit/6dce0a79d5b931f0e2a08475b90e0c33d2321b98) and [Luna's TH09 enemy-spawn closure](https://github.com/N0zoM1z0/th09/commit/1eb843383941d00065622a9e353146c4bb96979e). 
*   **Checks and diagnostics:**[TH08 floating-literal audit](https://github.com/N0zoM1z0/th08/commit/a393f400786e4cc6cbb1000af0dad3276da12c78), [TH08 numerical investigation](https://github.com/N0zoM1z0/th08/commit/af9cb1d3e839b15a78b47ac1701506083cc82847) and [TH09 replay-save reconstruction](https://github.com/N0zoM1z0/th09/commit/ab72fd77728293fc0beacfc656ca701b0e266016). 

The proposed specialist and RL comparisons are future experiments. The project histories motivate them; no trained specialist was evaluated for this essay.

