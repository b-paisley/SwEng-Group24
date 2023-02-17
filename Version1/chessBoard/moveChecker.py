from chessBoard import *
from Pieces import *

'''
Right now, this uses chessBoard to check if moves are valid, as a convenient accessible array of every piece on the board.
However, that means testing is difficult until moving pieces on the board is fully implemented, so there may be some bugs
I've missed.
'''

def move_checker(chess_board, piece, dest):
    # Converts chess notation to position in the array board (e.g. d2 -> board[1][3]) and gets that piece (e.g. d2 -> P)
    # Co-ords are preserved for future checks involving piece moving. Taking is relevant for pawn moves.
    taking = False
    dest_Y = int(dest[1])-1
    dest_X = ord(dest[0])-97
    dest_pos = chess_board.board[dest_Y][dest_X]
    if ((dest_X > 7 or dest_Y > 7) or (dest_X < 0 or dest_Y < 0)): return False # Moving off the board
    
    # Logic to check if square is occupied by friendly piece
    if (dest_pos != " "):
        if(dest_pos.isupper() and not piece.is_black):
            return False
        elif(dest_pos.islower() and piece.is_black):
            return False
        taking = True
    
    # Getting piece X and Y for comparison to target X and Y
    piece_X = piece.pos_to_tuple()[0]-1
    piece_Y = piece.pos_to_tuple()[1]-1
    
    # For pawns, it's easier to search for a valid move, while Rooks / Bishops etc. will search for an invalid move
    if(isinstance(piece, Pawn)):
        if ((not taking and piece_X == dest_X) or (taking and (piece_X == dest_X+1 or piece_X == dest_X-1))):
            if (piece.is_black and piece_Y-1 == dest_Y or (piece.has_moved == False and piece_Y-2 == dest_Y)):  
                return True
            if (not piece.is_black and piece_Y+1 == dest_Y or (piece.has_moved == False and piece_Y+2 == dest_Y)): 
                return True
        return False
        
    if(isinstance(piece, Rook)):
        if(piece_X != dest_X and piece_Y != dest_Y): return False # Checking if move is straight
        return check_straights(piece_X, piece_Y, dest_X, dest_Y, chess_board)
        
    
    if(isinstance(piece, Bishop)):
        if (abs(dest_X - piece_X) != abs(dest_Y - piece_Y)): return False # Checking if moving diagonally
        return check_diagonals(piece_X, piece_Y, dest_X, dest_Y, chess_board)
    
        
    if(isinstance(piece, Knight)):  
        if (abs(piece_X - dest_X) == 2 and abs(piece_Y - dest_Y) == 1): return True
        if (abs(piece_X - dest_X) == 1 and abs(piece_Y - dest_Y) == 2): return True
        return False
                  
    if(isinstance(piece, Queen)):
        if(piece_X == dest_X or piece_Y == dest_Y):
            return check_straights(piece_X, piece_Y, dest_X, dest_Y, chess_board)
        if (abs(dest_X - piece_X) == abs(dest_Y - piece_Y)):
            return check_diagonals(piece_X, piece_Y, dest_X, dest_Y, chess_board)
        return False
    
    if(isinstance(piece, King)):
        if (piece.is_black):
            black=1
        if (not piece.is_black):
            black=0
        if (movingIntoCheck(pieceX, pieceY, destX, destY, chessBoard,black)): #if it moves into check, its illegal  
            if (abs(pieceY - destY)<=1 and abs(pieceX-destX)<=1):  #if it moves by 1 or less in both directions its legal
                return True
            #here is where castling should be implemented, but we need to wait until pieces can be implemented first 
    return False
    
def check_straights(piece_X, piece_Y, dest_X, dest_Y, chess_board):
    if (piece_X > dest_X):
        check_square = piece_X-1
        while(check_square > dest_X):
            if (chess_board.board[check_square][piece_Y] != " "):
                return False
            check_square -= 1
            
    if (piece_X < dest_X):
        check_square = piece_X+1
        while(check_square < dest_X):
            if (chess_board.board[check_square][piece_Y] != " "):
                return False
            check_square += 1
        
    if (piece_Y > dest_Y):
        check_square = piece_Y-1
        while(check_square > dest_Y):
            if (chess_board.board[piece_X][check_square] != " "):
                return False
            check_square -= 1
            
    if (piece_Y < dest_Y):
        check_square = piece_Y+1
        while(check_square < dest_Y):
            if (chess_board.board[piece_X][check_square] != " "):
                return False
            check_square += 1
    return True
    
def check_diagonals(piece_X, piece_Y, dest_X, dest_Y, chess_board):
    if (dest_X > piece_X and dest_Y > piece_Y):
        check_X = piece_X-1
        check_Y = piece_Y-1
        while (check_X > dest_X):
            if(chess_board.board[check_X][check_Y] != " "):
                return False
            check_X -= 1
            check_Y -= 1
    if (dest_X > piece_X and dest_Y < piece_Y):
        check_X = piece_X-1
        check_Y = piece_Y+1
        while (check_X > dest_X):
            if(chess_board.board[check_X][check_Y] != " "):
                return False
            check_X -= 1
            check_Y += 1
    if (dest_X < piece_X and dest_Y < piece_Y):
        check_X = piece_X+1
        check_Y = piece_Y+1
        while (check_X < dest_X):
            if(chess_board.board[check_X][check_Y] != " "):
                return False
            check_X += 1
            check_Y += 1
    if (dest_X < piece_X and dest_Y > piece_Y):
        check_X = piece_X+1
        check_Y = piece_Y-1
        while (check_X < dest_X):
            if(chess_board.board[check_X][check_Y] != " "):
                return False
            check_X += 1
            check_Y -= 1
    return True


def movingIntoCheck(pieceX, pieceY, destX, destY, chessBoard,black):    #check if destination is in check.
# check for Rooks putting check on King
    squareToCheckX= destX +1
    squareToCheckY= destY - 2
    if ((black==1 and chess_board.board[squareToCheckX][squareToCheckY] == "N") or (black==0 and chess_board.board[squareToCheckX][squareToCheckY] == "n")):
        return False  
    squareToCheckX= destX -1
    if ((black==1 and chess_board.board[squareToCheckX][squareToCheckY] == "N") or black==0 and (chess_board.board[squareToCheckX][squareToCheckY] == "n")):
        return False  
    squareToCheckX= destX +1
    squareToCheckY= destY + 2
    if ((black==1 and chess_board.board[squareToCheckX][squareToCheckY] == "N") or black==0 and (chess_board.board[squareToCheckX][squareToCheckY] == "n")):
        return False  
    squareToCheckX= destX -1
    if ((black==1 and chess_board.board[squareToCheckX][squareToCheckY] == "N") or black==0 and (chess_board.board[squareToCheckX][squareToCheckY] == "n")):
        return False      
    squareToCheckY= destY +1
    squareToCheckX= destX - 2
    if ((black==1 and chess_board.board[squareToCheckX][squareToCheckY] == "N") or black==0 and (chess_board.board[squareToCheckX][squareToCheckY] == "n")):
        return False  
    squareToCheckY= destY -1
    if ((black==1 and chess_board.board[squareToCheckX][squareToCheckY] == "N") or black==0 and (chess_board.board[squareToCheckX][squareToCheckY] == "n")):
        return False  
    squareToCheckY= destY +1
    squareToCheckX= destX + 2
    if ((black==1 and chess_board.board[squareToCheckX][squareToCheckY] == "N") or black==0 and (chess_board.board[squareToCheckX][squareToCheckY] == "n")):
        return False  
    squareToCheckY= destY -1
    if ((black==1 and chess_board.board[squareToCheckX][squareToCheckY] == "N") or black==0 and (chess_board.board[squareToCheckX][squareToCheckY] == "n")):
        return False
#check for castles and queen straights
#check to its right
    squareToCheckX=destX
    squareToCheckY= destY 
    while(squareToCheckX < 7):
        squareToCheckX+1
        if ((black==1 and chess_board.board[squareToCheckX][squareToCheckY] == "R" or "Q") or black==0 and (chess_board.board[squareToCheckX][squareToCheckY] == "r" or "q")):
            return False
    #check to its left
    squareToCheckX=destX
    squareToCheckY= destY    
    while(squareToCheckX > 0):
        squareToCheckX-1
        if ((black==1 and chess_board.board[squareToCheckX][squareToCheckY] == "R" or "Q") or black==0 and (chess_board.board[squareToCheckX][squareToCheckY] == "r" or "q")):
            return False
    #check above it
    squareToCheckY=destY
    squareToCheckX= destX
    while(squareToCheckY < 7):
        squareToCheckY+1
        if ((black==1 and chess_board.board[squareToCheckX][squareToCheckY] == "R" or "Q") or black==0 and (chess_board.board[squareToCheckX][squareToCheckY] == "r" or "q")):
            return False
    #check below it
    squareToCheckY=destY 
    squareToCheckX= destX    
    while(squareToCheckY > 0):
        squareToCheckY-1
        if ((black==1 and chess_board.board[squareToCheckX][squareToCheckY] == "R" or "Q") or black==0 and (chess_board.board[squareToCheckX][squareToCheckY] == "r" or "q")):
            return False
#check diagonally for bishops and queens
#check diagonally up right
    squareToCheckX=destX
    squareToCheckY= destY
    while(squareToCheckX < 7 and squareToCheckY < 7):
        squareToCheckX+1
        squareToCheckY+1
        if ((black==1 and chess_board.board[squareToCheckX][squareToCheckY] == "R" or "Q") or black==0 and (chess_board.board[squareToCheckX][squareToCheckY] == "r" or "q")):
            return False
    #check diagonally up left
    squareToCheckX=destX 
    squareToCheckY= destY 
    while(squareToCheckX > 0 and squareToCheckY < 7):
        squareToCheckX-1
        squareToCheckY+1
        if ((black==1 and chess_board.board[squareToCheckX][squareToCheckY] == "R" or "Q") or black==0 and (chess_board.board[squareToCheckX][squareToCheckY] == "r" or "q")):
            return False
    #check diagonally to right below
    squareToCheckY=destY 
    squareToCheckX= destX 
    while(squareToCheckY > 0 and squareToCheckX < 7):
        squareToCheckX+1
        squareToCheckY-1
        if ((black==1 and chess_board.board[squareToCheckX][squareToCheckY] == "R" or "Q") or black==0 and (chess_board.board[squareToCheckX][squareToCheckY] == "r" or "q")):
            return False
    #check below it diagonally left
    squareToCheckY=destY 
    squareToCheckX= destX  
    while(squareToCheckY > 0 and squareToCheckX > 0):
        squareToCheckX+1
        squareToCheckY-1
        if ((black==1 and chess_board.board[squareToCheckX][squareToCheckY] == "R" or "Q") or black==0 and (chess_board.board[squareToCheckX][squareToCheckY] == "r" or "q")):
            return False
#check for pawn checks
    if (black==1):
        squareToCheckY=destY - 1
        squareToCheckX= destX - 1
        if (chess_board.board[squareToCheckX][squareToCheckY] == "P"):
            return False
        squareToCheckX= destX + 1
        if (chess_board.board[squareToCheckX][squareToCheckY] == "P"):
            return False
    if (black==0):
        squareToCheckY= destY + 1
        squareToCheckX= destX - 1
        if (chess_board.board[squareToCheckX][squareToCheckY] == "p"):
            return False
        squareToCheckX= destX + 1
        if (chess_board.board[squareToCheckX][squareToCheckY] == "p"):
            return False
    return True
