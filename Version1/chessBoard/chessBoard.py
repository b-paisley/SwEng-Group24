from Pieces import *


class ChessBoard:
    def __init__(self, points):
        # creates 2D 8X8 Array of pieces in their starting positions
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
        # this attribute is used to keep track of the pieces on the board. When a piece is added to the board, it also
        # gets added to the self.pieces list. likewise when a piece is removed from the board, it is removed from the
        # self.pieces list.
        self.pieces = []

        for i in range(8):
            for j in range(8):
                if self.board[i][j] == " ":
                    continue
                elif self.board[i][j] == "P":
                    self.pieces.append(Pawn(False, get_chess_notation((i, j)), points, self))
                elif self.board[i][j] == "p":
                    self.pieces.append(Pawn(True, get_chess_notation((i, j)), points, self))
                elif self.board[i][j] == "R":
                    self.pieces.append(Rook(False, get_chess_notation((i, j)), points, self))
                elif self.board[i][j] == "r":
                    self.pieces.append(Rook(True, get_chess_notation((i, j)), points, self))
                elif self.board[i][j] == "N":
                    self.pieces.append(Knight(False, get_chess_notation((i, j)), points, self))
                elif self.board[i][j] == "n":
                    self.pieces.append(Knight(True, get_chess_notation((i, j)), points, self))
                elif self.board[i][j] == "B":
                    self.pieces.append(Bishop(False, get_chess_notation((i, j)), points, self))
                elif self.board[i][j] == "b":
                    self.pieces.append(Bishop(True, get_chess_notation((i, j)), points, self))
                elif self.board[i][j] == "Q":
                    self.pieces.append(Queen(False, get_chess_notation((i, j)), points, self))
                elif self.board[i][j] == "q":
                    self.pieces.append(Queen(True, get_chess_notation((i, j)), points, self))
                elif self.board[i][j] == "K":
                    self.pieces.append(King(False, get_chess_notation((i, j)), points, self))
                elif self.board[i][j] == "k":
                    self.pieces.append(King(True, get_chess_notation((i, j)), points, self))

    # return current state of board.
    def get_board(self):
        return self.board

    # print to console a visual representation of the chess board
    def draw_board(self):
        print("\n  +---+---+---+---+---+---+---+---+")
        for i in range(8, 0, -1):
            print(f"{i} |", end=" ")
            for j in range(0, 8):
                print(f"{self.board[i - 1][j]} |", end=" ")
            print("\n  +---+---+---+---+---+---+---+---+")
        print("    a   b   c   d   e   f   g   h")

    def update(self):
        for i in range(8):
            for j in range(8):
                self.board[i][j] = ' '
        for p in self.pieces:
            pos = p.pos_to_tuple()
            self.board[pos[0]][pos[1]] = p


# take in array notation and return chess notation co-ordinates ( e.g. input : (2, 2) - output : d4
def get_chess_notation(coords):
    columns = "abcdefgh"
    row = str(coords[1]+1)
    column = columns[8 - coords[0] - 1]
    return column + row
