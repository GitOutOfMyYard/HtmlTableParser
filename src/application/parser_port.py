
from abc import ABC, abstractmethod
from typing import List

from src.domain.nodes.node import INode


class HtmlParserPort(ABC):
    """
    Abstract port/interface for parsing HTML and producing a tree of nodes.
    """

    @abstractmethod
    def parse(self, html: str) -> List[INode]:
        """
        Parse HTML and return the top-level nodes (e.g. tables and elements).

        Args:
            html: Raw HTML string.

        Returns:
            List of root nodes.
        """
        pass
