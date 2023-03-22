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

    def AccessSquare(self, square):
        letterFile = ord(square[0])-65
        numberRow = int(square[1]) - 1
        return self.board[numberRow][letterFile].GetPiece()

    # add all the original piece when completed the call draw
    def OriginalDraw(self, piece, square):
        # doing unicode calculations, easiest way to get the first index
        letterFile = ord(square[0])-65
        numberRow = int(square[1]) - 1
        squareObj = self.board[numberRow][letterFile]
        squareObj.PlacePiece(piece)

    def Draw(self):
        print("\n   +---+---+---+---+---+---+---+---+")
        for i in range(8):
            print(" "+str(8-i)+" ", end="")
            for j in range(8):
                piece = self.board[abs(i-7)][j].placedInSquare
                print("| ", end="")
                if (piece == None):
                    print("  ", end="")
                else:
                    print(repr(piece)+" ", end="")
            print("|")
            print("   +---+---+---+---+---+---+---+---+")
        print("     A   B   C   D   E   F   G   H\n")

    def UpdateBoard(self, prevSquare, newSquare):  # C1_C2
        letterFile = ord(prevSquare[0])-65
        numberRow = int(prevSquare[1]) - 1
        piece = self.board[numberRow][letterFile].MoveOffSquare()

        letterFile = ord(newSquare[0])-65
        numberRow = int(newSquare[1]) - 1

        pieceInDest = self.board[numberRow][letterFile].GetPiece()

        self.board[numberRow][letterFile].PlacePiece(piece)

        piece.hasMoved = True
        piece.hasMovedTwoSpacesLast = True 
        
        self.Draw()

    #will return FEN(Forsyth–Edwards Notation) this is return string
    def GiveFEN(self):
        count=0
        strFen=""
        for i in range(8):
            for j in range(8):
                piece = self.board[abs(i-7)][j].placedInSquare
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

