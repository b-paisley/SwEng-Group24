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
   if len(coordsCheckPieceArray) == 1: # Only one piece checking King
    coordsCheckPiece = (coordsCheckPieceArray[0][0], coordsCheckPieceArray[0][1])
    checkPieceNotation = GetChessNotation(coordsCheckPiece)
    # checkPiece = currentBoard.board[coordsCheckPiece[0]][coordsCheckPiece[1]].placed_in_square

    isCheck = movingIntoCheck(currentBoard, i, j, row, col, isBlack) 
    if isCheck == True:
        return False
    # Check if King can move out of check/take piece putting it in check
    elif move_checker(currentBoard, kingNotation, notation1) == True:
        return False
    elif move_checker(currentBoard, kingNotation, notation2) == True:
        return False
    elif move_checker(currentBoard, kingNotation, notation3) == True:
        return False
    elif move_checker(currentBoard, kingNotation, notation4) == True:
        return False
    elif move_checker(currentBoard, kingNotation, notation5) == True:
        return False
    elif move_checker(currentBoard, kingNotation, notation6) == True:
        return False
    elif move_checker(currentBoard, kingNotation, notation7) == True:
        return False
    elif move_checker(currentBoard, kingNotation, notation8) == True:
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
                    if move_checker(currentBoard, pieceNotation, checkPieceNotation):
                       return False
                    elif not pieceName.is_black and isBlack == 0:
                       if move_checker(currentBoard, pieceNotation, checkPieceNotation):
                          return False
                i += 1
        # Check if pieces can block 
        # Pawns and Knights can't be blocked -> if get this far, checkmate
        if isinstance(piece, Pawn) or isinstance(piece, Knight):
            return True
        else:
            # Check if there is a square between king and pieceChecking
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
                                 if move_checker(currentBoard, pieceNotation, blockNotation):
                                   return False
                                elif not pieceName.is_black and isBlack == 0:
                                  if move_checker(currentBoard, pieceNotation, blockNotation):
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
                                    if move_checker(currentBoard, pieceNotation, blockNotation):
                                        return False
                                elif not pieceName.is_black and isBlack == 0:
                                    if move_checker(currentBoard, pieceNotation, blockNotation):
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
                                    if move_checker(currentBoard, pieceNotation, blockNotation):
                                        return False
                                    elif not pieceName.is_black and isBlack == 0:
                                        if move_checker(currentBoard, pieceNotation, blockNotation):
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
                                    if move_checker(currentBoard, pieceNotation, blockNotation):
                                        return False
                                elif not pieceName.is_black and isBlack == 0:
                                    if move_checker(currentBoard, pieceNotation, blockNotation):
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
                                if move_checker(currentBoard, pieceNotation, blockNotation):
                                    return False
                            elif not pieceName.is_black and isBlack == 0:
                                if move_checker(currentBoard, pieceNotation, blockNotation):
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
                                if move_checker(currentBoard, pieceNotation, blockNotation):
                                    return False
                            elif not pieceName.is_black and isBlack == 0:
                                if move_checker(currentBoard, pieceNotation, blockNotation):
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
                                if move_checker(currentBoard, pieceNotation, blockNotation):
                                    return False
                            elif not pieceName.is_black and isBlack == 0:
                                if move_checker(currentBoard, pieceNotation, blockNotation):
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
                                if move_checker(currentBoard, pieceNotation, blockNotation):
                                    return False
                            elif not pieceName.is_black and isBlack == 0:
                                if move_checker(currentBoard, pieceNotation, blockNotation):
                                    return False
                        j += 1
                    checkCol -= 1
                    checkRow -= 1
                    i += 1
      
   return True # if get this far its checkmate 
      
def PiecesCausingCheck(chess_board, new_row, new_file, black):  # check what peice is putting check on King
    piecesCheckingArray = []
    # check for Rooks putting check on King
    squareToCheckX = new_file + 1
    squareToCheckY = new_row - 2
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if(not knightCheck(chess_board,squareToCheckX,squareToCheckY,black,piece)):
            piecesCheckingArray.append((squareToCheckY, squareToCheckX))

    squareToCheckX = new_file - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (not knightCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
            piecesCheckingArray.append((squareToCheckY, squareToCheckX))

    squareToCheckX = new_file + 1
    squareToCheckY = new_row + 2
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (not knightCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
            piecesCheckingArray.append((squareToCheckY, squareToCheckX))

    squareToCheckX = new_file - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (not knightCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
            piecesCheckingArray.append((squareToCheckY, squareToCheckX))

    squareToCheckY = new_row + 1
    squareToCheckX = new_file - 2
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (not knightCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
            piecesCheckingArray.append((squareToCheckY, squareToCheckX))

    squareToCheckY = new_row - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (not knightCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
            piecesCheckingArray.append((squareToCheckY, squareToCheckX))

    squareToCheckY = new_row + 1
    squareToCheckX = new_file + 2
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (not knightCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
            piecesCheckingArray.append((squareToCheckY, squareToCheckX))

    squareToCheckY = new_row - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (not knightCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
            piecesCheckingArray.append((squareToCheckY, squareToCheckX))

    # check for castles and queen straights
    # 0=castle  1=diff obj  2=nothing

    squareToCheckX = new_file
    squareToCheckY = new_row
    while (squareToCheckX < 7):
        squareToCheckX= squareToCheckX + 1
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (rookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)==0):
            piecesCheckingArray.append((squareToCheckY, squareToCheckX))
        if (rookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)==1):
            break

    squareToCheckX = new_file
    squareToCheckY = new_row
    while (squareToCheckX > 0):
        squareToCheckX=squareToCheckX - 1
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (rookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 0):
            piecesCheckingArray.append((squareToCheckY, squareToCheckX))
        if (rookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 1):
            break

    squareToCheckY = new_row
    squareToCheckX = new_file
    while (squareToCheckY < 7):
        squareToCheckY=squareToCheckY + 1
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (rookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 0):
            piecesCheckingArray.append((squareToCheckY, squareToCheckX))
        if (rookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 1):
            break

    squareToCheckY = new_row
    squareToCheckX = new_file
    while (squareToCheckY > 0):
        squareToCheckY=squareToCheckY - 1
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (rookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 0):
            piecesCheckingArray.append((squareToCheckY, squareToCheckX))
        if (rookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 1):
            break

    # check diagonally for bishops and queens
    # 0=bishop  1=diff obj  2=nothing

    squareToCheckX = new_file
    squareToCheckY = new_row
    while ((squareToCheckX < 7) and (squareToCheckY < 7)):
        squareToCheckX=squareToCheckX + 1
        squareToCheckY=squareToCheckY + 1
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (bishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 0):
            piecesCheckingArray.append((squareToCheckY, squareToCheckX))
        if (bishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 1):
            break

    squareToCheckX = new_file
    squareToCheckY = new_row
    while ((squareToCheckX > 0) and (squareToCheckY < 7)):
        squareToCheckX=squareToCheckX - 1
        squareToCheckY=squareToCheckY + 1
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (bishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 0):
            piecesCheckingArray.append((squareToCheckY, squareToCheckX))
        if (bishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 1):
            break

    squareToCheckY = new_row
    squareToCheckX = new_file
    while (squareToCheckY > 0 and squareToCheckX < 7):
        squareToCheckX=squareToCheckX + 1
        squareToCheckY=squareToCheckY - 1
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (bishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 0):
            piecesCheckingArray.append((squareToCheckY, squareToCheckX))
        if (bishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 1):
            break

    squareToCheckY = new_row
    squareToCheckX = new_file
    while (squareToCheckY > 0 and squareToCheckX > 0):
        squareToCheckX=squareToCheckX - 1
        squareToCheckY=squareToCheckY - 1
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (bishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 0):
            piecesCheckingArray.append((squareToCheckY, squareToCheckX))
        if (bishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 1):
            break

    #pawn checks
    squareToCheckY = new_row - 1
    squareToCheckX = new_file - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (not pawnCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
           piecesCheckingArray.append((squareToCheckY, squareToCheckX))

    squareToCheckX = new_file + 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (not pawnCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
            piecesCheckingArray.append((squareToCheckY, squareToCheckX))

    squareToCheckY = new_row + 1
    squareToCheckX = new_file - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (not pawnCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
            piecesCheckingArray.append((squareToCheckY, squareToCheckX))

    squareToCheckX = new_file + 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (not pawnCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
            piecesCheckingArray.append((squareToCheckY, squareToCheckX))
    return piecesCheckingArray 

# take in array notation and return chess notation co-ordinates ( e.g. input : (2, 2) - output : d4
def GetChessNotation(coords):
    row = int(coords[0]) + 1
    column = chr(coords[1]+65)
    return column + str(row)

# Takes in chess notation and retruns coords  
def GetCoords(notation):
    coords = []
    destY = int(notation[1])-1
    destX = ord(notation[0])-65
    coords.append([destY, destX])
    return coords

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
      
