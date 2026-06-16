# HTML Table Parser

Parses HTML and converts it to a **tree of Python objects**.


## Tree structure

- **TableNode**: `<table>` — has `.rows` (list of `RowNode`).
- **RowNode**: `<tr>` — has `.cells` (list of `CellNode`).
- **CellNode**: `<td>` or `<th>` — has `.children()` (e.g. `TextNode`, nested `TableNode`).
- **TextNode**: Raw text (no tag).
- **ElementNode**: Any other tag (e.g. `<div>`, `<span>`, `<p>`) with `.tag`, `.attributes`, `.children()`.

