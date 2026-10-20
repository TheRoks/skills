# Rule Reference

These skill-defined rules summarize the cited book sections. They are review criteria, not automatic refactoring commands. See the rule catalog index for source coverage and loading guidance.

## General principles

- **GEN-01 — Optimize for readers.** Prefer code whose purpose and flow can be understood without reconstructing hidden assumptions.
- **GEN-02 — Improve incrementally.** Leave touched code easier to understand than before; avoid postponing all cleanup to a hypothetical rewrite.
- **GEN-03 — Preserve intended behavior.** Treat a refactor as behavior-preserving unless the request explicitly changes behavior.
- **GEN-04 — Refine in small steps.** Make changes in reviewable increments and use available checks to detect accidental behavior changes.
- **GEN-05 — Prefer clear simplicity.** Reduce unnecessary code and concepts without compressing code into cryptic shorthand or removing useful boundaries.

## Names (Chapter 2)

- **NAME-01 — Reveal intent.** A name should communicate the value's role, purpose, or behavior.
- **NAME-02 — Avoid misleading names.** Do not imply a type, scope, guarantee, or behavior that the code does not provide.
- **NAME-03 — Distinguish meanings.** Different names should represent genuinely different concepts; avoid arbitrary suffixes or near-synonyms.
- **NAME-04 — Use pronounceable names.** Prefer names collaborators can comfortably discuss.
- **NAME-05 — Make important names searchable.** Give frequently used concepts and nontrivial constants stable, distinctive names.
- **NAME-06 — Avoid obsolete encodings.** Do not embed types, visibility, or other redundant metadata in names when the language and context already express it.
- **NAME-07 — Avoid mental translation.** Do not make readers decode arbitrary abbreviations or map letters to concepts.
- **NAME-08 — Name types as concepts.** Classes and similar types should usually read as nouns or noun phrases.
- **NAME-09 — Name operations as actions.** Methods and functions should normally use verbs or verb phrases.
- **NAME-10 — Prefer direct wording.** Avoid cute names, jokes, or obscure cultural references in production identifiers.
- **NAME-11 — Use one term for one concept.** Keep terminology consistent across related APIs and modules.
- **NAME-12 — Do not reuse a term for a different operation.** Avoid puns where the same word suggests incompatible behavior.
- **NAME-13 — Choose vocabulary for the audience.** Use implementation vocabulary for technical concepts and domain vocabulary for business concepts.
- **NAME-14 — Supply useful context.** Add a containing type or scope when it disambiguates a short name.
- **NAME-15 — Avoid gratuitous context.** Do not repeat a module or product name in every identifier when the scope already supplies it.

## Functions (Chapter 3)

- **FUNC-01 — Keep functions focused and small.** Split code when a function's size or branches obscure its purpose; there is no universal line-count threshold.
- **FUNC-02 — Do one coherent task.** A function should have one understandable responsibility and one reason to change.
- **FUNC-03 — Keep one abstraction level per function.** Separate high-level intent from low-level implementation details.
- **FUNC-04 — Make reading order top-down.** Arrange related helpers so the high-level flow leads naturally into details.
- **FUNC-05 — Limit nesting.** Use simple control flow and extract meaningful branches when nested blocks make the main path hard to follow.
- **FUNC-06 — Use descriptive function names.** A caller should be able to predict the function's effect from its name and signature.
- **FUNC-07 — Minimize arguments.** Reduce parameters where practical; group them only when they form a real concept.
- **FUNC-08 — Avoid output parameters.** Prefer returning a value or updating an explicitly owned object over mutating an argument in a surprising way.
- **FUNC-09 — Avoid boolean mode flags.** Split clearly different operations or model the variants explicitly when that makes calls easier to understand.
- **FUNC-10 — Keep argument lists understandable.** Avoid long positional lists; use a cohesive parameter object or named options when that clarifies meaning.
- **FUNC-11 — Avoid surprising side effects.** A function should not silently mutate unrelated state or perform hidden work.
- **FUNC-12 — Separate commands from queries.** An operation should either change state or return information, unless combining them is clear and intentional.
- **FUNC-13 — Avoid duplicated logic.** Extract shared behavior when one definition can remain clearer than the repeated versions.
- **FUNC-14 — Isolate exceptional flow.** Keep error handling from obscuring the ordinary path; use the language's exception or result idiom consistently.
- **FUNC-15 — Keep error handling focused.** Handle an error as a distinct responsibility and preserve enough context for the caller.
- **FUNC-16 — Use structured control flow.** Prefer language constructs with clear entry, exit, and ownership over unstructured jumps or tangled branches.

## Comments (Chapter 4)

- **COMM-01 — Let code explain what it does.** Improve unclear names or structure before adding commentary.
- **COMM-02 — Comment on necessary context.** Retain comments that explain intent, constraints, consequences, or non-obvious external facts that code cannot express well.
- **COMM-03 — Keep comments accurate and local.** A comment must match current behavior and sit near the code it explains.
- **COMM-04 — Remove noise and duplication.** Avoid comments that merely narrate obvious code, repeat signatures, or add boilerplate without a real reader benefit.
- **COMM-05 — Do not use comments to excuse poor code.** Replace explanatory comments with a clearer name, function, or structure when that can express the same idea.
- **COMM-06 — Remove commented-out implementation.** Use version control for history instead of leaving dead source in place.
- **COMM-07 — Keep TODOs actionable.** Include a concrete task and useful context; remove completed or abandoned notes.
- **COMM-08 — Use public API documentation deliberately.** Document public contracts where consumers need them; do not add ceremonial docs to private implementation.

## Formatting (Chapter 5)

- **FORMAT-01 — Follow the established formatter and team style.** Consistency is more valuable than imposing a new personal convention.
- **FORMAT-02 — Group concepts vertically.** Use whitespace and proximity to show which declarations belong together.
- **FORMAT-03 — Separate distinct concepts.** Use blank lines and clear structure to mark meaningful transitions.
- **FORMAT-04 — Keep related declarations close.** Place collaborators and their helpers near enough that readers can follow the connection.
- **FORMAT-05 — Order from high-level to detail.** Where practical, present the primary story before implementation details.
- **FORMAT-06 — Keep lines readable.** Avoid horizontal sprawl; follow the repository's formatter or line-width convention.
- **FORMAT-07 — Use indentation to show structure.** Nesting should be visually clear and reflect the actual control flow.
- **FORMAT-08 — Avoid visual tricks.** Do not add artificial alignment or empty scopes that obscure rather than clarify.
