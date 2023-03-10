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
    
    board.update_board('E8', 'A6')
    board.update_board('D8', 'C6')
    board.update_board('C1', 'D3')
    board.update_board('F1', 'C3')
    board.update_board('D1', 'E3')
    bool = CheckmateChecker(board, 'black')

    # Queen blocks rook
    # board.update_board('E8', 'E4')
    # board.update_board('D8', 'F6')
    # board.update_board('A1', 'G4')
    # board.update_board('H1', 'A5')

    #vertical rook test
    #board.update_board('E8', 'A4')
    #board.update_board('D8', 'F5')
    #board.update_board('A1', 'A6')
    #board.update_board('H1', 'B6')
    #board.update_board('B7', 'C6')
    #board.update_board('B8', 'A8')
    #board.update_board('C8', 'B8')

    #king-bishop-pawn test
    #board.update_board('E8', 'B3')
    #board.update_board('C1', 'F4')
    #board.update_board('G7', 'G5')

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