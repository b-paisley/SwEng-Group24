from Pieces import *
import pytest


def test_piece_captures():
    piece_one = Pawn(False)
    piece_two = Pawn(True)
    piece_one.capture(piece_two)
    
    assert piece_two.is_captured

def test_pawn():
    pawns = [Pawn(False) for i in range(4)]

    # Test string representation
    assert repr(pawns[0]) == 'p'

    # Check promotion
    notation_pieces_dict = {
        'R': Rook,
        'N': Knight,
        'B': Bishop,
        'Q': Queen
    }
    pawns[0].promote('R')
    print(pawns[0].__class__)
    assert isinstance(pawns[0],Rook)

    pawns[1].promote('N')
    assert isinstance(pawns[1],Knight)

    pawns[2].promote('B')
    assert isinstance(pawns[2],Bishop)

    pawns[3].promote('Q')
    assert isinstance(pawns[3],Queen)

def test_rook():
    rook = Rook(False)
    # Test string representation
    assert repr(rook) == 'r'

def test_knight():
    knight = Knight(False)
    # Test string representation
    assert repr(knight) == 'n'

def test_bishop():
    bishop = Bishop(False)
    # Test string representation
    assert repr(bishop) == 'b'

def test_queen():
    queen = Queen(False)
    # Test string representation
    assert repr(queen) == 'q'

def test_king():
    king = King(False)
    # Test string representation
    assert repr(king) == 'k'