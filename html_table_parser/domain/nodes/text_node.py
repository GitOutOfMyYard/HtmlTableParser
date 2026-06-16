"""Leaf node that holds raw text content."""
from typing import List

from html_table_parser.domain.nodes.node import INode


class TextNode(INode):
    """
    A node that represents a raw text (no HTML tags).

    Used for text inside elements (e.g. inside a table cell).
    """

    def __init__(self, text: str) -> None:
        super().__init__()
        self._text = text or ""

    def children(self) -> List["Node"]:
        return []

    @property
    def text(self) -> str:
        """Return the text content."""
        return self._text

    def get_contents(self) -> str:
        return self.text

    def get_html(self) -> str:
        return self._text

    def __repr__(self) -> str:
        snippet = self._text[:20] + "..." if len(self._text) > 20 else self._text
        return "TextNode({!r})".format(snippet)
