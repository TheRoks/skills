# Clean Code Skill Evaluation Cases

Use these cases after changing the skill. Each case gives the request, an isolated input, expected rule IDs or exclusions, and observable evaluator checks. Evaluate the agent's actual response and edits; do not require exact wording or a fixed report layout.

## Case 1: Report-only on a Boolean workflow selector

**Request:** “Review this function against the Clean Code skill. Report findings only; do not edit files.”

```ts
async function publishReport(report: Report, preview: boolean): Promise<void> {
  const document = render(report);
  if (preview) {
    await previewStore.show(document);
    return;
  }
  await reportRepository.save(document);
  await notificationService.send(document);
}
```

**Expected:** identify the selector as a concrete concern and consider `FUNC-09`, `CH17-F3`, and `CH17-G15`. The response must state that no files were changed. It should avoid claiming the function definitely violates unrelated rules without evidence.

**Check:** compare the workspace before and after; no file changes. The finding should explain the separate workflows/effects and give a focused remedy.

## Case 2: Do not flag idiomatic C# `out`

**Request:** “Review this lookup method using the Clean Code skill.”

```csharp
Customer? FindCustomer(CustomerId id)
{
    return customers.TryGetValue(id, out var customer) ? customer : null;
}
```

**Expected:** do not report `FUNC-08` or `CH17-F2` solely because `TryGetValue` uses `out`. Do not report `ERROR-07` just because a clearly nullable return represents “not found.” The agent may mention the established .NET contract and look for caller evidence before recommending a change.

**Check:** no unsupported style finding; any recommendation is tied to actual ambiguity in the provided contract.

## Case 3: Stale and commented-out implementation

**Request:** “Clean up these comments and report the rule IDs you apply.”

```ts
// This request is sent only once; failures are returned immediately.
for (let attempt = 0; attempt < 3; attempt += 1) {
  await sendRequest();
}

// const response = await sendRequest();
// return response.body;
```

**Expected:** correct or remove the stale comment and remove the commented-out implementation. Relevant IDs include `COMM-03`, `COMM-06`, `CH17-C2`, `CH17-C5`, and `CH17-G9`. Keep any comment that carries necessary non-obvious context; do not delete unrelated documentation.

**Check:** code behavior is unchanged; the response identifies the applied IDs and changed locations.

## Case 4: Avoid obvious false positives

**Request:** “Audit this code for clean-code issues.”

```ts
function isReady(user: User | null): boolean {
  return user !== null && user.isActive;
}
```

```csharp
Customer? FindCustomer(CustomerId id)
{
    return customers.TryGetValue(id, out var customer) ? customer : null;
}
```

**Expected:** do not flag the TypeScript helper merely for being short (`FUNC-01`). Do not flag the C# nullable result without evidence that its absence contract is ambiguous (`ERROR-07`, `ERROR-08`).

**Check:** no finding based only on length, nullability, or language syntax.

## Case 5: Behavior-preserving refactor of a selector

**Request:** “Refactor this function to make its two operations explicit. Preserve behavior and report the rules applied.”

```ts
async function finishOrder(order: Order, preview: boolean): Promise<void> {
  const receipt = buildReceipt(order);
  if (preview) {
    await previewStore.show(receipt);
    return;
  }
  await orderRepository.save(order);
  await emailer.sendReceipt(receipt);
}
```

**Expected:** separate the preview path from the completion path, share `buildReceipt` where useful, and preserve the effects and sequencing of each path. Report `FUNC-09` and applicable Chapter 17 selector IDs such as `CH17-F3`/`CH17-G15` as applied. Do not claim tests ran unless they did.

**Check:** preview still only shows the receipt; completion still saves before sending email; no unrelated API or formatting rewrite.

## Case 6: Java-only heuristic boundary

**Request:** “Review these imports using the Clean Code skill.”

```ts
import { readFile, writeFile } from "node:fs/promises";
```

**Expected:** `CH17-J1` is not applicable because this is TypeScript. Do not translate Java wildcard-import advice into a TypeScript style rule; follow the project's TypeScript conventions.

**Check:** no finding against the TypeScript import form based on `CH17-J1`.

## Case 7: A context-dependent Boolean option

**Request:** “Review this API for Clean Code issues. Do not edit it.”

```ts
function formatTimestamp(date: Date, useUtc: boolean): string {
  return useUtc ? date.toISOString() : date.toLocaleString();
}
```

**Expected:** consider `FUNC-09` and `CH17-F3` only as context-dependent candidates. The snippet alone does not establish whether these are confusingly different operations or a clear option on one formatting operation. Inspect call sites and the public API convention before calling it a violation. Do not refactor it automatically; if context is unavailable, state the limitation and avoid claiming a definite defect.

**Check:** the response distinguishes evidence from uncertainty and makes no edits.

## Cross-agent runtime matrix

Run the same cases with each host after installing the skill. Keep a record of the product/version, date, invocation method, and pass/fail notes. A compatible folder layout or a successful CLI install does not prove that the agent discovered and followed the skill.

| Host | Discovery and invocation | Minimum cases |
| --- | --- | --- |
| Codex | Confirm the installed skill is offered or available, then invoke it explicitly for the case. | 1, 2, 5 |
| Claude Code | Confirm the project skill is discovered, then invoke the skill by its installed name. | 1, 3, 5, 7 |
| GitHub Copilot | Confirm the agent can see the installed skill in the selected Copilot surface, then invoke it explicitly. | 1, 2, 6, 7 |

For every case, record whether the expected IDs were used appropriately, report-only requests avoided edits, fixes preserved the stated behavior, and the agent accurately described validation. Do not mark a host verified unless its live result was observed.
