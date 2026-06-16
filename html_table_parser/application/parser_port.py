"""Port (interface) for parsing HTML into a tree of nodes."""

from abc import ABC, abstractmethod
from typing import List

from html_table_parser.domain.nodes.node import INode


class HtmlParserPort(ABC):
    """
    Abstract port for parsing HTML and producing a tree of domain nodes.

    Implementations may use different backends (e.g. stdlib html.parser,
    or third-party libraries). The use case depends on this port.
    """

    @abstractmethod
    def parse(self, html: str) -> List[INode]:
        """
        Parse HTML and return the top-level nodes (e.g. tables and elements).

        Args:
            html: Raw HTML string.

        Returns:
            List of root nodes. Typically one or more TableNode or ElementNode
            for the document structure.
        """
        pass
