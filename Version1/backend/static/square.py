
class square:

    # this is for creating the square and will be used only when creating the board
    def __init__(self,square):
        self.square = square
        self.PlacedInSquare = None

    def PlacePiece(self,piece):
        if(self.PlacedInSquare == None):
            self.PlacedInSquare=piece
        else:
            self.TakePiece(piece,self.PlacedInSquare)
            

    def TakePiece(self, pieceTake, pieceTaken):
        self.PlacedInSquare=pieceTake
        #piecesPosDict.pop(pieceTaken)      <- TODO: Make this method work
        pieceTake.Capture(pieceTaken)

    def MoveOffSquare(self):
        piece=self.PlacedInSquare
        self.PlacedInSquare=None
        return piece

    def GetPiece(self):
        output=self.PlacedInSquare
        return output
