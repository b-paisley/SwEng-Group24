from chessBoard import *
from Points import *
from Pieces import *
from moveChecker import *
from aiMoveGenerator import *
from PiecesPosDict import *

board = ChessBoard()
board.draw()
class Game:
    count = 0
    for i in range(32):
        piece_to_draw = list(pieces_pos_dict.keys())[i]
        square_to_fill = pieces_pos_dict[piece_to_draw]
        board.orginal_draw(piece_to_draw, square_to_fill)
    board.draw()
    black=False

    def play(self):  
        if self.count == 0:
            board.update_board('B1','C3') #updates board
        self.count = 1      
        # print("white goes first")
        
        # move=input("Input move (example='C1_C2') ").upper() #get's input 
        # if(move=="QUIT"):  #checks if quit is used
        #     play=False #stops game
        # else:
        #     valid_move=False #both bools have to be set false to check error handling
        #     proper_colour = False
        #     while(not valid_move or not proper_colour):
        #         valid_move=move_checker(board,move[0:2],move[3:5]) #if valid
        #         if(board.access_square(move[0:2]).is_black==black): #check that not moving other player piece
        #             proper_colour=True
        #         if (not valid_move or not proper_colour):
        #             move=input("error not a valid move please try again: ").upper()
        #     black = not black #changes to other turn
    def getBoard(self):
            return board