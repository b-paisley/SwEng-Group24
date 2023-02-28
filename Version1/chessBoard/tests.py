import unittest
from aiMoveGenerator import *
from PiecesPosDict import *


class TestStringMethods(unittest.TestCase):

    def test_basic_movement(self):
        board = make_board()
        board.update_board("E8", "E5")  # update the board
        self.assertTrue(move_checker(board, "E5", "D5"))  # check if it can move left
        self.assertTrue(move_checker(board, "E5", "F5"))  # check if it can move right
        self.assertTrue(move_checker(board, "E5", "E6"))  # check if it can move up
        self.assertTrue(move_checker(board, "E5", "E4"))  # check if it can move down
        self.assertTrue(move_checker(board, "E5", "F6"))  # check if it can move right up
        self.assertTrue(move_checker(board, "E5", "D6"))  # check if it can move left up
        self.assertTrue(move_checker(board, "E5", "F4"))  # check if it can move right down
        self.assertTrue(move_checker(board, "E5", "D4"))  # check if it can move left down
        self.assertFalse(move_checker(board, "E5", "C5"))  # check if it can move two
        # board.update_board("E5", "E8")  # undo moves

    def test_knight_checks(self):
        board = make_board()
        board.update_board("E7", "E6")  # update the board
        board.update_board("E8", "E7")  # update the board
        self.assertTrue(move_checker(board, "E7", "D6"))  # try to move king into open square
        board.update_board("B1", "C4")  # move knight near king
        self.assertFalse(move_checker(board, "E7", "D6"))  # try to move king into knight check

    def test_straight_checks(self):
        board = make_board()
        board.update_board("E8", "E5")  # move king into the middle
        board.update_board("A1", "D3")  # move rook near middle
        self.assertFalse(move_checker(board, "E5", "D5"))  # move king into rook check
        board.update_board("D8", "D4")  # block future rook check with our queen
        self.assertTrue(move_checker(board, "E5", "D5"))  # move king into now blocked off no check

    def test_diagonal_checks(self):
        board = make_board()
        board.update_board("E8", "E5")  # move king into the middle
        board.update_board("F1", "B3")  # move bishop near king
        self.assertFalse(move_checker(board, "E5", "D5"))  # move king into bishop check
        board.update_board("D8", "C4")  # block future bishop check with our queen
        self.assertTrue(move_checker(board, "E5", "D5"))  # move king into now blocked off no check

    def test_pawn_checks(self):
        board = make_board()
        board.update_board("E8", "D6")  # move king into the middle
        board.update_board("F2", "C4")  # move pawn near king
        self.assertFalse(move_checker(board, "D6", "D5"))  # move king into pawn check
        self.assertTrue(move_checker(board, "D6", "C5"))  # move king opposite pawn


if __name__ == '__main__':
    unittest.main()


def make_board():
    board = ChessBoard()
    for i in range(32):
        piece_to_draw = list(pieces_pos_dict.keys())[i]
        square_to_fill = pieces_pos_dict[piece_to_draw]
        board.orginal_draw(piece_to_draw, square_to_fill)
    return board
