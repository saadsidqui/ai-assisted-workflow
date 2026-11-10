# R-01 · Further reading and resources

A starting index, grouped by the topics the module cards point to. Primary sources come first. Links were collected on 2026-11-10. The Anthropic and Claude Code pages were opened that day; the others are long-standing addresses that have not been re-opened. Check every link before a delivery, and prefer the vendor's own documentation for anything about features, permissions or data handling.

Rules for maintaining this list:

- Date-stamp anything likely to change.
- Vendor material describes the vendor's product. It is not independent evidence that something works.
- Remove a link that is broken or no longer maintained; do not let the list only grow.
- Third-party material keeps its own licence. Link to it; do not copy it in.

<a id="foundations"></a>

## Foundations

- [Anthropic: AI learning resources](https://www.anthropic.com/learn)
- [Google: Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
- [Microsoft Learn: training catalogue](https://learn.microsoft.com/en-us/training/)

<a id="working-method"></a>

## Working method and prompting

- [Anthropic: prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) and the model-specific guide for [Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)
- [OpenAI: prompt engineering guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Microsoft: Copilot documentation](https://learn.microsoft.com/en-us/copilot/)

<a id="coding-agents"></a>

## Coding agents

- [Claude Code: best practices](https://code.claude.com/docs/en/best-practices) and [how Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)
- [GitHub Copilot documentation](https://docs.github.com/en/copilot)
- [OpenAI Codex documentation](https://developers.openai.com/codex/)
- [Model Context Protocol documentation](https://modelcontextprotocol.io/docs/)
- [Git documentation](https://git-scm.com/doc)

<a id="repo-setup"></a>

## Repository setup

- [AGENTS.md: the open format](https://agents.md)
- Claude Code: [instruction files and memory](https://code.claude.com/docs/en/memory), [permissions](https://code.claude.com/docs/en/permissions), [permission modes](https://code.claude.com/docs/en/permission-modes), [sandboxing](https://code.claude.com/docs/en/sandboxing), [settings](https://code.claude.com/docs/en/settings), [the `.claude` directory](https://code.claude.com/docs/en/claude-directory)
- [Claude Code: skills](https://code.claude.com/docs/en/skills) and the [Agent Skills open standard](https://agentskills.io)
- [Claude Code release 2.1.277](https://github.com/anthropics/claude-code/releases/tag/v2.1.277), which added reading `AGENTS.md` when no `CLAUDE.md` exists

<a id="skills"></a>

## Skills worth studying

Read these as examples of how skills are written before installing any of them ([E-03.5](../tracks/engineering/repo-setup/E-03.5-skills.md)).

- [anthropics/skills](https://github.com/anthropics/skills): Anthropic's public skill repository
- [mattpocock/skills](https://github.com/mattpocock/skills): engineering and productivity skills, MIT licence
- [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop): a filter against generic AI output in copy, interfaces and code comments, MIT licence
- [plugin87/ux-ui-agent-skills](https://github.com/plugin87/ux-ui-agent-skills): design-system and accessibility skills, MIT licence
- [kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill): identity design from brief to vector files, MIT licence

<a id="security-privacy"></a>

## Security, privacy and governance

- [OWASP GenAI Security Project](https://genai.owasp.org), including the Top 10 for LLM applications
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [Claude Code: security](https://code.claude.com/docs/en/security)
- [Canadian Centre for Cyber Security](https://www.cyber.gc.ca/)
- [Office of the Privacy Commissioner of Canada](https://www.priv.gc.ca/)
- [Commission d'accès à l'information du Québec](https://www.cai.gouv.qc.ca/)

<a id="design-content"></a>

## Design and content

- [W3C: Web Content Accessibility Guidelines](https://www.w3.org/WAI/standards-guidelines/wcag/)
- The copywriting and interface skills in [anti-slop](https://github.com/miqdadbadjuber/anti-slop), as a catalogue of patterns that mark output as machine-made
- The frontend-design skill in [anthropics/skills](https://github.com/anthropics/skills)

<a id="language"></a>

## French language

- [Vitrine linguistique de l'Office québécois de la langue française](https://vitrinelinguistique.oqlf.gouv.qc.ca/), which includes the Grand dictionnaire terminologique and the typography and usage guidance
- [Termium Plus](https://www.btb.termiumplus.gc.ca/), the Government of Canada's terminology bank

<a id="adoption"></a>

## Adoption and measurement

- [DORA research](https://dora.dev/research/) on software delivery performance, including its work on AI-assisted development
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), for the governance vocabulary

<a id="staying-current"></a>

## Staying current

- [Claude Code changelog](https://github.com/anthropics/claude-code/releases)
- [GitHub Copilot changelog](https://github.blog/changelog/)
- The release notes of each tool on the organization's approved list. These are the source for refreshing the landscape snapshot ([C-02](../core/C-02-landscape-snapshot.md)).

---

[Curriculum index](../README.md) · [R-02 Glossary seed](R-02-glossary-seed.md) →
