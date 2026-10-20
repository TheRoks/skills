# Rule Reference

These skill-defined rules summarize the cited book sections. They are review criteria, not automatic refactoring commands. See the rule catalog index for source coverage and loading guidance.

## Objects and data structures (Chapter 6)

- **OBJECT-01 — Expose behavior or data intentionally.** Use an object abstraction to protect invariants; use a data structure when callers genuinely need the data.
- **OBJECT-02 — Hide implementation details.** Avoid leaking internal representation when a small behavior-focused API can preserve freedom to change it.
- **OBJECT-03 — Keep collaborators local.** Limit navigation through object graphs when it exposes internal structure or creates brittle coupling.
- **OBJECT-04 — Avoid train-wreck chains.** Replace long chains of unrelated getters with a meaningful operation or clearer ownership boundary when appropriate.
- **OBJECT-05 — Avoid unclear hybrids.** Do not mix mutable public data and behavior-heavy abstractions without a clear reason.
- **OBJECT-06 — Keep data transfer types honest.** Use transport records for carrying data and domain objects for enforcing domain behavior; avoid mixing their roles accidentally.

## Error handling (Chapter 7)

- **ERROR-01 — Use explicit failure mechanisms.** Prefer exceptions or the project's result type over ambiguous magic return codes.
- **ERROR-02 — Put resource cleanup on every path.** Use finally, disposal, defer, or equivalent scoped cleanup.
- **ERROR-03 — Catch at a useful boundary.** Handle an error where the program can take a meaningful action; do not swallow it.
- **ERROR-04 — Preserve error context.** Include operation, input, or boundary context that helps diagnose or recover.
- **ERROR-05 — Shape errors for callers.** Choose error types and categories around what callers can handle, not implementation trivia.
- **ERROR-06 — Keep normal flow obvious.** Avoid using exceptions for ordinary alternatives when a clear domain model exists.
- **ERROR-07 — Avoid null as an ambiguous signal.** Prefer explicit optional, result, or domain-specific absence representations where available.
- **ERROR-08 — Avoid passing null to mean many things.** Make required inputs and optional cases explicit at API boundaries.

## Boundaries and external dependencies (Chapter 8)

- **BOUND-01 — Isolate third-party APIs.** Keep vendor types and assumptions behind a small adapter where they would otherwise spread.
- **BOUND-02 — Learn unfamiliar APIs with focused experiments.** Verify assumptions against the real dependency rather than guessing at its behavior.
- **BOUND-03 — Keep application logic independent of replaceable details.** Depend on an owned interface or boundary when that makes change and testing clearer.
- **BOUND-04 — Test the boundary contract.** Check important behavior where external data or APIs enter the system.

## Classes and modules (Chapter 10)

- **CLASS-01 — Keep classes cohesive and focused.** A class should have a small, intelligible responsibility.
- **CLASS-02 — Apply single responsibility.** Group behavior that changes for the same reason; split unrelated responsibilities.
- **CLASS-03 — Keep state and behavior cohesive.** Members used together should belong together where that makes ownership clearer.
- **CLASS-04 — Split when cohesion demands it.** Extracting a focused type is useful when it creates a real boundary, not merely to lower a line count.
- **CLASS-05 — Encapsulate mutable state.** Limit access to data needed to preserve invariants.
- **CLASS-06 — Isolate likely change.** Depend on stable abstractions where change pressure justifies them.
- **CLASS-07 — Keep module dependencies understandable.** Avoid broad coupling between components that should change independently.

## Systems and architecture (Chapter 11)

- **SYSTEM-01 — Separate construction from use.** Keep object creation and application behavior from becoming inseparable.
- **SYSTEM-02 — Make composition visible.** Put startup and dependency wiring in an understandable composition boundary.
- **SYSTEM-03 — Use factories for meaningful construction choices.** Introduce a factory when callers need control over creation without owning concrete details.
- **SYSTEM-04 — Use dependency injection to reduce hard-wiring.** Keep it proportional to the architecture rather than adding a container for its own sake.
- **SYSTEM-05 — Separate cross-cutting concerns.** Avoid spreading infrastructure, logging, security, or transaction mechanics through domain behavior unnecessarily.
- **SYSTEM-06 — Test architecture through useful seams.** Keep components replaceable in tests where that matches real dependency boundaries.
- **SYSTEM-07 — Delay optimization until evidence supports it.** Avoid speculative complexity; measure real constraints before tuning.
- **SYSTEM-08 — Adopt standards when they add demonstrable value.** Do not add abstractions or frameworks solely because they are fashionable.
- **SYSTEM-09 — Use domain-specific language where it clarifies the model.** Prefer a small expressive vocabulary over incidental low-level detail.

## Emergent design (Chapter 12)

- **DESIGN-01 — Keep the relevant tests passing.** A design is not clean if it breaks required behavior.
- **DESIGN-02 — Remove duplication.** Keep one authoritative implementation for repeated knowledge where possible.
- **DESIGN-03 — Make intent expressive.** Use names, structure, and focused abstractions that let a reader understand the code.
- **DESIGN-04 — Minimize unnecessary parts.** Avoid speculative classes, methods, and layers while retaining useful separation.

## Successive refinement (Chapter 14)

- **REFINE-01 — Expect the first draft to need cleanup.** Refine names, structure, and responsibilities instead of treating initial code as final.
- **REFINE-02 — Refine without losing behavior.** Make small steps and use available checks to catch accidental changes.
- **REFINE-03 — Simplify after understanding.** Remove temporary scaffolding and duplication once the solution is clear.
- **REFINE-04 — Keep the final code readable.** The implementation should communicate the result, not preserve the history of how it was discovered.
