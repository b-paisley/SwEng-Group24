from chessBoard import *
from Points import *
from Pieces import *
from moveChecker import *
from aiMoveGenerator import *
from PiecesPosDict import *


board = ChessBoard()
board.draw()

for i in range(32):
    piece_to_draw = list(pieces_pos_dict.keys())[i]
    square_to_fill = pieces_pos_dict[piece_to_draw]
    board.orginal_draw(piece_to_draw, square_to_fill)

board.draw()
# print("The AI Player played " + ai_move_generator(board, 'black'))
# Quick Example Game - Player V Person
next_turn = False
colour = True
while colour:
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
# Big block of tests. Run these to get a better feel for how the move_checker handles certain things.
# Can be deleted whenever, just for demo purposes

# Pawn Testing
print(move_checker(board, "A2", "A3")) # True
print(move_checker(board, "A2", "A4")) # True
print(move_checker(board, "A2", "B3")) # False
print(move_checker(board, "A2", "A5")) # False
print(move_checker(board, "A4", "A5")) # False (It's actually checking for piece)
board.update_board("A2", "A4")
print(move_checker(board, "A4", "A5")) # True
print(move_checker(board, "A4", "A6")) # False
print(move_checker(board, "A4", "B5")) # False
print(move_checker(board, "B7", "B5")) # True
board.update_board("B7", "B5")
print(move_checker(board, "A4", "B5")) # True (Take logic for Pawn)
print(move_checker(board, "B5", "A4")) # True (Take logic for Pawn)

# Knight Testing
print(move_checker(board, "B1", "B3")) # False
print(move_checker(board, "B1", "C3")) # True
board.update_board("B1", "C3")
print(move_checker(board, "C3", "E3")) # False
print(move_checker(board, "C3", "E2")) # False (Collision with friendly piece disallowed)
print(move_checker(board, "C3", "B5")) # True (Collision with enemy piece allowed)

# Bishop Testing
board.update_board("G7", "G6")
print(move_checker(board, "F8", "F7")) # False
print(move_checker(board, "F8", "E7")) # False
print(move_checker(board, "F8", "G7")) # True
print(move_checker(board, "F8", "H7")) # False
print(move_checker(board, "F8", "H6")) # True
board.update_board("F8", "H6")
print(move_checker(board, "H6", "F4")) # True
board.update_board("H6", "F4")
print(move_checker(board, "F4", "C7")) # False (Collision)
print(move_checker(board, "F4", "D2")) # True (Take)
print(move_checker(board, "B8", "C6")) # True 
board.update_board("B8", "C6")
print(move_checker(board, "F4", "B8")) # False (Blocked Far) 
print(move_checker(board, "C6", "E5")) # True 
board.update_board("C6", "E5")
print(move_checker(board, "F4", "D6")) # False (Blocked Close)

# Rook Testing
print(move_checker(board, "A1", "A4")) # False
print(move_checker(board, "A1", "C1")) # False
print(move_checker(board, "A1", "B1")) # True
print(move_checker(board, "A1", "A3")) # True
board.update_board("A1", "A3")
print(move_checker(board, "A3", "F3")) # False
print(move_checker(board, "A3", "C4")) # False
print(move_checker(board, "A3", "C3")) # False
print(move_checker(board, "A3", "B3")) # True

# Queen testing
print(move_checker(board, "D8", "B6")) # False
print(move_checker(board, "C7", "C6")) # True
board.update_board("C7", "C6")
print(move_checker(board, "D8", "B6")) # True
board.update_board("D8", "B6")
print(move_checker(board, "B6", "C5")) # True
board.update_board("B6", "C5")
print(move_checker(board, "C5", "D5")) # True
print(move_checker(board, "C5", "A5")) # False
print(move_checker(board, "C5", "D6")) # True
print(move_checker(board, "C5", "D7")) # False
print(move_checker(board, "C5", "F8")) # False
print(move_checker(board, "C5", "F2")) # True


# Bill checking if King is working
#test set #1 move king around unchecked
board.update_board("E8", "E5")  # update the board
print(move_checker(board, "E5", "D5")) # check if it can move left
print(move_checker(board, "E5", "F5")) # check if it can move Right
print(move_checker(board, "E5", "E6")) # check if it can move UP
print(move_checker(board, "E5", "E4")) # check if it can move Down
print(move_checker(board, "E5", "F6")) # check if it can move r U
print(move_checker(board, "E5", "D6")) # check if it can move l u
print(move_checker(board, "E5", "F4")) # check if it can move r d
print(move_checker(board, "E5", "D4")) # check if it can move r d

#test set #2 move king into knight checks

print(move_checker(board, "E7", "E6"))  # move a pawn out of the way (true)
board.update_board("E7", "E6")  # update the board
print(move_checker(board, "E8", "E7"))  # move the king forward one(true)
board.update_board("E8", "E7")  # update the board
print(move_checker(board, "E7", "D6"))  # try to move king into open square
board.update_board("B1", "C4")  # move knight near king
print(move_checker(board, "E7", "D6"))  # try to move king into knight check (false)

# test set #3 move king into straight checks and blocked straight checks

board.update_board("E8", "E5")  # move king into the middle
board.update_board("A1", "D3")  # move rook near middle
print(move_checker(board, "E5", "D5")) # move king into rook check (false)
board.update_board("D8", "D4")  # block future rook check with our queen
print(move_checker(board, "E5", "D5")) # move king into now blocked no longer rook check (true)

# test set #4 moving king into diagonal checks and blocked diagonal checks

board.update_board("E8", "E5")  # move king into the middle
board.update_board("F1", "B3")  # move bishop near king
print(move_checker(board, "E5", "D5")) # move king into bishop check (false)
board.update_board("D8", "C4")  # block future bishop check with our queen
print(move_checker(board, "E5", "D5")) # move king into now blocked no longer rook check (true)

# test set #5 moving king into pawn checks

board.update_board("E8", "E5")  # move king into the middle
board.update_board("F2", "C4")  # move pawn near king
print(move_checker(board, "E5", "D5")) # move king into pawn check (false)

#Testing AI Move Generator Function - black pieces
black_pieces_array = [Knight(True,'f2',point), Pawn(True,'f2',point), Pawn(True,'d7',point)]
print(ai_move_generator(board, black_pieces_array))

#Testing AI Move Generator Function - white pieces
white_pieces_array = [Knight(False,'f2',point), Pawn(False,'d2',point), Pawn(False,'b7',point)]
print(ai_move_generator(board, white_pieces_array))
'''

# In this prototype chess game, the game ends when black or white lose all of their
# pieces.
