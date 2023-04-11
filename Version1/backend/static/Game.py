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
    gameOver = False

    def PlayMove(self, move:str):
        if not self.gameOver:
          move = move.upper()
          validMove=False #both bools have to be set false to check error handling
          properColour = False

          if self.black:
            white_colour = 0
          else:
            white_colour = 1

          if (move == "0-0") or (move == "O-O"):
            validMove = MoveChecker(self.board, "k", white_colour,0)  # kingside castling - set move checker to k
            properColour = True
          elif move == "0-0-0" or move == "O-O-O":
            validMove = MoveChecker(self.board, "q", white_colour, 0)  # queenside castling - set move checker to k
            properColour = True
          else:
            validMove=MoveChecker(self.board,move[0:2],move[3:5],1) #if valid
            sq = self.board.AccessSquare(move[0:2])
            if self.board.AccessSquare(move[0:2]) is not None: #check that not moving other player piece
              if self.board.AccessSquare(move[0:2]).isBlack==self.black:
                properColour=True

          if (not validMove or not properColour):
              return "error"
          if move == "0-0" or move == "O-O":
            if self.black:
              self.board.UpdateBoard("E8", "G8")
              self.board.UpdateBoard("H8", "F8")
            if not self.black:
              self.board.UpdateBoard("E1", "G1")
              self.board.UpdateBoard("H1", "F1")
          elif move == "0-0-0" or move == "O-O-O":
            if self.black:
              self.board.UpdateBoard("E8", "C8")
              self.board.UpdateBoard("A8", "D8")
            if not self.black:
              self.board.UpdateBoard("E1", "C1")
              self.board.UpdateBoard("A1", "D1")

          else:
              self.board.UpdateBoard(move[0:2],move[3:5]) #updates board
          self.black = not self.black #changes to other turn
          print(self.board.ProperFen(self.black))

    def GetBoard(self):
            return self.board
    
    def Restart(self):
        self.gameOver = False
        for i in range(8):
            for j in range(8):
                self.board.board[i][j].ResetSquare()
        for i in range(32):
            pieceToDraw = list(piecesPosDict.keys())[i]
            pieceToDraw.hasMoved = False
            squareToFill = piecesPosDict[pieceToDraw]
            self.board.OriginalDraw(pieceToDraw, squareToFill)
        self.board.Draw()
        self.black=False
