# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from chessBoard import ChessBoard
from Points import *
from Pieces import *
from moveChecker import *
from aiMoveGenerator import ai_move_generator

board = ChessBoard()
board.draw_board()
point=points()


#testing out points calculation 
#has to put points object in piece class
knight=Knight(False,'g1',point)
wPawn=Pawn(False,'d2',point)
bPawn=Pawn(True,'a7',point)
#q=Rook(False,'e6',point)
#q.capture(p,point)


print(move_checker(board, knight, "e2")) # False
print(move_checker(board, knight, "f3")) # True
print(move_checker(board, knight, "g3")) # False
print(move_checker(board, wPawn, "d3")) # True
print(move_checker(board, wPawn, "d4")) # True
print(move_checker(board, wPawn, "c3")) # False
print(move_checker(board, bPawn, "b7")) # False
print(move_checker(board, bPawn, "a6")) # True
print(move_checker(board, bPawn, "a5")) # True
print(move_checker(board, bPawn, "a4")) # False

#Testing AI Move Generator Function - black pieces
black_pieces_array = [Knight(True,'f2',point), Pawn(True,'f2',point), Pawn(True,'d7',point)]
print(ai_move_generator(board, black_pieces_array))

#Testing AI Move Generator Function - white pieces
white_pieces_array = [Knight(False,'f2',point), Pawn(False,'d2',point), Pawn(False,'b7',point)]
print(ai_move_generator(board, white_pieces_array))




#demo of creating pieces and how we are using the points calcualtor 




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
