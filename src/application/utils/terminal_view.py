"""Funcs to display table cells text in console"""

from src import ParseHtmlUseCase
from src.domain import TableNode, CellNode, TextNode
from src.domain.nodes.element_node import IElementNode
from src.domain.nodes.node import INode
from src.infrastructure import StdlibHtmlParser
from typing import List, Any


def view_html(html: str, *_: Any) -> None:
    parser = StdlibHtmlParser()
    use_case = ParseHtmlUseCase(parser)
    roots = use_case.execute(html)
    for root in roots:
        print_table_nodes(root)


def print_table_nodes(root: INode) -> None:
    if isinstance(root, TableNode):
        print_table_in_console(root)
    else:
        for child in root.children():
            print_table_nodes(child)
        else:
            print(f"Node: {root}")


def _fetch_cell_text(node: INode) -> List[str]:
    if isinstance(node, TextNode):
        return [node.text]
    else:
        result = []
        for child in node.children():
            result.extend(_fetch_cell_text(child))
        return result


def print_table_in_console(node: TableNode) -> None:
    print("Table ({} rows):".format(len(node.rows)))
    for row_index, row in enumerate(node.rows, 1):

        cells_to_print = []
        for cell_num, cell in enumerate(row.cells, 1):
            parts = _fetch_cell_text(cell)
            cells_to_print.append(
                "  Cell {}: {}".format(cell_num, " ".join(parts)))

        row_to_print = ' | '.join(cells_to_print)
        row_num_text_prefix = f"===== Row: {row_index}  ====="
        max_row_len = len(row_to_print) + 1
        row_num_text_postfix_len = max_row_len - len(row_num_text_prefix)
        if row_num_text_postfix_len < 0:
            row_num_text_postfix_len = 0
        row_num_text_postfix = "=" * row_num_text_postfix_len
        print(f"{row_num_text_prefix}{row_num_text_postfix}")
        print(row_to_print)
        print('=' * max_row_len)


if __name__ == "__main__":
    import sys
    view_html(*sys.argv[1:])
