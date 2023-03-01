

# Della_20_RandomAIUnitTests

from aiMoveGenerator import *
from PiecesPosDict import *
import pytest

def test_ai_move_generator():
    # Test all possible random moves from start of game position for black 
    board = MakeBoard()
    move = ai_move_generator(board, 'black')
    validMove = False
    index = 0
    startBlackMoves = ['A7_A6', 'A7_A5', 'B7_B6', 'B7_B5', 'C7_C6', 'C7_C5', 'D7_D6', 'D7_D5', 'E7_E6', 'E7_E5', 'F7_F6', 'F7_F5', 'G7_G6', 'G7_G5', 'H7_H6', 'H7_H5', 'nB8_A6', 'nB8_C6', 'nG8_F6', 'nG8_H6']
    startWhiteMoves = ['A2_A3', 'A2_A4', 'B2_B3', 'B2_B4', 'C2_C3', 'C2_C4', 'D2_D3', 'D2_D4', 'E2_E3', 'E2_E4', 'F2_F3', 'F2_F4', 'G2_G3', 'G2_G3', 'H2_H3', 'H2_H4', 'NB1_A3', 'NB8_C3', 'NG1_F3', 'NG1_H3']
    for i in startBlackMoves:
        if move == startBlackMoves[index]:
            validMove = True
        index += 1
    assert(validMove)
    # Test all possible random moves from start of game position for 
    board = MakeBoard()
    move = ai_move_generator(board, 'white')
    validMove = False
    index = 0
    for i in startWhiteMoves:
        if move == startWhiteMoves[index]:
            validMove = True
        index += 1
    assert(validMove)

def test_get_chess_notation(): 
    # The coords (2, 2) should return the chess notation 'C3'
    coords = (2, 2)
    assert (get_chess_notation(coords)) == 'C3' 
    # The coords (6, 0) should return the chess notation 'A7'
    coords = (6, 0)
    assert (get_chess_notation(coords)) == 'A7' 
    # The coords (4, 3) should return the chess notation 'D5'
    coords = (4, 3)
    assert (get_chess_notation(coords)) == 'D5' 

def test_get_piece_array():
    # Returns all pieces that are of the colour black on the currentBoard
    # Black pieces
    board = MakeBoard()
    assert(get_piece_array(board, 'black')) == [[6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7]]
    # White pieces
    board = MakeBoard()
    assert(get_piece_array(board, 'white')) == [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]

def test_get_coords():
    # The chess notation 'C3' should return the coords (2, 2)
    notation = 'C3'
    assert(get_coords(notation)) == [(2, 2)]  
    # The chess notation 'A7' should return the coords (6, 0)
    notation = 'A7'
    assert(get_coords(notation)) == [(6, 0)]
    # The chess notation 'D5' should return the coords (4, 3)
    notation = 'D5'
    assert(get_coords(notation)) == [(4, 3)]

def test_valid_pawn_move():
    # Check valid pawn moves from 'F7' with black pawn @ start of game
    board = MakeBoard()
    pieces_array = get_piece_array(board, 'black')
    piece = pieces_array[5]
    piece_name = board.board[piece[0]][piece[1]].placed_in_square
    move = valid_pawn_move(piece_name, board, 'F7')
    if move == 'F6':
        assert(move_checker(board, "F7", move))
    elif move == 'F5':
        assert(move_checker(board, "F7", move)) 

    # Check valid pawn moves from 'F2' with white pawn @ start of game
    board = MakeBoard()
    pieces_array = get_piece_array(board, 'black')
    piece = pieces_array[5]
    piece_name = board.board[piece[0]][piece[1]].placed_in_square
    move = valid_pawn_move(piece_name, board, 'F7')
    if move == 'F3':
        assert(move_checker(board, "F2", move))
    elif move == 'F4':
        assert(move_checker(board, "F2", move))                

def MakeBoard():
    board = ChessBoard()
    board.draw()
    for i in range(32):
        pieceToDraw = list(pieces_pos_dict.keys())[i]
        squareToFill = pieces_pos_dict[pieceToDraw]
        board.orginal_draw(pieceToDraw, squareToFill)
    board.draw()
    return board


