from chessBoard import *
from Points import *
from Pieces import *
from moveChecker import *
from aiMoveGenerator import *
from PiecesPosDict import *
from CheckmateChecker import *


# board.draw()
class Game:
    board = ChessBoard()
    for i in range(32):
        piece_to_draw = list(pieces_pos_dict.keys())[i]
        square_to_fill = pieces_pos_dict[piece_to_draw]
        board.orginal_draw(piece_to_draw, square_to_fill)
    board.draw()
    black=False
    
    board.update_board('E8', 'E3')
    bool = CheckmateChecker(board, 'black')

    def playMove(self, move:str):  
        move = move.upper()

        valid_move=False #both bools have to be set false to check error handling
        proper_colour = False
        valid_move=move_checker(self.board,move[0:2],move[3:5]) #if valid
        if(self.board.access_square(move[0:2]).is_black==self.black): #check that not moving other player piece
            proper_colour=True
        if (not valid_move or not proper_colour):
             return "error"
        self.board.update_board(move[0:2],move[3:5]) #updates board
        self.black = not self.black #changes to other turn

    def getBoard(self):
            return self.board