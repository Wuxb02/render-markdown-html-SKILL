"""Markdown to HTML helper."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict


def md_to_html(source: str, output_path: str | None = None) -> Dict[str, Any]:
    """Prepare Markdown content for HTML rendering."""
    source_path = Path(source)
    if source_path.exists():
        markdown_text = source_path.read_text(encoding="utf-8")
        source_name = source_path.name
    else:
        markdown_text = source
        source_name = "inline.md"

    return {
        "success": True,
        "source_name": source_name,
        "output_path": output_path,
        "markdown": markdown_text,
        "html": None,
        "note": "Render the HTML in the surrounding workflow or with a future template layer.",
    }
