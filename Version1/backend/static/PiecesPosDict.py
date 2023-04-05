from Pieces import *

piecesPosDict = {
    # White pieces
    Rook(False): "A1",
    Knight(False): "B1",
    Bishop(False): "C1",
    Queen(False): "D1",
    King(False): "E1",
    Bishop(False): "F1",
    Knight(False): "G1",
    Rook(False): "H1",
    Pawn(False): "A2",
    Pawn(False): "B2",
    Pawn(False): "C2",
    Pawn(False): "D2",
    Pawn(False): "E2",
    Pawn(False): "F2",
    Pawn(False): "G2",
    Pawn(False): "H2",

    # Black pieces
    Pawn(True): "A7",
    Pawn(True): "B7",
    Pawn(True): "C7",
    Pawn(True): "D7",
    Pawn(True): "E7",
    Pawn(True): "F7",
    Pawn(True): "G7",
    Pawn(True): "H7",
    Rook(True): "A8",
    Knight(True): "B8",
    Bishop(True): "C8",
    Queen(True): "D8",
    King(True): "E8",
    Bishop(True): "F8",
    Knight(True): "G8",
    Rook(True): "H8"
}


# For Stalemate Checker Tests
piecesPosDict1 = {
    # White pieces
    Queen(False): "B1",
    King(False): "H1",
    Rook(False): "A1",
    Rook(False): "H7",
    Knight(False): "F3",
    Pawn(False): "H4",

    
    # Black pieces
    King(True): "A8",
    Pawn(True): "H5",
    Pawn(True): "F4",
    Bishop(True): "A3"

    
}

# King Queen, black stalemate as king cant move
piecesPosDict2 = {
    # White pieces
    Queen(False): "F2",
    King(False): "A8",
    
    # Black pieces
    King(True): "H1"
    
}

piecesPosDict3 = {
    # White pieces
    Pawn(False): "E7",
    King(False): "E6",
    
    # Black pieces
    King(True): "E8"
    
}

# King Queen, black stalemate as king cant move
piecesPosDict4 = {
    # White pieces
    Queen(False): "E4",
    
    # Black pieces
    King(True): "E8",
    Knight(True): "G8"
    
}

