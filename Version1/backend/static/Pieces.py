from chessBoard import *
from Points import *

class Piece:
    '''
    Abstract "piece" class. All of the pieces in
    the game will extend from this class.
    '''

    def __init__(self, value, isBlack):
        self.value = value
        self.isBlack = isBlack
        self.hasMoved = False
        self.isCaptured = False

    def __repr__(self, notation):
        if not self.isBlack:
            return notation.lower()
        return notation

    def Capture(self, other):
        '''
        Captures the opposing piece.
        '''
        other.Remove()

    def Remove(self):
        '''
        Removes the piece from the game.
        '''
        self.isCaptured = True
        

class Pawn(Piece):

    def __init__(self, isBlack):
        super().__init__(1, isBlack)
        self.hasMovedTwoSpacesLast = False

    def Promote(self, newPieceNotation):
        '''
        Promote the pawn to another piece. Returns a
        boolean variable determining if the promotion
        is successful.
        '''

        notationPiecesDict = {
        'R': Rook,
        'N': Knight,
        'B': Bishop,
        'Q': Queen,
        'K': King
        }
        
        if newPieceNotation not in notationPiecesDict.keys() or newPieceNotation == 'K':
            return False
        
        self.__class__ = (notationPiecesDict[newPieceNotation])
        return True

    def __repr__(self):
        return super().__repr__('P')


class Rook(Piece):
    def __init__(self, isBlack):
        super().__init__(5, isBlack)

    def __repr__(self):
        return super().__repr__('R')


class Knight(Piece):
    def __init__(self, isBlack):
        super().__init__(3, isBlack)

    def __repr__(self) -> str:
        return super().__repr__('N')


class Bishop(Piece):
    def __init__(self, isBlack):
        super().__init__(3, isBlack)

    def __repr__(self):
        return super().__repr__('B')


class King(Piece):
    def __init__(self, isBlack):
        super().__init__(0, isBlack)

    def __repr__(self):
        return super().__repr__('K')


class Queen(Piece):
    def __init__(self, isBlack):
        super().__init__(9, isBlack)

    def __repr__(self):
        return super().__repr__('Q')
