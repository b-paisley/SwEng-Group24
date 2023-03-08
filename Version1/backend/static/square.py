
class square:

    # this is for creating the square and will be used only when creating the board
    def __init__(self,square):
        self.square = square
        self.placedInSquare = None

    def PlacePiece(self,piece):
        if(self.placedInSquare == None):
            self.placedInSquare=piece
        else:
            self.takePiece(piece,self.placedInSquare)
            

    def TakePiece(self, pieceTake, pieceTaken):
        self.placedInSquare=pieceTake
        #piecesPosDict.pop(pieceTaken)      <- TODO: Make this method work
        pieceTake.capture(pieceTaken)

    def MoveOffSquare(self):
        piece=self.placedInSquare
        self.placedInSquare=None
        return piece

    def GetPiece(self):
        thing=self.placedInSquare
        return thing
