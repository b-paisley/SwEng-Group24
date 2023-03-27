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
      if MoveChecker(currentBoard, kingNotation, kingNotationArray[k], 0):
        return False
      k += 1
    else:
      piecesArray = GetPieceArray(currentBoard, playerColour)
      if CheckPieceBlock(currentBoard, piecesArray, checkPieceNotation, isBlack) == False:
        return False
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
        if checkHorizonal(currentBoard, coordsCheckPiece, kingRow, kingCol, piecesArray, isBlack) == False:
          return False
        if checkVertical(currentBoard, coordsCheckPiece, kingRow, kingCol, piecesArray, isBlack):
          return False
        # Blocking when piece checking is Bishop/Queen diag
        if CheckLeftDiagonal(currentBoard, coordsCheckPiece, kingRow, kingCol, piecesArray, isBlack) == False:
          return False
        if CheckRightDiagonal(currentBoard, coordsCheckPiece, kingRow, kingCol, piecesArray, isBlack):
          return False
  else:
    # More than one piece putting king in check
    # Check if King can move out of check/take piece putting it in check
    k = 0
    while k < len(kingNotationArray):
      if MoveChecker(currentBoard, kingNotation, kingNotationArray[k], 0):
        return False
      k += 1
  return True  # if get this far its checkmate


def CheckPieceBlock(currentBoard, piecesArray, checkPieceNotation, isBlack):
  # Check if other pieces can take the piece putting the King in check
  i = 0
  while i < len(piecesArray):
    pieceTaking = piecesArray[i]
    pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placedInSquare
    pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1]))
    if not isinstance(pieceName, King):
      if pieceName.isBlack and isBlack == 1:
        if MoveChecker(currentBoard, pieceNotation, checkPieceNotation, 0):
          return False
      elif not pieceName.isBlack and isBlack == 0:
        if MoveChecker(currentBoard, pieceNotation, checkPieceNotation, 0):
          return False
    i += 1
  return True


def CheckPieceTake(currentBoard, piecesArray, checkPieceNotation, isBlack):
  i = 0
  # Check if other pieces can take the piece putting the King in check
  while i < len(piecesArray):
    pieceTaking = piecesArray[i]
    pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placedInSquare
    pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1]))
    if not isinstance(pieceName, King):
      if pieceName.isBlack and isBlack == 1:
        if MoveChecker(currentBoard, pieceNotation, checkPieceNotation, 0):
          return False
      elif not pieceName.isBlack and isBlack == 0:
        if MoveChecker(currentBoard, pieceNotation, checkPieceNotation, 0):
          return False
    i += 1


def checkHorizonal(currentBoard, coordsCheckPiece, kingRow, kingCol, piecesArray, isBlack):
  i=0
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
              if MoveChecker(currentBoard, pieceNotation, blockNotation, 0):
                return False
            elif not pieceName.isBlack and isBlack == 0:
              if MoveChecker(currentBoard, pieceNotation, blockNotation, 0):
                return False
          j += 1
        checkCol += 1
        i += 1
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
              if MoveChecker(currentBoard, pieceNotation, blockNotation, 0) == True:
                return False
            elif not pieceName.isBlack and isBlack == 0:
              if MoveChecker(currentBoard, pieceNotation, blockNotation, 0) == True:
                return False
          j += 1
        checkCol -= 1
        i += 1
  return True


def checkVertical(currentBoard, coordsCheckPiece, kingRow, kingCol, piecesArray, isBlack):
  # Vertical -
  i=0
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
              if MoveChecker(currentBoard, pieceNotation, blockNotation, 0):
                return False
            elif not pieceName.isBlack and isBlack == 0:
              if MoveChecker(currentBoard, pieceNotation, blockNotation, 0):
                return False
          j += 1
        checkRow += 1
        i += 1
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
              if MoveChecker(currentBoard, pieceNotation, blockNotation, 0):
                return False
            elif not pieceName.isBlack and isBlack == 0:
              if MoveChecker(currentBoard, pieceNotation, blockNotation, 0):
                return False
          j += 1
        checkRow -= 1
        i += 1
  return True


def CheckLeftDiagonal(currentBoard, coordsCheckPiece, kingRow, kingCol, piecesArray, isBlack):
  i=0
  # Diag Left Below
  if coordsCheckPiece[0] < kingRow and coordsCheckPiece[1] < kingCol:
    checkCol = coordsCheckPiece[1] + 1
    checkRow = coordsCheckPiece[1] + 1
    while checkCol < kingCol and checkRow < kingRow:
      blockNotation = GetChessNotation((checkRow, checkCol))
      j = 0
      while j < len(piecesArray):
        pieceTaking = piecesArray[j]
        pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placedInSquare
        pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1]))
        if not isinstance(pieceName, King):
          if pieceName.isBlack and isBlack == 1:
            if MoveChecker(currentBoard, pieceNotation, blockNotation, 0):
              return False
          elif not pieceName.isBlack and isBlack == 0:
            if MoveChecker(currentBoard, pieceNotation, blockNotation, 0):
              return False
        j += 1
      checkCol += 1
      checkRow += 1
      i += 1
  # Diag Left Above
  elif coordsCheckPiece[0] > kingRow and coordsCheckPiece[1] < kingCol:
    checkCol = coordsCheckPiece[1] + 1
    checkRow = coordsCheckPiece[1] - 1
    while checkCol < kingCol and checkRow > kingRow:
      blockNotation = GetChessNotation((checkRow, checkCol))
      j = 0
      while j < len(piecesArray):
        pieceTaking = piecesArray[j]
        pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placedInSquare
        pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1]))
        if not isinstance(pieceName, King):
          if pieceName.isBlack and isBlack == 1:
            if MoveChecker(currentBoard, pieceNotation, blockNotation, 0):
              return False
          elif not pieceName.isBlack and isBlack == 0:
            if MoveChecker(currentBoard, pieceNotation, blockNotation, 0):
              return False
        j += 1
      checkCol += 1
      checkRow -= 1
      i += 1
  return True


def CheckRightDiagonal(currentBoard, coordsCheckPiece, kingRow, kingCol, piecesArray, isBlack):
  i=0
  # Diag Right Below
  if coordsCheckPiece[0] < kingRow and coordsCheckPiece[1] > kingCol:
    checkCol = coordsCheckPiece[1] - 1
    checkRow = coordsCheckPiece[1] + 1
    while checkCol > kingCol and checkRow < kingRow:
      blockNotation = GetChessNotation((checkRow, checkCol))
      j = 0
      while j < len(piecesArray):
        pieceTaking = piecesArray[j]
        pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placedInSquare
        pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1]))
        if not isinstance(pieceName, King):
          if pieceName.isBlack and isBlack == 1:
            if MoveChecker(currentBoard, pieceNotation, blockNotation, 0):
              return False
          elif not pieceName.isBlack and isBlack == 0:
            if MoveChecker(currentBoard, pieceNotation, blockNotation, 0):
              return False
        j += 1
      checkCol -= 1
      checkRow += 1
      i += 1
  # Diag Right Above
  elif coordsCheckPiece[0] > kingRow and coordsCheckPiece[1] < kingCol:
    checkCol = coordsCheckPiece[1] - 1
    checkRow = coordsCheckPiece[1] - 1
    while checkCol > kingCol and checkRow > kingRow:
      blockNotation = GetChessNotation((checkRow, checkCol))
      j = 0
      while j < len(piecesArray):
        pieceTaking = piecesArray[j]
        pieceName = currentBoard.board[pieceTaking[0]][pieceTaking[1]].placedInSquare
        pieceNotation = GetChessNotation((pieceTaking[0], pieceTaking[1]))
        if not isinstance(pieceName, King):
          if pieceName.isBlack and isBlack == 1:
            if MoveChecker(currentBoard, pieceNotation, blockNotation, 0):
              return False
          elif not pieceName.isBlack and isBlack == 0:
            if MoveChecker(currentBoard, pieceNotation, blockNotation, 0):
              return False
        j += 1
      checkCol -= 1
      checkRow -= 1
      i += 1
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
