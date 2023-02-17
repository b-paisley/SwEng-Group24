from chessBoard import *
from Points import *
from Pieces import *
from moveChecker import *
from aiMoveGenerator import *

points = points()
board = ChessBoard(points)

# In this prototype chess game, the game ends when black or white lose all of their
# pieces.
game_over = filter(lambda p: p.is_black == False, board.pieces) == board.pieces or \
    filter(lambda p: p.is_black == True, board.pieces) == board.pieces

turn_num = 0

while not game_over:
    if turn_num % 2 == 0: # white's turn
        white_move = input("White's turn: Pick your move") # Example input: Nc3xBd5
        for p in board.pieces:
            if p.pos == white_move[1:3]:
                if 'x' in white_move:
                    dest_square = white_move[4:]
                else:
                    dest_square = white_move[3:]
                p.move(dest_square)
    else: # black's turn
        pass

    board.update()
    board.draw_board()
    turn_num += 1