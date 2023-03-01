import pytest
from aiMoveGenerator import *
from PiecesPosDict import *
import unittest
from chessBoard import ChessBoard
from Pieces import Rook
from Pieces import Pawn
from Pieces import Knight
from square import square



def test_BasicMovement():
    board = MakeBoard()
    board.update_board("E8", "E5")  # update the board
    assert (move_checker(board, "E5", "D5"))   # check if it can move left
    assert (move_checker(board, "E5", "F5"))   # check if it can move right
    assert (move_checker(board, "E5", "E6"))   # check if it can move up
    assert (move_checker(board, "E5", "E4"))   # check if it can move down
    assert (move_checker(board, "E5", "F6"))   # check if it can move right up
    assert (move_checker(board, "E5", "D6"))   # check if it can move left up
    assert (move_checker(board, "E5", "F4"))   # check if it can move right down
    assert (move_checker(board, "E5", "D4"))   # check if it can move left down
    assert (not move_checker(board, "E5", "C5"))   # check if it can move two


def test_KnightChecks():
    board = MakeBoard()
    board.update_board("E7", "E6")  # update the board
    board.update_board("E8", "E7")  # update the board
    assert (move_checker(board, "E7", "D6"))  # try to move king into open square
    board.update_board("B1", "C4")  # move knight near king
    assert (not move_checker(board, "E7", "D6"))  # try to move king into knight check


def test_StraightChecks():
    board = MakeBoard()
    board.update_board("E8", "E5")  # move king into the middle
    board.update_board("A1", "D3")  # move rook near middle
    assert (move_checker(board, "E5", "D5")) == False  # move king into rook check
    board.update_board("D8", "D4")  # block future rook check with our queen
    assert (move_checker(board, "E5", "D5")) # move king into now blocked off no check


def test_DiagonalChecks():
    board = MakeBoard()
    board.update_board("E8", "E5")  # move king into the middle
    board.update_board("F1", "B3")  # move bishop near king
    assert (not move_checker(board, "E5", "D5"))  # move king into bishop check
    board.update_board("D8", "C4")  # block future bishop check with our queen
    assert (move_checker(board, "E5", "D5"))  # move king into now blocked off no check


def test_PawnChecks():
    board = MakeBoard()
    board.update_board("E8", "D6")  # move king into the middle
    board.update_board("F2", "C4")  # move pawn near king
    assert (not move_checker(board, "D6", "D5"))  # move king into pawn check
    assert (move_checker(board, "D6", "C5"))  # move king opposite pawn


def MakeBoard():
    board = ChessBoard()
    for i in range(32):
        piece_to_draw = list(pieces_pos_dict.keys())[i]
        square_to_fill = pieces_pos_dict[piece_to_draw]
        board.orginal_draw(piece_to_draw, square_to_fill)
    return board

# check for correct creation of board
def test_chessboard_init():
    cb = ChessBoard()
    assert len(cb.board) == 8  # Check if board has 8 rows
    assert len(cb.board[0]) == 8  # check if the board has 8 colums
    assert cb.board[0][0].square == "A1"  # check if the bottom left square is "A1"
    assert cb.board[7][7].square == "H8"  # Check the top right square is "H8"


def test_access_square_returns_piece():
    cb = ChessBoard()
    # Place piece in square B2
    cb.orginal_draw(Rook(False), "B2")
    # assert that access_square returns the piece in B2
    assert isinstance(cb.access_square("B2"), Rook)


def test_access_square_returns_none():
    cb = ChessBoard()
    # check that access_square returns None for an empty square
    assert cb.access_square("C3") is None


def test_orginal_draw():
    cb = ChessBoard()
    # place a white pawn on a2
    piece = Pawn(False)
    cb.orginal_draw(piece, "A2")  # place piece on A2
    assert isinstance(cb.access_square("A2"), Pawn)  # check if pawn object is on A2

    # Place a black pawn on h7
    piece = Pawn(True)
    cb.orginal_draw(piece, "H7")
    assert isinstance(cb.access_square("H7"), Pawn)  # checking for correct placement

    # placing the pawn on an invalid square (outside of the board)
    with pytest.raises(IndexError):
        cb.orginal_draw(piece, "I9")

    # Try placing a knight on a valid square
    piece = Knight(False)
    cb.orginal_draw(piece, "B1")
    assert isinstance(cb.access_square("B1"), Knight)  # check the knight's square


# update_board test case 1: Move a pawn from square A2 to A3
def test_update_board_pawn_move():
    cb = ChessBoard()
    pawn = Pawn(True)
    cb.orginal_draw(pawn, "A2")
    cb.update_board("A2", "A3")
    # check if the pawn is now on square A3 and that A2 is empty
    assert cb.access_square("A3") == pawn
    assert cb.access_square("A2") is None


# update_board test case 2: Move a rook from square H8 to E8
def test_update_board_rook_move():
    cb = ChessBoard()
    rook = Rook(False)
    #  place and move the rook 3 squares
    cb.orginal_draw(rook, "H8")
    cb.update_board("H8", "E8")
    assert cb.access_square("E8") == rook  # check rooks position
    assert cb.access_square("H8") is None  # check if previous position is empty


# update_board test case 3: Move a pawn from square H2 to H4 (2 spaces)
def test_update_board_pawn_move_two_spaces():
    cb = ChessBoard()
    pawn = Pawn(True)
    cb.orginal_draw(pawn, "H2")
    cb.update_board("H2", "H4")  # move pawn two sqaures
    # confirm the pawns movement of 2 squares
    assert cb.access_square("H4") == pawn
    assert cb.access_square("H2") is None


# update_board test case 3: move white pawn onto black pawn square, checking for correct capture
def test_update_board_capture_opponent():
    cb = ChessBoard()
    pawn1 = Pawn(False)  # white pawn
    pawn2 = Pawn(True)  # black pawn
    cb.orginal_draw(pawn1, "B2")
    cb.orginal_draw(pawn2, "C3")
    cb.update_board("B2", "C3")  # white pawn captures black pawn
    assert cb.access_square("C3") == pawn1  # checks if the piece on the square "C3" is pawn1
    assert cb.access_square("B2") is None  # Checks to see that the square B2 is empty
    captured_piece = cb.access_square("C3")
    assert captured_piece is not None  # checks that the captured piece is not none

    print(captured_piece)
    print(type(captured_piece))
    print(captured_piece.is_black)
    assert captured_piece.is_black is False  # Checks to see if the is_black attribute of the captured_piece
    # object is false, which confrims that the captured piece was the black pawn


# test creation of a square
def test_square_init():
    s = square("A1")
    assert s.square == "A1"
    assert s.placed_in_square is None


def test_place_piece():
    # Create a square object and put a piece on it
    s = square("A1")
    piece1 = Pawn(True)
    s.place_piece(piece1)
    # check that the piece is placed in the square
    assert s.placed_in_square == piece1
    # make another piece and place it on the square, which already has a piece
    piece2 = Rook(False)
    s.place_piece(piece2)
    # check to see if the second piece takes the place of the first piece
    assert s.placed_in_square == piece2


def test_move_off_square():
    # Test case 1: No piece on square
    s = square("A1")
    piece = s.move_off_square()
    assert piece is None

    # Test case 2: Piece on square
    s = square("A1")  # create a new square and place a piece on it
    piece = Pawn(True)
    s.place_piece(piece)
    s.move_off_square()  # move the piece off the square
    assert s.placed_in_square is None  # check that the piece was removed from the square


def test_get_piece():
    # Test case 1: No piece on square
    s = square("A1")
    assert s.get_piece() is None  # check that no piece is on the square

    # Test case 2: Piece on square
    s = square("A1")
    piece = Pawn(True)
    s.place_piece(piece)  # place the pawn on the square
    assert s.get_piece() == piece  # check that the pawn is on the square

def test_Get_fen():
    board=ChessBoard()
    for i in range(32):
        piece_to_draw = list(pieces_pos_dict.keys())[i]
        square_to_fill = pieces_pos_dict[piece_to_draw]
        board.orginal_draw(piece_to_draw, square_to_fill)
    assert(board.GiveFEN() == "RNBQKBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbqkbnr")
    board.update_board("E2","E4")
    assert(board.GiveFEN() == "RNBQKBNR/PPPPPPPP/8/8/4p3/8/pppp1ppp/rnbqkbnr") 
