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
   
   isCheck = movingIntoCheck(currentBoard, i, j, row, col, is_black) 
   if isCheck == True:
      return False
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
      return True
      
      
      
