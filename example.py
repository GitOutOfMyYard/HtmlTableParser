""" Example module"""

from src import ParseHtmlUseCase
from src.infrastructure import StdlibHtmlParser
from src.application.utils.terminal_view import view_html


def main() -> None:
    html =  """

<html>
<style>
table, th, td {
  border:1px solid black;
}
</style>
<body>

<h2>HTML table example</h2>

<table style="width:100%">
  <tr>
    <th>Header column 1</th>
    <th>Header column 2</th>
    <th>Header column 3</th>
  </tr>
  <tr>
    <td>column 1 row 2</td>
    <td>column 2 row 2</td>
    <td>column 3 <p>row 2</p></td>
  </tr>
  <tr>
    <td>column 1 row 3</td>
    <td some_attr='I am attribute'>column 2 row 3</td>
    <td>column 3 row 3<p>The End.</p></td>
  </tr>
</table>

<p>Some text, no a table.</p>

</body>
</html>
    """

    view_html(html)

if __name__ == "__main__":
    main()
