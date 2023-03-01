from Pieces import *
from square import *


class ChessBoard:
    board = [[], [], [], [], [], [], [], []]
    # board bottom left starting point
    def __init__(self):
        letters = "ABCDEFGH"
        for i in range(8):  # num
            for j in range(8):  # char
                self.board[i].append(square(letters[j]+str(i+1)))
                # print((self.board[i][j]).square)

    def access_square(self, square):
        letter_file = ord(square[0])-65
        number_row = int(square[1]) - 1
        return self.board[number_row][letter_file].get_piece()

    # add all the orginal piece when completed the call draw
    def orginal_draw(self, piece, square):
        # doing unicode calculations, easiest way to get the first index
        letter_file = ord(square[0])-65
        number_row = int(square[1]) - 1
        square_obj = self.board[number_row][letter_file]
        square_obj.place_piece(piece)

    def draw(self):
        print("\n   +---+---+---+---+---+---+---+---+")
        for i in range(8):
            print(" "+str(8-i)+" ", end="")
            for j in range(8):
                piece = self.board[abs(i-7)][j].placed_in_square
                print("| ", end="")
                if (piece == None):
                    print("  ", end="")
                else:
                    print(repr(piece)+" ", end="")
            print("|")
            print("   +---+---+---+---+---+---+---+---+")
        print("     A   B   C   D   E   F   G   H\n")

    def update_board(self, prev_square, new_square):  # C1_C2
        letter_file = ord(prev_square[0])-65
        number_row = int(prev_square[1]) - 1
        piece = self.board[number_row][letter_file].move_off_square()

        letter_file = ord(new_square[0])-65
        number_row = int(new_square[1]) - 1
        
        piece_in_dest = self.board[number_row][letter_file].get_piece()
        
        self.board[number_row][letter_file].place_piece(piece)
        
        piece.has_moved = True
        
        self.draw()

    #will return FEN(Forsyth–Edwards Notation) this is return string
    def giveFEN(self):
        count=0
        strFen=""
        for i in range(8):
            for j in range(8):
                piece = self.board[abs(i-7)][j].placed_in_square
                if(piece==None):
                    count+=1
                else:
                    strFen+=(str(count) if count!=0 else "")+repr(piece)
                    count=0
            if(count!=0):
                strFen+=str(count)
                count=0
            if(i!=7):
                strFen+="/"
        return strFen
    