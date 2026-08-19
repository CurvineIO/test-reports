#!/usr/bin/env python3
"""Remove report posts and static attachments older than 30 calendar days."""

from __future__ import annotations

import datetime as dt
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "reports"
STATIC = ROOT / "static" / "files"
KEEP_DAYS = 30
DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})")


def cutoff_date() -> dt.date:
    return dt.date.today() - dt.timedelta(days=KEEP_DAYS)


def date_from_name(path: Path) -> dt.date | None:
    match = DATE_RE.match(path.name)
    if not match:
        return None
    return dt.date.fromisoformat(match.group(1))


def main() -> int:
    cutoff = cutoff_date()
    removed = []

    for path in sorted(CONTENT.glob("*.md")):
        if path.name.startswith("_"):
            continue
        report_date = date_from_name(path)
        if report_date is None or report_date >= cutoff:
            continue
        path.unlink()
        removed.append(path)

        static_dir = STATIC / report_date.isoformat()
        if static_dir.is_dir():
            shutil.rmtree(static_dir)
            removed.append(static_dir)

    if not removed:
        print(f"Nothing older than {cutoff.isoformat()}")
        return 0

    print(f"Removed {len(removed)} item(s) older than {cutoff.isoformat()}:")
    for item in removed:
        print(f"  {item.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
