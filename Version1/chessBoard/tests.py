import pytest
from aiMoveGenerator import *
from PiecesPosDict import *
import unittest
from chessBoard import *
from Pieces import *
from square import square
from moveChecker import *
from allMovesFinder import *


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
        piece_to_draw.has_moved = False
        square_to_fill = pieces_pos_dict[piece_to_draw]
        test_board.orginal_draw(piece_to_draw, square_to_fill)
        
    test_board.draw()    
        
    return test_board

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

def test_all_moves_finder_pawn():
    test_board = create_test_board()
    assert(allMovesFinder(test_board, "B2") == ["B3", "B4"])    # All valid White B-Pawn moves
    assert(allMovesFinder(test_board, "D7") == ["D5", "D6"])    # All valid Black D-Pawn moves
    
    test_board.update_board("B7", "B5")
    test_board.update_board("B5", "B4")
    
    assert(allMovesFinder(test_board, "B2") == ["B3"])          # White B-Pawn double move blocked
    test_board.update_board("B4", "B3")
    assert(allMovesFinder(test_board, "B2") == [])              # All White B-Pawn moves blocked
    test_board.update_board("D2", "D4")
    test_board.update_board("D4", "D5")
    assert(allMovesFinder(test_board, "D7") == ["D6"])          # Black D-Pawn double move blocked
    test_board.update_board("D5", "D6")
    assert(allMovesFinder(test_board, "D7") == [])              # All Black D-Pawn moves blocked
    
    assert(allMovesFinder(test_board, "A2") == ["A3", "A4", "xB3"])  # All White A-Pawn moves, including +file take
    assert(allMovesFinder(test_board, "C2") == ["C3", "C4", "xB3"])  # All White C-Pawn moves, including -file take
    assert(allMovesFinder(test_board, "C7") == ["C5", "C6", "xD6"])  # All Black C-Pawn moves, including +file take
    assert(allMovesFinder(test_board, "E7") == ["E5", "E6", "xD6"])  # All Black E-Pawn moves, including -file take
    
def test_all_moves_finder_knight():
    test_board = create_test_board()
    assert(allMovesFinder(test_board, "B1") == ["A3", "C3"])         # All White B-Knight moves
    assert(allMovesFinder(test_board, "G1") == ["F3", "H3"])         # All White B-Knight moves
    assert(allMovesFinder(test_board, "B8") == ["A6", "C6"])         # All White B-Knight moves
    assert(allMovesFinder(test_board, "G8") == ["F6", "H6"])         # All White B-Knight moves
    test_board.update_board("B1", "C3")
    assert(allMovesFinder(test_board, "C3") == ["A4", "B1", "B5", "D5", "E4"])   # All White C-Knight moves
    test_board.update_board("C3", "D5")
    # All White D-Knight moves, inc takes
    assert(allMovesFinder(test_board, "D5") == ["B4", "B6", "C3", "E3", "F4", "F6", "xC7", "xE7"]) 
    
def test_all_moves_finder_rook():
    test_board = create_test_board()
    assert(allMovesFinder(test_board, "A1") == [])    # No moves available for White Rook
    test_board.update_board("A2", "A4")
    assert(allMovesFinder(test_board, "A1") == ["A2", "A3"])                         # Vertical Moves + Collision
    test_board.update_board("A1", "A3")
    assert(allMovesFinder(test_board, "A3") == ["A1", "A2", "B3", "C3", "D3", 
                                                "E3", "F3", "G3", "H3"])             # Horizontal Moves
    test_board.update_board("A3", "D3")
    assert(allMovesFinder(test_board, "D3") == ["A3", "B3", "C3", "D4", "D5", "D6",
                                                "E3", "F3", "G3", "H3", "xD7"])      # All Moves + Taking
    
def test_all_moves_finder_bishop():
    test_board = create_test_board()
    assert(allMovesFinder(test_board, "C1") == [])    # No moves available for White Rook
    test_board.update_board("D2", "D3")
    assert(allMovesFinder(test_board, "C1") == ["D2", "E3", "F4", "G5", "H6"]) # Diagonal opened
    test_board.update_board("C1", "F4")
    assert(allMovesFinder(test_board, "F4") == ["C1", "D2", "D6", "E3", "E5", 
                                                "G3", "G5", "H6", "xC7"])             # Both Diagonals + Taking
    
def test_all_moves_finder_queen():
    test_board = create_test_board()
    assert(allMovesFinder(test_board, "D1") == [])    # No moves available for White Queen
    test_board.update_board("E2", "E3")
    assert(allMovesFinder(test_board, "D1") == ["E2", "F3", "G4", "H5"])        # Diagonal Opened
    test_board.update_board("D1", "G4")
    assert(allMovesFinder(test_board, "G4") == ["A4", "B4", "C4", "D1", "D4", "E2",
                                                "E4", "E6", "F3", "F4", "F5", "G3", 
                                                "G5", "G6", "H3", "H4", "H5", "xD7",
                                                "xG7"])        # All directions + Taking