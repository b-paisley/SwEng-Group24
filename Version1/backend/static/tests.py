import pytest
from aiMoveGenerator import *
from PiecesPosDict import *
import unittest
from chessBoard import *
from Pieces import *
from Game import *
from square import square
from moveChecker import *
#from app import app # Flask instance of the API
from StalemateChecker import *

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

def test_CheckmateChecker():
    board = MakeBoard()
    # King not in check
    board = MakeBoard()
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate) == False
    
    # Horse Block
    board.UpdateBoard('D8', 'H5')
    board.UpdateBoard('D1', 'E4')
    board.UpdateBoard('E7', 'H6')
    board.UpdateBoard('A8', 'D8')
    board.UpdateBoard('G7', 'F8')
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate) == False

    # King takes pawn putting it in check
    board.UpdateBoard('F8', 'G7')
    board.UpdateBoard('D8', 'A8')
    board.UpdateBoard('H6', 'E7')
    board.UpdateBoard('E4', 'D1')
    board.UpdateBoard('H5', 'D8')

    board.UpdateBoard('E8', 'E6')
    board.UpdateBoard('B2', 'D5')
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate) == False

    # Pawn Checkmate
    board.UpdateBoard('D5', 'B2')
    board.UpdateBoard('E6', 'E8')

    board.UpdateBoard('E8', 'A6')
    board.UpdateBoard('A2', 'A5')
    board.UpdateBoard('B2', 'B5')
    board.UpdateBoard('C2', 'B4')
    board.UpdateBoard('D2', 'C4')
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate)

    # Bishop - Queen checkmate
    board.UpdateBoard('C4', 'D2')
    board.UpdateBoard('B4', 'C2')
    board.UpdateBoard('B5', 'B2')
    board.UpdateBoard('A5', 'A2')
    board.UpdateBoard('A6', 'E8')

    board.UpdateBoard('E8', 'A5')
    board.UpdateBoard('A1', 'A3')
    board.UpdateBoard('H1', 'E5')
    board.UpdateBoard('D1', 'C3')
    board.UpdateBoard('F1', 'D3')
    board.UpdateBoard('C1', 'E3')
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate)

    # Queen Blocks
    board.UpdateBoard('E3', 'C1')
    board.UpdateBoard('D3', 'F1')
    board.UpdateBoard('C3', 'D1')
    board.UpdateBoard('E5', 'H1')
    board.UpdateBoard('A3', 'A1')
    board.UpdateBoard('A5', 'E8')

    board.UpdateBoard('E8', 'E4')
    board.UpdateBoard('D8', 'F6')
    board.UpdateBoard('A1', 'G4')
    board.UpdateBoard('H1', 'A5')
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate) == False

    # diag bishop check with bishop and queen either side
    board.UpdateBoard('A5', 'H1')
    board.UpdateBoard('G4', 'A1')
    board.UpdateBoard('F6', 'D8')
    board.UpdateBoard('E4', 'E8')

    board.UpdateBoard('E8', 'A6')
    board.UpdateBoard('D8', 'C6')
    board.UpdateBoard('C1', 'D3')
    board.UpdateBoard('F1', 'C3')
    board.UpdateBoard('D1', 'E3')
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate) == False

    #vertical rook test (block)
    board.UpdateBoard('E3', 'D1')
    board.UpdateBoard('C3', 'F1')
    board.UpdateBoard('D3', 'C1')
    board.UpdateBoard('C6', 'D8')
    board.UpdateBoard('A6', 'E8')

    board.UpdateBoard('E8', 'A4')
    board.UpdateBoard('D8', 'F5')
    board.UpdateBoard('A1', 'A6')
    board.UpdateBoard('H1', 'B6')
    board.UpdateBoard('B7', 'C6')
    board.UpdateBoard('B8', 'A8')
    board.UpdateBoard('C8', 'B8')
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate) == False

    # Pawn takes bishop putting King in check
    board.UpdateBoard('B8', 'C8')
    board.UpdateBoard('A8', 'B8')
    board.UpdateBoard('C6', 'B7')
    board.UpdateBoard('B6', 'H1')
    board.UpdateBoard('A6', 'A1')
    board.UpdateBoard('F5', 'D8')
    board.UpdateBoard('A4', 'E8')

    board.UpdateBoard('E8', 'B3')
    board.UpdateBoard('C1', 'F4')
    board.UpdateBoard('G7', 'G5')
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate) == False



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

def MakeBoard4():
  board = ChessBoard()
  for i in range(8):
    for j in range(8):
        board.board[i][j].ResetSquare()
  for i in range(10):
    pieceToDraw = list(piecesPosDict4.keys())[i]
    squareToFill = piecesPosDict4[pieceToDraw]
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

 



