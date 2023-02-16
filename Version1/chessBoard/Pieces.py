from chessBoard import *
from Points import *

notation_pieces_dict = {
    '':'Pawn',
    'R':'Rook',
    'N':'Knight',
    'B':'Bishop',
    'Q':'Queen',
    'K':'King'
    }

class Piece:
    '''
    Abstract "piece" class. All of the pieces in
    the game will extend from this class.
    '''
    def __init__(self, value, is_black, pos,points):
        self.value = value
        self.is_black = is_black
        self.pos = pos
        if(self.is_black):
            points.change_b_points(self.value)
        else:
            points.change_w_points(self.value)


    def pos_to_tuple(self):
        '''
        Returns the position of the piece as a
        2-tuple containing the row and the
        column of the position. The row and
        column numbers are one-indexed.

        Example: 'c2' -> (3,2)
        '''
        rows = 'abcdefgh'
        row = rows.index(self.pos[0]) + 1
        col = int(self.pos[1])
        return (row, col)

    def __repr__(self, notation):
        return notation

    def capture(self, other,points):
        '''
        Captures the opposing piece. Returns True if
        a piece is captured.
        '''
        
        other.remove(points)

    def remove(self,points):
        '''
        Removes the piece from the game. Returns a
        2-tuple containing the value and the colour
        of the piece.
        '''
        if(self.is_black):
            points.change_b_points(-self.value)
        else:
            points.change_w_points(-self.value)
        value = self.value
        colour = self.is_black
        del self
        return (value,colour)


class Pawn(Piece):
    
    def __init__(self, is_black, pos,points):
        super().__init__(1, is_black, pos,points)
        

    def promote(self, new_piece_notation):
        '''
        Promote the pawn to another piece. Returns a
        boolean variable determining if the promotion
        is successful.
        '''
        if new_piece_notation not in notation_pieces_dict.keys() or new_piece_notation == '' \
            or new_piece_notation == 'K':
            return False
        self.__class__ = eval(notation_pieces_dict[new_piece_notation])
        return True

    def __repr__(self):
        return super().__repr__('')


class Rook(Piece):
    def __init__(self, is_black, pos,points):
        super().__init__(5, is_black, pos,points)
        
    def __repr__(self):
        return super().__repr__('R')
    

class Knight(Piece):
    def __init__(self, is_black, pos,points):
        super().__init__(3, is_black, pos,points)
    
    def __repr__(self) -> str:
        return super().__repr__('N')


class Bishop(Piece):
    def __init__(self, is_black, pos,points):
        super().__init__(3, is_black, pos,points)

    def __repr__(self):
        return super().__repr__('B')


class King(Piece):
    def __init__(self, is_black, pos,points):
        super().__init__(0, is_black, pos,points)

    def __repr__(self):
        return super().__repr__('K')


class Queen(Piece):
    def __init__(self, is_black, pos,points):
        super().__init__(9, is_black, pos,points)

    def __repr__(self):
        return super().__repr__('Q')