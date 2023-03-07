from chessBoard import *
from Points import *
from Pieces import *
from moveChecker import *
from aiMoveGenerator import *
from PiecesPosDict import *


# board.draw()
class Game:
    board = ChessBoard()
    for i in range(32):
        pieceToDraw = list(piecesPosDict.keys())[i]
        squareToFill = piecesPosDict[pieceToDraw]
        board.orginal_draw(pieceToDraw, squareToFill)
    board.draw()
    black=False

    def PlayMove(self, move:str):  
        move = move.upper()

        validMove=False #both bools have to be set false to check error handling
        properColour = False
        validMove=moveChecker(self.board,move[0:2],move[3:5]) #if valid
        if(self.board.access_square(move[0:2]).isBlack==self.black): #check that not moving other player piece
            properColour=True
        if (not validMove or not properColour):
             return "error"
        self.board.update_board(move[0:2],move[3:5]) #updates board
        self.black = not self.black #changes to other turn

    def GetBoard(self):
            return self.board
