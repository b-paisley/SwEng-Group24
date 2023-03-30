from moveChecker import *

def StalemateChecker(currentBoard, playerColour):
    if playerColour.lower() == 'black':
        isBlack = 1
    else:
        isBlack = 0
    piecesArray = GetPieceArray(currentBoard, playerColour)
    piece = ''
    kingFound = False
    i = 0
    while not kingFound: 
        pieceCoords = piecesArray[i]
        piece = currentBoard.board[pieceCoords[0]][pieceCoords[1]].placedInSquare
        if isinstance(piece, King):
            kingFound = True
            break
        i += 1
        # See if king in check
    if not MovingIntoCheck(currentBoard, pieceCoords[0], pieceCoords[1], pieceCoords[0], pieceCoords[1], isBlack):
        return False
    else:
        piecesLength = len(piecesArray)
        i = 0
        while i < piecesLength:
            piece = piecesArray[i]
            pieceObject = currentBoard.board[piece[0]][piece[1]].placedInSquare
            if(isinstance(pieceObject, King)):
                row = piece[0]
                col = piece[1]
                kingNotation = GetChessNotation((row, col))
              # Possible King moves from current square in chess notation
                notation1 = GetChessNotation((row - 1, col))
                notation2 = GetChessNotation((row + 1, col))
                notation3 = GetChessNotation((row - 1, col - 1))
                notation4 = GetChessNotation((row - 1, col + 1))
                notation5 = GetChessNotation((row + 1, col - 1))
                notation6 = GetChessNotation((row + 1, col + 1))
                notation7 = GetChessNotation((row, col - 1))
                notation8 = GetChessNotation((row, col + 1))
                kingNotationArray = [notation1, notation2, notation3, notation4, notation5, notation6,
                                    notation7, notation8]
                # Check if King can make a legal move
                k = 0
                while k < len(kingNotationArray):
                    if MoveChecker(currentBoard, kingNotation, kingNotationArray[k], 0):
                        return False
                    k += 1

            elif(isinstance(pieceObject, Pawn)):
                row = piece[0]
                col = piece[1]
                pawnNotation = GetChessNotation((row, col))
              # Possible King moves from current square in chess notation
                notation1 = GetChessNotation((row - 1, col))
                notation2 = GetChessNotation((row + 1, col))
                notation3 = GetChessNotation((row - 2, col))
                notation4 = GetChessNotation((row + 2, col))
                notation5 = GetChessNotation((row + 1, col - 1))
                notation6 = GetChessNotation((row + 1, col + 1))
                notation7 = GetChessNotation((row - 1, col - 1))
                notation8 = GetChessNotation((row - 1, col + 1))
                pawnNotationArray = [notation1, notation2, notation3, notation4, notation5, notation6,
                                    notation7, notation8]
                # Check if pawn can make a legal move
                k = 0
                while k < len(pawnNotationArray):
                    if MoveChecker(currentBoard, pawnNotation, pawnNotationArray[k], 0):
                        return False
                    k += 1
            elif(isinstance(pieceObject, Knight)):
                row = piece[0]
                col = piece[1]
                knightNotation = GetChessNotation((row, col))
              # Possible King moves from current square in chess notation
                notation1 = GetChessNotation((row - 2, col - 1))
                notation2 = GetChessNotation((row - 2, col + 1))
                notation3 = GetChessNotation((row - 1, col + 2))
                notation4 = GetChessNotation((row - 1, col - 2))
                notation5 = GetChessNotation((row + 1, col - 2))
                notation6 = GetChessNotation((row + 1, col + 2))
                notation7 = GetChessNotation((row + 2, col - 1))
                notation8 = GetChessNotation((row + 2, col + 1))
                knightNotationArray = [notation1, notation2, notation3, notation4, notation5, notation6,
                                    notation7, notation8]
                # Check if pawn can make a legal move
                k = 0
                while k < len(knightNotationArray):
                    if MoveChecker(currentBoard, knightNotation, knightNotationArray[k], 0):
                        return False
                    k += 1
            elif(isinstance(pieceObject, Bishop)):
                row = piece[0]
                col = piece[1]
                bishopNotation = GetChessNotation((row, col))
                if not CheckRightDiagMoves(currentBoard, row, col, bishopNotation):
                   return False
                if not CheckLeftDiagMoves(currentBoard, row, col, bishopNotation):
                    return False
            elif(isinstance(pieceObject, Rook)):
                row = piece[0]
                col = piece[1]
                rookNotation = GetChessNotation((row, col))
                if not CheckHorizonalMoves(currentBoard, row, col, rookNotation):
                   return False
                if not CheckVerticalMoves(currentBoard, row, col, rookNotation):
                    return False
            elif(isinstance(pieceObject, Queen)):
                row = piece[0]
                col = piece[1]
                queenNotation = GetChessNotation((row, col))
                if not CheckHorizonalMoves(currentBoard, row, col, queenNotation):
                   return False
                if not CheckVerticalMoves(currentBoard, row, col, queenNotation):
                    return False
                if not CheckRightDiagMoves(currentBoard, row, col, queenNotation):
                   return False
                if not CheckLeftDiagMoves(currentBoard, row, col, queenNotation):
                    return False
            i += 1
        return True
    
def CheckHorizonalMoves(currentBoard, row, col, pieceNotation):
  # Horizontal -
    # Horizontal Left Check -
    tempRow = row 
    tempCol = col - 1
    
    while tempCol >= 0:
       notation = GetChessNotation((tempRow, tempCol))
       if MoveChecker(currentBoard, pieceNotation, notation, 0):
           return False
       tempCol -= 1
    
    # Horizontal Right Check -
    tempCol = col + 1

    while tempCol < 8:
       notation = GetChessNotation((tempRow, tempCol))
       if MoveChecker(currentBoard, pieceNotation, notation, 0):
           return False
       tempCol += 1
        
    return True

def CheckVerticalMoves(currentBoard, row, col, pieceNotation):
  # Vertical -
    # Vertical Below Check -
    tempRow = row - 1 
    tempCol = col 
    
    while tempRow >= 0:
       notation = GetChessNotation((tempRow, tempCol))
       if MoveChecker(currentBoard, pieceNotation, notation, 0):
           return False
       tempRow -= 1
    
    # Vertical Above Check -
    tempRow = row + 1

    while tempRow < 8:
       notation = GetChessNotation((tempRow, tempCol))
       if MoveChecker(currentBoard, pieceNotation, notation, 0):
           return False
       tempRow += 1
        
    return True

def CheckRightDiagMoves(currentBoard, row, col, pieceNotation):
  # Right Diagonal -
    # Right Diagonal Below Check -
    tempRow = row - 1 
    tempCol = col + 1
    
    while tempRow >= 0:
       notation = GetChessNotation((tempRow, tempCol))
       if MoveChecker(currentBoard, pieceNotation, notation, 0):
           return False
       tempRow -= 1
       tempCol += 1
    
    # Right Diagonal Above Check -
    tempRow = row + 1
    tempCol = col + 1

    while tempRow < 8:
       notation = GetChessNotation((tempRow, tempCol))
       if MoveChecker(currentBoard, pieceNotation, notation, 0):
           return False
       tempRow += 1
       tempCol += 1
        
    return True

def CheckLeftDiagMoves(currentBoard, row, col, pieceNotation):
  # Left Diagonal -
    # Left Diagonal Below Check -
    tempRow = row - 1 
    tempCol = col - 1
    
    while tempRow >= 0:
       notation = GetChessNotation((tempRow, tempCol))
       if MoveChecker(currentBoard, pieceNotation, notation, 0):
           return False
       tempRow -= 1
       tempCol -= 1
    
    # Left Diagonal Above Check -
    tempRow = row + 1
    tempCol = col - 1

    while tempRow < 8:
       notation = GetChessNotation((tempRow, tempCol))
       if MoveChecker(currentBoard, pieceNotation, notation, 0):
           return False
       tempRow += 1
       tempCol -= 1

    return True

            
    