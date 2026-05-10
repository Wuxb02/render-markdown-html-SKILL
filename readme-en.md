# render-markdown-html

English | [中文](./readme.md)

> A bidirectional Markdown ↔ HTML skill for Claude Code — high-quality document rendering with write-back support.

## Features

| Capability | Description |
| --- | --- |
| **Markdown → HTML** | Render Markdown into a clean, readable single-file HTML document |
| **Editable parameters** | Expose colors, spacing, layout as visual controls |
| **Write Back** | Provide an explicit "write-back" button for every configurable item |
| **HTML → Markdown** | Recover semantic structure from HTML into clean Markdown source |
| **Language consistency** | Match the source language — Chinese UI labels for Chinese documents |

## When to use

- User needs a `.md` file rendered as a browsable HTML page
- User wants to tune theme colors, spacing, or density directly in HTML
- User wants to recover Markdown from an HTML document
- User needs a human-friendly long-form document view

## Quick start

```bash
# Render Markdown as HTML
/render-markdown-html docs/summary.md

# Recover Markdown from HTML
/html-to-md report.html
```

## Project structure

```text
render-markdown-html/
├── SKILL.md                        # Skill definition and rules
├── scripts/
│   ├── md_to_html.py               # Markdown input parser
│   └── html_to_md.py               # HTML input parser
├── references/
│   ├── template-library.md         # Visual and interaction patterns
│   └── examples/
│       ├── 01-document-review.html       # Long-form document review layout
│       ├── 02-configurable-card.html     # Configurable card with controls
│       └── 03-editorial-split-view.html  # Editor split-view layout
├── readme.md                       # 中文说明
└── readme-en.md                    # English README (this file)
```

## Design style

A calm editorial interface — not a flashy landing page:

- Low-saturation palette — ivory / slate / clay / olive
- Thin borders, restrained shadows, compact radii
- Serif headings with sans-serif body text
- Side navigation + sticky toolbar + split preview
- Clear state feedback: saved / unsaved / written back / exported

## References

- [Skill Spec](./SKILL.md)
- [Template Library](./references/template-library.md)

## Acknowledgments

- [Thariq's original post](https://x.com/trq212/status/2052809885763747935) inspired the design of this skill
- [HTML example site](https://thariqs.github.io/html-effectiveness/) provided visual and interaction references
