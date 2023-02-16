# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from chessBoard import ChessBoard
from Points import *
from Pieces import *

board = ChessBoard()
board.draw_board()
point=points()


#testing out points calculation 
#has to put points object in piece class
p=Knight(True,'e4',point)
q=Rook(False,'e6',point)
q.capture(p,point)



#demo of creating pieces and how we are using the points calcualtor 




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
