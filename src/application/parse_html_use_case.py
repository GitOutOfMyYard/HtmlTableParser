"""Use case: parse HTML string into a tree of nodes."""

from typing import List

from src.domain.nodes.node import INode
from src.application.parser_port import HtmlParserPort


class ParseHtmlUseCase:
    """
    Use case that parses HTML and returns a tree of nodes.

    Depends on HtmlParserPort (injected) so the actual parsing strategy
    can be swapped (e.g. stdlib vs third-party parser).
    """

    def __init__(self, parser: HtmlParserPort) -> None:
        """
        Initialize the use case with a parser implementation.

        Args:
            parser: Implementation of/adapter for HtmlParserPort
        """
        self._parser = parser

    def execute(self, html: str) -> List[INode]:
        """
        Parse the given HTML and return the root nodes of the tree.
        """
        return self._parser.parse(html)
