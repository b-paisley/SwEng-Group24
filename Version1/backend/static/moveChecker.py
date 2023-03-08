from chessBoard import *
from Pieces import *

# Single unified function for checking if a move is legal. Returns true for a legal move, false otherwise
def MoveChecker(chessBoard, prevSquare, newSquare):
    if(not isinstance(newSquare[0], str) or not newSquare[1].isdigit()): return False
    prevFile = ord(prevSquare[0])-65
    prevRow = int(prevSquare[1])-1
    newFile = ord(newSquare[0])-65
    newRow = int(newSquare[1])-1
    if (newFile < 0 or newRow < 0 or newFile > 7 or newRow > 7): return False
    taking = False
    
    #Checking if moving square is occupied at all, and if target square is occupied by other piece
    movingSquarePiece = chessBoard.board[prevRow][prevFile].placedInSquare
    if (movingSquarePiece == None): return False
    targetSquarePiece = chessBoard.board[newRow][newFile].placedInSquare
    if (targetSquarePiece != None):
        taking = True
        if (movingSquarePiece.isBlack == targetSquarePiece.isBlack): return False
        
    if (isinstance(movingSquarePiece, Pawn)):
        if (not taking):
            if (not movingSquarePiece.hasMoved):
                if (movingSquarePiece.isBlack and prevRow-2 == newRow and prevFile == newFile and
                    chessBoard.board[prevRow-1][prevFile].placedInSquare == None): return True
                if (not movingSquarePiece.isBlack and prevRow+2 == newRow and prevFile == newFile and
                    chessBoard.board[prevRow+1][prevFile].placedInSquare == None): return True
            if (movingSquarePiece.isBlack and prevRow-1 == newRow and prevFile == newFile): return True
            if (not movingSquarePiece.isBlack and prevRow+1 == newRow and prevFile == newFile): return True
        else:
            if (movingSquarePiece.isBlack and prevRow-1 == newRow and (1 == abs(newFile - prevFile))): return True
            if (not movingSquarePiece.isBlack and prevRow+1 == newRow and (1 == abs(newFile - prevFile))): return True
        return False
    
    if (isinstance(movingSquarePiece, Rook)):
        return checkStraights(chessBoard, prevRow, prevFile, newRow, newFile)
    
    if (isinstance(movingSquarePiece, Bishop)):
        return checkDiagonals(chessBoard, prevRow, prevFile, newRow, newFile)
    
    if (isinstance(movingSquarePiece, Queen)):
        if (checkStraights(chessBoard, prevRow, prevFile, newRow, newFile) 
            or checkDiagonals(chessBoard, prevRow, prevFile, newRow, newFile)): return True
        else: return False
        
    if (isinstance(movingSquarePiece, Knight)):
        if (abs(newFile - prevFile) == 2 and abs(newRow - prevRow) == 1): return True
        elif (abs(newFile - prevFile) == 1 and abs(newRow - prevRow) == 2): return True
        else: return False
        
    if (isinstance(movingSquarePiece, King)):
        if (movingSquarePiece.isBlack):
            black = 1
        if (not movingSquarePiece.isBlack):
            black = 0
        if (movingIntoCheck(chessBoard, prevRow, prevFile, newRow, newFile, black)):
            # if it moves by 1 or less in both directions its legal
            if (abs(newFile - prevFile) <= 1 and abs(newRow - prevRow) <= 1):
                return True
        return False
    
# this is only used by moveChecker, so I'm just passing the files and rows directly
# we don't need to check the target square itself, as that's handled in moveChecker
# returns True if the straight move is clear
def CheckStraights(chessBoard, prevRow, prevFile, newRow, newFile):
    if (prevRow == newRow):
        if (newFile > prevFile):
            checkedFile = prevFile+1
            while (checkedFile < newFile):
                if (chessBoard.board[prevRow][checkedFile].placedInSquare != None): return False
                checkedFile += 1
            return True
        else:
            checkedFile = prevFile-1
            while (checkedFile > newFile):
                if (chessBoard.board[prevRow][checkedFile].placedInSquare != None): return False
                checkedFile -= 1
            return True
    elif (prevFile == newFile):
        if (newRow > prevRow):
            checkedRow = prevRow+1
            while (checkedRow < newRow):
                if (chessBoard.board[checkedRow][prevFile].placedInSquare != None): return False
                checkedRow += 1
            return True
        else:
            checkedRow = prevRow-1
            while (checkedRow < newRow):
                if (chessBoard.board[checkedRow][prevFile].placedInSquare != None): return False
                checkedRow -= 1
            return True       
    else: return False
    
# Returns True if diagonal move is clear
def CheckDiagonals(chessBoard, prevRow, prevFile, newRow, newFile):
    if (abs(newRow - prevRow) == abs(newFile - prevFile)):
        if (newRow > prevRow and newFile > prevFile):
            checkedRow = prevRow + 1
            checkedFile = prevFile + 1
            while (checkedRow < newRow):
                if (chessBoard.board[checkedRow][checkedFile].placedInSquare != None): return False
                checkedRow += 1
                checkedFile += 1
            return True
        if (newRow > prevRow and newFile < prevFile):
            checkedRow = prevRow + 1
            checkedFile = prevFile - 1
            while (checkedRow < newRow):
                if (chessBoard.board[checkedRow][checkedFile].placedInSquare != None): return False
                checkedRow += 1
                checkedFile -= 1
            return True
        if (newRow < prevRow and newFile > prevFile):
            checkedRow = prevRow - 1
            checkedFile = prevFile + 1
            while (checkedRow > newRow):
                if (chessBoard.board[checkedRow][checkedFile].placedInSquare != None): return False
                checkedRow -= 1
                checkedFile += 1
            return True          
        if (newRow < prevRow and newFile < prevFile):
            checkedRow = prevRow - 1
            checkedFile = prevFile - 1
            while (checkedRow > newRow):
                if (chessBoard.board[checkedRow][checkedFile].placedInSquare != None): return False
                checkedRow -= 1
                checkedFile -= 1
            return True           
    return False

def MovingIntoCheck(chessBoard, prevRow, prevFile, newRow, newFile, black):  # check if destination is in check.
    # check for Rooks putting check on King
    squareToCheckX = newFile + 1
    squareToCheckY = newRow - 2
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if(not knightCheck(chessBoard,squareToCheckX,squareToCheckY,black,piece)):
            return False

    squareToCheckX = newFile - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not knightCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return False

    squareToCheckX = newFile + 1
    squareToCheckY = newRow + 2
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not knightCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return False

    squareToCheckX = newFile - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not knightCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return False

    squareToCheckY = newRow + 1
    squareToCheckX = newFile - 2
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not knightCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return False

    squareToCheckY = newRow - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not knightCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return False

    squareToCheckY = newRow + 1
    squareToCheckX = newFile + 2
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not knightCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return False

    squareToCheckY = newRow - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not knightCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return False

    # check for castles and queen straights
    # 0=castle  1=diff obj  2=nothing

    squareToCheckX = newFile
    squareToCheckY = newRow
    while (squareToCheckX < 7):
        squareToCheckX= squareToCheckX + 1
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (rookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)==0):
            return False
        if (rookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)==1):
            break

    squareToCheckX = newFile
    squareToCheckY = newRow
    while (squareToCheckX > 0):
        squareToCheckX=squareToCheckX - 1
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (rookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 0):
            return False
        if (rookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 1):
            break

    squareToCheckY = newRow
    squareToCheckX = newFile
    while (squareToCheckY < 7):
        squareToCheckY=squareToCheckY + 1
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (rookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 0):
            return False
        if (rookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 1):
            break

    squareToCheckY = newRow
    squareToCheckX = newFile
    while (squareToCheckY > 0):
        squareToCheckY=squareToCheckY - 1
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (rookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 0):
            return False
        if (rookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 1):
            break

    # check diagonally for bishops and queens
    # 0=bishop  1=diff obj  2=nothing

    squareToCheckX = newFile
    squareToCheckY = newRow
    while ((squareToCheckX < 7) and (squareToCheckY < 7)):
        squareToCheckX=squareToCheckX + 1
        squareToCheckY=squareToCheckY + 1
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (bishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 0):
            return False
        if (bishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 1):
            break

    squareToCheckX = newFile
    squareToCheckY = newRow
    while ((squareToCheckX > 0) and (squareToCheckY < 7)):
        squareToCheckX=squareToCheckX - 1
        squareToCheckY=squareToCheckY + 1
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (bishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 0):
            return False
        if (bishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 1):
            break

    squareToCheckY = newRow
    squareToCheckX = newFile
    while (squareToCheckY > 0 and squareToCheckX < 7):
        squareToCheckX=squareToCheckX + 1
        squareToCheckY=squareToCheckY - 1
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (bishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 0):
            return False
        if (bishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 1):
            break

    squareToCheckY = newRow
    squareToCheckX = newFile
    while (squareToCheckY > 0 and squareToCheckX > 0):
        squareToCheckX=squareToCheckX - 1
        squareToCheckY=squareToCheckY - 1
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (bishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 0):
            return False
        if (bishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 1):
            break

    #pawn checks
    squareToCheckY = newRow - 1
    squareToCheckX = newFile - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not pawnCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
           return False

    squareToCheckX = newFile + 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not pawnCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return False

    squareToCheckY = newRow + 1
    squareToCheckX = newFile - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not pawnCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return False

    squareToCheckX = newFile + 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not pawnCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return False
    return True


def KnightCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece):
    if (piece != None):
        if (black == 1):
            if (not piece.isBlack):
                if (isinstance(piece, Knight)):
                    return False
        elif (black == 0):
            if (piece.isBlack):
                if (isinstance(piece, Knight)):
                    return False
    return True

def RookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece):
    if (piece != None):
        if (black == 1):
            if (not piece.isBlack):
                if (isinstance(piece, Rook)):
                    return 0
                if(isinstance(piece, Queen)):
                    return 0
        elif (black == 0):
            if (piece.isBlack):
                if (isinstance(piece, Rook)):
                    return 0
                if (isinstance(piece, Queen)):
                    return 0
        return 1
    return 2

def BishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece):
    if (piece != None):
        if (black == 1):
            if (not piece.isBlack):
                if (isinstance(piece, Bishop)):
                    return 0
                if(isinstance(piece, Queen)):
                    return 0
        elif (black == 0):
            if (piece.isBlack):
                if (isinstance(piece, Bishop)):
                    return 0
                if (isinstance(piece, Queen)):
                    return 0
        return 1
    return 2

def PawnCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece):
    if (piece != None):
        if (black == 1):
            if (not piece.isBlack):
                if (isinstance(piece, Pawn)):
                    return False
        elif (black == 0):
            if (piece.isBlack):
                if (isinstance(piece, Pawn)):
                    return False
    return True
