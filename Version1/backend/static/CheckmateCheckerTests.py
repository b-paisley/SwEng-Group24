import pytest
from CheckmateChecker import *
from PiecesPosDict import *

def test_CheckmateChecker():
    tempBoard =MakeBoard()
    # King not in check
    board = tempBoard
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate) == False

    # Horse and Rook Checkmate
    board = tempBoard
    board.update_board('B2', 'B5')
    board.update_board('A1', 'B2')
    board.update_board('E8', 'A1')
    board.update_board('B1', 'B3')
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate)

    # Pawn checkmate
    board = tempBoard
    board.update_board('E8', 'A6')
    board.update_board('A2', 'A5')
    board.update_board('B2', 'B5')
    board.update_board('C2', 'B4')
    board.update_board('D2', 'C4')
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate)

    # Bishop - Queen checkmate
    board = tempBoard
    board.update_board('E8', 'A5')
    board.update_board('A1', 'A3')
    board.update_board('H1', 'E5')
    board.update_board('D1', 'C3')
    board.update_board('F1', 'D3')
    board.update_board('C1', 'E3')
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate)

    # Queen Blocks
    board = tempBoard
    board.update_board('E8', 'E4')
    board.update_board('D8', 'F6')
    board.update_board('A1', 'G4')
    board.update_board('H1', 'A5')
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate) == False

    # diag bishop check with bishop and queen either side 
    board = tempBoard
    board.update_board('E8', 'A6')
    board.update_board('D8', 'C6')
    board.update_board('C1', 'D3')
    board.update_board('F1', 'C3')
    board.update_board('D1', 'E3')
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate) == False

    #vertical rook test (block)
    board = tempBoard
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
    board = tempBoard
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
