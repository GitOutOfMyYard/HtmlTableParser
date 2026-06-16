"""Node representing an HTML <table> element."""

from typing import Dict, List, Optional
from html_table_parser.domain.nodes.element_node import ElementNode, IElementNode
from html_table_parser.domain.nodes.row_node import RowNode


class TableNode(ElementNode):
    """
    A node that represents an HTML table (<table>).

    Contains an ordered list of rows. Attributes from the original
    <table> tag are preserved.
    """

    def __init__(
        self,
        tag: str = "table",
        attributes: Optional[Dict[str, str]] = None,
        children: Optional[List[IElementNode]] = None,
    ) -> None:
        """
        Initialize a table node.

        Args:
            attributes: Optional mapping of attribute name -> value from the table tag.
            rows: Optional list of row nodes.
        """
        super().__init__(tag, attributes, children)


    @property
    def attributes(self) -> Dict[str, str]:
        """Return a copy of the attributes dictionary."""
        return dict(self._attributes)

    @property
    def rows(self) -> List[RowNode]:
        """Return the list of row nodes."""
        return list(self.children())

    def append_row(self, row: RowNode) -> None:
        """Add a row to the table."""
        self.rows.append(row)

    def __repr__(self) -> str:
        return "TableNode({} rows)".format(len(self._rows))
