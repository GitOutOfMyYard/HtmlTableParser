from src import ParseHtmlUseCase
from src.infrastructure import StdlibHtmlParser
from src.application.parser import HtmlParser
from src.di_configuration.factories.factory import IParserFactory


class StdLibParserFactory(IParserFactory):

    def __call__(self) -> HtmlParser:
        return HtmlParser(ParseHtmlUseCase(StdlibHtmlParser()))
