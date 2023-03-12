from Points import *
from Pieces import *
from chessBoard import *
from moveChecker import *
from square import *
from allMovesFinder import *
from aiMoveGenerator import *

def CheckmateChecker(currentBoard, playerColour):
   # Find King
   kingPiece = False
   if playerColour.lower() == 'black':
        isBlack = 1
   else:
        isBlack = 0
   i = 0
   row = 0
   col = 0
   while kingPiece == False:
      for j in range(8):
        piece = currentBoard.board[i][j].placed_in_square
        if piece != None:
          # Black King
          if piece.is_black == True and isBlack == True:
            if isinstance(piece, King):
               kingPiece = True
               row = i
               col = j
          
          # White King
          elif piece.is_black == False and isBlack == False:
            if isinstance(piece, King):
               kingPiece = True
               row = i
               col = j
      i += 1
      j = 0   
   kingRow = row
   kingCol = col
   kingNotation = GetChessNotation((row, col))
   # If King not in check
   isCheck = MovingIntoCheck(currentBoard, i, j, row, col, isBlack) 
   if isCheck == True:
       return False
   # Possible King moves from current square in chess notation
   notation1 = GetChessNotation((row-1, col))
   notation2 = GetChessNotation((row+1, col))
   notation3 = GetChessNotation((row-1, col-1))
   notation4 = GetChessNotation((row-1, col+1))
   notation5 = GetChessNotation((row+1, col-1))
   notation6 = GetChessNotation((row+1, col+1))
   notation7 = GetChessNotation((row, col-1))
   notation8 = GetChessNotation((row, col+1))
   coordsCheckPieceArray = PiecesCausingCheck(currentBoard, row, col, isBlack)
   coordsCheckPiece = (coordsCheckPieceArray[0][0], coordsCheckPieceArray[0][1])
   checkPieceNotation = GetChessNotation(coordsCheckPiece)
   
   if len(coordsCheckPieceArray) == 1:
    # Check if King can move out of check/take piece putting it in check
    if MoveChecker(currentBoard, kingNotation, notation1) == True:
        return False
    elif MoveChecker(currentBoard, kingNotation, notation2) == True:
        return False
    elif MoveChecker(currentBoard, kingNotation, notation3) == True:
        return False
    elif MoveChecker(currentBoard, kingNotation, notation4) == True:
        return False
    elif MoveChecker(currentBoard, kingNotation, notation5) == True:
        return False
    elif MoveChecker(currentBoard, kingNotation, notation6) == True:
        return False
    elif MoveChecker(currentBoard, kingNotation, notation7) == True:
        return False
    elif MoveChecker(currentBoard, kingNotation, notation8) == True:
        return False
    else:
        piecesArray = GetPieceArray(currentBoard, playerColour)
        i = 0
        # Check if other pieces can take the piece putting the King in check
        while i < len(piecesArray):
                pieceTaking = piecesArray[i]
                pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placed_in_square
                pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1])) 
                if not isinstance(pieceName, King):
                    if pieceName.is_black and isBlack == 1:
                        if MoveChecker(currentBoard, pieceNotation, checkPieceNotation):
                            return False
                    elif not pieceName.is_black and isBlack == 0:
                        if MoveChecker(currentBoard, pieceNotation, checkPieceNotation):
                            return False
                i += 1
        # Check if pieces can block 
        # Pawns and Knights can't be blocked -> if get this far, checkmate
        if isinstance(piece, Pawn) or isinstance(piece, Knight):
            return True
        else:
            # Check if there is a square between king and pieceChecking (for blocking)
            if (coordsCheckPiece[0] == kingRow+1 and coordsCheckPiece[1] == kingCol) or (coordsCheckPiece[0] == kingRow-1 and coordsCheckPiece[1] == kingCol):
                return True
            elif (coordsCheckPiece[0] == kingRow-1 and coordsCheckPiece[1] == kingCol+1) or (coordsCheckPiece[0] == kingRow-1 and coordsCheckPiece[1] == kingCol-1):
                return True
            elif (coordsCheckPiece[0] == kingRow+1 and coordsCheckPiece[1] == kingCol+1) or (coordsCheckPiece[0] == kingRow+1 and coordsCheckPiece[1] == kingCol-1):
                return True
            elif (coordsCheckPiece[0] == kingRow and coordsCheckPiece[1] == kingCol-1) or (coordsCheckPiece[0] == kingRow and coordsCheckPiece[1] == kingCol+1):
                return True
            # Blocking when piece checking is a Rook/Queen straight 
            # Horizontal -
            if coordsCheckPiece[0] == kingRow:
                checkCol = coordsCheckPiece[1]+1
                # Horizontal Left Check -
                if coordsCheckPiece[1] < kingCol:
                    while checkCol < kingCol:
                        blockNotation = GetChessNotation((kingRow, checkCol))
                        j = 0
                        while j < len(piecesArray):
                            pieceTaking = piecesArray[j]
                            pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placed_in_square
                            pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1])) 
                            if not isinstance(pieceName, King):
                                if pieceName.is_black and isBlack == 1:
                                    if MoveCheckermove_checker(currentBoard, pieceNotation, blockNotation):
                                        return False
                                elif not pieceName.is_black and isBlack == 0:
                                    if MoveChecker(currentBoard, pieceNotation, blockNotation):
                                        return False
                            j += 1
                        checkCol += 1
                        i += 1
                # Horizontal Right Check -
                elif coordsCheckPiece[1] > kingCol:
                    checkCol = coordsCheckPiece[1]-1
                    while checkCol > kingCol:
                        blockNotation = GetChessNotation((kingRow, checkCol))
                        j = 0
                        while j < len(piecesArray):
                            pieceTaking = piecesArray[j]
                            pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placed_in_square
                            pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1])) 
                            if not isinstance(pieceName, King):
                                if pieceName.is_black and isBlack == 1:
                                    if MoveChecker(currentBoard, pieceNotation, blockNotation) == True:
                                        return False
                                elif not pieceName.is_black and isBlack == 0:
                                    if MoveChecker(currentBoard, pieceNotation, blockNotation) == True:
                                        return False
                            j += 1
                        checkCol -= 1
                        i += 1 
            # Vertical - 
            elif coordsCheckPiece[1] == kingCol: 
                checkRow = coordsCheckPiece[0]+1
                # Vertical Above Check - 
                if coordsCheckPiece[0] < kingRow: 
                    while checkRow < kingRow:
                        blockNotation = GetChessNotation((checkRow, kingCol))
                        j = 0
                        while j < len(piecesArray):
                            pieceTaking = piecesArray[j]
                            pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placed_in_square
                            pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1])) 
                            if not isinstance(pieceName, King):
                                if pieceName.is_black and isBlack == 1:
                                    if MoveChecker(currentBoard, pieceNotation, blockNotation):
                                        return False
                                elif not pieceName.is_black and isBlack == 0:
                                    if MoveChecker(currentBoard, pieceNotation, blockNotation):
                                        return False
                            j += 1
                        checkRow += 1
                        i += 1     
                # Vertical Below Check - 
                elif coordsCheckPiece[0] > kingRow: 
                    checkRow = coordsCheckPiece[0]-1
                    while checkRow > kingRow:
                        blockNotation = GetChessNotation((checkRow, kingCol))
                        j = 0
                        while j < len(piecesArray):
                            pieceTaking = piecesArray[j]
                            pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placed_in_square
                            pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1])) 
                            if not isinstance(pieceName, King):
                                if pieceName.is_black and isBlack == 1:
                                    if MoveChecker(currentBoard, pieceNotation, blockNotation):
                                        return False
                                elif not pieceName.is_black and isBlack == 0:
                                    if MoveChecker(currentBoard, pieceNotation, blockNotation):
                                        return False
                            j += 1
                        checkRow -= 1
                        i += 1
                
            # Blocking when piece checking is Bishop/Queen diag
            # Diag Left Below
            if coordsCheckPiece[0] < kingRow and coordsCheckPiece[1] < kingCol:
                checkCol = coordsCheckPiece[1]+1
                checkRow = coordsCheckPiece[1]+1
                while checkCol < kingCol and checkRow < kingRow:
                    blockNotation = GetChessNotation((checkRow, checkCol))
                    j = 0
                    while j < len(piecesArray):
                        pieceTaking = piecesArray[j]
                        pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placed_in_square
                        pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1])) 
                        if not isinstance(pieceName, King):
                            if pieceName.is_black and isBlack == 1:
                                if MoveChecker(currentBoard, pieceNotation, blockNotation):
                                    return False
                            elif not pieceName.is_black and isBlack == 0:
                                if MoveChecker(currentBoard, pieceNotation, blockNotation):
                                    return False
                        j += 1
                    checkCol += 1
                    checkRow += 1
                    i += 1
            # Diag Left Above
            elif coordsCheckPiece[0] > kingRow and coordsCheckPiece[1] < kingCol:
                checkCol = coordsCheckPiece[1]+1
                checkRow = coordsCheckPiece[1]-1
                while checkCol < kingCol and checkRow > kingRow:
                    blockNotation = GetChessNotation((checkRow, checkCol))
                    j = 0
                    while j < len(piecesArray):
                        pieceTaking = piecesArray[j]
                        pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placed_in_square
                        pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1])) 
                        if not isinstance(pieceName, King):
                            if pieceName.is_black and isBlack == 1:
                                if MoveChecker(currentBoard, pieceNotation, blockNotation):
                                    return False
                            elif not pieceName.is_black and isBlack == 0:
                                if MoveChecker(currentBoard, pieceNotation, blockNotation):
                                    return False
                        j += 1
                    checkCol += 1
                    checkRow -= 1
                    i += 1
            # Diag Right Below
            elif coordsCheckPiece[0] < kingRow and coordsCheckPiece[1] > kingCol:
                checkCol = coordsCheckPiece[1]-1
                checkRow = coordsCheckPiece[1]+1
                while checkCol > kingCol and checkRow < kingRow:
                    blockNotation = GetChessNotation((checkRow, checkCol))
                    j = 0
                    while j < len(piecesArray):
                        pieceTaking = piecesArray[j]
                        pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placed_in_square
                        pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1])) 
                        if not isinstance(pieceName, King):
                            if pieceName.is_black and isBlack == 1:
                                if MoveChecker(currentBoard, pieceNotation, blockNotation):
                                    return False
                            elif not pieceName.is_black and isBlack == 0:
                                if MoveChecker(currentBoard, pieceNotation, blockNotation):
                                    return False
                        j += 1
                    checkCol -= 1
                    checkRow += 1
                    i += 1
            # Diag Right Above
            elif coordsCheckPiece[0] > kingRow and coordsCheckPiece[1] < kingCol:
                checkCol = coordsCheckPiece[1]-1
                checkRow = coordsCheckPiece[1]-1
                while checkCol > kingCol and checkRow > kingRow:
                    blockNotation = GetChessNotation((checkRow, checkCol))
                    j = 0
                    while j < len(piecesArray):
                        pieceTaking = piecesArray[j]
                        pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placed_in_square
                        pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1])) 
                        if not isinstance(pieceName, King):
                            if pieceName.is_black and isBlack == 1:
                                if MoveChecker(currentBoard, pieceNotation, blockNotation):
                                    return False
                            elif not pieceName.is_black and isBlack == 0:
                                if MoveChecker(currentBoard, pieceNotation, blockNotation):
                                    return False
                        j += 1
                    checkCol -= 1
                    checkRow -= 1
                    i += 1
   else:
       # More than one piece putting king in check
       # Check if King can move out of check/take piece putting it in check
    if MoveChecker(currentBoard, kingNotation, notation1) == True:
        return False
    elif MoveChecker(currentBoard, kingNotation, notation2) == True:
        return False
    elif MoveChecker(currentBoard, kingNotation, notation3) == True:
        return False
    elif MoveChecker(currentBoard, kingNotation, notation4) == True:
        return False
    elif MoveChecker(currentBoard, kingNotation, notation5) == True:
        return False
    elif MoveChecker(currentBoard, kingNotation, notation6) == True:
        return False
    elif MoveChecker(currentBoard, kingNotation, notation7) == True:
        return False
    elif MoveChecker(currentBoard, kingNotation, notation8) == True:
        return False
   return True # if get this far its checkmate 
      
def PiecesCausingCheck(chessBoard, newRow, newFile, black):  # check what peice is putting check on King
    piecesCheckingArray = []
    # check for Rooks putting check on King
    squareToCheckX = newFile + 1
    squareToCheckY = newRow - 2
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if(not knightCheck(chessBoard,squareToCheckX,squareToCheckY,black,piece)):
            return piecesCheckingArray.append((squareToCheckY, squareToCheckX))

    squareToCheckX = newFile - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not knightCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return piecesCheckingArray.append((squareToCheckY, squareToCheckX))

    squareToCheckX = newFile + 1
    squareToCheckY = newRow + 2
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not knightCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return piecesCheckingArray.append((squareToCheckY, squareToCheckX))

    squareToCheckX = newFile - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not knightCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return piecesCheckingArray.append((squareToCheckY, squareToCheckX))

    squareToCheckY = newRow + 1
    squareToCheckX = newFile - 2
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not knightCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return piecesCheckingArray.append((squareToCheckY, squareToCheckX))

    squareToCheckY = newRow - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not knightCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return piecesCheckingArray.append((squareToCheckY, squareToCheckX))

    squareToCheckY = newRow + 1
    squareToCheckX = newFile + 2
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not knightCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return piecesCheckingArray.append((squareToCheckY, squareToCheckX))

    squareToCheckY = newRow - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not knightCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return piecesCheckingArray.append((squareToCheckY, squareToCheckX))

    # check for castles and queen straights
    # 0=castle  1=diff obj  2=nothing

    squareToCheckX = newFile
    squareToCheckY = newRow
    while (squareToCheckX < 7):
        squareToCheckX= squareToCheckX + 1
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (rookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)==0):
            return piecesCheckingArray.append((squareToCheckY, squareToCheckX))
        if (rookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)==1):
            if(not isinstance(piece, King)):
              break
            elif(isinstance(piece, King) and piece.is_black == True and black != 1) or (isinstance(piece, King) and piece.is_black == False and black != 0):
              break

    squareToCheckX = newFile
    squareToCheckY = newRow
    while (squareToCheckX > 0):
        squareToCheckX=squareToCheckX - 1
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (rookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 0):
            return piecesCheckingArray.append((squareToCheckY, squareToCheckX))
        if (rookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 1):
            if(not isinstance(piece, King)):
              break
            elif(isinstance(piece, King) and piece.is_black == True and black != 1) or (isinstance(piece, King) and piece.is_black == False and black != 0):
              break

    squareToCheckY = newRow
    squareToCheckX = newFile
    while (squareToCheckY < 7):
        squareToCheckY=squareToCheckY + 1
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (rookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 0):
            return piecesCheckingArray.append((squareToCheckY, squareToCheckX))
        if (rookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 1):
            if(not isinstance(piece, King)):
              break
            elif(isinstance(piece, King) and piece.is_black == True and black != 1) or (isinstance(piece, King) and piece.is_black == False and black != 0):
              break

    squareToCheckY = newRow
    squareToCheckX = newFile
    while (squareToCheckY > 0):
        squareToCheckY=squareToCheckY - 1
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (rookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 0):
            return piecesCheckingArray.append((squareToCheckY, squareToCheckX))
        if (rookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 1):
            if(not isinstance(piece, King)):
              break
            elif(isinstance(piece, King) and piece.is_black == True and black != 1) or (isinstance(piece, King) and piece.is_black == False and black != 0):
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
            return piecesCheckingArray.append((squareToCheckY, squareToCheckX))
        if (bishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 1):
            if(not isinstance(piece, King)):
              break
            elif(isinstance(piece, King) and piece.is_black == True and black != 1) or (isinstance(piece, King) and piece.is_black == False and black != 0):
              break

    squareToCheckX = newFile
    squareToCheckY = newRow
    while ((squareToCheckX > 0) and (squareToCheckY < 7)):
        squareToCheckX=squareToCheckX - 1
        squareToCheckY=squareToCheckY + 1
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (bishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 0):
            return piecesCheckingArray.append((squareToCheckY, squareToCheckX))
        if (bishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 1):
            if(not isinstance(piece, King)):
              break
            elif(isinstance(piece, King) and piece.is_black == True and black != 1) or (isinstance(piece, King) and piece.is_black == False and black != 0):
              break

    squareToCheckY = newRow
    squareToCheckX = newFile
    while (squareToCheckY > 0 and squareToCheckX < 7):
        squareToCheckX=squareToCheckX + 1
        squareToCheckY=squareToCheckY - 1
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (bishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 0):
            return piecesCheckingArray.append((squareToCheckY, squareToCheckX))
        if (bishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 1):
            if(not isinstance(piece, King)):
              break
            elif(isinstance(piece, King) and piece.is_black == True and black != 1) or (isinstance(piece, King) and piece.is_black == False and black != 0):
              break

    squareToCheckY = newRow
    squareToCheckX = newFile
    while (squareToCheckY > 0 and squareToCheckX > 0):
        squareToCheckX=squareToCheckX - 1
        squareToCheckY=squareToCheckY - 1
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (bishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 0):
            return piecesCheckingArray.append((squareToCheckY, squareToCheckX))
        if (bishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 1):
            if(not isinstance(piece, King)):
              break
            elif(isinstance(piece, King) and piece.is_black == True and black != 1) or (isinstance(piece, King) and piece.is_black == False and black != 0):
              break

    #pawn checks
    squareToCheckY = newRow - 1
    squareToCheckX = newFile - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not pawnCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
           return piecesCheckingArray.append((squareToCheckY, squareToCheckX))

    squareToCheckX = newFile + 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not pawnCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return piecesCheckingArray.append((squareToCheckY, squareToCheckX))

    squareToCheckY = newRow + 1
    squareToCheckX = newFile - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not pawnCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return piecesCheckingArray.append((squareToCheckY, squareToCheckX))

    squareToCheckX = newFile + 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not pawnCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return piecesCheckingArray.append((squareToCheckY, squareToCheckX))
    return piecesCheckingArray 

# take in array notation and return chess notation co-ordinates ( e.g. input : (2, 2) - output : d4
def GetChessNotation(coords):
    row = int(coords[0]) + 1
    column = chr(coords[1]+65)
    return column + str(row)

# This gets all the pieces of the colour of the ai player
def GetPieceArray(chessBoard, playerColour):
    pieceArray = []
    if playerColour.lower() == 'black':
        isBlack = True
    else:
        isBlack = False
    for i in range(8):
        for j in range(8):
            piece = chessBoard.board[i][j].placed_in_square
            if piece != None:
                # Black Piece Array
                if piece.is_black == True and isBlack == True:
                    pieceArray.append([i,j])

                # White Piece Array
                elif piece.is_black == False and isBlack == False:
                   pieceArray.append([i,j])

    return pieceArray  
      
