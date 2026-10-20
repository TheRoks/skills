# Chapter 17 Heuristics

These entries preserve the book's Chapter 17 category and item identifiers for traceability. The descriptions are concise paraphrases. Apply only when relevant to the language and repository.

### Comments

- **CH17-C1 — Relevant comment content.** Keep commentary focused on information a reader needs at this code location.
- **CH17-C2 — Current comments.** Remove or correct commentary that no longer matches behavior.
- **CH17-C3 — Nonredundant comments.** Remove commentary that only repeats what the code already says.
- **CH17-C4 — Clear comments.** Make necessary comments accurate, specific, and easy to understand.
- **CH17-C5 — No commented-out implementation.** Remove inactive code from the source and rely on version history.

### Environment

- **CH17-E1 — Simple build path.** Keep the documented build operation straightforward and repeatable.
- **CH17-E2 — Simple test path.** Keep the documented test operation straightforward and repeatable.

### Functions

- **CH17-F1 — Manageable argument count.** Reduce excessive parameters or make their meaning clearer.
- **CH17-F2 — No surprising output arguments.** Return results or make mutation explicit in the owning abstraction.
- **CH17-F3 — Avoid selector flags.** Do not make a Boolean parameter secretly choose different operations.
- **CH17-F4 — No dead functions.** Remove unused functions or make their intended use real and clear.

### General

- **CH17-G1 — One source language at a time.** Avoid mixing unrelated languages or embedded mini-languages in one source file without a clear need.
- **CH17-G2 — Complete obvious behavior.** Do not leave expected, plainly implied functionality unimplemented.
- **CH17-G3 — Correct boundaries.** Handle limits, empty values, and off-by-one cases correctly.
- **CH17-G4 — Preserve safeguards.** Do not bypass protections, checks, or safe fallbacks without a justified replacement.
- **CH17-G5 — Remove duplication.** Consolidate repeated logic when that improves clarity and prevents drift.
- **CH17-G6 — Match abstraction level.** Keep code in the layer where its concepts belong.
- **CH17-G7 — Keep base abstractions independent of derivatives.** Higher-level types should not need to know concrete subclasses that depend on them.
- **CH17-G8 — Limit exposed information.** Keep APIs and modules as small as their callers need.
- **CH17-G9 — Remove dead code.** Delete unreachable, unused, or obsolete implementation.
- **CH17-G10 — Keep related code together.** Avoid arbitrary gaps between declarations that collaborate.
- **CH17-G11 — Be consistent within a codebase.** Follow one established convention unless a reason justifies a change.
- **CH17-G12 — Remove clutter.** Delete unused imports, empty scaffolding, redundant wrappers, and other distractions.
- **CH17-G13 — Avoid artificial coupling.** Do not make independent concepts depend on one another without a real need.
- **CH17-G14 — Keep behavior near its data.** Move logic toward the state or concept it primarily uses when that clarifies ownership.
- **CH17-G15 — Avoid selector parameters.** Prefer distinct operations or polymorphic behavior when a parameter only selects a mode.
- **CH17-G16 — Make intent visible.** Write code so its purpose is not hidden behind clever syntax or unnecessary indirection.
- **CH17-G17 — Put responsibility in the right place.** Keep decisions with the component that owns the relevant knowledge.
- **CH17-G18 — Use static behavior deliberately.** Avoid static when instance state or polymorphism is needed; use it when behavior is truly independent.
- **CH17-G19 — Name important intermediate values.** Introduce explanatory variables when they make a condition or calculation easier to read.
- **CH17-G20 — Make function names predictive.** A name should let callers anticipate the operation and its effects.
- **CH17-G21 — Understand the algorithm.** Verify that the implementation is correct and clear before polishing its presentation.
- **CH17-G22 — Encode logical dependencies.** Make required ordering, inputs, and relationships explicit in the structure or types.
- **CH17-G23 — Use polymorphism for stable behavioral variants.** Replace large type-based branches when subtype behavior is a natural fit.
- **CH17-G24 — Follow relevant conventions.** Use the language and repository's normal practices.
- **CH17-G25 — Name meaningful constants.** Replace unexplained literal values with concepts that communicate their purpose.
- **CH17-G26 — Be precise.** Choose types, conditions, and claims that match the actual range and behavior.
- **CH17-G27 — Prefer explicit structure to fragile convention.** Encode important relationships in code where relying on an implicit pattern is brittle.
- **CH17-G28 — Encapsulate complex conditions.** Name or model a condition when its meaning deserves a reusable concept.
- **CH17-G29 — Prefer positive conditions when clearer.** Avoid negated branches that make the main path difficult to follow.
- **CH17-G30 — Keep each function focused.** Split unrelated work into understandable operations.
- **CH17-G31 — Show required sequencing.** Make order-dependent operations explicit rather than relying on hidden timing assumptions.
- **CH17-G32 — Avoid arbitrary design choices.** Give abstractions, names, and structure a reason that can be understood.
- **CH17-G33 — Centralize boundary handling.** Keep edge-case logic consistent and close to the boundary it protects.
- **CH17-G34 — Keep one abstraction level in a function.** Move detailed work to helpers rather than mixing it with the main story.
- **CH17-G35 — Keep configuration visible.** Put changeable configuration where operators and maintainers can find and understand it.
- **CH17-G36 — Avoid transitive navigation.** Do not force callers to traverse several collaborators to reach data they should not own.

### Java-specific heuristics

- **CH17-J1 — Keep import lists concise.** In Java, when several classes come from one package, a wildcard import can reduce a long import list. Respect repository conventions and use explicit imports when needed to resolve ambiguity. Do not transfer this Java-specific rule to other languages.
- **CH17-J2 — Do not inherit constants accidentally.** Put constants in an intentional owner rather than exposing them through an unrelated base type.
- **CH17-J3 — Choose enum-like representations deliberately.** Use the language's appropriate named finite-value construct rather than an unexplained collection of constants.

### Names

- **CH17-N1 — Descriptive names.** Make names convey their role and intent.
- **CH17-N2 — Appropriate abstraction.** Choose names at the level of detail visible to their callers.
- **CH17-N3 — Standard terminology.** Prefer established names for recognized patterns and concepts.
- **CH17-N4 — Unambiguous names.** Make the scope and meaning clear enough to distinguish likely interpretations.
- **CH17-N5 — Scope-aware length.** Use enough detail for long-lived or wide-scope names; keep tiny local names proportionate.
- **CH17-N6 — Avoid encodings.** Do not make readers decode type or scope prefixes unnecessarily.
- **CH17-N7 — Disclose side effects.** Do not name an operation as a pure lookup if it also changes state.

### Tests

- **CH17-T1 — Adequate behavioral tests.** Cover the meaningful behavior and risks in scope.
- **CH17-T2 — Use coverage evidence when available.** A coverage tool can expose gaps, but it cannot establish correctness alone.
- **CH17-T3 — Do not dismiss small cases automatically.** Test simple behavior when it is part of the contract or guards a likely regression.
- **CH17-T4 — Explain skipped tests.** Resolve ambiguity behind disabled tests or record why the skip is intentional.
- **CH17-T5 — Test boundaries.** Exercise empty, minimum, maximum, and transition cases that matter.
- **CH17-T6 — Test near known defects.** Add focused regression coverage around fragile paths when authorized and appropriate.
- **CH17-T7 — Investigate failure patterns.** Related failures may point to one shared defect or assumption.
- **CH17-T8 — Read coverage patterns.** Missing areas can reveal untested behavior; inspect what matters rather than chasing a number.
- **CH17-T9 — Keep tests fast enough to use.** Slow tests discourage frequent feedback; optimize only where delay is real.
