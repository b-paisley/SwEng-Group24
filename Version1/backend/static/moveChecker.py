from chessBoard import *
from Pieces import *
import copy


# Single unified function for checking if a move is legal. Returns true for a legal move, false otherwise
def MoveChecker(chessBoard, prevSquare, newSquare, inDrawFunctionForPossibleEnPassant):
  if prevSquare == "k" or prevSquare == "q":
    return Castling(chessBoard, prevSquare, newSquare)
  if (not isinstance(newSquare[0], str) or not newSquare[1].isdigit()): return False
  prevFile = ord(prevSquare[0]) - 65
  prevRow = int(prevSquare[1]) - 1
  newFile = ord(newSquare[0]) - 65
  newRow = int(newSquare[1]) - 1
  if (newFile < 0 or newRow < 0 or newFile > 7 or newRow > 7): return False
  taking = False

  # Checking if moving square is occupied at all, and if target square is occupied by other piece
  movingSquarePiece = chessBoard.board[prevRow][prevFile].placedInSquare
  if (movingSquarePiece == None): return False
  targetSquarePiece = chessBoard.board[newRow][newFile].placedInSquare
  if (targetSquarePiece != None):
    taking = True
    if (movingSquarePiece.isBlack == targetSquarePiece.isBlack): return False

  #scary
  kingPos = getKingPosition(chessBoard, prevRow, prevFile)
  kingFile = ord(kingPos[0]) - 65
  kingRow = int(kingPos[1]) - 1

  if isinstance(movingSquarePiece, King):
    kingIs= 1
  elif taking:
    pieceCopy = copy.copy(chessBoard.board[newRow][newFile].placedInSquare)
    pieceCopyOurPiece = copy.copy(chessBoard.board[prevRow][prevFile].placedInSquare)
    chessBoard.UpdateBoard(prevSquare, newSquare)

    if not MovingIntoCheck(chessBoard, prevRow, prevFile, kingRow, kingFile,
                       chessBoard.board[newRow][newFile].placedInSquare.isBlack):
      chessBoard.UpdateBoard(newSquare, prevSquare)
      chessBoard.board[newRow][newFile].placedInSquare = pieceCopy
      chessBoard.board[prevRow][prevFile].placedInSquare = pieceCopyOurPiece
      return False
    chessBoard.UpdateBoard(newSquare, prevSquare)
    chessBoard.board[newRow][newFile].placedInSquare = pieceCopy
    chessBoard.board[prevRow][prevFile].placedInSquare = pieceCopyOurPiece
  elif (EnPassant(chessBoard, prevRow, prevFile, newRow, newFile)):
    pieceCopy = copy.copy(chessBoard.board[prevRow][newFile].placedInSquare)
    pieceCopyOurPiece = copy.copy(chessBoard.board[prevRow][prevFile].placedInSquare)
    chessBoard.board[prevRow][newFile].placedInSquare = None
    chessBoard.UpdateBoard(prevSquare, newSquare)
    if not MovingIntoCheck(chessBoard, prevRow, prevFile, kingRow, kingFile,
                       chessBoard.board[newRow][newFile].placedInSquare.isBlack):
      chessBoard.UpdateBoard(newSquare, prevSquare)
      chessBoard.board[prevRow][newFile].placedInSquare = pieceCopy
      chessBoard.board[prevRow][prevFile].placedInSquare = pieceCopyOurPiece
      return False
    chessBoard.UpdateBoard(newSquare, prevSquare)
    chessBoard.board[prevRow][newFile].placedInSquare = pieceCopy
    chessBoard.board[prevRow][prevFile].placedInSquare = pieceCopyOurPiece
  else:
    pieceCopyOurPiece = copy.copy(chessBoard.board[prevRow][prevFile].placedInSquare)
    chessBoard.UpdateBoard(prevSquare, newSquare)
    if not MovingIntoCheck(chessBoard, prevRow, prevFile, kingRow, kingFile,
                        chessBoard.board[newRow][newFile].placedInSquare.isBlack):
      chessBoard.UpdateBoard(newSquare, prevSquare)
      chessBoard.board[prevRow][prevFile].placedInSquare = pieceCopyOurPiece
      return False
    chessBoard.UpdateBoard(newSquare, prevSquare)
    chessBoard.board[prevRow][prevFile].placedInSquare = pieceCopyOurPiece

  movingSquarePiece = chessBoard.board[prevRow][prevFile].placedInSquare


  if (isinstance(movingSquarePiece, Pawn)):
    if (not taking):
      if (not movingSquarePiece.hasMoved):
        if (movingSquarePiece.isBlack and prevRow - 2 == newRow and prevFile == newFile and
          chessBoard.board[prevRow - 1][prevFile].placedInSquare == None): return True
        if (not movingSquarePiece.isBlack and prevRow + 2 == newRow and prevFile == newFile and
          chessBoard.board[prevRow + 1][prevFile].placedInSquare == None): return True
      if (movingSquarePiece.isBlack and prevRow - 1 == newRow and prevFile == newFile): return True
      if (not movingSquarePiece.isBlack and prevRow + 1 == newRow and prevFile == newFile):
        return True
      elif EnPassant(chessBoard, prevRow, prevFile, newRow, newFile):
        theirPieceSquare = newSquare[0] + str(prevSquare[1])
        if (inDrawFunctionForPossibleEnPassant == 1):
          chessBoard.UpdateBoard(theirPieceSquare, newSquare)
        return True
    else:
      if (movingSquarePiece.isBlack and prevRow - 1 == newRow and (1 == abs(newFile - prevFile))): return True
      if (not movingSquarePiece.isBlack and prevRow + 1 == newRow and (1 == abs(newFile - prevFile))): return True
    return False

  if (isinstance(movingSquarePiece, Rook)):
    return CheckStraights(chessBoard, prevRow, prevFile, newRow, newFile)

  if (isinstance(movingSquarePiece, Bishop)):
    return CheckDiagonals(chessBoard, prevRow, prevFile, newRow, newFile)

  if (isinstance(movingSquarePiece, Queen)):
    if (CheckStraights(chessBoard, prevRow, prevFile, newRow, newFile)
      or CheckDiagonals(chessBoard, prevRow, prevFile, newRow, newFile)):
      return True
    else:
      return False

  if (isinstance(movingSquarePiece, Knight)):
    if (abs(newFile - prevFile) == 2 and abs(newRow - prevRow) == 1):
      return True
    elif (abs(newFile - prevFile) == 1 and abs(newRow - prevRow) == 2):
      return True
    else:
      return False

  if (isinstance(movingSquarePiece, King)):
    if (movingSquarePiece.isBlack):
      black = 1
    if (not movingSquarePiece.isBlack):
      black = 0
    if (MovingIntoCheck(chessBoard, prevRow, prevFile, newRow, newFile, black)):
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
      checkedFile = prevFile + 1
      while (checkedFile < newFile):
        if (chessBoard.board[prevRow][checkedFile].placedInSquare != None): return False
        checkedFile += 1
      return True
    else:
      checkedFile = prevFile - 1
      while (checkedFile > newFile):
        if (chessBoard.board[prevRow][checkedFile].placedInSquare != None): return False
        checkedFile -= 1
      return True
  elif (prevFile == newFile):
    if (newRow > prevRow):
      checkedRow = prevRow + 1
      while (checkedRow < newRow):
        if (chessBoard.board[checkedRow][prevFile].placedInSquare != None): return False
        checkedRow += 1
      return True
    else:
      checkedRow = prevRow - 1
      while (checkedRow > newRow):
        if (chessBoard.board[checkedRow][prevFile].placedInSquare != None): return False
        checkedRow -= 1
      return True
  else:
    return False


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
      if (not KnightCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
         return False

    squareToCheckX = newFile - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
      piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
      if (not KnightCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
        return False

    squareToCheckX = newFile + 1
    squareToCheckY = newRow + 2
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
      piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
      if (not KnightCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
        return False

    squareToCheckX = newFile - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
      piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
      if (not KnightCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
        return False

    squareToCheckY = newRow + 1
    squareToCheckX = newFile - 2
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
      piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
      if (not KnightCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
        return False

    squareToCheckY = newRow - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
      piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
      if (not KnightCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
        return False

    squareToCheckY = newRow + 1
    squareToCheckX = newFile + 2
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
      piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
      if (not KnightCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
        return False

    squareToCheckY = newRow - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
      piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
      if (not KnightCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
        return False


  # check for castles and queen straights
  # 0=castle  1=diff obj  2=nothing

    squareToCheckX = newFile
    squareToCheckY = newRow
    while (squareToCheckX < 7):
      squareToCheckX = squareToCheckX + 1
      piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
      if (RookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 0):
        return False
      if (RookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 1):
        if (not isinstance(piece, King)):
          break
        elif (isinstance(piece, King) and piece.isBlack == True and black != 1) or (
          isinstance(piece, King) and piece.isBlack == False and black != 0):
          break

    squareToCheckX = newFile
    squareToCheckY = newRow
    while (squareToCheckX > 0):
      squareToCheckX = squareToCheckX - 1
      piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
      if (RookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 0):
        return False
      if (RookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 1):
        if (not isinstance(piece, King)):
          break
        elif (isinstance(piece, King) and piece.isBlack == True and black != 1) or (
          isinstance(piece, King) and piece.isBlack == False and black != 0):
          break

    squareToCheckY = newRow
    squareToCheckX = newFile
    while (squareToCheckY < 7):
      squareToCheckY = squareToCheckY + 1
      piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
      if (RookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 0):
        return False
      if (RookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 1):
        if (not isinstance(piece, King)):
          break
        elif (isinstance(piece, King) and piece.isBlack == True and black != 1) or (
          isinstance(piece, King) and piece.isBlack == False and black != 0):
          break


    squareToCheckY = newRow
    squareToCheckX = newFile
    while (squareToCheckY > 0):
      squareToCheckY = squareToCheckY - 1
      piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
      if (RookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 0):
        return False
      if (RookCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 1):
        if (not isinstance(piece, King)):
          break
        elif (isinstance(piece, King) and piece.isBlack == True and black != 1) or (
          isinstance(piece, King) and piece.isBlack == False and black != 0):
          break

  # check diagonally for bishops and queens
  # 0=bishop  1=diff obj  2=nothing

    squareToCheckX = newFile
    squareToCheckY = newRow
    while ((squareToCheckX < 7) and (squareToCheckY < 7)):
      squareToCheckX = squareToCheckX + 1
      squareToCheckY = squareToCheckY + 1
      piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
      if (BishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 0):
        return False
      if (BishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 1):
        if (not isinstance(piece, King)):
          break
        elif (isinstance(piece, King) and piece.isBlack == True and black != 1) or (
          isinstance(piece, King) and piece.isBlack == False and black != 0):
          break

    squareToCheckX = newFile
    squareToCheckY = newRow
    while ((squareToCheckX > 0) and (squareToCheckY < 7)):
      squareToCheckX = squareToCheckX - 1
      squareToCheckY = squareToCheckY + 1
      piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
      if (BishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 0):
        return False
      if (BishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 1):
        if (not isinstance(piece, King)):
          break
        elif (isinstance(piece, King) and piece.isBlack == True and black != 1) or (
          isinstance(piece, King) and piece.isBlack == False and black != 0):
          break

    squareToCheckY = newRow
    squareToCheckX = newFile
    while (squareToCheckY > 0 and squareToCheckX < 7):
      squareToCheckX = squareToCheckX + 1
      squareToCheckY = squareToCheckY - 1
      piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
      if (BishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 0):
        return False
      if (BishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 1):
        if (not isinstance(piece, King)):
          break
        elif (isinstance(piece, King) and piece.isBlack == True and black != 1) or (
          isinstance(piece, King) and piece.isBlack == False and black != 0):
          break

    squareToCheckY = newRow
    squareToCheckX = newFile
    while (squareToCheckY > 0 and squareToCheckX > 0):
      squareToCheckX = squareToCheckX - 1
      squareToCheckY = squareToCheckY - 1
      piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
      if (BishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 0):
        return False
      if (BishopCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece) == 1):
        if (not isinstance(piece, King)):
          break
        elif (isinstance(piece, King) and piece.isBlack == True and black != 1) or (
          isinstance(piece, King) and piece.isBlack == False and black != 0):
          break

  # pawn checks
    squareToCheckY = newRow - 1
    squareToCheckX = newFile - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
      piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
      if (not PawnCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
        return False

    squareToCheckX = newFile + 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
      piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
      if (not PawnCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
        return False

    squareToCheckY = newRow + 1
    squareToCheckX = newFile - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
      piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
      if (not PawnCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
        return False

    squareToCheckX = newFile + 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
      piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
      if (not PawnCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
        return False

    # king checks
    squareToCheckY = newRow - 1
    squareToCheckX = newFile - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not KingCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return False

    squareToCheckY = newRow
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not KingCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return False

    squareToCheckY = newRow + 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not KingCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return False

    squareToCheckX = newFile
    squareToCheckY = newRow + 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not KingCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return False

    squareToCheckX = newFile
    squareToCheckY = newRow - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not KingCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return False


    squareToCheckY = newRow - 1
    squareToCheckX = newFile + 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not KingCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return False

    squareToCheckY = newRow
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not KingCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
            return False

    squareToCheckY = newRow + 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chessBoard.board[squareToCheckY][squareToCheckX].placedInSquare
        if (not KingCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece)):
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
        if (isinstance(piece, Queen)):
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
        if (isinstance(piece, Queen)):
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


def KingCheck(chessBoard, squareToCheckX, squareToCheckY, black, piece):
  if (piece != None):
    if (black == 1):
      if (not piece.isBlack):
        if (isinstance(piece, King)):
          return False
    elif (black == 0):
      if (piece.isBlack):
        if (isinstance(piece, King)):
          return False
  return True


def Castling(chessBoard, sideCastling, colour):
  if colour == 0:  # if black
    kingSquare = chessBoard.board[7][4].placedInSquare
    if not isinstance(kingSquare, King):
      return False
    if not MovingIntoCheck(chessBoard, 7, 4, 7, 4, 1):  # if king is currently in check
      return False
    if kingSquare.hasMoved:
      return False
    if sideCastling == "q":  # if queenside castling
      leftRook = chessBoard.board[7][0].placedInSquare
      if not isinstance(leftRook, Rook):
        return False
      if leftRook.hasMoved:
        return False
      b8 = chessBoard.board[7][1].placedInSquare
      c8 = chessBoard.board[7][2].placedInSquare
      d8 = chessBoard.board[7][3].placedInSquare
      if (b8 != None or c8 != None or d8 != None):
        return False
      if not MovingIntoCheck(chessBoard, 7, 3, 7, 3, 1):  # if king is currently in check
        return False
      if not MovingIntoCheck(chessBoard, 7, 2, 7, 2, 1):  # if king is currently in check
        return False
    if sideCastling == "k":  # if kingside castling
      rightRook = chessBoard.board[7][7].placedInSquare
      if not isinstance(rightRook, Rook):
        return False
      if rightRook.hasMoved:
        return False
      g8 = chessBoard.board[7][6].placedInSquare
      f8 = chessBoard.board[7][5].placedInSquare
      if (g8 != None or f8 != None):
        return False
      if not MovingIntoCheck(chessBoard, 7, 5, 7, 5, 1):  # if king is currently in check
        return False
      if not MovingIntoCheck(chessBoard, 7, 6, 7, 6, 1):  # if king is currently in check
        return False

  if colour == 1:  # if white
    kingSquare = chessBoard.board[0][4].placedInSquare
    if not isinstance(kingSquare, King):
      return False
    if not MovingIntoCheck(chessBoard, 0, 4, 0, 4, 0):  # if king is currently in check
      return False
    if kingSquare.hasMoved:
      return False
    if sideCastling == "q":  # if queenside castling
      leftRook = chessBoard.board[0][0].placedInSquare
      if not isinstance(leftRook, Rook):
        return False
      if leftRook.hasMoved:
        return False
      b1 = chessBoard.board[0][1].placedInSquare
      c1 = chessBoard.board[0][2].placedInSquare
      d1 = chessBoard.board[0][3].placedInSquare
      if (b1 != None or c1 != None or d1 != None):
        return False
      if not MovingIntoCheck(chessBoard, 0, 3, 0, 3, 0):  # if king is currently in check
        return False
      if not MovingIntoCheck(chessBoard, 0, 2, 0, 2, 0):  # if king is currently in check
        return False
    if sideCastling == "k":  # if kingside castling
      rightRook = chessBoard.board[0][7].placedInSquare
      if not isinstance(rightRook, Rook):
        return False
      if rightRook.hasMoved:
        return False
      g1 = chessBoard.board[0][6].placedInSquare
      f1 = chessBoard.board[0][5].placedInSquare
      if (g1 != None or f1 != None):
        return False
      if not MovingIntoCheck(chessBoard, 0, 5, 0, 5, 0):  # if king is currently in check
        return False
      if not MovingIntoCheck(chessBoard, 0, 6, 0, 6, 0):  # if king is currently in check
        return False
  return True


def EnPassant(chessBoard, prev_row, prev_file, newRow, newFile):
  ourPiece = chessBoard.board[prev_row][prev_file].placedInSquare
  theirPiece = chessBoard.board[prev_row][newFile].placedInSquare
  destinationSquare = chessBoard.board[newRow][newFile].placedInSquare
  if ((abs((prev_file-newFile))!=1)):
    return False
  if (not isinstance(ourPiece, Pawn)) or (not isinstance(theirPiece, Pawn)):  # if not two pawns there false
    return False
  if (ourPiece.isBlack and prev_row != 3 and newRow != 2) or (
    not ourPiece.isBlack and prev_row != 4 and newRow != 5):  # if wrong location false
    return False
  if destinationSquare != None:  # this will never be true as they just moved two but just in case x
    return False
  if not theirPiece.hasMovedTwoSpacesLast:  # if their pawn hasn't just moved forward two
    return False
  return True


def getKingPosition(chessBoard, prevRow, prevFile):
  kingPiece = False
  isBlack = chessBoard.board[prevRow][prevFile].placedInSquare.isBlack
  i = 0
  row = 0
  col = 0
  while kingPiece == False:
    for j in range(8):
      piece = chessBoard.board[i][j].placedInSquare
      if piece != None:
        # Black King
        if piece.isBlack == True and isBlack == True:
          if isinstance(piece, King):
            kingPiece = True
            row = i
            col = j

        # White King
        elif piece.isBlack == False and isBlack == False:
          if isinstance(piece, King):
            kingPiece = True
            row = i
            col = j
    i += 1
    j = 0
  return GetChessNotation((row, col))

# Check if king is in Checkmate
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
      piece = currentBoard.board[i][j].placedInSquare
      if piece != None:
        # Black King
        if piece.isBlack == True and isBlack == True:
          if isinstance(piece, King):
            kingPiece = True
            row = i
            col = j

        # White King
        elif piece.isBlack == False and isBlack == False:
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
  coordsCheckPieceArray = PiecesCausingCheck(currentBoard, row, col, isBlack)
  coordsCheckPiece = (coordsCheckPieceArray[0][0], coordsCheckPieceArray[0][1])
  checkPieceNotation = GetChessNotation(coordsCheckPiece)

  if len(coordsCheckPieceArray) == 1:
    # Check if King can move out of check/take piece putting it in check
    k = 0
    while k < len(kingNotationArray):
      if MoveChecker1(currentBoard, kingNotation, kingNotationArray[k], 0):
        return False
      k += 1
    else:
      piecesArray = GetPieceArray(currentBoard, playerColour)
      if CheckPieceTake(currentBoard, piecesArray, checkPieceNotation, isBlack) == False:
        return False

        # Check if pieces can block
        # Pawns and Knights can't be blocked -> if get this far, checkmate
      if isinstance(piece, Pawn) or isinstance(piece, Knight):
        return True
      else:
        # Check if there is a square between king and pieceChecking
        if (coordsCheckPiece[0] == kingRow + 1 and coordsCheckPiece[1] == kingCol) or (
          coordsCheckPiece[0] == kingRow - 1 and coordsCheckPiece[1] == kingCol):
          return True
        elif (coordsCheckPiece[0] == kingRow - 1 and coordsCheckPiece[1] == kingCol + 1) or (
          coordsCheckPiece[0] == kingRow - 1 and coordsCheckPiece[1] == kingCol - 1):
          return True
        elif (coordsCheckPiece[0] == kingRow + 1 and coordsCheckPiece[1] == kingCol + 1) or (
          coordsCheckPiece[0] == kingRow + 1 and coordsCheckPiece[1] == kingCol - 1):
          return True
        elif (coordsCheckPiece[0] == kingRow and coordsCheckPiece[1] == kingCol - 1) or (
          coordsCheckPiece[0] == kingRow and coordsCheckPiece[1] == kingCol + 1):
          return True
        # Blocking when piece checking is a Rook/Queen straight
        if CheckHorizonal(currentBoard, coordsCheckPiece, kingRow, kingCol, piecesArray, isBlack) == False:
          return False
        if CheckVertical(currentBoard, coordsCheckPiece, kingRow, kingCol, piecesArray, isBlack) == False:
          return False
        # Blocking when piece checking is Bishop/Queen diag
        if CheckLeftDiagonal(currentBoard, coordsCheckPiece, kingRow, kingCol, piecesArray, isBlack) == False:
          return False
        if CheckRightDiagonal(currentBoard, coordsCheckPiece, kingRow, kingCol, piecesArray, isBlack) == False:
          return False
  else:
    # More than one piece putting king in check
    # Check if King can move out of check/take piece putting it in check
    k = 0
    while k < len(kingNotationArray):
      if MoveChecker1(currentBoard, kingNotation, kingNotationArray[k], 0):
        return False
      k += 1
  return True  # if get this far its checkmate

def CheckPieceTake(currentBoard, piecesArray, checkPieceNotation, isBlack):
  i = 0
  # Check if other pieces can take the piece putting the King in check
  while i < len(piecesArray):
    pieceTaking = piecesArray[i]
    pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placedInSquare
    pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1]))
    if not isinstance(pieceName, King):
      if pieceName.isBlack and isBlack == 1:
        if MoveChecker1(currentBoard, pieceNotation, checkPieceNotation, 0):
          return False
      elif not pieceName.isBlack and isBlack == 0:
        if MoveChecker1(currentBoard, pieceNotation, checkPieceNotation, 0):
          return False
    i += 1


def CheckHorizonal(currentBoard, coordsCheckPiece, kingRow, kingCol, piecesArray, isBlack):
  # Horizontal -
  if coordsCheckPiece[0] == kingRow:
    checkCol = coordsCheckPiece[1] + 1
    # Horizontal Left Check -
    if coordsCheckPiece[1] < kingCol:
      while checkCol < kingCol:
        blockNotation = GetChessNotation((kingRow, checkCol))
        j = 0
        while j < len(piecesArray):
          pieceTaking = piecesArray[j]
          pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placedInSquare
          pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1]))
          if not isinstance(pieceName, King):
            if pieceName.isBlack and isBlack == 1:
              if MoveChecker1(currentBoard, pieceNotation, blockNotation, 0):
                return False
            elif not pieceName.isBlack and isBlack == 0:
              if MoveChecker1(currentBoard, pieceNotation, blockNotation, 0):
                return False
          j += 1
        checkCol += 1
    # Horizontal Right Check -
    elif coordsCheckPiece[1] > kingCol:
      checkCol = coordsCheckPiece[1] - 1
      while checkCol > kingCol:
        blockNotation = GetChessNotation((kingRow, checkCol))
        j = 0
        while j < len(piecesArray):
          pieceTaking = piecesArray[j]
          pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placedInSquare
          pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1]))
          if not isinstance(pieceName, King):
            if pieceName.isBlack and isBlack == 1:
              if MoveChecker1(currentBoard, pieceNotation, blockNotation, 0) == True:
                return False
            elif not pieceName.isBlack and isBlack == 0:
              if MoveChecker1(currentBoard, pieceNotation, blockNotation, 0) == True:
                return False
          j += 1
        checkCol -= 1
  return True


def CheckVertical(currentBoard, coordsCheckPiece, kingRow, kingCol, piecesArray, isBlack):
  # Vertical -
  if coordsCheckPiece[1] == kingCol:
    checkRow = coordsCheckPiece[0] + 1
    # Vertical Above Check -
    if coordsCheckPiece[0] < kingRow:
      while checkRow < kingRow:
        blockNotation = GetChessNotation((checkRow, kingCol))
        j = 0
        while j < len(piecesArray):
          pieceTaking = piecesArray[j]
          pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placedInSquare
          pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1]))
          if not isinstance(pieceName, King):
            if pieceName.isBlack and isBlack == 1:
              if MoveChecker1(currentBoard, pieceNotation, blockNotation, 0):
                return False
            elif not pieceName.isBlack and isBlack == 0:
              if MoveChecker1(currentBoard, pieceNotation, blockNotation, 0):
                return False
          j += 1
        checkRow += 1
        # Vertical Below Check -
    elif coordsCheckPiece[0] > kingRow:
      checkRow = coordsCheckPiece[0] - 1
      while checkRow > kingRow:
        blockNotation = GetChessNotation((checkRow, kingCol))
        j = 0
        while j < len(piecesArray):
          pieceTaking = piecesArray[j]
          pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placedInSquare
          pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1]))
          if not isinstance(pieceName, King):
            if pieceName.isBlack and isBlack == 1:
              if MoveChecker1(currentBoard, pieceNotation, blockNotation, 0):
                return False
            elif not pieceName.isBlack and isBlack == 0:
              if MoveChecker1(currentBoard, pieceNotation, blockNotation, 0):
                return False
          j += 1
        checkRow -= 1
  return True


def CheckLeftDiagonal(currentBoard, coordsCheckPiece, kingRow, kingCol, piecesArray, isBlack):
  # Diag Left Below
  if coordsCheckPiece[0] < kingRow and coordsCheckPiece[1] < kingCol:
    checkCol = coordsCheckPiece[1] + 1
    checkRow = coordsCheckPiece[0] + 1
    while checkCol < kingCol and checkRow < kingRow:
      blockNotation = GetChessNotation((checkRow, checkCol))
      j = 0
      while j < len(piecesArray):
        pieceTaking = piecesArray[j]
        pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placedInSquare
        pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1]))
        if not isinstance(pieceName, King):
          if pieceName.isBlack and isBlack == 1:
            if MoveChecker1(currentBoard, pieceNotation, blockNotation, 0):
              return False
          elif not pieceName.isBlack and isBlack == 0:
            if MoveChecker1(currentBoard, pieceNotation, blockNotation, 0):
              return False
        j += 1
      checkCol += 1
      checkRow += 1
  # Diag Left Above
  elif coordsCheckPiece[0] > kingRow and coordsCheckPiece[1] < kingCol:
    checkCol = coordsCheckPiece[1] + 1
    checkRow = coordsCheckPiece[0] - 1
    while checkCol < kingCol and checkRow > kingRow:
      blockNotation = GetChessNotation((checkRow, checkCol))
      j = 0
      while j < len(piecesArray):
        pieceTaking = piecesArray[j]
        pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placedInSquare
        pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1]))
        if not isinstance(pieceName, King):
          if pieceName.isBlack and isBlack == 1:
            if MoveChecker1(currentBoard, pieceNotation, blockNotation, 0):
              return False
          elif not pieceName.isBlack and isBlack == 0:
            if MoveChecker1(currentBoard, pieceNotation, blockNotation, 0):
              return False
        j += 1
      checkCol += 1
      checkRow -= 1
  return True


def CheckRightDiagonal(currentBoard, coordsCheckPiece, kingRow, kingCol, piecesArray, isBlack):
  # Diag Right Below
  if coordsCheckPiece[0] < kingRow and coordsCheckPiece[1] > kingCol:
    checkCol = coordsCheckPiece[1] - 1
    checkRow = coordsCheckPiece[0] + 1
    while checkCol > kingCol and checkRow < kingRow:
      blockNotation = GetChessNotation((checkRow, checkCol))
      j = 0
      while j < len(piecesArray):
        pieceTaking = piecesArray[j]
        pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placedInSquare
        pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1]))
        if not isinstance(pieceName, King):
          if pieceName.isBlack and isBlack == 1:
            if MoveChecker1(currentBoard, pieceNotation, blockNotation, 0):
              return False
          elif not pieceName.isBlack and isBlack == 0:
            if MoveChecker1(currentBoard, pieceNotation, blockNotation, 0):
              return False
        j += 1
      checkCol -= 1
      checkRow += 1
  # Diag Right Above
  elif coordsCheckPiece[0] > kingRow and coordsCheckPiece[1] < kingCol:
    checkCol = coordsCheckPiece[1] - 1
    checkRow = coordsCheckPiece[0] - 1
    while checkCol > kingCol and checkRow > kingRow:
      blockNotation = GetChessNotation((checkRow, checkCol))
      j = 0
      while j < len(piecesArray):
        pieceTaking = piecesArray[j]
        pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placedInSquare
        pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1]))
        if not isinstance(pieceName, King):
          if pieceName.isBlack and isBlack == 1:
            if MoveChecker1(currentBoard, pieceNotation, blockNotation, 0):
              return False
          elif not pieceName.isBlack and isBlack == 0:
            if MoveChecker1(currentBoard, pieceNotation, blockNotation, 0):
              return False
        j += 1
      checkCol -= 1
      checkRow -= 1
  return True


def PiecesCausingCheck(chess_board, new_row, new_file, black):  # check what peice is putting check on King
  piecesCheckingArray = []
  # check for Rooks putting check on King
  squareToCheckX = new_file + 1
  squareToCheckY = new_row - 2
  if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
    piece = chess_board.board[squareToCheckY][squareToCheckX].placedInSquare
    if (not KnightCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
      piecesCheckingArray.append((squareToCheckY, squareToCheckX))

  squareToCheckX = new_file - 1
  if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
    piece = chess_board.board[squareToCheckY][squareToCheckX].placedInSquare
    if (not KnightCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
      piecesCheckingArray.append((squareToCheckY, squareToCheckX))

  squareToCheckX = new_file + 1
  squareToCheckY = new_row + 2
  if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
    piece = chess_board.board[squareToCheckY][squareToCheckX].placedInSquare
    if (not KnightCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
      piecesCheckingArray.append((squareToCheckY, squareToCheckX))

  squareToCheckX = new_file - 1
  if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
    piece = chess_board.board[squareToCheckY][squareToCheckX].placedInSquare
    if (not KnightCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
      piecesCheckingArray.append((squareToCheckY, squareToCheckX))

  squareToCheckY = new_row + 1
  squareToCheckX = new_file - 2
  if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
    piece = chess_board.board[squareToCheckY][squareToCheckX].placedInSquare
    if (not KnightCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
      piecesCheckingArray.append((squareToCheckY, squareToCheckX))

  squareToCheckY = new_row - 1
  if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
    piece = chess_board.board[squareToCheckY][squareToCheckX].placedInSquare
    if (not KnightCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
      piecesCheckingArray.append((squareToCheckY, squareToCheckX))

  squareToCheckY = new_row + 1
  squareToCheckX = new_file + 2
  if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
    piece = chess_board.board[squareToCheckY][squareToCheckX].placedInSquare
    if (not KnightCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
      piecesCheckingArray.append((squareToCheckY, squareToCheckX))

  squareToCheckY = new_row - 1
  if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
    piece = chess_board.board[squareToCheckY][squareToCheckX].placedInSquare
    if (not KnightCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
      piecesCheckingArray.append((squareToCheckY, squareToCheckX))

  # check for castles and queen straights
  # 0=castle  1=diff obj  2=nothing

  squareToCheckX = new_file
  squareToCheckY = new_row
  while (squareToCheckX < 7):
    squareToCheckX = squareToCheckX + 1
    piece = chess_board.board[squareToCheckY][squareToCheckX].placedInSquare
    if (RookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 0):
      piecesCheckingArray.append((squareToCheckY, squareToCheckX))
    if (RookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 1):
      break

  squareToCheckX = new_file
  squareToCheckY = new_row
  while (squareToCheckX > 0):
    squareToCheckX = squareToCheckX - 1
    piece = chess_board.board[squareToCheckY][squareToCheckX].placedInSquare
    if (RookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 0):
      piecesCheckingArray.append((squareToCheckY, squareToCheckX))
    if (RookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 1):
      break

  squareToCheckY = new_row
  squareToCheckX = new_file
  while (squareToCheckY < 7):
    squareToCheckY = squareToCheckY + 1
    piece = chess_board.board[squareToCheckY][squareToCheckX].placedInSquare
    if (RookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 0):
      piecesCheckingArray.append((squareToCheckY, squareToCheckX))
    if (RookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 1):
      break

  squareToCheckY = new_row
  squareToCheckX = new_file
  while (squareToCheckY > 0):
    squareToCheckY = squareToCheckY - 1
    piece = chess_board.board[squareToCheckY][squareToCheckX].placedInSquare
    if (RookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 0):
      piecesCheckingArray.append((squareToCheckY, squareToCheckX))
    if (RookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 1):
      break

  # check diagonally for bishops and queens
  # 0=bishop  1=diff obj  2=nothing

  squareToCheckX = new_file
  squareToCheckY = new_row
  while ((squareToCheckX < 7) and (squareToCheckY < 7)):
    squareToCheckX = squareToCheckX + 1
    squareToCheckY = squareToCheckY + 1
    piece = chess_board.board[squareToCheckY][squareToCheckX].placedInSquare
    if (BishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 0):
      piecesCheckingArray.append((squareToCheckY, squareToCheckX))
    if (BishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 1):
      break

  squareToCheckX = new_file
  squareToCheckY = new_row
  while ((squareToCheckX > 0) and (squareToCheckY < 7)):
    squareToCheckX = squareToCheckX - 1
    squareToCheckY = squareToCheckY + 1
    piece = chess_board.board[squareToCheckY][squareToCheckX].placedInSquare
    if (BishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 0):
      piecesCheckingArray.append((squareToCheckY, squareToCheckX))
    if (BishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 1):
      break

  squareToCheckY = new_row
  squareToCheckX = new_file
  while (squareToCheckY > 0 and squareToCheckX < 7):
    squareToCheckX = squareToCheckX + 1
    squareToCheckY = squareToCheckY - 1
    piece = chess_board.board[squareToCheckY][squareToCheckX].placedInSquare
    if (BishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 0):
      piecesCheckingArray.append((squareToCheckY, squareToCheckX))
    if (BishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 1):
      break

  squareToCheckY = new_row
  squareToCheckX = new_file
  while (squareToCheckY > 0 and squareToCheckX > 0):
    squareToCheckX = squareToCheckX - 1
    squareToCheckY = squareToCheckY - 1
    piece = chess_board.board[squareToCheckY][squareToCheckX].placedInSquare
    if (BishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 0):
      piecesCheckingArray.append((squareToCheckY, squareToCheckX))
    if (BishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 1):
      break

  # pawn checks
  squareToCheckY = new_row - 1
  squareToCheckX = new_file - 1
  if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
    piece = chess_board.board[squareToCheckY][squareToCheckX].placedInSquare
    if (not PawnCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
      piecesCheckingArray.append((squareToCheckY, squareToCheckX))

  squareToCheckX = new_file + 1
  if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
    piece = chess_board.board[squareToCheckY][squareToCheckX].placedInSquare
    if (not PawnCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
      piecesCheckingArray.append((squareToCheckY, squareToCheckX))

  squareToCheckY = new_row + 1
  squareToCheckX = new_file - 1
  if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
    piece = chess_board.board[squareToCheckY][squareToCheckX].placedInSquare
    if (not PawnCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
      piecesCheckingArray.append((squareToCheckY, squareToCheckX))

  squareToCheckX = new_file + 1
  if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
    piece = chess_board.board[squareToCheckY][squareToCheckX].placedInSquare
    if (not PawnCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
      piecesCheckingArray.append((squareToCheckY, squareToCheckX))
  return piecesCheckingArray


# take in array notation and return chess notation co-ordinates ( e.g. input : (2, 2) - output : d4
def GetChessNotation(coords):
  row = int(coords[0]) + 1
  column = chr(coords[1] + 65)
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
      piece = chessBoard.board[i][j].placedInSquare
      if piece != None:
        # Black Piece Array
        if piece.isBlack == True and isBlack == True:
          pieceArray.append([i, j])

        # White Piece Array
        elif piece.isBlack == False and isBlack == False:
          pieceArray.append([i, j])

  return pieceArray



# Single unified function for checking if a move is legal. Returns true for a legal move, false otherwise
def MoveChecker1(chessBoard, prevSquare, newSquare, inDrawFunctionForPossibleEnPassant):
  if prevSquare == "k" or prevSquare == "q":
    return Castling(chessBoard, prevSquare, newSquare)
  if (not isinstance(newSquare[0], str) or not newSquare[1].isdigit()): return False
  prevFile = ord(prevSquare[0]) - 65
  prevRow = int(prevSquare[1]) - 1
  newFile = ord(newSquare[0]) - 65
  newRow = int(newSquare[1]) - 1
  if (newFile < 0 or newRow < 0 or newFile > 7 or newRow > 7): return False
  taking = False

  # Checking if moving square is occupied at all, and if target square is occupied by other piece
  movingSquarePiece = chessBoard.board[prevRow][prevFile].placedInSquare
  if (movingSquarePiece == None): return False
  targetSquarePiece = chessBoard.board[newRow][newFile].placedInSquare
  if (targetSquarePiece != None):
    taking = True
    if (movingSquarePiece.isBlack == targetSquarePiece.isBlack): return False

  #scary
  kingPos = getKingPosition(chessBoard, prevRow, prevFile)
  kingFile = ord(kingPos[0]) - 65
  kingRow = int(kingPos[1]) - 1


  if (isinstance(movingSquarePiece, Pawn)):
    if (not taking):
      if (not movingSquarePiece.hasMoved):
        if (movingSquarePiece.isBlack and prevRow - 2 == newRow and prevFile == newFile and
          chessBoard.board[prevRow - 1][prevFile].placedInSquare == None): return True
        if (not movingSquarePiece.isBlack and prevRow + 2 == newRow and prevFile == newFile and
          chessBoard.board[prevRow + 1][prevFile].placedInSquare == None): return True
      if (movingSquarePiece.isBlack and prevRow - 1 == newRow and prevFile == newFile): return True
      if (not movingSquarePiece.isBlack and prevRow + 1 == newRow and prevFile == newFile):
        return True
      elif EnPassant(chessBoard, prevRow, prevFile, newRow, newFile):
        theirPieceSquare = newSquare[0] + str(prevSquare[1])
        #if (inDrawFunctionForPossibleEnPassant == 1):
         # chessBoard.update_board(theirPieceSquare, newSquare)
        return True
    else:
      if (movingSquarePiece.isBlack and prevRow - 1 == newRow and (1 == abs(newFile - prevFile))): return True
      if (not movingSquarePiece.isBlack and prevRow + 1 == newRow and (1 == abs(newFile - prevFile))): return True
    return False

  if (isinstance(movingSquarePiece, Rook)):
    return CheckStraights(chessBoard, prevRow, prevFile, newRow, newFile)

  if (isinstance(movingSquarePiece, Bishop)):
    return CheckDiagonals(chessBoard, prevRow, prevFile, newRow, newFile)

  if (isinstance(movingSquarePiece, Queen)):
    if (CheckStraights(chessBoard, prevRow, prevFile, newRow, newFile)
      or CheckDiagonals(chessBoard, prevRow, prevFile, newRow, newFile)):
      return True
    else:
      return False

  if (isinstance(movingSquarePiece, Knight)):
    if (abs(newFile - prevFile) == 2 and abs(newRow - prevRow) == 1):
      return True
    elif (abs(newFile - prevFile) == 1 and abs(newRow - prevRow) == 2):
      return True
    else:
      return False

  if (isinstance(movingSquarePiece, King)):
    if (movingSquarePiece.isBlack):
      black = 1
    if (not movingSquarePiece.isBlack):
      black = 0
    if (MovingIntoCheck(chessBoard, prevRow, prevFile, newRow, newFile, black)):
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
      checkedFile = prevFile + 1
      while (checkedFile < newFile):
        if (chessBoard.board[prevRow][checkedFile].placedInSquare != None): return False
        checkedFile += 1
      return True
    else:
      checkedFile = prevFile - 1
      while (checkedFile > newFile):
        if (chessBoard.board[prevRow][checkedFile].placedInSquare != None): return False
        checkedFile -= 1
      return True
  elif (prevFile == newFile):
    if (newRow > prevRow):
      checkedRow = prevRow + 1
      while (checkedRow < newRow):
        if (chessBoard.board[checkedRow][prevFile].placedInSquare != None): return False
        checkedRow += 1
      return True
    else:
      checkedRow = prevRow - 1
      while (checkedRow > newRow):
        if (chessBoard.board[checkedRow][prevFile].placedInSquare != None): return False
        checkedRow -= 1
      return True
  else:
    return False


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
