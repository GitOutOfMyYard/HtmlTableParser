from typing import List

from src import ParseHtmlUseCase
from src.domain.nodes.node import INode


class HtmlParser:
    def __init__(self, parsing_use_case: ParseHtmlUseCase) -> None:
        self._parsing_use_case = parsing_use_case

    def parse(self, html_doc: str) -> List[INode]:
        return self._parsing_use_case.execute(html_doc)
