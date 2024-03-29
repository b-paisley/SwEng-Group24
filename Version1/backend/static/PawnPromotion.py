from Pieces import *

def PawnPromotion(currentBoard, move, newPieceNotation):
    '''
    Function that takes in the board, the current move being
    played and the new notation of the piece. (R,N,B,Q)

    Promotes the pawn.
    '''
    coords = GetCoords(move[3:5])
    piece = currentBoard.board[coords[0][0]][coords[0][1]].placedInSquare
    if isinstance(piece, Pawn):
       i = 0
       if piece.isBlack == True and coords[0][0] == 0:
           piece = Promote(piece, newPieceNotation)
           currentBoard.board[coords[0][0]][coords[0][1]].placedInSquare = piece
       elif piece.isBlack == False and coords[0][0] == 7:
           piece = Promote(piece, newPieceNotation)
           print(piece)
           currentBoard.board[coords[0][0]][coords[0][1]].placedInSquare = piece
           print(currentBoard.board[coords[0][0]][coords[0][1]].GetPiece())
    return currentBoard

# Takes in chess notation and retruns coords  
def GetCoords(notation):
    coords = []
    destY = int(notation[1])-1
    destX = ord(notation[0])-65
    coords.append([destY, destX])
    return coords