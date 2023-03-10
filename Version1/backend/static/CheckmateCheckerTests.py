import pytest
from CheckmateChecker import *
from PiecesPosDict import *

def test_CheckmateChecker():
    # King not in check
    board = MakeBoard()
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate) == False

    # Horse and Rook Checkmate
    board.update_board('B2', 'B5')
    board.update_board('A1', 'B2')
    board.update_board('E8', 'A1')
    board.update_board('B1', 'B3')
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate)

    # Pawn checkmate
    board.update_board('B3', 'B1')
    board.update_board('A1', 'E8')
    board.update_board('B2', 'A1')
    board.update_board('B5', 'B2')
    
    board.update_board('E8', 'A6')
    board.update_board('A2', 'A5')
    board.update_board('B2', 'B5')
    board.update_board('C2', 'B4')
    board.update_board('D2', 'C4')
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate)

    # Bishop - Queen checkmate
    board.update_board('C4', 'D2')
    board.update_board('B4', 'C2')
    board.update_board('B5', 'B2')
    board.update_board('A5', 'A2')
    board.update_board('A6', 'E8')

    board.update_board('E8', 'A5')
    board.update_board('A1', 'A3')
    board.update_board('H1', 'E5')
    board.update_board('D1', 'C3')
    board.update_board('F1', 'D3')
    board.update_board('C1', 'E3')
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate)

    # Queen Blocks
    board.update_board('E3', 'C1')
    board.update_board('D3', 'F1')
    board.update_board('C3', 'D1')
    board.update_board('E5', 'H1')
    board.update_board('A3', 'A1')
    board.update_board('A5', 'E8')

    board.update_board('E8', 'E4')
    board.update_board('D8', 'F6')
    board.update_board('A1', 'G4')
    board.update_board('H1', 'A5')
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate) == False

    # diag bishop check with bishop and queen either side 
    board.update_board('A5', 'H1')
    board.update_board('G4', 'A1')
    board.update_board('F6', 'D8')
    board.update_board('E4', 'E8')
    
    board.update_board('E8', 'A6')
    board.update_board('D8', 'C6')
    board.update_board('C1', 'D3')
    board.update_board('F1', 'C3')
    board.update_board('D1', 'E3')
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate) == False

    #vertical rook test (block)
    board.update_board('E3', 'D1')
    board.update_board('C3', 'F1')
    board.update_board('D3', 'C1')
    board.update_board('C6', 'D8')
    board.update_board('A6', 'E8')

    board.update_board('E8', 'A4')
    board.update_board('D8', 'F5')
    board.update_board('A1', 'A6')
    board.update_board('H1', 'B6')
    board.update_board('B7', 'C6')
    board.update_board('B8', 'A8')
    board.update_board('C8', 'B8')
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate) == False

    # Pawn takes bishop putting King in check
    board.update_board('B8', 'C8')
    board.update_board('A8', 'B8')
    board.update_board('C6', 'B7')
    board.update_board('B6', 'H1')
    board.update_board('A6', 'A1')
    board.update_board('F5', 'D8')
    board.update_board('A4', 'E8')

    board.update_board('E8', 'B3')
    board.update_board('C1', 'F4')
    board.update_board('G7', 'G5')
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate) == False

def MakeBoard():
    board = ChessBoard()
    for i in range(32):
        piece_to_draw = list(pieces_pos_dict.keys())[i]
        square_to_fill = pieces_pos_dict[piece_to_draw]
        board.orginal_draw(piece_to_draw, square_to_fill)
    board.draw()
    return board
