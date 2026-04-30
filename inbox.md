# Inbox

Drop URLs below under `## Pending`. Run `/pin-llm-wiki run <url>` to ingest a single URL (auto-queues it if missing), or `/pin-llm-wiki run` to batch-process every pending item. Agents may use `/pin-llm-wiki queue <url>` to suggest URLs without immediately ingesting them.

## Pending

<!-- Add URLs here, one per line, as markdown checkboxes.
     Supported inline tags (append each wrapped in HTML comment syntax):
       detail:brief        — override detail level for this source
       detail:standard
       detail:deep
       branch:dev          — GitHub: use this branch instead of default
       clone               — GitHub deep: full git clone to raw/github/<org>-<repo>/
       skip                — skip this URL on the next run
       companion:github.com/<org>/<repo>  — web: use this repo as companion (skip auto-discovery)
        no-companion        — web: suppress companion GitHub fetch even if a repo is found
        note: <text>        — freeform note for human review (ignored by ingest)
-->

- [ ] https://github.com/njbrake/agent-of-empires
- [ ] https://github.com/nidhinjs/prompt-master
- [ ] https://factory.ai/
- [ ] https://github.com/Gitlawb/openclaude
- [ ] https://medium.com/@unicodeveloper/10-must-have-clis-for-your-ai-agents-in-2026-51ba0d0881df
- [ ] https://x.com/ericzakariasson/status/2036762680401223946?s=20
- [ ] https://focusee.imobie.com/
- [ ] https://wisprflow.ai/
- [ ] https://github.com/VoltAgent/awesome-agent-skills
- [ ] https://github.com/zilliztech/claude-context
- [ ] https://pi.dev/
- [ ] https://brave.com/search/api/
- [ ] https://resend.com/
- [ ] https://www.hostinger.com/1
- [ ] https://microsoft.github.io/autogen/stable//index.html#
- [ ] https://zapier.com/
- [ ] https://n8n.io/
- [ ] https://hermes-agent.nousresearch.com/
- [ ] https://www.teamoffsite.ai/
- [ ] https://github.com/mksglu/context-mode
- [ ] https://tolaria.md/

## Completed

<!-- Processed lines are moved here automatically.
     Format after ingest: - [x] https://... with an "ingested YYYY-MM-DD" HTML comment appended.
     To re-fetch: add a "refresh" HTML comment to the line, then run /pin-llm-wiki run.
     The refresh tag is removed automatically after re-fetch.
-->

- [x] https://paperclip.ing <!-- ingested 2026-04-28 -->
- [x] https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking <!-- detail:brief --> <!-- ingested 2026-04-28 -->
- [x] https://www.langchain.com/ <!-- detail:deep --> <!-- ingested 2026-04-29 --> <!-- refreshed 2026-04-29 --> <!-- refreshed 2026-04-29 -->
- [x] https://runcabinet.com/ <!-- detail:deep --> <!-- ingested 2026-04-29 -->
- [x] https://skills.sh/ <!-- ingested 2026-04-30 -->
