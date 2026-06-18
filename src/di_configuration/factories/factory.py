from abc import ABC, abstractmethod
from src.application.parser import HtmlParser


class IParserFactory(ABC):

    @abstractmethod
    def __call__(self) -> HtmlParser:
        pass
