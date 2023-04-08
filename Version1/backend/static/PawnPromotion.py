from Pieces import *

def PawnPromotion(currentBoard, move):
    coords = GetCoords(move[3:5])
    piece = currentBoard.board[coords[0][0]][coords[0][1]].placedInSquare
    if isinstance(piece, Pawn):
       i = 0
       if piece.isBlack == True and coords[0][0] == 0:
           promote = input("Choose a piece to promote to [Q, R, B, N]")
           piece = Promote(piece, promote)
           return piece
       elif piece.isBlack == False and coords[0][0] == 7:
           promote = input("Choose a piece to promote to [Q, R, B, N] ")
           piece = Promote(piece, promote)
           return piece
    return piece

# Takes in chess notation and retruns coords  
def GetCoords(notation):
    coords = []
    destY = int(notation[1])-1
    destX = ord(notation[0])-65
    coords.append([destY, destX])
    return coords