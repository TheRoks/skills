# Rule Reference

These skill-defined rules summarize the cited book sections. They are review criteria, not automatic refactoring commands. See the rule catalog index for source coverage and loading guidance.

## Tests (Chapter 9)

- **TEST-01 — Keep tests readable and maintained.** Test code is production code for the development process.
- **TEST-02 — Test behavior, not incidental implementation.** A refactor should not require rewriting tests that only mirror private structure.
- **TEST-03 — Give tests a clear domain vocabulary.** Small helpers may express setup and assertions in terms of the behavior under test.
- **TEST-04 — Keep each test focused on one concept.** Assertions may be grouped when they prove the same behavior.
- **TEST-05 — Keep the suite dependable.** Tests should be fast, independent, repeatable, self-checking, and written in time to guide the change.
- **TEST-06 — Cover important behavior and failure paths.** Do not mistake a passing test count for adequate behavioral coverage.
- **TEST-07 — Exercise boundaries and regressions.** Include edge cases and cases near previously fixed defects when relevant.
- **TEST-08 — Use coverage evidence thoughtfully.** Coverage tools can reveal untested paths, but a percentage alone does not prove correctness.
- **TEST-09 — Resolve ignored tests.** An ignored or skipped test should have an explained, intentional status rather than silently hiding an unclear requirement.
- **TDD-01 — Write a failing test before production code.** In a TDD workflow, demonstrate the missing behavior with a failing test before implementing it.
- **TDD-02 — Keep the test step minimal.** Add only enough test code to produce a meaningful failure; a compile failure may establish that the test is not yet satisfied.
- **TDD-03 — Keep the implementation step minimal.** Add only enough production code to pass the current failing test, then refine while keeping the suite passing.

## Concurrency (Chapter 13 and Appendix A)

- **CONC-01 — Use concurrency for a real requirement.** Account for its cost in complexity and failure modes.
- **CONC-02 — Separate concurrency concerns.** Keep synchronization and task coordination distinct from domain work where practical.
- **CONC-03 — Limit shared mutable state.** Prefer immutable data, ownership, or copies when they reduce races.
- **CONC-04 — Keep concurrent tasks independent.** Minimize coordination and shared-state dependencies.
- **CONC-05 — Understand the runtime and library model.** Use the actual execution semantics and thread-safe primitives correctly.
- **CONC-06 — Keep critical sections small.** Protect only the work that must be atomic and avoid hidden lock dependencies.
- **CONC-07 — Make coordination protocols explicit.** Model producer/consumer, reader/writer, cancellation, and related relationships clearly where they occur.
- **CONC-08 — Design shutdown deliberately.** Ensure tasks can stop and resources can close without hangs or lost work.
- **CONC-09 — Verify concurrent behavior under varied schedules.** Use tests, stress, instrumentation, and supported platforms where available.
- **CONC-10 — Stabilize sequential behavior first.** Establish correct nonconcurrent behavior before adding concurrency when the design permits.
- **CONC-11 — Make concurrency tunable only where useful.** Expose configuration for meaningful runtime constraints without making every detail a knob.
