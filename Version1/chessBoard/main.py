from chessBoard import *
from Points import *
from Pieces import *
from moveChecker import *
from aiMoveGenerator import *


board = ChessBoard()
board.draw()
board.orginal_draw(Pawn(False),"A2")
board.orginal_draw(Pawn(False),"B2")
board.orginal_draw(Pawn(False),"C2")
board.orginal_draw(Pawn(False),"D2")
board.orginal_draw(Pawn(False),"E2")
board.orginal_draw(Pawn(False),"F2")
board.orginal_draw(Pawn(False),"G2")
board.orginal_draw(Pawn(False),"H2")
board.orginal_draw(Rook(False),"A1")
board.orginal_draw(Knight(False),"B1")
board.orginal_draw(Bishop(False),"C1")
board.orginal_draw(Queen(False),"D1")
board.orginal_draw(King(False),"E1")
board.orginal_draw(Bishop(False),"F1")
board.orginal_draw(Knight(False),"G1")
board.orginal_draw(Rook(False),"H1")
board.orginal_draw(Pawn(True),"A7")
board.orginal_draw(Pawn(True),"B7")
board.orginal_draw(Pawn(True),"C7")
board.orginal_draw(Pawn(True),"D7")
board.orginal_draw(Pawn(True),"E7")
board.orginal_draw(Pawn(True),"F7")
board.orginal_draw(Pawn(True),"G7")
board.orginal_draw(Pawn(True),"H7")
board.orginal_draw(Rook(True),"A8")
board.orginal_draw(Knight(True),"B8")
board.orginal_draw(Bishop(True),"C8")
board.orginal_draw(Queen(True),"D8")
board.orginal_draw(King(True),"E8")
board.orginal_draw(Bishop(True),"F8")
board.orginal_draw(Knight(True),"G8")
board.orginal_draw(Rook(True),"H8")
board.draw()
board.update_board("A7","A6")

# In this prototype chess game, the game ends when black or white lose all of their
# pieces.
game_over = filter(lambda p: p.is_black == False, board.pieces) == board.pieces or \
    filter(lambda p: p.is_black == True, board.pieces) == board.pieces

turn_num = 0
board.update()
board.draw_board()

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