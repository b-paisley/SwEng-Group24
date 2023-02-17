from chessBoard import *
from Pieces import *

'''
Right now, this uses chessBoard to check if moves are valid, as a convenient accessible array of every piece on the board.
However, that means testing is difficult until moving pieces on the board is fully implemented, so there may be some bugs
I've missed.
'''

def moveChecker(chessBoard, piece, dest):
    # Converts chess notation to position in the array board (e.g. d2 -> board[1][3]) and gets that piece (e.g. d2 -> P)
    # Co-ords are preserved for future checks involving piece moving. Taking is relevant for pawn moves.
    taking = False
    destY = int(dest[1])-1
    destX = ord(dest[0])-97
    destPos = chessBoard.board[destY][destX]
    if ((destX or destY) > 7 or (destX or destY) < 0): return False # Moving off the board
    
    # Logic to check if square is occupied by friendly piece
    if (destPos != " "):
        if(destPos.isupper() and not piece.is_black):
            return False
        elif(destPos.islower() and piece.is_black):
            return False
        taking = True
    
    # Getting piece X and Y for comparison to target X and Y
    pieceX = piece.pos_to_tuple()[0]-1
    pieceY = piece.pos_to_tuple()[1]-1
    
    # For pawns, it's easier to search for a valid move, while Rooks / Bishops etc. will search for an invalid move
    if(isinstance(piece, Pawn)):
        if ((taking == False and pieceX == destX) or (taking and pieceX == (destX+1 or destX-1))):
            if (piece.is_black and pieceY-1 == destY or (piece.has_moved == False and pieceY-2 == destY)):  
                return True
            if (not piece.is_black and pieceY+1 == destY or (piece.has_moved == False and pieceY+2 == destY)): 
                return True
        return False
        
    if(isinstance(piece, Rook)):
        if(pieceX != destX and pieceY != destY): return False # Checking if move is straight
        return checkStraights(pieceX, pieceY, destX, destY, chessBoard)
        
    
    if(isinstance(piece, Bishop)):
        if (abs(destX - pieceX) != abs(destY - pieceY)): return False # Checking if moving diagonally
        return checkDiagonals(pieceX, pieceY, destX, destY, chessBoard)
    
        
    if(isinstance(piece, Knight)):  
        if (abs(pieceX - destX) == 2 and abs(pieceY - destY) == 1): return True
        if (abs(pieceX - destX) == 1 and abs(pieceY - destY) == 2): return True
        return False
                  
    if(isinstance(piece, Queen)):
        if(pieceX == destX or pieceY == destY):
            return checkStraights(pieceX, pieceY, destX, destY, chessBoard)
        if (abs(destX - pieceX) == abs(destY - pieceY)):
            return checkDiagonals(pieceX, pieceY, destX, destY, chessBoard)
        return False
    
def checkStraights(pieceX, pieceY, destX, destY, chessBoard):
    if (pieceX > destX):
        checkSquare = pieceX-1
        while(checkSquare > destX):
            if (chessBoard.board[checkSquare][pieceY] != " "):
                return False
            checkSquare -= 1
            
    if (pieceX < destX):
        checkSquare = pieceX+1
        while(checkSquare < destX):
            if (chessBoard.board[checkSquare][pieceY] != " "):
                return False
            checkSquare += 1
        
    if (pieceY > destY):
        checkSquare = pieceY-1
        while(checkSquare > destY):
            if (chessBoard.board[pieceX][checkSquare] != " "):
                return False
            checkSquare -= 1
            
    if (pieceY < destY):
        checkSquare = pieceY+1
        while(checkSquare < destY):
            if (chessBoard.board[pieceX][checkSquare] != " "):
                return False
            checkSquare += 1
    return True
    
def checkDiagonals(pieceX, pieceY, destX, destY, chessBoard):
    if (destX > pieceX and destY > pieceY):
        checkX = pieceX-1
        checkY = pieceY-1
        while (checkX > destX):
            if(chessBoard.board[checkX][checkY] != " "):
                return False
            checkX -= 1
            checkY -= 1
    if (destX > pieceX and destY < pieceY):
        checkX = pieceX-1
        checkY = pieceY+1
        while (checkX > destX):
            if(chessBoard.board[checkX][checkY] != " "):
                return False
            checkX -= 1
            checkY += 1
    if (destX < pieceX and destY < pieceY):
        checkX = pieceX+1
        checkY = pieceY+1
        while (checkX < destX):
            if(chessBoard.board[checkX][checkY] != " "):
                return False
            checkX += 1
            checkY += 1
    if (destX < pieceX and destY > pieceY):
        checkX = pieceX+1
        checkY = pieceY-1
        while (checkX < destX):
            if(chessBoard.board[checkX][checkY] != " "):
                return False
            checkX += 1
            checkY -= 1
    return True
