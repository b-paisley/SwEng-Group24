from moveChecker import *

def AllMovesFinder(chessBoard, square):
    taking = ""
    validMoves = []
    file = ord(square[0])-65
    row = int(square[1])-1
    piece = chessBoard.board[row][file].placedInSquare
    
    # Brute Force approach for Pawn
    if (isinstance(piece, Pawn)):
        rowShift = [2, 1, 1, 1]
        fileShift = [0, -1, 0, 1]
        if (not piece.isBlack):
            for x in range (4):
                if (MoveChecker(chessBoard, square, PositionsToNotation(file+fileShift[x], row+rowShift[x]))):
                    if(CheckIfTaking(chessBoard, PositionsToNotation(file+fileShift[x], row+rowShift[x]))): taking = "x"
                    else: taking = ""
                    validMoves.append(taking + PositionsToNotation(file+fileShift[x], row+rowShift[x]))
        else:
            for x in range (4):
                if (MoveChecker(chessBoard, square, PositionsToNotation(file+fileShift[x], row-rowShift[x]))):
                    if(CheckIfTaking(chessBoard, PositionsToNotation(file+fileShift[x], row-rowShift[x]))): taking = "x"
                    else: taking = ""
                    validMoves.append(taking + PositionsToNotation(file+fileShift[x], row-rowShift[x]))
    
    # Brute force also applicable for Knight  
    if (isinstance(piece, Knight)):
        rowShift = [2, 2, 1, 1, -1, -1, -2, -2]
        fileShift = [-1, 1, -2, 2, -2, 2, -1, 1]
        for x in range(8):
            if (MoveChecker(chessBoard, square, PositionsToNotation(file+fileShift[x], row+rowShift[x]))):
                if(CheckIfTaking(chessBoard, PositionsToNotation(file+fileShift[x], row+rowShift[x]))): taking = "x"
                else: taking = ""
                validMoves.append(taking + PositionsToNotation(file+fileShift[x], row+rowShift[x]))
        
    if (isinstance(piece, Rook)):
        validMoves = AppendValidStraights(chessBoard, square, file, row, validMoves)
    
    if (isinstance(piece, Bishop)):
        validMoves = AppendValidDiagonals(chessBoard, square, file, row, validMoves)
    
    if (isinstance(piece, Queen)):
        validMoves = AppendValidStraights(chessBoard, square, file, row, validMoves)
        validMoves = AppendValidDiagonals(chessBoard, square, file, row, validMoves)
    
    validMoves.sort()
    return validMoves
    
def AppendValidStraights(chessBoard, square, file, row, validMoves):
    taking = ""
    checkedRow = 7
    while (checkedRow > row):
        if MoveChecker(chessBoard, square, PositionsToNotation(file, checkedRow)):
            while (checkedRow > row):
                if(CheckIfTaking(chessBoard, PositionsToNotation(file, checkedRow))): taking = "x"
                else: taking = ""
                validMoves.append(taking + PositionsToNotation(file, checkedRow))
                checkedRow -= 1
        checkedRow -= 1
    checkedRow = 0
    while (checkedRow < row):
        if MoveChecker(chessBoard, square, PositionsToNotation(file, checkedRow)):
            while (checkedRow < row):
                if(CheckIfTaking(chessBoard, PositionsToNotation(file, checkedRow))): taking = "x"
                else: taking = ""
                validMoves.append(taking + PositionsToNotation(file, checkedRow))
                checkedRow += 1
        checkedRow += 1
        
    checkedFile = 7
    while (checkedFile > file):
        if MoveChecker(chessBoard, square, PositionsToNotation(checkedFile, row)):
            while (checkedFile > file):
                if(CheckIfTaking(chessBoard, PositionsToNotation(checkedFile, row))): taking = "x"
                else: taking = ""
                validMoves.append(taking + PositionsToNotation(checkedFile, row))
                checkedFile -= 1
        checkedFile -= 1
    checkedFile = 0
    while (checkedFile < file):
        if MoveChecker(chessBoard, square, PositionsToNotation(checkedFile, row)):
            while (checkedFile < file):
                if(CheckIfTaking(chessBoard, PositionsToNotation(checkedFile, row))): taking = "x"
                else: taking = ""
                validMoves.append(taking + PositionsToNotation(checkedFile, row))
                checkedFile += 1
        checkedFile += 1
    return validMoves

def AppendValidDiagonals(chessBoard, square, file, row, validMoves):
    checkedFile = file
    checkedRow = row
    while (checkedFile > 0 and checkedRow < 7):
        checkedFile -= 1
        checkedRow += 1
    while (checkedFile < file):
        if MoveChecker(chessBoard, square, PositionsToNotation(checkedFile, checkedRow)):
            while (checkedFile < file):
                if(CheckIfTaking(chessBoard, PositionsToNotation(checkedFile, checkedRow))): taking = "x"
                else: taking = ""
                validMoves.append(taking + PositionsToNotation(checkedFile, checkedRow))
                checkedFile += 1
                checkedRow -= 1
        checkedFile += 1
        checkedRow -= 1
        
    checkedFile = file
    checkedRow = row
    while (checkedFile < 7 and checkedRow < 7):
        checkedFile += 1
        checkedRow += 1
    while (checkedFile > file):
        if MoveChecker(chessBoard, square, PositionsToNotation(checkedFile, checkedRow)):
            while (checkedFile > file):
                if(CheckIfTaking(chessBoard, PositionsToNotation(checkedFile, checkedRow))): taking = "x"
                else: taking = ""
                validMoves.append(taking + PositionsToNotation(checkedFile, checkedRow))
                checkedFile -= 1
                checkedRow -= 1
        checkedFile -= 1
        checkedRow -= 1
        
    while (checkedFile > 0 and checkedRow > 0):
        checkedFile -= 1
        checkedRow -= 1
    while (checkedFile < file):
        if MoveChecker(chessBoard, square, PositionsToNotation(checkedFile, checkedRow)):
            while (checkedFile < file):
                if(CheckIfTaking(chessBoard, PositionsToNotation(checkedFile, checkedRow))): taking = "x"
                else: taking = ""
                validMoves.append(taking + PositionsToNotation(checkedFile, checkedRow))
                checkedFile += 1
                checkedRow += 1
        checkedFile += 1
        checkedRow += 1
        
    checkedFile = file
    checkedRow = row
    while (checkedFile < 7 and checkedRow > 0):
        checkedFile += 1
        checkedRow -= 1
    while (checkedFile > file):
        if MoveChecker(chessBoard, square, PositionsToNotation(checkedFile, checkedRow)):
            while (checkedFile > file):
                if(CheckIfTaking(chessBoard, PositionsToNotation(checkedFile, checkedRow))): taking = "x"
                else: taking = ""
                validMoves.append(taking + PositionsToNotation(checkedFile, checkedRow))
                checkedFile -= 1
                checkedRow += 1
        checkedFile -= 1
        checkedRow += 1
    
    return validMoves

def PositionsToNotation(file, row):
        return chr(file+65) + str(row+1)
    
def CheckIfTaking(chessBoard, square):
    file = ord(square[0])-65
    row = int(square[1])-1
    if (chessBoard.board[row][file].placedInSquare == None): return False
    else: return True
