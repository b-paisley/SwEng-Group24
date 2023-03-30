import pytest
from aiMoveGenerator import *
from PiecesPosDict import *
import unittest
from chessBoard import *
from Pieces import *
from Game import *
from square import square
from moveChecker import *
from app import app # Flask instance of the API
 
def MakeBoard1():
  board = ChessBoard()
  for i in range(8):
    for j in range(8):
        board.board[i][j].ResetSquare()
  for i in range(10):
    pieceToDraw = list(piecesPosDict1.keys())[i]
    squareToFill = piecesPosDict1[pieceToDraw]
    board.OriginalDraw(pieceToDraw, squareToFill)
  return board

def MakeBoard2():
  board = ChessBoard()
  for i in range(8):
    for j in range(8):
        board.board[i][j].ResetSquare()
  for i in range(3):
    pieceToDraw = list(piecesPosDict2.keys())[i]
    squareToFill = piecesPosDict2[pieceToDraw]
    board.OriginalDraw(pieceToDraw, squareToFill)
  return board

def MakeBoard3():
  board = ChessBoard()
  for i in range(8):
    for j in range(8):
        board.board[i][j].ResetSquare()
  for i in range(3):
    pieceToDraw = list(piecesPosDict3.keys())[i]
    squareToFill = piecesPosDict3[pieceToDraw]
    board.OriginalDraw(pieceToDraw, squareToFill)
  return board

def test_StalemateChecker():
    board = MakeBoard()
    stalemate = StalemateChecker(board, 'black')
    assert(stalemate) == False

    board = MakeBoard1()
    stalemate = StalemateChecker(board, 'black')
    assert(stalemate)

    board = MakeBoard2()
    stalemate = StalemateChecker(board, 'black')
    assert(stalemate)

    board = MakeBoard3()
    stalemate = StalemateChecker(board, 'black')
    assert(stalemate)

def MakeBoard():
  board = ChessBoard()
  for i in range(8):
    for j in range(8):
        board.board[i][j].ResetSquare()
  for i in range(32):
    pieceToDraw = list(piecesPosDict.keys())[i]
    squareToFill = piecesPosDict[pieceToDraw]
    board.OriginalDraw(pieceToDraw, squareToFill)
  return board



