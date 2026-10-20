#!/usr/bin/env python3
"""Check stable catalog IDs, local Markdown links, and cross-agent alias wiring."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlsplit


SKILL_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_ROOT.parents[2]

EXPECTED_RANGES = {
    "GEN": (1, 5),
    "NAME": (1, 15),
    "FUNC": (1, 16),
    "COMM": (1, 8),
    "FORMAT": (1, 8),
    "OBJECT": (1, 6),
    "ERROR": (1, 8),
    "BOUND": (1, 4),
    "TEST": (1, 9),
    "TDD": (1, 3),
    "CLASS": (1, 7),
    "SYSTEM": (1, 9),
    "DESIGN": (1, 4),
    "CONC": (1, 11),
    "REFINE": (1, 4),
}
EXPECTED_CH17 = {
    "C": 5,
    "E": 2,
    "F": 4,
    "G": 36,
    "J": 3,
    "N": 7,
    "T": 9,
}
RULE_LINE = re.compile(r"^\s*-\s+\*\*([A-Z]+-\d{2}|CH17-[A-Z]\d+) —", re.MULTILINE)
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_frontmatter() -> None:
    content = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", content, re.DOTALL)
    if not match:
        fail("SKILL.md must start with YAML frontmatter")
    frontmatter = match.group(1)
    if not re.search(r"^name:\s*clean-code\s*$", frontmatter, re.MULTILINE):
        fail("frontmatter must define name: clean-code")
    if not re.search(r"^description:\s*\S.*$", frontmatter, re.MULTILINE):
        fail("frontmatter must define a non-empty description")


def validate_links() -> None:
    for markdown in SKILL_ROOT.rglob("*.md"):
        content = markdown.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(content):
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("#"):
                continue
            link_path = parsed.path
            if not link_path:
                continue
            resolved = (markdown.parent / link_path).resolve()
            if not resolved.exists():
                fail(f"broken link in {markdown.relative_to(SKILL_ROOT)}: {target}")


def collect_rule_ids() -> set[str]:
    found: list[str] = []
    for markdown in (SKILL_ROOT / "references" / "rules").glob("*.md"):
        found.extend(RULE_LINE.findall(markdown.read_text(encoding="utf-8")))
    duplicates = sorted({rule_id for rule_id in found if found.count(rule_id) > 1})
    if duplicates:
        fail(f"duplicate rule IDs: {', '.join(duplicates)}")
    return set(found)


def expected_rule_ids() -> set[str]:
    expected = {
        f"{prefix}-{number:02d}"
        for prefix, (first, last) in EXPECTED_RANGES.items()
        for number in range(first, last + 1)
    }
    expected.update(
        f"CH17-{category}{number}"
        for category, last in EXPECTED_CH17.items()
        for number in range(1, last + 1)
    )
    return expected


def validate_rule_ids() -> set[str]:
    actual = collect_rule_ids()
    expected = expected_rule_ids()
    missing = sorted(expected - actual)
    unexpected = sorted(actual - expected)
    if missing or unexpected:
        details = []
        if missing:
            details.append(f"missing: {', '.join(missing)}")
        if unexpected:
            details.append(f"unexpected: {', '.join(unexpected)}")
        fail("catalog ID mismatch (" + "; ".join(details) + ")")

    eval_file = SKILL_ROOT / "evals" / "cases.md"
    if not eval_file.exists():
        fail("missing evals/cases.md")
    eval_text = eval_file.read_text(encoding="utf-8")
    eval_ids = set(re.findall(r"\b(?:[A-Z]+-\d{2}|CH17-[A-Z]\d+)\b", eval_text))
    unknown_eval_ids = sorted(eval_ids - actual)
    if unknown_eval_ids:
        fail(f"eval references unknown rule IDs: {', '.join(unknown_eval_ids)}")
    return actual


def validate_claude_alias() -> None:
    alias = REPO_ROOT / ".claude" / "skills" / "clean-code"
    if not alias.is_symlink():
        fail(".claude/skills/clean-code must remain a symlink to the canonical skill")
    if alias.resolve() != SKILL_ROOT.resolve():
        fail(".claude/skills/clean-code does not resolve to .agents/skills/clean-code")


def main() -> None:
    validate_frontmatter()
    validate_links()
    rule_ids = validate_rule_ids()
    validate_claude_alias()
    print(f"PASS: frontmatter, Markdown links, {len(rule_ids)} unique catalog IDs, eval references, and Claude alias")


if __name__ == "__main__":
    main()
