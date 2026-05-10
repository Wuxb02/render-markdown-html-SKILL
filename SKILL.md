---
name: render-markdown-html
description: Render Markdown as HTML or convert HTML back into Markdown. Use whenever the user explicitly wants one of those two outputs, especially for long Markdown documents that should become human-friendly HTML pages, browser-tuned document parameters that need write-back controls, saved HTML summaries, or HTML that should be recovered as Markdown.
tools:
  - md_to_html
  - html_to_md
---

# Markdown to HTML Workbench

Turn Markdown into a readable HTML workspace when HTML is requested, or recover Markdown when Markdown is requested. Do not assume both steps are needed.

## When to use

- The user wants a long agent summary saved as HTML instead of a long Markdown file.
- The user wants an existing `.md` file converted into a cleaner HTML presentation.
- The user wants to change colors, spacing, labels, parameters, or other document settings directly in HTML.
- The user wants to convert HTML back into Markdown and keep working in Markdown.

## Core rules

1. Separate content from presentation. Markdown carries structure; HTML carries reading and interaction.
2. Prefer a single self-contained HTML file that can be opened, edited, and saved without a build step.
3. Expose any editable setting as a visible control in HTML.
4. If the HTML includes any parameter or configuration field, always add an explicit write-back button near that control group.
5. Only chain HTML back to Markdown when the user asks for Markdown output or explicit recovery.
6. Keep the page readable, scannable, and printable. Visual polish should support comprehension, not distract from it.

## Output targets

Choose the output based on the task the user asked for:

- `html` for reading, sharing, or archiving
- `html + controls` for in-page tuning of parameters
- `md` for downstream editing or agent handoff

## Recommended workflow

### If the user wants HTML

- Detect headings, lists, tables, code blocks, quotes, and parameter blocks.
- Rebuild the document with semantic HTML.
- Add a table of contents, anchor links, and a compact summary for long documents.
- Surface key parameters as editable controls.
- Add a write-back or export button whenever any parameter can be changed.

### If the user wants editable HTML

- Group configurable items into a clear settings area.
- Prefer buttons, toggles, sliders, select menus, and color pickers over free-form source editing.
- Show instant preview updates for appearance settings such as theme, scale, spacing, and accent color.
- Use explicit Apply, Reset, Write Back, and Export actions.

### If the user wants Markdown

- Recover the document semantics first, then the formatting.
- Preserve heading hierarchy, lists, tables, links, code blocks, and emphasis.
- Drop layout-only details that do not contribute to the document content.

## Style direction

Use a calm, editorial interface rather than a flashy landing page. The visual language should pull from the reference notes in `references/`:

- low-saturation ivory, slate, clay, and olive tones
- thin borders, restrained shadows, and compact radii
- serif headings with sans-serif body text
- side navigation, sticky toolbars, and split previews
- clear state feedback such as saved, unsaved, written back, and exported

## Practical guidance

- When the source is Markdown, preserve its structure unless the user asks for a rewrite.
- When the user says to make it editable, treat that as a request for an interactive HTML surface, not a static export.
- When the user asks for HTML, do not generate Markdown unless they also asked for Markdown output.
- When the user asks for Markdown, recover the meaning of the content rather than the visual styling and do not force an HTML detour.

## Typical usage

```bash
/render-markdown-html docs/summary.md
```

```bash
/html-to-md report.html
```

## Output conventions

- Keep the output filename aligned with the source filename and change only the extension when possible.
- If the HTML exposes editable parameters, include a dedicated write-back button in the interface.
- If the output includes Markdown, preserve the original semantic hierarchy as much as possible.
