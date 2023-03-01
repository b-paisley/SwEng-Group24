import pytest
from aiMoveGenerator import *
from PiecesPosDict import *


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
