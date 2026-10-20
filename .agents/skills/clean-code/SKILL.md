---
name: clean-code
description: Review, explain, and refactor code using an explicit Clean Code rule catalog. Use for code-quality audits and behavior-preserving cleanups in TypeScript, C#, .NET, and other languages.
---

# Clean Code Review and Refactoring

Use this skill to find concrete maintainability problems, explain them with stable rule IDs, and make focused fixes when requested. The catalog is a traceable checklist, not a mandate to rewrite code toward a single style.

The index at [references/rule-catalog.md](references/rule-catalog.md) is required reading for every review or refactor. It maps the catalog to Robert C. Martin's *Clean Code* (2008), records the limits of coverage, and routes to focused rule references. The catalog uses original paraphrases; it does not reproduce the book's prose or examples.

## Workflow

1. Read the rule-catalog index. Then read the topic reference(s) for the code in scope and the corresponding category in `references/rules/chapter-17.md`. For broad audits, read every rule reference. Identify the requested files, behavior, language, and local conventions or analyzer settings.
2. Treat the user's intent, correctness, security, accessibility, performance constraints, public contracts, and established project conventions as hard context. Apply a rule only when it fits the language and the code's purpose. Do not turn a stylistic preference into a defect. See [references/examples.md](references/examples.md) when applicability is uncertain or an idiomatic construct could look like a violation.
3. Inspect enough surrounding code and tests to understand callers, ownership, error paths, and boundaries. Do not infer a violation from a name or isolated line when nearby code changes its meaning.
4. Map every finding to one or more catalog IDs. Prefer the most specific rule. Include a short code location, observable evidence, why it matters, and a practical remedy. Separate definite violations from risks or context-dependent choices.
5. If the user requests an audit or report only, do not edit files. If the user asks to clean, refactor, or fix the code, make focused changes and preserve externally visible behavior unless the user asks for behavior changes. Do not add an abstraction just to satisfy a rule label; use the smallest change that makes the design clearer.
6. Keep a refactor small enough to review. Avoid unrelated formatting or architectural rewrites. Preserve public APIs, data formats, exception behavior, resource lifetime, and concurrency semantics unless changing them is part of the request.
7. Use the project's existing validation commands when the task calls for verification. Report exactly which checks ran and their result; never imply that unrun tests passed. Do not add tests solely to satisfy a style rule. Add or update a regression test when the requested change affects behavior and the task authorizes that work.
8. Finish with a rule trace: identify the IDs found, fixed, or deliberately applied, and distinguish these from rules that were not assessed. Do not claim that the whole book was checked: Chapters 1–14 are practical summaries, while Chapter 17's 66 listed heuristics are enumerated individually.

## Language adaptation

TypeScript is the primary example language, but most catalog entries apply across languages. Use the repository's formatter, compiler, linter, type system, and idioms as evidence; do not invent new style requirements. For TypeScript, consider types, discriminated unions, module boundaries, async behavior, and nullability as they fit the project. For C#/.NET, consider nullable reference types, exceptions, analyzers, access modifiers, records, and dependency injection as they fit the project. Adapt a rule only where an equivalent construct exists. Preserve idiomatic APIs such as C# `TryGetValue(..., out value)` when their contract is clear. Java-specific heuristics apply only to Java.

The three `TDD-*` items describe a test-driven development process. Assess them only when the task or repository is using TDD; do not classify ordinary code as noncompliant just because its original author did not follow that process.

## Finding and change records

Use these statuses:

- **Violated**: evidence shows the rule is not met.
- **Applied**: the refactor deliberately used this rule; cite the changed location or describe the decision.
- **Compliant**: checked in the stated scope and no violation was found.
- **Not applicable**: explain why the rule does not fit this code or language.
- **Not assessed**: outside the review scope or not enough evidence.

Severity reflects likely impact in this project, not the agent's stylistic preference. Use high for material correctness, operational, or maintenance risk; medium for a meaningful local cost; low for a contained clarity issue. Explain severity briefly when it is not obvious.

For each finding or refactor decision, report:

- Rule ID and short rule name
- Status and severity appropriate to the project's risk
- File and line (or the smallest stable location available)
- Concrete evidence and the impact
- A focused fix or, when refactoring, the change made

Use a compact table when it helps the reader compare findings: Rule | Status | Severity | Location | Evidence and impact | Fix or applied decision.

Do not report every catalog item as compliant unless each was actually checked. State the review scope, group duplicate symptoms under their root cause, and list all relevant IDs when one change addresses multiple rules.

## Skill validation

The local [evaluation cases](evals/cases.md) check whether this skill reports applicable rules, avoids known false positives, respects report-only requests, and preserves behavior during fixes. Run them when changing the skill itself; they are skill-quality checks, not extra rules for application code. The cases include a manual matrix for Codex, Claude Code, and GitHub Copilot because compatible files alone do not prove that each host discovers and follows the skill.

