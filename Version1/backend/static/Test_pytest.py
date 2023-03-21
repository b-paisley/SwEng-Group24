import pytest
import unittest
from chessBoard import *
from Game import *
from square import *
from Pieces import *
from PiecesPosDict import *

def test_ResetSqaure():
    game = Game()
    game.board.update_board("D1","C4")
    square="C4"
    letter_file = ord(square[0])-65
    number_row = int(square[1]) - 1
    square_obj=game.board.board[number_row][letter_file]
    square_obj.reset_square()
    assert (game.board.board[number_row][letter_file].placed_in_square ) == None

def test_Restart():
    game = Game()
    #game.board.update_board("D1","C4") #queen

    game.board.update_board("C1","B3") #bishop
    game.board.update_board("E1","F4") #king
    game.board.update_board("F2","F5") #pawn
    game.restart()
    #assert (repr(game.board.access_square("D1")) == "q")
    assert (repr(game.board.access_square("E1")) == "k")
    assert (repr(game.board.access_square("F2")) == "p")
    assert (repr(game.board.access_square("C1"))=="b")
    
def test_IsMoved():
    game=Game()
    game.board.update_board("F2","F4")
    game.restart()
    piece = game.board.access_square("F2")
    assert (piece.has_moved == False)


