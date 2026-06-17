"""Node representing an HTML <td> or <th> (table cell) element."""

from typing import Dict, List, Optional

from src.domain.nodes.element_node import ElementNode
from src.domain.nodes.node import INode


class CellNode(ElementNode):
    """
    A node that represents a table cell (<td> or <th>).

    Contains a list of child nodes (text, nested tables, or other elements).
    The tag type ('td' or 'th') and attributes are preserved.
    """
    _default_tag: str = "td"
    allowed_tags = frozenset(("td", "th"))

    def __init__(
        self,
        tag: str = _default_tag,
        attributes: Optional[Dict[str, str]] = None,
        children: Optional[List[INode]] = None,
    ) -> None:
        tag = tag.lower() or self._default_tag
        super().__init__(tag, attributes, children)

    @property
    def is_header(self) -> bool:
        """Return True if this cell is a header (th)."""
        return self._tag == "th"

    def __repr__(self) -> str:
        return "CellNode({!r}, {} children)".format(self._tag, len(self._children))
