import pytest
from aiMoveGenerator import *
from PiecesPosDict import *
import unittest
from chessBoard import *
from Pieces import *
from square import square
from moveChecker import *
from CheckmateChecker import *


def test_AiMoveGenerator():
    # Test all possible random moves from start of game position for black
    board = MakeBoard()
    move = AiMoveGenerator(board, 'black')
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
    move = AiMoveGenerator(board, 'white')
    validMove = False
    index = 0
    for i in startWhiteMoves:
        if move == startWhiteMoves[index]:
            validMove = True
        index += 1
    assert(validMove)

def test_GetChessNotation():
    # The coords (2, 2) should return the chess notation 'C3'
    coords = (2, 2)
    assert (GetChessNotation(coords)) == 'C3'
    # The coords (6, 0) should return the chess notation 'A7'
    coords = (6, 0)
    assert (GetChessNotation(coords)) == 'A7'
    # The coords (4, 3) should return the chess notation 'D5'
    coords = (4, 3)
    assert (GetChessNotation(coords)) == 'D5'

def test_GetPieceArray():
    # Returns all pieces that are of the colour black on the currentBoard
    # Black pieces
    board = MakeBoard()
    assert(GetPieceArray(board, 'black')) == [[6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7]]
    # White pieces
    board = MakeBoard()
    assert(GetPieceArray(board, 'white')) == [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]

def test_GetCoords():
    # The chess notation 'C3' should return the coords (2, 2)
    notation = 'C3'
    assert(GetCoords(notation)) == [(2, 2)]
    # The chess notation 'A7' should return the coords (6, 0)
    notation = 'A7'
    assert(GetCoords(notation)) == [(6, 0)]
    # The chess notation 'D5' should return the coords (4, 3)
    notation = 'D5'
    assert(GetCoords(notation)) == [(4, 3)]

def test_ValidPawnMove():
    # Check valid pawn moves from 'F7' with black pawn @ start of game
    board = MakeBoard()
    piecesArray = GetPieceArray(board, 'black')
    piece = piecesArray[5]
    pieceName = board.board[piece[0]][piece[1]].placedInSquare
    move = ValidPawnMove(pieceName, board, 'F7')
    if move == 'F6':
        assert(MoveChecker(board, "F7", move), 0)
    elif move == 'F5':
        assert(MoveChecker(board, "F7", move), 0)

    # Check valid pawn moves from 'F2' with white pawn @ start of game
    board = MakeBoard()
    piecesArray = GetPieceArray(board, 'black')
    piece = piecesArray[5]
    pieceName = board.board[piece[0]][piece[1]].placedInSquare
    move = ValidPawnMove(pieceName, board, 'F7')
    if move == 'F3':
        assert(MoveChecker(board, "F2", move), 0)
    elif move == 'F4':
        assert(MoveChecker(board, "F2", move), 0)



def test_BasicMovement():
    board = MakeBoard()
    board.UpdateBoard("E8", "E5")  # update the board
    assert (MoveChecker(board, "E5", "D5"), 0)   # check if it can move left
    assert (MoveChecker(board, "E5", "F5"), 0)   # check if it can move right
    assert (MoveChecker(board, "E5", "E6"), 0)   # check if it can move up
    assert (MoveChecker(board, "E5", "E4"), 0)   # check if it can move down
    assert (MoveChecker(board, "E5", "F6"), 0)   # check if it can move right up
    assert (MoveChecker(board, "E5", "D6"), 0)   # check if it can move left up
    assert (MoveChecker(board, "E5", "F4"), 0)   # check if it can move right down
    assert (MoveChecker(board, "E5", "D4"), 0)   # check if it can move left down
    assert (not MoveChecker(board, "E5", "C5"), 0)   # check if it can move two


def test_KnightChecks():
    board = MakeBoard()
    board.UpdateBoard("E7", "E6")  # update the board
    board.UpdateBoard("E8", "E7")  # update the board
    assert (MoveChecker(board, "E7", "D6"), 0)  # try to move king into open square
    board.UpdateBoard("B1", "C4")  # move knight near king
    assert (not MoveChecker(board, "E7", "D6"), 0)  # try to move king into knight check


def test_StraightChecks():
    board = MakeBoard()
    board.UpdateBoard("E8", "E5")  # move king into the middle
    board.UpdateBoard("A1", "D3")  # move rook near middle
    assert (MoveChecker(board, "E5", "D5"), 0) == False  # move king into rook check
    board.UpdateBoard("D8", "D4")  # block future rook check with our queen
    assert (MoveChecker(board, "E5", "D5"), 0) # move king into now blocked off no check


def test_DiagonalChecks():
    board = MakeBoard()
    board.UpdateBoard("E8", "E5")  # move king into the middle
    board.UpdateBoard("F1", "B3")  # move bishop near king
    assert (not MoveChecker(board, "E5", "D5"), 0)  # move king into bishop check
    board.UpdateBoard("D8", "C4")  # block future bishop check with our queen
    assert (MoveChecker(board, "E5", "D5"), 0)  # move king into now blocked off no check


def test_PawnChecks():
    board = MakeBoard()
    board.UpdateBoard("E8", "D6")  # move king into the middle
    board.UpdateBoard("F2", "C4")  # move pawn near king
    assert (not MoveChecker(board, "D6", "D5"), 0)  # move king into pawn check
    assert (MoveChecker(board, "D6", "C5"), 0)  # move king opposite pawn


def test_KingFakeChecks():
    board = MakeBoard()
    board.UpdateBoard("E8", "D6")  # move king into the middle
    board.UpdateBoard("E1", "C4")  # move pawn near king
    assert (not MoveChecker(board, "D6", "D5", 0))  # move king into "king" check
    assert (not MoveChecker(board, "D6", "C5", 0))


def test_CastlingAllowed():
    # assert we are allowed castle queenside white
    board = MakeBoard()
    board.UpdateBoard("D2", "D4")
    board.UpdateBoard("D1", "D3")
    board.UpdateBoard("C1", "D2")
    board.UpdateBoard("B1", "A3")
    assert (MoveChecker(board, "q", 1, 1))
    # assert we are allowed castle queenside black
    board = MakeBoard()
    board.UpdateBoard("D7", "D5")
    board.UpdateBoard("D8", "D6")
    board.UpdateBoard("C8", "D7")
    board.UpdateBoard("B8", "A6")
    assert (MoveChecker(board, "q", 0, 1))
    # assert we are allowed castle kingside white
    board = MakeBoard()
    board.UpdateBoard("E2", "E4")
    board.UpdateBoard("F1", "E2")
    board.UpdateBoard("G1", "H3")
    assert (MoveChecker(board, "k", 1, 1))
    # assert we are allowed castle kingside black
    board = MakeBoard()
    board.UpdateBoard("E7", "E5")
    board.UpdateBoard("F8", "F7")
    board.UpdateBoard("G8", "H6")
    assert (MoveChecker(board, "k", 0, 1))
    # castling with piece there
    board = MakeBoard()
    board.UpdateBoard("E2", "E3")
    board.UpdateBoard("F1", "E2")
    assert (not MoveChecker(board, "k", 1, 1))
    # Castling without rook
    board = MakeBoard()
    board.UpdateBoard("E2", "E3")
    board.UpdateBoard("F1", "E2")
    board.UpdateBoard("G1", "F3")
    board.UpdateBoard("H2", "H3")
    board.UpdateBoard("H1", "H2")
    assert (not MoveChecker(board, "k", 1, 1))
    # castling with rook having moved
    board = MakeBoard()
    board.UpdateBoard("E2", "E3")
    board.UpdateBoard("F1", "E2")
    board.UpdateBoard("G1", "F3")
    board.UpdateBoard("H2", "H3")
    board.UpdateBoard("H1", "H2")
    board.UpdateBoard("H2", "H1")
    assert (not MoveChecker(board, "k", 1, 1))
    # castling with king not there
    board = MakeBoard()
    board.UpdateBoard("E2", "E4")
    board.UpdateBoard("F1", "D3")
    board.UpdateBoard("G1", "F3")
    board.UpdateBoard("E1", "E2")
    assert (not MoveChecker(board, "k", 1, 1))
    # castling with king having moved
    board = MakeBoard()
    board.UpdateBoard("E2", "E4")
    board.UpdateBoard("F1", "D3")
    board.UpdateBoard("G1", "F3")
    board.UpdateBoard("E1", "E2")
    board.UpdateBoard("E2", "E1")
    assert (not MoveChecker(board, "k", 1, 1))
    # castling while in check
    board = MakeBoard()
    board.UpdateBoard("E2", "A4")
    board.UpdateBoard("F1", "D3")
    board.UpdateBoard("G1", "H3")
    board.UpdateBoard("D8", "E4")
    assert (not MoveChecker(board, "k", 1, 1))
    # castling while where king castles through is in check
    board = MakeBoard()
    board.UpdateBoard("E2", "A4")
    board.UpdateBoard("F1", "E2")
    board.UpdateBoard("G1", "H3")
    board.UpdateBoard("D8", "F4")
    board.UpdateBoard("F2", "A6")
    assert (not MoveChecker(board, "k", 1, 1))
    # castling while where king castles inTO check
    board = MakeBoard()
    board.UpdateBoard("E2", "A4")
    board.UpdateBoard("F1", "E2")
    board.UpdateBoard("G1", "H3")
    board.UpdateBoard("D8", "G4")
    board.UpdateBoard("G2", "A6")
    assert (not MoveChecker(board, "k", 1, 1))


def test_EnPassant():
    # Successful left
    board = MakeBoard()
    board.UpdateBoard("E2", "E5")
    board.UpdateBoard("D7", "D5")
    assert (MoveChecker(board, "E5", "D6", 0))
    # Successful right
    board = MakeBoard()
    board.UpdateBoard("E2", "E5")
    board.UpdateBoard("F7", "F5")
    assert (MoveChecker(board, "E5", "F6", 0))
    # Unsuccessful-wrong rank
    board = MakeBoard()
    board.UpdateBoard("E2", "E4")
    board.UpdateBoard("F7", "F5")
    assert (not MoveChecker(board, "E5", "F6", 0))
    # Unsuccessful-wrong rank
    board = MakeBoard()
    board.UpdateBoard("E2", "E6")
    board.UpdateBoard("F7", "F6")
    assert (not MoveChecker(board, "E6", "E5", 0))
    # opposite pawn didnt move last turn (Relies on has_moved_two_spaces_last function and therefore is not being tested rn)
    # board = MakeBoard()
    # board.UpdateBoard("E2", "E4")
    # board.UpdateBoard("D7", "D5")
    # board.UpdateBoard("E4", "E5")
    # board.UpdateBoard("D6", "D5")
    # assert (not move_checker(board, "E5", "D6", 0))
    # they didnt just move two (Relies on has_moved_two_spaces_last function and therefore is not being tested rn)
    # board = MakeBoard()
    # board.UpdateBoard("E2", "E5")
    # board.UpdateBoard("D7", "D6")
    # board.UpdateBoard("D6", "D5")
    # assert (not move_checker(board, "E5", "D6", 0))

def MakeBoard():
    board = ChessBoard()
    for i in range(32):
        pieceToDraw = list(piecesPosDict.keys())[i]
        squareToFill = piecesPosDict[pieceToDraw]
        board.OriginalDraw(pieceToDraw, squareToFill)
    return board

# check for correct creation of board
def test_ChessboardInit():
    cb = ChessBoard()
    assert len(cb.board) == 8  # Check if board has 8 rows
    assert len(cb.board[0]) == 8  # check if the board has 8 colums
    assert cb.board[0][0].square == "A1"  # check if the bottom left square is "A1"
    assert cb.board[7][7].square == "H8"  # Check the top right square is "H8"


def test_AccessSquareReturnsPiece():
    cb = ChessBoard()
    # Place piece in square B2
    cb.OriginalDraw(Rook(False), "B2")
    # assert that access_square returns the piece in B2
    assert isinstance(cb.AccessSquare("B2"), Rook)


def test_AccessSquareReturnsNone():
    cb = ChessBoard()
    # check that access_square returns None for an empty square
    assert cb.AccessSquare("C3") is None


def test_OrginalDraw():
    cb = ChessBoard()
    # place a white pawn on a2
    piece = Pawn(False)
    cb.OriginalDraw(piece, "A2")  # place piece on A2
    assert isinstance(cb.AccessSquare("A2"), Pawn)  # check if pawn object is on A2

    # Place a black pawn on h7
    piece = Pawn(True)
    cb.OriginalDraw(piece, "H7")
    assert isinstance(cb.AccessSquare("H7"), Pawn)  # checking for correct placement

    # placing the pawn on an invalid square (outside of the board)
    with pytest.raises(IndexError):
        cb.OriginalDraw(piece, "I9")

    # Try placing a knight on a valid square
    piece = Knight(False)
    cb.OriginalDraw(piece, "B1")
    assert isinstance(cb.AccessSquare("B1"), Knight)  # check the knight's square


# UpdateBoard test case 1: Move a pawn from square A2 to A3
def test_UpdateBoardPawn_move():
    cb = ChessBoard()
    pawn = Pawn(True)
    cb.OriginalDraw(pawn, "A2")
    cb.UpdateBoard("A2", "A3")
    # check if the pawn is now on square A3 and that A2 is empty
    assert cb.AccessSquare("A3") == pawn
    assert cb.AccessSquare("A2") is None


# UpdateBoard test case 2: Move a rook from square H8 to E8
def test_UpdateBoardRookMove():
    cb = ChessBoard()
    rook = Rook(False)
    #  place and move the rook 3 squares
    cb.OriginalDraw(rook, "H8")
    cb.UpdateBoard("H8", "E8")
    assert cb.AccessSquare("E8") == rook  # check rooks position
    assert cb.AccessSquare("H8") is None  # check if previous position is empty


# UpdateBoard test case 3: Move a pawn from square H2 to H4 (2 spaces)
def test_UpdateBoardPawnMoveTwoSpaces():
    cb = ChessBoard()
    pawn = Pawn(True)
    cb.OriginalDraw(pawn, "H2")
    cb.UpdateBoard("H2", "H4")  # move pawn two sqaures
    # confirm the pawns movement of 2 squares
    assert cb.AccessSquare("H4") == pawn
    assert cb.AccessSquare("H2") is None


# UpdateBoard test case 3: move white pawn onto black pawn square, checking for correct capture
def test_UpdateBoardCaptureOpponent():
    cb = ChessBoard()
    pawn1 = Pawn(False)  # white pawn
    pawn2 = Pawn(True)  # black pawn
    cb.OriginalDraw(pawn1, "B2")
    cb.OriginalDraw(pawn2, "C3")
    cb.UpdateBoard("B2", "C3")  # white pawn captures black pawn
    assert cb.AccessSquare("C3") == pawn1  # checks if the piece on the square "C3" is pawn1
    assert cb.AccessSquare("B2") is None  # Checks to see that the square B2 is empty
    capturedPiece = cb.AccessSquare("C3")
    assert capturedPiece is not None  # checks that the captured piece is not none

    print(capturedPiece)
    print(type(capturedPiece))
    print(capturedPiece.isBlack)
    assert capturedPiece.isBlack is False  # Checks to see if the is_black attribute of the captured_piece
    # object is false, which confrims that the captured piece was the black pawn


# test creation of a square
def test_SquareInit():
    s = square("A1")
    assert s.square == "A1"
    assert s.placedInSquare is None


def test_PlacePiece():
    # Create a square object and put a piece on it
    s = square("A1")
    piece1 = Pawn(True)
    s.PlacePiece(piece1)
    # check that the piece is placed in the square
    assert s.placedInSquare == piece1
    # make another piece and place it on the square, which already has a piece
    piece2 = Rook(False)
    s.PlacePiece(piece2)
    # check to see if the second piece takes the place of the first piece
    assert s.placedInSquare == piece2


def test_MoveOffSquare():
    # Test case 1: No piece on square
    s = square("A1")
    piece = s.moveOffSquare()
    assert piece is None

    # Test case 2: Piece on square
    s = square("A1")  # create a new square and place a piece on it
    piece = Pawn(True)
    s.PlacePiece(piece)
    s.MoveOffSquare()  # move the piece off the square
    assert s.placedInSquare is None  # check that the piece was removed from the square


def test_GetPiece():
    # Test case 1: No piece on square
    s = square("A1")
    assert s.GetPiece() is None  # check that no piece is on the square

    # Test case 2: Piece on square
    s = square("A1")
    piece = Pawn(True)
    s.PlacePiece(piece)  # place the pawn on the square
    assert s.GetPiece() == piece  # check that the pawn is on the square

def test_GetFEN():
    board=ChessBoard()
    for i in range(32):
        pieceToDraw = list(piecesPosDict.keys())[i]
        squareToFill = piecesPosDict[pieceToDraw]
        board.OriginalDraw(pieceToDraw, squareToFill)
    assert(board.GiveFEN() == "RNBQKBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbqkbnr")
    board.UpdateBoard("E2","E4")
    assert(board.GiveFEN() == "RNBQKBNR/PPPPPPPP/8/8/4p3/8/pppp1ppp/rnbqkbnr")

def test_SuperClass():

    testBoard = CreateTestBoard()
    assert(MoveChecker(testBoard, "G1", "E0", 0) == False)   # Illegal out of bounds, vertical
    assert(MoveChecker(testBoard, "E3", "E4", 0) == False)   # Empty square detectioin
    testBoard.UpdateBoard("G1", "H3")
    assert(MoveChecker(testBoard, "H3", "F2", 0) == False)   # Illegal collision detection
    testBoard.UpdateBoard("H3", "G5")
    assert(MoveChecker(testBoard, "G5", "H7", 0) == True)    # Taking legal
    assert(MoveChecker(testBoard, "G5", "I6", 0) == False)   # Illegal out of bounds, horizontal

# Pawn must have seperate tests for white / black, as movement direction changes with colour
def test_Pawn():
    testBoard = CreateTestBoard()
    assert(MoveChecker(testBoard, "A2", "A3", 0) == True)     # W. Legal move
    testBoard.UpdateBoard("A2", "A3")
    assert(MoveChecker(testBoard, "B2", "B4", 0) == True)     # W. Legal first double move
    testBoard.UpdateBoard("B2", "B4")
    assert(MoveChecker(testBoard, "A3", "A5", 0) == False)    # W. Illegal second double move
    testBoard.UpdateBoard("B7", "B5")
    assert(MoveChecker(testBoard, "B4", "B5", 0) == False)    # W. Illegal forward take
    assert(MoveChecker(testBoard, "B4", "A5", 0) == False)    # W. Illegal diagonal move
    testBoard.UpdateBoard("A7", "A5")
    assert(MoveChecker(testBoard, "B4", "A5", 0) == True)     # W. Legal diagonal take

    assert(MoveChecker(testBoard, "H7", "H6", 0) == True)     # B. Legal move
    testBoard.UpdateBoard("H7", "H6")
    assert(MoveChecker(testBoard, "G7", "G5", 0) == True)     # B. Legal first double move
    testBoard.UpdateBoard("G7", "G5")
    assert(MoveChecker(testBoard, "H6", "H4", 0) == False)    # B. Illegal second double move
    testBoard.UpdateBoard("G2", "G4")
    assert(MoveChecker(testBoard, "G5", "G4", 0) == False)    # B. Illegal forward take
    assert(MoveChecker(testBoard, "G5", "H4", 0) == False)    # B. Illegal diagonal move
    testBoard.UpdateBoard("H2", "H4")
    assert(MoveChecker(testBoard, "G5", "H4", 0) == True)     # B. Legal diagonal take

def test_Knight():
    testBoard = CreateTestBoard()
    testBoard.UpdateBoard("B1", "C3")
    assert(MoveChecker(testBoard, "C3", "A5", 0) == False)    # Illegal moves, vertical...
    assert(MoveChecker(testBoard, "C3", "C5", 0) == False)
    assert(MoveChecker(testBoard, "C3", "E5", 0) == False)
    assert(MoveChecker(testBoard, "C3", "B4", 0) == False)
    assert(MoveChecker(testBoard, "C3", "C4", 0) == False)
    assert(MoveChecker(testBoard, "C3", "D4", 0) == False)
    assert(MoveChecker(testBoard, "C3", "B5", 0) == True)     # Legal moves...
    assert(MoveChecker(testBoard, "C3", "D5", 0) == True)

    testBoard.UpdateBoard("C3", "E4")
    assert(MoveChecker(testBoard, "E4", "C4", 0) == False)    # Illegal moves, horizontal...
    assert(MoveChecker(testBoard, "E4", "D4", 0) == False)
    assert(MoveChecker(testBoard, "E4", "C3", 0) == True)     # Legal moves...
    assert(MoveChecker(testBoard, "E4", "C5", 0) == True)


def test_Rook():
    testBoard = CreateTestBoard()
    assert(MoveChecker(testBoard, "A1", "A3", 0) == False)    # Illegal move, jumping
    testBoard.UpdateBoard("A2", "A4")
    assert(MoveChecker(testBoard, "A1", "A3", 0) == True)     # Legal move, vertical
    testBoard.UpdateBoard("A1", "A3")
    assert(MoveChecker(testBoard, "A3", "D4", 0) == False)    # Illegal move
    assert(MoveChecker(testBoard, "A3", "D6", 0) == False)    # Illegal move, diagonal
    assert(MoveChecker(testBoard, "A3", "C3", 0) == True)     # Legal move, horizonal
    testBoard.UpdateBoard("A3", "C3")
    testBoard.UpdateBoard("B8", "C6")
    assert(MoveChecker(testBoard, "C3", "C7", 0) == False)    # Illegal take, vertical jumping
    testBoard.UpdateBoard("C6", "B8")
    assert(MoveChecker(testBoard, "C3", "C7", 0) == True)     # Legal take


def test_Bishop():
    testBoard = CreateTestBoard()
    assert(MoveChecker(testBoard, "C1", "F4", 0) == False)    # Illegal move, jumping
    testBoard.UpdateBoard("D2", "D3")
    assert(MoveChecker(testBoard, "C1", "F4", 0) == True)     # Legal move
    testBoard.UpdateBoard("C1", "F4")
    assert(MoveChecker(testBoard, "F4", "D5", 0) == False)    # Illegal move
    assert(MoveChecker(testBoard, "F4", "H4", 0) == False)    # Illegal move, horizontal
    assert(MoveChecker(testBoard, "F4", "F3", 0) == False)    # Illegal move, vertical
    assert(MoveChecker(testBoard, "F4", "B8", 0) == False)    # Illegal take, jumping
    testBoard.UpdateBoard("C7", "C6")
    assert(MoveChecker(testBoard, "F4", "B8", 0) == True)     # Legal take

def test_Queen():
    testBoard = CreateTestBoard()
    assert(MoveChecker(testBoard, "D1", "F3", 0) == False)    # Illegal move, diagonal jumping
    assert(MoveChecker(testBoard, "D1", "D3", 0) == False)    # Illegal move, vertical jumping
    testBoard.UpdateBoard("D2", "D4")
    assert(MoveChecker(testBoard, "D1", "D3", 0) == True)     # Legal move, vertical
    testBoard.UpdateBoard("D1", "D3")
    assert(MoveChecker(testBoard, "D3", "C4", 0) == True)     # Legal move, diagonal
    testBoard.UpdateBoard("D3", "C4")
    assert(MoveChecker(testBoard, "C4", "A4", 0) == True)     # Legal move, horizontal
    assert(MoveChecker(testBoard, "C4", "E4", 0) == False)    # Illegal move, horizontal jumping
    assert(MoveChecker(testBoard, "C4", "A5", 0) == False)    # Illegal move

    testBoard.UpdateBoard("B8", "C6")
    assert(MoveChecker(testBoard, "C4", "C7", 0) == False)    # Illegal take, vertical jumping
    testBoard.UpdateBoard("C6", "B4")
    assert(MoveChecker(testBoard, "C4", "C7", 0) == True)     # Legal take, vertical
    assert(MoveChecker(testBoard, "C4", "G8", 0) == False)    # Illegal take, diagonal jumping
    testBoard.UpdateBoard("F7", "F6")
    assert(MoveChecker(testBoard, "C4", "G8", 0) == True)     # Legal take, diagonal
    testBoard.UpdateBoard("A7", "A5")
    testBoard.UpdateBoard("A5", "A4")
    assert(MoveChecker(testBoard, "C4", "A4", 0) == False)    # Illegal take, horizontal jumping
    testBoard.UpdateBoard("B4", "A6")
    assert(MoveChecker(testBoard, "C4", "A4", 0) == True)     # Legal take, horizontal

def CreateTestBoard():
    testBoard = ChessBoard()
    testBoard.Draw()

    for i in range(32):
        pieceToDraw = list(piecesPosDict.keys())[i]
        squareToFill = piecesPosDict[pieceToDraw]
        testBoard.OriginalDraw(pieceToDraw, squareToFill)

    return testBoard
def test_PieceCaptures():
    pieceOne = Pawn(False)
    pieceTwo = Pawn(True)
    pieceOne.Capture(pieceTwo)

    assert pieceTwo.isCaptured

def test_Pawn():
    pawns = [Pawn(False) for i in range(4)]

    # Test string representation
    assert repr(pawns[0]) == 'p'

    # Check promotion
    notationPiecesDict = {
        'R': Rook,
        'N': Knight,
        'B': Bishop,
        'Q': Queen
    }
    pawns[0].Promote('R')
    print(pawns[0].__class__)
    assert isinstance(pawns[0],Rook)

    pawns[1].promote('N')
    assert isinstance(pawns[1],Knight)

    pawns[2].promote('B')
    assert isinstance(pawns[2],Bishop)

    pawns[3].promote('Q')
    assert isinstance(pawns[3],Queen)

def test_Rook():
    rook = Rook(False)
    # Test string representation
    assert repr(rook) == 'r'

def test_Knight():
    knight = Knight(False)
    # Test string representation
    assert repr(knight) == 'n'

def test_Bishop():
    bishop = Bishop(False)
    # Test string representation
    assert repr(bishop) == 'b'

def test_Queen():
    queen = Queen(False)
    # Test string representation
    assert repr(queen) == 'q'

def test_King():
    king = King(False)
    # Test string representation
    assert repr(king) == 'k'

def test_CheckmateChecker():
    # King not in check
    board = MakeBoard()
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate) == False

    # King takes pawn putting it in check
    board.update_board('E8', 'E6')
    board.update_board('B2', 'D5')
    checkmate = CheckmateChecker(board, 'black')
    assert(checkmate) == False

    # Horse and Rook Checkmate
    board.update_board('E6', 'E8')
    board.update_board('D5', 'B2')

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

