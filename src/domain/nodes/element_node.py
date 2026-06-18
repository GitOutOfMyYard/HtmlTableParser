"""Generic element node for any HTML tag (e.g. div, span, nested table container)."""

from typing import Dict, List, Optional
from abc import abstractmethod
from src.domain.nodes.node import INode


class IElementNode(INode):

    @property
    @abstractmethod
    def tag(self) -> str:
        pass

    @abstractmethod
    def append_child(self, node: INode) -> None:
        pass

    @property
    @abstractmethod
    def attributes(self) -> Dict[str, str]:
        pass


class ElementNode(IElementNode):
    """
    A node that represents an HTML element: tag name, attributes, and children.

    Used for non-table structural tags (e.g. div, span) and as a generic
    container so the tree can represent full HTML. Table/row/cell nodes
    are used for table structure specifically.
    """

    def __init__(
        self,
        tag: str,
        attributes: Optional[Dict[str, str]] = None,
        children: Optional[List[INode]] = None,
    ) -> None:
        super().__init__()
        self._tag = tag.lower() or ""
        self._attributes = dict(attributes) if attributes else {}
        self._children = list(children) if children else []

    @property
    def tag(self) -> str:
        """Return the tag name."""
        return self._tag

    def _get_open_tag(self) -> str:
        serialized_attrs = ''
        return f'<{self._tag} {serialized_attrs}>'

    def _get_close_tag(self) -> str:
        return f'</{self._tag}>'

    @property
    def attributes(self) -> Dict[str, str]:
        """Return a copy of the attributes mapping."""
        return dict(self._attributes)

    def children(self) -> List[INode]:
        """Return the list of child nodes."""
        return list(self._children)

    def append_child(self, node: INode) -> None:
        """Add a child node."""
        self._children.append(node)

    def to_html(self) -> str:
        result = ''
        result += self._get_open_tag()
        for child in self._children:
            result += child.to_html()
        result += self._get_close_tag()
        return result

    def __repr__(self) -> str:
        attrs = " ".join('{}="{}"'.format(k, v) for k, v in self._attributes.items())

        if attrs:
            return "ElementNode({!r}, {{{}}}, {} children)".format(
                self._tag, attrs, len(self._children)
            )
        return "ElementNode({!r}, {} children)".format(self._tag, len(self._children))
