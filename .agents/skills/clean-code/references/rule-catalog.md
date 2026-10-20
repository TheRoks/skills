# Clean Code Rule Catalog Index

This index is the entry point for the clean-code skill. Rule IDs are stable labels for findings and refactors. Skill-defined IDs summarize ideas from the book; only CH17 IDs preserve the book's own heuristic labels. The descriptions are original paraphrases, not quotations.

## Source

Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship* (2008). Chapter and page references below refer to the printed page numbers.

## Coverage map

| Book section | Printed pages | Catalog IDs | Coverage |
| --- | --- | --- | --- |
| Chapter 1: Clean Code | 1-15 | GEN-01 to GEN-05 | Concise synthesis of the chapter's general principles. |
| Chapter 2: Meaningful Names | 17-30 | NAME-01 to NAME-15 | Operational naming checklist. |
| Chapter 3: Functions | 31-52 | FUNC-01 to FUNC-16 | Operational function checklist. |
| Chapter 4: Comments | 53-74 | COMM-01 to COMM-08 | Operational comment checklist. |
| Chapter 5: Formatting | 75-92 | FORMAT-01 to FORMAT-08 | Operational formatting checklist. |
| Chapter 6: Objects and Data Structures | 93-102 | OBJECT-01 to OBJECT-06 | Concise abstraction and data-structure checklist. |
| Chapter 7: Error Handling | 103-112 | ERROR-01 to ERROR-08 | Operational error-handling checklist. |
| Chapter 8: Boundaries | 113-120 | BOUND-01 to BOUND-04 | Boundary and dependency checklist. |
| Chapter 9: Unit Tests | 121-133 | TEST-01 to TEST-09; TDD-01 to TDD-03 | Testing guidance plus the three TDD laws, marked as process-specific. |
| Chapter 10: Classes | 135-151 | CLASS-01 to CLASS-07 | Concise class and cohesion checklist. |
| Chapter 11: Systems | 153-169 | SYSTEM-01 to SYSTEM-09 | Concise construction and architecture checklist. |
| Chapter 12: Emergence | 171-176 | DESIGN-01 to DESIGN-04 | The four simple-design criteria. |
| Chapter 13: Concurrency | 177-191; Appendix A, 317-342 | CONC-01 to CONC-11 | Concise concurrency and testing checklist. |
| Chapter 14: Successive Refinement | 193-250 | REFINE-01 to REFINE-04 | Concise refinement checklist. |
| Chapters 15-16: Worked examples | 251-284 | No separate IDs | Examples inform interpretation; they are not converted into additional rules. |
| Chapter 17: Smells and Heuristics | 285-315 | CH17-C1 to CH17-T9 | All 66 listed heuristics are enumerated in the dedicated reference. |

The first 14 chapters are summarized as a practical checklist, not exhaustively restated line by line. The 66 Chapter 17 heuristic identifiers are all present. If a review needs a specific book claim not represented here, mark it not assessed and consult the source rather than inventing a rule.

## Load only relevant references

- Always read this index.
- For a focused review, read the relevant rule file and the corresponding category in `rules/chapter-17.md`.
- For a broad audit, read all three chapter-rule files and `rules/chapter-17.md`.
- Read `examples.md` when deciding whether a rule is applicable or could create a false positive.
- Use `../evals/cases.md` only to evaluate the skill's behavior, not as extra coding rules.

| Topic | Reference |
| --- | --- |
| Names, functions, comments, formatting | `rules/names-functions-comments.md` |
| Objects, errors, boundaries, classes, systems, design | `rules/structure-errors.md` |
| Tests, TDD, concurrency | `rules/testing-concurrency.md` |
| Every Chapter 17 heuristic | `rules/chapter-17.md` |
