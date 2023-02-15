class ChessBoard:
    def __init__(self):
        self.board = [
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"],
        ]

    def draw_board(self):
        for i in range(8, 0, -1):
            print(f"{i} |", end=" ")
            for j in range(0, 8):
                print(f"{self.board[i-1][j]} |", end=" ")
            print("\n  +---+---+---+---+---+---+---+---+")
        print("    a   b   c   d   e   f   g   h")


def get_chess_notation(coords):
    columns = "abcdefgh"
    row = str(coords[1])
    column = columns[coords[0]-1]
    return column + row

