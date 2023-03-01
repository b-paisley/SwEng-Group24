

# Della_20_RandomAIUnitTests

from chessBoard import *
from Points import *
from Pieces import *
from moveChecker import *
from aiMoveGenerator import *
from PiecesPosDict import *
import unittest

def make_board():
    board = ChessBoard()
    board.draw()
    for i in range(32):
        piece_to_draw = list(pieces_pos_dict.keys())[i]
        square_to_fill = pieces_pos_dict[piece_to_draw]
        board.orginal_draw(piece_to_draw, square_to_fill)
    board.draw()
    return board

class TestStringMethods(unittest.TestCase):

    def test_ai_move_generator(self):
        board = make_board()
        move = ai_move_generator(board, 'black')
        self.assertEqual( move_checker(board, move[0:2], move[3:5]), True ) # check if it can move left

    def test_get_chess_notation(self): 
        coords = (2,2)
        self.assertEqual(get_chess_notation(coords), 'C3')

    def test_get_coords(self):
        notation = 'C3'
        self.assertEqual(get_coords(notation), [[2, 2]])   

    def test_get_piece_array(self):
        board = make_board()
        self.assertEqual(get_piece_array(board, 'black'), [[6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7]]) 
    
    def test_valid_pawn_move(self):
        board = make_board()
        pieces_array = get_piece_array(board, 'black')
        piece_name = pieces_array[53]
        move = valid_pawn_move(piece_name, board, 'F7')
        self.assertEqual(move_checker(board, "F7", move), True)                
	

if __name__ == '__main__':
    unittest.main()


