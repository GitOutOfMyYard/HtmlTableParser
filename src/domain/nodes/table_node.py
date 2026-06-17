"""Node representing an HTML <table> element."""

from typing import Dict, List, Optional
from src.domain.nodes.element_node import ElementNode, IElementNode
from src.domain.nodes.row_node import RowNode


class TableNode(ElementNode):
    """
    A node that represents an HTML table (<table>).

    Contains an ordered list of rows. Attributes from the original
    <table> tag are preserved.
    """
    allowed_tags = frozenset(("table",))

    def __init__(
        self,
        tag: str,
        attributes: Optional[Dict[str, str]] = None,
        children: Optional[List[IElementNode]] = None,
    ) -> None:
        super().__init__(tag, attributes, children)

    @property
    def attributes(self) -> Dict[str, str]:
        """Return a copy of the attributes mapping."""
        return dict(self._attributes)

    @property
    def rows(self) -> List[RowNode]:
        return list(self.children())

    def append_row(self, row: RowNode) -> None:
        self.rows.append(row)

    def __repr__(self) -> str:
        return "TableNode({} rows)".format(len(self._rows))
