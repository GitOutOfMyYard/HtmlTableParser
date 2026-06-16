"""
HTML table parser: parses HTML and converts it to a tree of Python objects.

Usage:

    from html_table_parser import ParseHtmlUseCase
    from html_table_parser.infrastructure import StdlibHtmlParser

    parser = StdlibHtmlParser()
    use_case = ParseHtmlUseCase(parser)
    roots = use_case.execute("<table><tr><td>Hello</td></tr></table>")
    # roots[0] is a TableNode with rows and cells
"""

from html_table_parser.application import ParseHtmlUseCase
from html_table_parser.domain import (
    INode,
    TableNode,
    RowNode,
    CellNode,
    TextNode,
    ElementNode,
)

__all__ = [
    "ParseHtmlUseCase",
    "INode",
    "TableNode",
    "RowNode",
    "CellNode",
    "TextNode",
    "ElementNode",
]
