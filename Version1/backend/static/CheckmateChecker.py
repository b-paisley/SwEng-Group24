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
        is_black = 1
   else:
        is_black = 0
   i = 0
   row = 0
   col = 0
   while kingPiece == False:
      for j in range(8):
        piece = currentBoard.board[i][j].placed_in_square
        if piece != None:
          # Black King
          if piece.is_black == True and is_black == True:
            if isinstance(piece, King):
               kingPiece = True
               row = i
               col = j
          
          # White King
          elif piece.is_black == False and is_black == False:
            if isinstance(piece, King):
               kingPiece = True
               row = i
               col = j
      i += 1
      j = 0   
   kingNotation = get_chess_notation((row, col))
   # Possible King moves from current square in chess notation
   notation1 = get_chess_notation((row-1, col))
   notation2 = get_chess_notation((row+1, col))
   notation3 = get_chess_notation((row-1, col-1))
   notation4 = get_chess_notation((row-1, col+1))
   notation5 = get_chess_notation((row+1, col-1))
   notation6 = get_chess_notation((row+1, col+1))
   notation7 = get_chess_notation((row, col-1))
   notation8 = get_chess_notation((row, col+1))
   
   coords = PieceCausingCheck(currentBoard, row, col, is_black)
   checkPieceNotation = get_chess_notation(coords)
   piece = currentBoard.board[coords[0]][coords[1]].placed_in_square

   isCheck = movingIntoCheck(currentBoard, i, j, row, col, is_black) 
   if isCheck == True:
      return False
   # Check if King can move out of check/take piece putting it in check
   elif move_checker(currentBoard, kingNotation, notation1)== True:
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
      # Check if other pieces can take the piece putting the King in check
      for i in range(8):
         for j in range(8):
            piece1 = currentBoard.board[i][j].placed_in_square
            pieceNotation = get_chess_notation((i, j)) 
            if piece1 != None:
               if piece1.is_black and is_black == 1:
                  if move_checker(currentBoard, checkPieceNotation, pieceNotation):
                     return False
               elif not piece1.is_black and is_black == 0:
                   if move_checker(currentBoard, checkPieceNotation, pieceNotation):
                     return False
      # Check if pieces can block 
      # Pawns and Knights can't be blocked -> if get this far, checkmate
      if isinstance(piece, Pawn) or isinstance(piece, Knight):
          return True
      else:
          is_blocked = False
          # Blocking when piece is a Rook
          # Horizontal Check - 
          # Vertical Check - 

          # Blocking when piece is Bishop
          # Blocking when piece is Queen


          if is_blocked == False:
              return True
      
      return True
      
def PieceCausingCheck(chess_board, new_row, new_file, black):  # check what peice is putting check on King
    # check for Rooks putting check on King
    squareToCheckX = new_file + 1
    squareToCheckY = new_row - 2
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if(not knightCheck(chess_board,squareToCheckX,squareToCheckY,black,piece)):
            return piece

    squareToCheckX = new_file - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (not knightCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
            return False

    squareToCheckX = new_file + 1
    squareToCheckY = new_row + 2
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (not knightCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
            return False

    squareToCheckX = new_file - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (not knightCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
            return False

    squareToCheckY = new_row + 1
    squareToCheckX = new_file - 2
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (not knightCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
            return False

    squareToCheckY = new_row - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (not knightCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
            return False

    squareToCheckY = new_row + 1
    squareToCheckX = new_file + 2
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (not knightCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
            return False

    squareToCheckY = new_row - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (not knightCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
            return False

    # check for castles and queen straights
    # 0=castle  1=diff obj  2=nothing

    squareToCheckX = new_file
    squareToCheckY = new_row
    while (squareToCheckX < 7):
        squareToCheckX= squareToCheckX + 1
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (rookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)==0):
            return False
        if (rookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)==1):
            break

    squareToCheckX = new_file
    squareToCheckY = new_row
    while (squareToCheckX > 0):
        squareToCheckX=squareToCheckX - 1
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (rookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 0):
            return False
        if (rookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 1):
            break

    squareToCheckY = new_row
    squareToCheckX = new_file
    while (squareToCheckY < 7):
        squareToCheckY=squareToCheckY + 1
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (rookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 0):
            return False
        if (rookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 1):
            break

    squareToCheckY = new_row
    squareToCheckX = new_file
    while (squareToCheckY > 0):
        squareToCheckY=squareToCheckY - 1
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (rookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 0):
            return False
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
            return (squareToCheckY, squareToCheckX)
        if (bishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 1):
            break

    squareToCheckX = new_file
    squareToCheckY = new_row
    while ((squareToCheckX > 0) and (squareToCheckY < 7)):
        squareToCheckX=squareToCheckX - 1
        squareToCheckY=squareToCheckY + 1
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (bishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 0):
            return (squareToCheckY, squareToCheckX)
        if (bishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 1):
            break

    squareToCheckY = new_row
    squareToCheckX = new_file
    while (squareToCheckY > 0 and squareToCheckX < 7):
        squareToCheckX=squareToCheckX + 1
        squareToCheckY=squareToCheckY - 1
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (bishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 0):
            return (squareToCheckY, squareToCheckX)
        if (bishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 1):
            break

    squareToCheckY = new_row
    squareToCheckX = new_file
    while (squareToCheckY > 0 and squareToCheckX > 0):
        squareToCheckX=squareToCheckX - 1
        squareToCheckY=squareToCheckY - 1
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (bishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 0):
            return (squareToCheckY, squareToCheckX)
        if (bishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece) == 1):
            break

    #pawn checks
    squareToCheckY = new_row - 1
    squareToCheckX = new_file - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (not pawnCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
           return False

    squareToCheckX = new_file + 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (not pawnCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
            return False

    squareToCheckY = new_row + 1
    squareToCheckX = new_file - 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (not pawnCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
            return False

    squareToCheckX = new_file + 1
    if (squareToCheckY >= 0 and squareToCheckX <= 7 and squareToCheckY >= 0 and squareToCheckY <= 7):
        piece = chess_board.board[squareToCheckY][squareToCheckX].placed_in_square
        if (not pawnCheck(chess_board, squareToCheckX, squareToCheckY, black, piece)):
            return False
    return True  

def knightCheck(chess_board, squareToCheckX, squareToCheckY, black, piece):
    if (piece != None):
        if (black == 1):
            if (not piece.is_black):
                if (isinstance(piece, Knight)):
                    return False
        elif (black == 0):
            if (piece.is_black):
                if (isinstance(piece, Knight)):
                    return False
    return True

def rookCheck(chess_board, squareToCheckX, squareToCheckY, black, piece):
    if (piece != None):
        if (black == 1):
            if (not piece.is_black):
                if (isinstance(piece, Rook)):
                    return 0
                if(isinstance(piece, Queen)):
                    return 0
        elif (black == 0):
            if (piece.is_black):
                if (isinstance(piece, Rook)):
                    return 0
                if (isinstance(piece, Queen)):
                    return 0
        return 1
    return 2

def bishopCheck(chess_board, squareToCheckX, squareToCheckY, black, piece):
    if (piece != None):
        if (black == 1):
            if (not piece.is_black):
                if (isinstance(piece, Bishop)):
                    return 0
                if(isinstance(piece, Queen)):
                    return 0
        elif (black == 0):
            if (piece.is_black):
                if (isinstance(piece, Bishop)):
                    return 0
                if (isinstance(piece, Queen)):
                    return 0
        return 1
    return 2

def pawnCheck(chess_board, squareToCheckX, squareToCheckY, black, piece):
    if (piece != None):
        if (black == 1):
            if (not piece.is_black):
                if (isinstance(piece, Pawn)):
                    return False
        elif (black == 0):
            if (piece.is_black):
                if (isinstance(piece, Pawn)):
                    return False
    return True    
      
