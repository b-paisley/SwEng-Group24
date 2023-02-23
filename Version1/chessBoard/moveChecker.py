from chessBoard import *
from Pieces import *

# Single unified function for checking if a move is legal. Returns true for a legal move, false otherwise
def move_checker(chess_board, prev_square, new_square):
    prev_file = ord(prev_square[0])-65
    prev_row = int(prev_square[1])-1
    new_file = ord(new_square[0])-65
    new_row = int(new_square[1])-1
    if (new_file < 0 or new_row < 0 or new_file > 7 or new_row > 7): return False
    taking = False
    
    #Checking if moving square is occupied at all, and if target square is occupied by other piece
    moving_square_piece = chess_board.board[prev_row][prev_file].placed_in_square
    if (moving_square_piece == None): return False
    target_square_piece = chess_board.board[new_row][new_file].placed_in_square
    if (target_square_piece != None):
        taking = True
        if (moving_square_piece.is_black == target_square_piece.is_black): return False
        
    if (isinstance(moving_square_piece, Pawn)):
        if (not taking):
            if (not moving_square_piece.has_moved):
                if (moving_square_piece.is_black and prev_row-2 == new_row and prev_file == new_file and
                    chess_board.board[prev_row-1][prev_file].placed_in_square == None): return True
                if (not moving_square_piece.is_black and prev_row+2 == new_row and prev_file == new_file and
                    chess_board.board[prev_row+1][prev_file].placed_in_square == None): return True
            if (moving_square_piece.is_black and prev_row-1 == new_row and prev_file == new_file): return True
            if (not moving_square_piece.is_black and prev_row+1 == new_row and prev_file == new_file): return True
        else:
            if (moving_square_piece.is_black and prev_row-1 == new_row and (1 == abs(new_file - prev_file))): return True
            if (not moving_square_piece.is_black and prev_row+1 == new_row and (1 == abs(new_file - prev_file))): return True
        return False
    
    if (isinstance(moving_square_piece, Rook)):
        return check_straights(chess_board, prev_row, prev_file, new_row, new_file)
    
    if (isinstance(moving_square_piece, Bishop)):
        return check_diagonals(chess_board, prev_row, prev_file, new_row, new_file)
    
    if (isinstance(moving_square_piece, Queen)):
        if (check_straights(chess_board, prev_row, prev_file, new_row, new_file) 
            or check_diagonals(chess_board, prev_row, prev_file, new_row, new_file)): return True
        else: return False
        
    if (isinstance(moving_square_piece, Knight)):
        if (abs(new_file - prev_file) == 2 and abs(new_row - prev_row) == 1): return True
        elif (abs(new_file - prev_file) == 1 and abs(new_row - prev_row) == 2): return True
        else: return False
    
# this is only used by moveChecker, so I'm just passing the files and rows directly
# we don't need to check the target square itself, as that's handled in moveChecker
# returns True if the straight move is clear
def check_straights(chess_board, prev_row, prev_file, new_row, new_file):
    if (prev_row == new_row):
        if (new_file > prev_file):
            checked_file = prev_file+1
            while (checked_file < new_file):
                if (chess_board.board[prev_row][checked_file].placed_in_square != None): return False
                checked_file += 1
            return True
        else:
            checked_file = prev_file-1
            while (checked_file > new_file):
                if (chess_board.board[prev_row][checked_file].placed_in_square != None): return False
                checked_file -= 1
            return True
    elif (prev_file == new_file):
        if (new_row > prev_row):
            checked_row = prev_row+1
            while (checked_row < new_row):
                if (chess_board.board[checked_row][prev_file].placed_in_square != None): return False
                checked_row += 1
            return True
        else:
            checked_row = prev_row-1
            while (checked_row < new_row):
                if (chess_board.board[checked_row][prev_file].placed_in_square != None): return False
                checked_row -= 1
            return True       
    else: return False
    
# Returns True if diagonal move is clear
def check_diagonals(chess_board, prev_row, prev_file, new_row, new_file):
    if (abs(new_row - prev_row) == abs(new_file - prev_file)):
        if (new_row > prev_row and new_file > prev_file):
            checked_row = prev_row + 1
            checked_file = prev_file + 1
            while (checked_row < new_row):
                if (chess_board.board[checked_row][checked_file].placed_in_square != None): return False
                checked_row += 1
                checked_file += 1
            return True
        if (new_row > prev_row and new_file < prev_file):
            checked_row = prev_row + 1
            checked_file = prev_file - 1
            while (checked_row < new_row):
                if (chess_board.board[checked_row][checked_file].placed_in_square != None): return False
                checked_row += 1
                checked_file -= 1
            return True
        if (new_row < prev_row and new_file > prev_file):
            checked_row = prev_row - 1
            checked_file = prev_file + 1
            while (checked_row > new_row):
                if (chess_board.board[checked_row][checked_file].placed_in_square != None): return False
                checked_row -= 1
                checked_file += 1
            return True          
        if (new_row < prev_row and new_file < prev_file):
            checked_row = prev_row - 1
            checked_file = prev_file - 1
            while (checked_row > new_row):
                if (chess_board.board[checked_row][checked_file].placed_in_square != None): return False
                checked_row -= 1
                checked_file -= 1
            return True           
    return False

def movingIntoCheck(pieceX, pieceY, destX, destY, chess_board,black):    #check if destination is in check.
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
