# Applicability Examples

These small examples show how to apply rules without treating them as mechanical lint checks. The code is illustrative; local contracts and repository conventions still decide.

## A Boolean that selects different operations

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

The flag chooses two meaningfully different workflows and side effects. In a review, consider `FUNC-09`, `CH17-F3`, and `CH17-G15`. In a refactor, separate the preview and publish operations if callers benefit from explicit intent; keep shared rendering in one place and preserve the order and effects of each branch. A Boolean that merely enables an optional, same-operation detail is not automatically a violation.

## An idiomatic C# output parameter

```csharp
if (customers.TryGetValue(customerId, out Customer? customer))
{
    return customer;
}

return null;
```

Do not report `FUNC-08` or `CH17-F2` just because the API has an `out` parameter. `TryGetValue` is a well-known .NET contract: the Boolean says whether the lookup succeeded, and the output value is explicit at the call site. Consider changing it only if this project's API contract or usage is actually confusing.

## A meaningful nullable result

```csharp
Customer? FindCustomer(CustomerId id)
{
    return customers.TryGetValue(id, out var customer) ? customer : null;
}
```

An explicit nullable return can be the natural contract for “not found.” Do not report `ERROR-07` or `ERROR-08` without evidence that callers cannot distinguish absence from another outcome or that null is being overloaded to mean several things. Prefer the repository's established optional/result pattern when one exists.

## A short, clear helper

```ts
function isReady(user: User | null): boolean {
  return user !== null && user.isActive;
}
```

Its short length is not a defect. Do not flag `FUNC-01` merely because a function is small or could be expanded. Report a function-size issue only when its responsibilities, branches, or abstraction levels make it hard to understand.

## A language-specific import heuristic

`CH17-J1` concerns Java imports. It must not be reported for TypeScript or C# imports. Even in Java, repository formatter or explicit-import conventions are relevant evidence; do not change imports against a deliberate local policy just to apply the heuristic.
