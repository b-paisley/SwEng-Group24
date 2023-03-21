
class square:

    # this is for creating the square and will be used only when creating the board
    def __init__(self,square):
        self.square = square
        self.placedInSquare = None

    def place_piece(self,piece):
        if(self.placedInSquare == None):
            self.placedInSquare=piece
        else:
            self.take_piece(piece,self.placedInSquare)
            

    def take_piece(self, piece_take, piece_taken):
        self.placedInSquare=piece_take
        #pieces_pos_dict.pop(piece_taken)      <- TODO: Make this method work
        piece_take.capture(piece_taken)

    def move_off_square(self):
        piece=self.placedInSquare
        self.placedInSquare=None
        return piece

    def GetPiece(self):
        return self.placedInSquare
    

    def ResetSquare(self):
        self.placedInSquare=None