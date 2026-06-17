"""Generic element node for any HTML tag (e.g. div, span, nested table container)."""

from typing import Dict, List, Optional
from abc import abstractmethod
from src.domain.nodes.node import INode


class IElementNode(INode):

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
        """
        Initialize an element node.

        Args:
            tag: Lowercase tag name (e.g. 'div', 'table').
            attributes: Optional mapping of attribute name -> value.
            children: Optional list of child nodes.
        """
        super().__init__()
        self._tag = tag.lower() if tag else ""
        self._attributes = dict(attributes) if attributes else {}
        self._children = list(children) if children else []

    @property
    def tag(self) -> str:
        """Return the tag name."""
        return self._tag

    def get_open_tag(self) -> str:
        serialized_attrs = ''
        return f'<{self._tag} {serialized_attrs}>'

    def get_close_tag(self) -> str:
        serialized_attrs = ''
        return f'</{self._tag}>'

    @property
    def attributes(self) -> Dict[str, str]:
        """Return a copy of the attributes dictionary."""
        return dict(self._attributes)

    def children(self) -> List[INode]:
        """Return the list of child nodes."""
        return list(self._children)

    def append_child(self, node: INode) -> None:
        """Add a child node."""
        self._children.append(node)

    def get_html(self) -> str:

        result = ''
        result += self.get_open_tag()

        for child in self._children:
            result += child.get_html()
        result += self.get_close_tag()
        return result
        return ''.join(child.get_html() for child in self._children)

    def __repr__(self) -> str:
        attrs = " ".join('{}="{}"'.format(k, v) for k, v in self._attributes.items())

        if attrs:
            return "ElementNode({!r}, {{{}}}, {} children)".format(
                self._tag, attrs, len(self._children)
            )
        return "ElementNode({!r}, {} children)".format(self._tag, len(self._children))
