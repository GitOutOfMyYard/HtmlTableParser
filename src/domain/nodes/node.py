"""Abstract base for all nodes in the HTML tree."""

from abc import ABC, abstractmethod
from typing import List, Optional, Any, Iterable, Union


class INode(ABC):
    """
    Base type for every node in the parsed HTML tree.

    Subclasses represent different kinds of content: elements (table, row, cell),
    or raw text. The tree is built by the parser and can be traversed or
    converted to other formats.
    """

    def __init__(self) -> None:
        """Initialize a node. Subclasses may add attributes."""
        pass

    @abstractmethod
    def children(self) -> List["INode"]:
        """
        Return the list of child nodes.

        Default is empty list. Element-like nodes override to return their
        actual children.
        """
        pass

    @abstractmethod
    def get_html(self) -> str:
        return ''

    # def __repr__(self) -> str:
    #     """String representation for debugging."""
    #     pass
