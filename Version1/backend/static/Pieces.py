from chessBoard import *
from Points import *

class Piece:
    '''
    Abstract "piece" class. All of the pieces in
    the game will extend from this class.
    '''

    def __init__(self, value, is_black):
        self.value = value
        self.is_black = is_black
        self.has_moved = False
        self.is_captured = False

    def __repr__(self, notation):
        if not self.is_black:
            return notation.lower()
        return notation

    def capture(self, other):
        '''
        Captures the opposing piece.
        '''
        other.remove()

    def remove(self):
        '''
        Removes the piece from the game.
        '''
        self.is_captured = True
        

class Pawn(Piece):

    def __init__(self, is_black):
        super().__init__(1, is_black)
        self.has_moved_two_spaces_last = False

    def promote(self, new_piece_notation):
        '''
        Promote the pawn to another piece. Returns a
        boolean variable determining if the promotion
        is successful.
        '''

        notation_pieces_dict = {
        'R': Rook,
        'N': Knight,
        'B': Bishop,
        'Q': Queen,
        'K': King
        }
        
        if new_piece_notation not in notation_pieces_dict.keys() or new_piece_notation == 'K':
            return False
        
        self.__class__ = (notation_pieces_dict[new_piece_notation])
        return True

    def __repr__(self):
        return super().__repr__('P')


class Rook(Piece):
    def __init__(self, is_black):
        super().__init__(5, is_black)

    def __repr__(self):
        return super().__repr__('R')


class Knight(Piece):
    def __init__(self, is_black):
        super().__init__(3, is_black)

    def __repr__(self) -> str:
        return super().__repr__('N')


class Bishop(Piece):
    def __init__(self, is_black):
        super().__init__(3, is_black)

    def __repr__(self):
        return super().__repr__('B')


class King(Piece):
    def __init__(self, is_black):
        super().__init__(0, is_black)

    def __repr__(self):
        return super().__repr__('K')


class Queen(Piece):
    def __init__(self, is_black):
        super().__init__(9, is_black)

    def __repr__(self):
        return super().__repr__('Q')