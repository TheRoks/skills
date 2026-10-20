# Agent Skills

Portable skills for coding agents. Each skill follows the shared Agent Skills format and includes focused references where needed.

## Skills

- [clean-code](.agents/skills/clean-code/SKILL.md) — review, explain, and refactor code against an explicit Clean Code rule catalog, with TypeScript examples and guidance for C#/.NET and other languages.

## Install with the `skills` CLI

The [Agent Skills CLI](https://github.com/vercel-labs/skills) can install a skill into a project or into your personal agent directories. Run these commands from the project where you want to use the skill.

### Install from this GitHub repository

After this repository is published, replace `OWNER/REPO` with its GitHub owner and repository name:

```sh
npx skills add OWNER/REPO --skill clean-code -a codex -a claude-code -a github-copilot
```

The CLI will ask where to install and whether to symlink or copy. Project installation is the default and can be committed for the team. Choose `--copy` instead of symlinks if your environment does not support them:

```sh
npx skills add OWNER/REPO --skill clean-code -a codex -a claude-code -a github-copilot --copy
```

For a personal installation shared across projects, add `--global`:

```sh
npx skills add OWNER/REPO --skill clean-code --global -a codex -a claude-code -a github-copilot
```

### Install from a local checkout

From the project where you want the skill, point the CLI at this repository's local checkout:

```sh
npx skills add /absolute/path/to/skills --skill clean-code -a codex -a claude-code -a github-copilot
```

Use the `--global` flag for a personal install. The source repository itself does not need to be the target project.

### Check and update

List skills available from the source without installing them, list installed skills, or update this skill later:

```sh
npx skills add OWNER/REPO --list
npx skills list
npx skills update clean-code
```

Replace `OWNER/REPO` in each GitHub command with the published repository coordinate. See the CLI's [command reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md) for supported agents, flags, and current behavior.

## Skill layout and discovery

The canonical skill is in `.agents/skills/clean-code/`. The `.claude/skills/clean-code` path in this repository links to that same directory. The CLI can create the agent-specific project or personal links when installing. Shared file format and installation do not guarantee that every agent host discovers or follows a skill, so confirm it is available in each host and run the [cross-agent evaluation cases](.agents/skills/clean-code/evals/cases.md).

To invoke it, ask the agent to use the `clean-code` skill for a review or refactor. Ask for “report only” when you want findings without edits, or request a behavior-preserving refactor when you want changes. Reports and fixes should identify the specific rule IDs used.

## Maintain and validate

When changing the skill, update the rule references and evaluation cases together. Run the standard-library validation script:

```sh
python3 .agents/skills/clean-code/scripts/validate_skill.py
```

The script checks required skill metadata, local Markdown links, catalog ID completeness and uniqueness, evaluation references, and the Claude alias. It does not establish that a live agent behaves correctly; run the cases for each host you support and record the product/version and result.
