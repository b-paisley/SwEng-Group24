
class square:

    # this is for creating the square and will be used only when creating the board
    def __init__(self,square):
        self.square = square
        self.placed_in_square = None

    def place_piece(self,piece):
        if(self.placed_in_square == None):
            self.placed_in_square=piece
        else:
            self.take_piece(piece,self.placed_in_square)
            

    def take_piece(self, piece_take, piece_taken):
        self.placed_in_square=piece_take
        #pieces_pos_dict.pop(piece_taken)      <- TODO: Make this method work
        piece_take.capture(piece_taken)

    def move_off_square(self):
        piece=self.placed_in_square
        self.placed_in_square=None
        return piece

    def GetPiece(self):
        return self.placed_in_square
    

    def ResetSquare(self):
        self.placed_in_square=None