# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from chessBoard import ChessBoard
from Points import *
from Pieces import *
from moveChecker import *

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


print(moveChecker(board, knight, "e2")) # False
print(moveChecker(board, knight, "f3")) # True
print(moveChecker(board, knight, "g3")) # False
print(moveChecker(board, wPawn, "d3")) # True
print(moveChecker(board, wPawn, "d4")) # True
print(moveChecker(board, wPawn, "c3")) # False
print(moveChecker(board, bPawn, "b7")) # False
print(moveChecker(board, bPawn, "a6")) # True
print(moveChecker(board, bPawn, "a5")) # True
print(moveChecker(board, bPawn, "a4")) # False




#demo of creating pieces and how we are using the points calcualtor 




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
