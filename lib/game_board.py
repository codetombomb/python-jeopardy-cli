from rich.console import Console
from rich.table import Table
from rich import box


# Implement Rich tables: https://rich.readthedocs.io/en/stable/tables.html


class GameBoard:
    # Init with 30 question object list and an optional column config obj
    #
    def __init__(
        self,
        board_data,
        column_config={"justify": "center", "style": "blue", "no_wrap": False},
    ):
        if len(board_data) == 30:
            self.board_data = board_data
        else:
            raise Exception("Board data must contain 30 clues")

        self.board = Table(title="J! Round", show_lines=True, box=box.ROUNDED)
        self.table_column_config = column_config
        self.console = Console()
        self.init_board()
        self.print_table()
        self.print_selection()

    def init_board(self):
        categories = list(set(map(lambda q: q.category, self.board_data)))
        for cat in categories:
            self.board.add_column(
                cat,
                justify=self.table_column_config["justify"],
                style=self.table_column_config["style"],
                no_wrap=self.table_column_config["no_wrap"]
            )
        values = ["$200", "$400", "$600", "$800", "$1000"]

        for value in values:
            self.board.add_row(
                value,
                value,
                value,
                value,
                value,
                value
            )

    # Print the table
    def print_table(self):
        self.console.print(self.board)
        
    def print_selection(self):
        pass
