"""Node representing an HTML <td> or <th> (table cell) element."""

from typing import Dict, List, Optional

from html_table_parser.domain.nodes.element_node import ElementNode
from html_table_parser.domain.nodes.node import INode


class CellNode(ElementNode):
    """
    A node that represents a table cell (<td> or <th>).

    Contains a list of child nodes (text, nested tables, or other elements).
    The tag type ('td' or 'th') and attributes are preserved.
    """

    def __init__(
        self,
        tag: str = "td",
        attributes: Optional[Dict[str, str]] = None,
        children: Optional[List[INode]] = None,
    ) -> None:
        """
        Initialize a cell node.

        Args:
            tag: Either 'td' or 'th'.
            attributes: Optional mapping of attribute name -> value.
            children: Optional list of child nodes (e.g. TextNode, TableNode).
        """
        tag = tag.lower() if tag in ("td", "th") else "td"
        super().__init__(tag, attributes, children)

    @property
    def tag(self) -> str:
        """Return 'td' or 'th'."""
        return self._tag

    @property
    def is_header(self) -> bool:
        """Return True if this cell is a header (th)."""
        return self._tag == "th"

    @property
    def attributes(self) -> Dict[str, str]:
        """Return a copy of the attributes dictionary."""
        return dict(self._attributes)

    # def children(self) -> List[INode]:
    #     """Return the list of child nodes."""
    #     return list(self._children)

    # def append_child(self, node: INode) -> None:
    #     """Add a child node (e.g. text or nested table)."""
    #     self._children.append(node)

    def __repr__(self) -> str:
        return "CellNode({!r}, {} children)".format(self._tag, len(self._children))
