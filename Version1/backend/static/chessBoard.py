from Pieces import *
from square import *


class ChessBoard:
    board = []
    enpassantSquare = '-'
    fullMoveCount = 2
    halfMoveCount = 0
    # board bottom left starting point
    def __init__(self):
        letters = "ABCDEFGH"
        self.board = [[], [], [], [], [], [], [], []]
        for i in range(8):  # num
          for j in range(8):  # char
            self.board[i].append(square(letters[j] + str(i + 1)))
        self.possibleEnPassantPawn = None

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
        oldLetterFile = ord(prevSquare[0])-65
        oldNumberRow = int(prevSquare[1]) - 1
        piece = self.board[oldNumberRow][oldLetterFile].MoveOffSquare()

        newLetterFile = ord(newSquare[0])-65
        newNumberRow = int(newSquare[1]) - 1

        taken =False
        if self.AccessSquare(newSquare) != None:
            taken = True
        self.board[newNumberRow][newLetterFile].PlacePiece(piece)

        # If a position that allows en passant was two moves ago, en passant is no
        # longer possible.
        if self.possibleEnPassantPawn != None:
            self.possibleEnPassantPawn.hasMovedTwoSpacesLast = False
            self.possibleEnPassantPawn = None

        # If a position that allows en passant is reached, allow en passant.
        if isinstance(piece, Pawn):
            if piece.isBlack:
                if oldNumberRow == 6 and newNumberRow == 4:
                    piece.hasMovedTwoSpacesLast = True
                    self.possibleEnPassantPawn = piece
            else:
                if oldNumberRow == 1 and newNumberRow == 3:
                    piece.hasMovedTwoSpacesLast = True
                    self.possibleEnPassantPawn = piece
        piece.hasMoved = True
        if repr(self.AccessSquare(newSquare)).lower() == "p":
            if (not piece.hasMovedTwoSpacesLast) and (newNumberRow == 3 or newNumberRow == 4 ):
                if piece.isBlack:
                    self.enpassantSquare=newSquare[0].lower()+str(newNumberRow+2)
                else:
                    self.enpassantSquare=newSquare[0].lower()+str(newNumberRow)
        else:
            self.enpassantSquare = '-'
        piece.hasMovedTwoSpacesLast = True
        self.fullMoveCount+=1
        if repr(piece).lower() == 'p' or taken:
            self.halfMoveCount=0
        else:
            self.halfMoveCount+=1     
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

    def ProperFen(self, isBlack):
        count=0
        strFen=""
        for i in range(8):
            for j in range(8):
                piece = self.board[abs(i-7)][j].placedInSquare
                if(piece==None):
                    count+=1
                else:
                    pieceStr = ""
                    if repr(piece).islower():
                        pieceStr=repr(piece).upper()
                    else:
                        pieceStr = repr(piece).lower()
                    strFen+=(str(count) if count!=0 else "")+pieceStr
                    count=0
            if(count!=0):
                strFen+=str(count)
                count=0
            if(i!=7):
                strFen+="/"
        if isBlack:
            strFen+= " b "
        else:
            strFen+=" w "
        entered = False
        if repr(self.AccessSquare("E1")) == "k":
            if self.AccessSquare("E1").hasMoved == False:
                if repr(self.AccessSquare("H1")) == "r":
                    if self.AccessSquare("H1").hasMoved == False:
                        strFen+="K"
                        entered=True
                if repr(self.AccessSquare("A1")) =="r":
                    if self.AccessSquare("A1").hasMoved == False:
                        strFen+="Q"
                        entered=True
        if (repr(self.AccessSquare("E8"))) == "K":
            if self.AccessSquare("E8").hasMoved == False:
                if repr(self.AccessSquare("H8")) == "R":
                    if self.AccessSquare("H8").hasMoved == False:
                        strFen+="k"
                        entered=True
                if repr(self.AccessSquare("A8")) =="R":
                    if self.AccessSquare("A8").hasMoved == False:
                        strFen+="q"
                        entered=True
        if entered:
            strFen+=" "
        else:
            strFen+="- "
        strFen += self.enpassantSquare
        strFen+=" "+str(self.halfMoveCount)
        strFen+=" "+str(int(self.fullMoveCount/2))
        return strFen