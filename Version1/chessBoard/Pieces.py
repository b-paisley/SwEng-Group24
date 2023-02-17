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

files = 'abcdefgh'
rows = [i for i in range(1,9)]

class Piece:
    '''
    Abstract "piece" class. All of the pieces in
    the game will extend from this class.

    The "pos" parameter will take in a named square,
    like "e2".
    '''
    def __init__(self, value, is_black, pos, points, board):
        self.value = value
        self.is_black = is_black
        self.pos = pos
        self.has_moved = False
        if self.is_black:
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
        
        col = files.index(self.pos[0]) + 1
        row = int(self.pos[1])
        return (col, row)

    def __repr__(self, notation):
        if not self.is_black:
            return notation.lower()
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
    
    def move(self, new_pos, valid_square) -> bool:
        '''
        Moves the piece to a desired square.
        Returns True if the move is valid. Else it
        returns False.
        '''
        if self.pos == new_pos or not valid_square:
            return False
        
        self.pos = new_pos
        has_moved = True
        return True


class Pawn(Piece):
    
    def __init__(self, is_black, pos,points, board):
        super().__init__(1, is_black, pos,points, board)
        self.has_moved_two_spaces_last = False
        

    def promote(self, new_piece_notation):
        '''
        Promote the pawn to another piece. Returns a
        boolean variable determining if the promotion
        is successful.
        '''
        if new_piece_notation not in notation_pieces_dict.keys() or new_piece_notation == '' \
            or new_piece_notation == 'K' or new_piece_notation == 'k':
            return False
        self.__class__ = eval(notation_pieces_dict[new_piece_notation])
        return True

    def __repr__(self):
        return super().__repr__('')
    
    def move_forwards_one(self):
        if not self.is_black:
            self.pos = self.pos[0] + str(int(self.pos[1])+1)
        else:
            self.pos = self.pos[0] + str(int(self.pos[1])-1)
        self.has_moved_two_spaces_last = False

    def move_forwards_two(self):
        if not self.is_black:
            self.pos = self.pos[0] + str(int(self.pos[1])+2)
        else:
            self.pos = self.pos[0] + str(int(self.pos[1])-2)
        self.has_moved_two_spaces_last = True

    def move_diagonally_left(self):
        if not self.is_black:
            self.pos = self.pos[0] + str(int(self.pos[1])+1)
        else:
            self.pos = self.pos[0] + str(int(self.pos[1])-1)
        self.pos = files[files.index(self.pos[0])-1] + self.pos[1]
        self.has_moved_two_spaces_last = False

    def move_diagonally_right(self):
        if not self.is_black:
            self.pos = self.pos[0] + str(int(self.pos[1])+1)
        else:
            self.pos = self.pos[0] + str(int(self.pos[1])-1)
        self.pos = files[files.index(self.pos[0])+1] + self.pos[1]
        self.has_moved_two_spaces_last = False


class Rook(Piece):
    def __init__(self, is_black, pos,points):
        super().__init__(5, is_black, pos,points)
        
    def __repr__(self):
        return super().__repr__('R')
    
    def move(self, new_pos):
        is_valid = (new_pos[0] == self.pos[0]) ^ (new_pos[1] == self.pos[1])

        super().move(new_pos, is_valid)
    

class Knight(Piece):
    def __init__(self, is_black, pos,points):
        super().__init__(3, is_black, pos,points)
    
    def __repr__(self) -> str:
        return super().__repr__('N')
    
    def move(self, new_pos: str):
        is_valid = (abs(rows.index(self.pos[1]) - rows.index(new_pos[1])) == 1 and \
        abs(files.index(self.pos[0]) - files.index(new_pos[0])) == 2) or \
        (abs(rows.index(self.pos[1]) - rows.index(new_pos[1])) == 2 and \
        abs(files.index(self.pos[0]) - files.index(new_pos[0])) == 1)

        super().move(new_pos, is_valid)


class Bishop(Piece):
    def __init__(self, is_black, pos,points):
        super().__init__(3, is_black, pos,points)

    def __repr__(self):
        return super().__repr__('B')
    
    def move(self, new_pos):
        is_valid = abs(rows.index[self.pos[1]] - rows.index(new_pos[1])) == \
        abs(files.index(self.pos[0]) - files.index(new_pos[0]))

        super().move(new_pos, is_valid)


class King(Piece):
    def __init__(self, is_black, pos,points):
        super().__init__(0, is_black, pos,points)

    def __repr__(self):
        return super().__repr__('K')
    
    def move(self, new_pos):
        is_valid = abs(rows.index(self.pos[1]) - rows.index(new_pos[1])) <= 1 and \
            abs(files.index(self.pos[0]) - files.index(new_pos[0])) <= 1
        
        super().move(new_pos, is_valid)


class Queen(Piece):
    def __init__(self, is_black, pos,points):
        super().__init__(9, is_black, pos,points)

    def __repr__(self):
        return super().__repr__('Q')
    
    def move(self, new_pos):
        is_valid = (abs(rows.index[self.pos[1]] - rows.index(new_pos[1])) == \
        abs(files.index(self.pos[0]) - files.index(new_pos[0]))) or (
            (new_pos[0] == self.pos[0]) ^ (new_pos[1] == self.pos[1])
        )

        super().move(new_pos, is_valid)

