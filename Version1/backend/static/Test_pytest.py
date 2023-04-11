import pytest
import unittest
from chessBoard import *
from Game import *
from square import *
from Pieces import *
from PiecesPosDict import *

def test_ResetSqaure():
    game = Game()
    game.board.UpdateBoard("D1","C4")
    square="C4"
    letterFile = ord(square[0])-65
    numberRow = int(square[1]) - 1
    squareObj=game.board.board[numberRow][letterFile]
    squareObj.ResetSquare()
    assert (game.board.board[numberRow][letterFile].placedInSquare ) == None

def test_Restart():
    game = Game()
    #game.board.update_board("D1","C4") #queen

    game.board.UpdateBoard("C1","B3") #bishop
    game.board.UpdateBoard("E1","F4") #king
    game.board.UpdateBoard("F2","F5") #pawn
    game.Restart()
    #assert (repr(game.board.access_square("D1")) == "q")
    assert (repr(game.board.AccessSquare("E1")) == "k")
    assert (repr(game.board.AccessSquare("F2")) == "p")
    assert (repr(game.board.AccessSquare("C1"))=="b")
    
def test_IsMoved():
    game=Game()
    game.board.UpdateBoard("F2","F4")
    game.Restart()
    piece = game.board.AccessSquare("F2")
    assert (piece.hasMoved == False)


def test_GetFEN():
    board=ChessBoard()
    for i in range(32):
        pieceToDraw = list(piecesPosDict.keys())[i]
        squareToFill = piecesPosDict[pieceToDraw]
        board.OriginalDraw(pieceToDraw, squareToFill)
    assert(board.GiveFEN() == "RNBQKBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbqkbnr")
    board.UpdateBoard("E2","E4")
    assert(board.GiveFEN() == "RNBQKBNR/PPPPPPPP/8/8/4p3/8/pppp1ppp/rnbqkbnr")