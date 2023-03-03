from chessBoard import *
from Points import *
from Pieces import *
from moveChecker import *
from aiMoveGenerator import *
from PiecesPosDict import *
'''
from allMovesFinder import *
from tests import *

test_all_moves_finder_pawn()
'''

board = ChessBoard()
board.draw()

for i in range(32):
    piece_to_draw = list(pieces_pos_dict.keys())[i]
    square_to_fill = pieces_pos_dict[piece_to_draw]
    board.orginal_draw(piece_to_draw, square_to_fill)

board.draw()
play=True
black=False
thing=board.GiveFEN()
print("white goes first")
while(play):
    move=input("Input move (example='C1_C2') ").upper() #get's input 
    if(move=="QUIT"):  #checks if quit is used
        play=False #stops game
    else:
        valid_move=False #both bools have to be set false to check error handling
        proper_colour = False
        while(not valid_move or not proper_colour):
            valid_move=move_checker(board,move[0:2],move[3:5]) #if valid
            if(board.access_square(move[0:2]).is_black==black): #check that not moving other player piece
                proper_colour=True
            if (not valid_move or not proper_colour):
                move=input("error not a valid move please try again: ").upper()
        board.update_board(move[0:2],move[3:5]) #updates board
        thing=board.GiveFEN()
        black = not black #changes to other turn
# print("The AI Player played " + ai_move_generator(board, 'black'))
# Quick Example Game - Player V Person
'''
next_turn = False
colour = True
while colour: t
    player_colour = input("Pick your colour [white or blank]: \n")
    if player_colour.lower() == 'black':
        ai_colour = 'white'
        colour = False
    elif player_colour.lower() == 'white':
        ai_color = 'black'
        colour = False
    elif player_colour.lower() != 'white' or player_colour.lower() != 'black':
        print("Enter the colour White or Black \n")
        
# When 0 -> Player Turn/When 1 -> AI Turn
turn_tracker = 0
game_over = False

while not game_over:
    if turn_tracker == 0:
        while not next_turn:
            piece = input("Enter the chess notation of the piece you want to move: \n")
            move = input("Enter your move in chess notation: \n")
            if move_checker(board, piece, move):
                next_turn = True
            else:
                print("Invalid Move! Try Again \n")
        board.update_board(piece, move)
        print("The Player played " + piece + move)
        turn_tracker = 1
    elif turn_tracker == 1:
        print("The AI Player played " + ai_move_generator(board, ai_colour))
        turn_tracker = 0




# board.update_board("A7", "A6")
'''
'''

#Testing AI Move Generator Function - black pieces
black_pieces_array = [Knight(True,'f2',point), Pawn(True,'f2',point), Pawn(True,'d7',point)]
print(ai_move_generator(board, black_pieces_array))

#Testing AI Move Generator Function - white pieces
white_pieces_array = [Knight(False,'f2',point), Pawn(False,'d2',point), Pawn(False,'b7',point)]
print(ai_move_generator(board, white_pieces_array))
'''

# In this prototype chess game, the game ends when black or white lose all of their
# pieces.
