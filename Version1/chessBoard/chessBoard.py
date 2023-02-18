from Pieces import *
from square import *

class ChessBoard:

    #board bottom left starting point
    def __init__(self):
        letters="ABCDEFGH"    
        self.board= [[],[],[],[],[],[],[],[]]
        for i in range(8): #num
            for j in range (8): #char
                self.board[i].append(square(letters[j]+str(i+1)))
                #print((self.board[i][j]).square)
    
    #add all the orginal piece when completed the call draw
    def orginal_draw(self,piece,square):
        letter_file = 65-ord(square[0])  #doing unicode calculations, easiest way to get the first index
        number_row = square[1] -1 
        square_obj=self.board[letter_file][number_row]
        self.board[letter_file][number_row]=square_obj.place_piece(piece)

    def draw(self): 
        print("\n   +---+---+---+---+---+---+---+---+")
        for i in range(8):
            print(" "+str(8-i)+" ",end="")
            for j in range(8):
                piece=self.board[-(i+1)][j].placed_in_square
                print("| ",end="")
                if (piece == None):
                    print("  ",end="")
                else:
                    print(+repr(piece)+" ",end="")
            print("|")
            print("   +---+---+---+---+---+---+---+---+")
        print("     A   B   C   D   E   F   G   H\n")


    def update_board(self,prev_square, new_square): #C1_C2
        letter_file = 65-ord(prev_square[0])
        number_row = prev_square[1] -1
        piece=self.board[letter_file][number_row].move_off_square()

        letter_file = 65-ord(new_square[0])
        number_row = new_square[1] -1
        self.board[letter_file][number_row].place_piece(piece)
        self.draw()
         
