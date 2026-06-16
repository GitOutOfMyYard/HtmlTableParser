"""Use case: parse HTML string into a tree of nodes."""

from typing import List

from html_table_parser.domain.nodes.node import INode
from html_table_parser.application.parser_port import HtmlParserPort


class ParseHtmlUseCase:
    """
    Application use case that parses HTML and returns a tree of domain nodes.

    Depends on HtmlParserPort (injected) so the actual parsing strategy
    can be swapped (e.g. stdlib vs third-party parser).
    """

    def __init__(self, parser: HtmlParserPort) -> None:
        """
        Initialize the use case with a parser implementation.

        Args:
            parser: Implementation of HtmlParserPort (e.g. StdlibHtmlParser).
        """
        self._parser = parser

    def execute(self, html: str) -> List[INode]:
        """
        Parse the given HTML and return the root nodes of the tree.

        Args:
            html: Raw HTML string (e.g. from a file or HTTP response).

        Returns:
            List of root nodes. For a document with one table, this will
            typically be a single TableNode. For multiple top-level elements,
            multiple nodes are returned.
        """
        return self._parser.parse(html)
