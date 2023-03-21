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
        board.OriginalDraw(pieceToDraw, squareToFill)
    board.Draw()
    black=False

    def PlayMove(self, move:str):
        move = move.upper()
        validMove=False #both bools have to be set false to check error handling
        properColour = False

        if self.black:
          white_colour = 0
        else:
          white_colour = 1

        if (move == "0-0") or (move == "O-O"):
          valid_move = MoveChecker(self.board, "k", white_colour,0)  # kingside castling - set move checker to k
          proper_colour = True
        elif move == "0-0-0" or move == "O-O-O":
          valid_move = MoveChecker(self.board, "q", white_colour, 0)  # queenside castling - set move checker to k
          proper_colour = True
        else:
          validMove=MoveChecker(self.board,move[0:2],move[3:5],1) #if valid
          if(self.board.AccessSquare(move[0:2]).isBlack==self.black): #check that not moving other player piece
            properColour=True

        if (not validMove or not properColour):
             return "error"
        if move == "0-0" or move == "O-O":
          if self.black:
            self.board.update_board("E8", "G8")
            self.board.update_board("H8", "F8")
          if not self.black:
            self.board.update_board("E1", "G1")
            self.board.update_board("H1", "F1")
        elif move == "0-0-0" or move == "O-O-O":
          if self.black:
            self.board.update_board("E8", "C8")
            self.board.update_board("A8", "D8")
          if not self.black:
            self.board.update_board("E1", "C1")
            self.board.update_board("A1", "D1")

        else:
            self.board.UpdateBoard(move[0:2],move[3:5]) #updates board
        self.black = not self.black #changes to other turn

    def GetBoard(self):
            return self.board
    
    def Restart(self):
        for i in range(8):
            for j in range(8):
                self.board.board[i][j].ResetSquare()
        for i in range(32):
            pieceToDraw = list(piecesPosDict.keys())[i]
            pieceToDraw.hasMoved=False
            squareToFill = piecesPosDict[pieceToDraw]
            self.board.OriginalDraw(pieceToDraw, squareToFill)
        self.board.Draw()
        self.black=False
