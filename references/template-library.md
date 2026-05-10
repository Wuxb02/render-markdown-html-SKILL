# Template Library Notes

This reference captures the visual and interaction patterns to reuse for Markdown-to-HTML and HTML-to-Markdown work in this repository.

## What to borrow

- Calm editorial styling instead of marketing polish
- Ivory backgrounds with slate text
- Clay and olive accents for emphasis and state
- Serif headings with sans-serif body text
- Thin borders, restrained shadows, and compact radii
- Dense but readable toolbars and side panels
- Controls that look like tools, not decoration

## Structural patterns

- A header that states the document name immediately
- A sticky toolbar for save, export, and theme actions
- Side navigation or anchor navigation for sections
- A main reading pane plus a companion editing or settings pane
- A clear preview area for rendered content
- A dedicated export affordance for HTML and Markdown

## Interaction patterns

- Toggle between read and edit modes
- Slider controls for spacing, scale, or density
- Color pickers for highlight or accent tuning
- Separate Apply, Reset, Write Back, and Export actions
- State labels such as saved, unsaved, written back, or exported

## Content patterns

- Long documents should be broken into sections
- Tables of contents should stay visible for multi-section documents
- Configuration should be surfaced as editable controls when possible
- Code, tables, and lists should remain semantic in the HTML output

## Design cues from the reference page

- Side-by-side comparison of Markdown and HTML is useful
- The interface should feel like a working surface, not a brochure
- Small labels and metadata help with scanning
- The page should reveal the next section slightly so it never feels empty

## Local examples

Use the example pages in `references/examples/` as starting points when shaping future HTML outputs:

- `01-document-review.html` for long-form documents and summaries
- `02-configurable-card.html` for parameterized content that needs write-back controls
- `03-editorial-split-view.html` for Markdown / HTML comparison and optional side-by-side editing
