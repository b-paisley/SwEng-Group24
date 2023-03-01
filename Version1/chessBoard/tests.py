

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
        # Test all possible random moves from start of game
        board = make_board()
        move = ai_move_generator(board, 'black')
        if move == 'A7_A6':
            self.assertEqual( move_checker(board, move[0:2], move[3:5]), True ) 
        elif move == 'A7_A5':
            self.assertEqual( move_checker(board, move[0:2], move[3:5]), True ) 
        elif move == 'B7_B6':
            self.assertEqual( move_checker(board, move[0:2], move[3:5]), True ) 
        elif move == 'B7_B5':
            self.assertEqual( move_checker(board, move[0:2], move[3:5]), True )
        elif move == 'C7_C6':
            self.assertEqual( move_checker(board, move[0:2], move[3:5]), True ) 
        elif move == 'C7_C5':
            self.assertEqual( move_checker(board, move[0:2], move[3:5]), True )
        elif move == 'D7_D6':
            self.assertEqual( move_checker(board, move[0:2], move[3:5]), True ) 
        elif move == 'D7_D5':
            self.assertEqual( move_checker(board, move[0:2], move[3:5]), True )
        elif move == 'E7_E6':
            self.assertEqual( move_checker(board, move[0:2], move[3:5]), True ) 
        elif move == 'E7_E5':
            self.assertEqual( move_checker(board, move[0:2], move[3:5]), True )
        elif move == 'F7_F6':
            self.assertEqual( move_checker(board, move[0:2], move[3:5]), True ) 
        elif move == 'F7_F5':
            self.assertEqual( move_checker(board, move[0:2], move[3:5]), True )
        elif move == 'H7_H6':
            self.assertEqual( move_checker(board, move[0:2], move[3:5]), True ) 
        elif move == 'H7_H5':
            self.assertEqual( move_checker(board, move[0:2], move[3:5]), True )
        elif move == 'B8_A6':
            self.assertEqual( move_checker(board, move[0:2], move[3:5]), True ) 
        elif move == 'B8_C6':
            self.assertEqual( move_checker(board, move[0:2], move[3:5]), True )
        elif move == 'F8_E6':
            self.assertEqual( move_checker(board, move[0:2], move[3:5]), True ) 
        elif move == 'F8_H6':
            self.assertEqual( move_checker(board, move[0:2], move[3:5]), True )

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
        # Check valid pawn moves from 'F7' @ start of game
        board = make_board()
        pieces_array = get_piece_array(board, 'black')
        piece = pieces_array[5]
        piece_name = board.board[piece[0]][piece[1]].placed_in_square
        move = valid_pawn_move(piece_name, board, 'F7')
        if move == 'F6':
            self.assertEqual(move_checker(board, "F7", move), True)
        elif move == 'F5':
            self.assertEqual(move_checker(board, "F7", move), True)                
	

if __name__ == '__main__':
    unittest.main()


