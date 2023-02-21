from chessBoard import *
from Points import *
from Pieces import *
from moveChecker import *
from aiMoveGenerator import *
from PiecesPosDict import *


board = ChessBoard()
board.draw()

for i in range(32):
    piece_to_draw = list(pieces_pos_dict.keys())[i]
    square_to_fill = pieces_pos_dict[piece_to_draw]
    board.orginal_draw(piece_to_draw, square_to_fill)

board.draw()
board.update_board("A7", "A6")

# In this prototype chess game, the game ends when black or white lose all of their
# pieces.
