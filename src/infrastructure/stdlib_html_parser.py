"""HTML table parser implementation using the standard library html.parser."""

import html.parser
from collections import deque
from typing import Dict, List, Optional

from src.application.parser_port import HtmlParserPort
from src.domain.nodes.node import INode
from src.domain.nodes.table_node import TableNode
from src.domain.nodes.row_node import RowNode
from src.domain.nodes.cell_node import CellNode
from src.domain.nodes.text_node import TextNode
from src.domain.nodes.element_node import ElementNode, IElementNode


def _attrs_to_dict(attrs: List[tuple]) -> Dict[str, str]:
    """Convert list of (name, value) attribute pairs of element to a dict."""
    return dict(attrs) if attrs else {}


def _tag_of(node: INode) -> Optional[str]:
    """Return the HTML tag name for a node,
    or None for non-elements (e.g. TextNode)."""
    if isinstance(node, TableNode):
        return "table"
    if isinstance(node, RowNode):
        return "tr"
    if isinstance(node, CellNode):
        return node.tag
    if isinstance(node, ElementNode):
        return node.tag
    return None


class _TableParser(html.parser.HTMLParser):
    """
    HTML parser implementation that builds a tree of
    TableNode/RowNode/CellNode/TextNode.

    Handles <table>, <tr>, <td>, <th> and nested content. Other tags are
    represented as ElementNode. Builds a stack of open elements and
    attaches children to the appropriate parent.
    """

    def __init__(self) -> None:
        super().__init__()
        self._roots: List[INode] = []
        self._stack: List[INode] = []
        self._stack = deque()
        self._current_table: Optional[TableNode] = None
        self._current_row: Optional[RowNode] = None
        self.top_obj: Optional[IElementNode] = None

    def _push(self, node: INode, parent_accepts: bool = True) -> None:
        """Push node onto stack and optionally attach to parent."""
        if parent_accepts:
            parent = None
            if self._stack:
                parent = self._stack[-1]
            if isinstance(parent, ElementNode):
                parent.append_child(node)
        self._stack.append(node)

    def handle_starttag(self, tag: str, attrs: List[tuple]) -> None:
        tag_lower = tag.lower()
        attrs_d = _attrs_to_dict(attrs)

        if tag_lower == "table":
            node = TableNode(attributes=attrs_d)
            self._current_table = node

        elif tag_lower == "tr":
            node = RowNode(attributes=attrs_d)
            self._current_row = node

        elif tag_lower in ("td", "th"):
            node = CellNode(tag=tag_lower, attributes=attrs_d)

        else:
            node = ElementNode(tag=tag_lower, attributes=attrs_d)
        self._push(node)

    def handle_endtag(self, tag: str) -> None:
        tag_lower = tag.lower()
        node = None
        while self._stack:
            node = self._stack.pop()
            if tag_lower == "table" and isinstance(node, TableNode):
                self._current_table = None
            if tag_lower == "tr" and isinstance(node, RowNode):
                self._current_row = None
            if node.tag == tag_lower:
                self.top_obj = None
                break
        if not self._stack and node:
            self._roots.append(node)


    def handle_data(self, data: str) -> None:
        text = data.strip()
        if not text:
            return
        node = TextNode(text)
        if self._stack:
            parent = self._stack[-1]
            if isinstance(parent, CellNode):
                parent.append_child(node)
            elif isinstance(parent, ElementNode):
                parent.append_child(node)

    def get_roots(self) -> List[INode]:
        """Return the list of root nodes after parsing."""
        return self._roots


class StdlibHtmlParser(HtmlParserPort):
    """
    Parses HTML using built-in html.parser.HTMLParser.

    Produces a tree of TableNode, RowNode, CellNode, TextNode, and
    ElementNode.
    """

    def parse(self, html_content: str) -> List[INode]:
        """
        Returns List of root-level nodes. TableNode instances for
        each <table>, and any top-level non-table elements as ElementNode.
        """
        parser = _TableParser()
        parser.feed(html_content)
        return parser.get_roots()
