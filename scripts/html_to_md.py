"""HTML to Markdown helper."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict


def html_to_md(source: str, output_path: str | None = None) -> Dict[str, Any]:
    """Prepare HTML content for Markdown recovery."""
    source_path = Path(source)
    if source_path.exists():
        html_text = source_path.read_text(encoding="utf-8")
        source_name = source_path.name
    else:
        html_text = source
        source_name = "inline.html"

    return {
        "success": True,
        "source_name": source_name,
        "output_path": output_path,
        "html": html_text,
        "markdown": None,
        "note": "Recover Markdown in the surrounding workflow or with a future parser layer.",
    }
