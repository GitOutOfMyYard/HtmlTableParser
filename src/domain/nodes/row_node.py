"""Node representing an HTML <tr> (table row) element."""

from typing import Dict, List, Optional

from src.domain.nodes.element_node import ElementNode
from src.domain.nodes.cell_node import CellNode


class RowNode(ElementNode):
    """
    A node that represents a table row (<tr>).

    Contains an ordered list of cells (td/th)
    """
    allowed_tags = frozenset(("tr",))

    def __init__(
        self,
        tag: str,
        attributes: Optional[Dict[str, str]] = None,
        children: Optional[List[CellNode]] = None,
    ) -> None:
        """
        Initialize a row node.

        Args:
            attributes: Optional mapping of attribute name -> value from the tr tag.
            cells: Optional list of cell nodes.
        """
        super().__init__(tag, attributes, children)

    @property
    def cells(self) -> List[CellNode]:
        """Return the list of cell nodes."""
        return list(self.children())

    def append_cell(self, cell: CellNode) -> None:
        """Add a cell to the row."""
        self.children().append(cell)

    def __repr__(self) -> str:
        return "RowNode({} cells)".format(len(self.cells))
