from moveChecker import *
from chessBoard import *
from PiecesPosDict import *

def test_superclass():
    
    test_board = create_test_board()
    assert(move_checker(test_board, "G1", "E0") == False)   # Illegal out of bounds, vertical
    assert(move_checker(test_board, "E3", "E4") == False)   # Empty square detectioin
    test_board.update_board("G1", "H3")
    assert(move_checker(test_board, "H3", "F2") == False)   # Illegal collision detection
    test_board.update_board("H3", "G5")
    assert(move_checker(test_board, "G5", "H7") == True)    # Taking legal
    assert(move_checker(test_board, "G5", "I6") == False)   # Illegal out of bounds, horizontal

# Pawn must have seperate tests for white / black, as movement direction changes with colour
def test_pawn():        
    test_board = create_test_board()
    assert(move_checker(test_board, "A2", "A3") == True)     # W. Legal move
    test_board.update_board("A2", "A3")
    assert(move_checker(test_board, "B2", "B4") == True)     # W. Legal first double move
    test_board.update_board("B2", "B4")
    assert(move_checker(test_board, "A3", "A5") == False)    # W. Illegal second double move
    test_board.update_board("B7", "B5")
    assert(move_checker(test_board, "B4", "B5") == False)    # W. Illegal forward take
    assert(move_checker(test_board, "B4", "A5") == False)    # W. Illegal diagonal move
    test_board.update_board("A7", "A5")
    assert(move_checker(test_board, "B4", "A5") == True)     # W. Legal diagonal take

    assert(move_checker(test_board, "H7", "H6") == True)     # B. Legal move
    test_board.update_board("H7", "H6")
    assert(move_checker(test_board, "G7", "G5") == True)     # B. Legal first double move
    test_board.update_board("G7", "G5")
    assert(move_checker(test_board, "H6", "H4") == False)    # B. Illegal second double move
    test_board.update_board("G2", "G4")
    assert(move_checker(test_board, "G5", "G4") == False)    # B. Illegal forward take
    assert(move_checker(test_board, "G5", "H4") == False)    # B. Illegal diagonal move
    test_board.update_board("H2", "H4")
    assert(move_checker(test_board, "G5", "H4") == True)     # B. Legal diagonal take
    
def test_knight():
    test_board = create_test_board()
    test_board.update_board("B1", "C3")
    assert(move_checker(test_board, "C3", "A5") == False)    # Illegal moves, vertical...
    assert(move_checker(test_board, "C3", "C5") == False)
    assert(move_checker(test_board, "C3", "E5") == False)
    assert(move_checker(test_board, "C3", "B4") == False)
    assert(move_checker(test_board, "C3", "C4") == False)
    assert(move_checker(test_board, "C3", "D4") == False)
    assert(move_checker(test_board, "C3", "B5") == True)     # Legal moves...
    assert(move_checker(test_board, "C3", "D5") == True)
    
    test_board.update_board("C3", "E4")
    assert(move_checker(test_board, "E4", "C4") == False)    # Illegal moves, horizontal...
    assert(move_checker(test_board, "E4", "D4") == False)
    assert(move_checker(test_board, "E4", "C3") == True)     # Legal moves...
    assert(move_checker(test_board, "E4", "C5") == True)
    
    
def test_rook():
    test_board = create_test_board()
    assert(move_checker(test_board, "A1", "A3") == False)    # Illegal move, jumping
    test_board.update_board("A2", "A4")
    assert(move_checker(test_board, "A1", "A3") == True)     # Legal move, vertical
    test_board.update_board("A1", "A3")
    assert(move_checker(test_board, "A3", "D4") == False)    # Illegal move
    assert(move_checker(test_board, "A3", "D6") == False)    # Illegal move, diagonal
    assert(move_checker(test_board, "A3", "C3") == True)     # Legal move, horizonal
    test_board.update_board("A3", "C3")
    test_board.update_board("B8", "C6")
    assert(move_checker(test_board, "C3", "C7") == False)    # Illegal take, vertical jumping
    test_board.update_board("C6", "B8")
    assert(move_checker(test_board, "C3", "C7") == True)     # Legal take
    
    
def test_bishop():
    test_board = create_test_board()
    assert(move_checker(test_board, "C1", "F4") == False)    # Illegal move, jumping
    test_board.update_board("D2", "D3")
    assert(move_checker(test_board, "C1", "F4") == True)     # Legal move
    test_board.update_board("C1", "F4")
    assert(move_checker(test_board, "F4", "D5") == False)    # Illegal move
    assert(move_checker(test_board, "F4", "H4") == False)    # Illegal move, horizontal
    assert(move_checker(test_board, "F4", "F3") == False)    # Illegal move, vertical
    assert(move_checker(test_board, "F4", "B8") == False)    # Illegal take, jumping
    test_board.update_board("C7", "C6")
    assert(move_checker(test_board, "F4", "B8") == True)     # Legal take
    
def test_queen():
    test_board = create_test_board()
    assert(move_checker(test_board, "D1", "F3") == False)    # Illegal move, diagonal jumping
    assert(move_checker(test_board, "D1", "D3") == False)    # Illegal move, vertical jumping
    test_board.update_board("D2", "D4")
    assert(move_checker(test_board, "D1", "D3") == True)     # Legal move, vertical
    test_board.update_board("D1", "D3")
    assert(move_checker(test_board, "D3", "C4") == True)     # Legal move, diagonal
    test_board.update_board("D3", "C4")
    assert(move_checker(test_board, "C4", "A4") == True)     # Legal move, horizontal
    assert(move_checker(test_board, "C4", "E4") == False)    # Illegal move, horizontal jumping
    assert(move_checker(test_board, "C4", "A5") == False)    # Illegal move
    
    test_board.update_board("B8", "C6")
    assert(move_checker(test_board, "C4", "C7") == False)    # Illegal take, vertical jumping
    test_board.update_board("C6", "B4")
    assert(move_checker(test_board, "C4", "C7") == True)     # Legal take, vertical 
    assert(move_checker(test_board, "C4", "G8") == False)    # Illegal take, diagonal jumping
    test_board.update_board("F7", "F6")
    assert(move_checker(test_board, "C4", "G8") == True)     # Legal take, diagonal  
    test_board.update_board("A7", "A5")
    test_board.update_board("A5", "A4")
    assert(move_checker(test_board, "C4", "A4") == False)    # Illegal take, horizontal jumping
    test_board.update_board("B4", "A6")
    assert(move_checker(test_board, "C4", "A4") == True)     # Legal take, horizontal
    
    
    
def create_test_board():
    test_board = ChessBoard()
    test_board.draw()

    for i in range(32):
        piece_to_draw = list(pieces_pos_dict.keys())[i]
        square_to_fill = pieces_pos_dict[piece_to_draw]
        test_board.orginal_draw(piece_to_draw, square_to_fill)
        
    return test_board