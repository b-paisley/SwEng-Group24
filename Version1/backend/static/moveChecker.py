from chessBoard import *
from Pieces import *


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
          chessBoard.update_board(theirPieceSquare, newSquare)
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
      while (checkedRow < newRow):
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
