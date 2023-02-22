from Points import *
from Pieces import *
import random
from chessBoard import *
from moveChecker import *

'''
This function takes in the current state of the board (current_board) and an 
array of piece objects which relate to the colour whose go it is (pieces_array).
It is used to generate random moves for the AI player anf returns in the forms:
1) Non-capture -> nf2h3 (knight at starting postion f2 moves to h3) 
2) Capture -> nf2xh3 (knight at starting position f2 moves to and takes at h3)
 ->
'''

def ai_move_generator(current_board, pieces_array):
    not_valid_move = True
    # Continue looping until find a valid move
    while not_valid_move:
        rand_index = random.randint(0, len(pieces_array)-1)
        piece = pieces_array[rand_index]

        rand_row = random.randint(0, 8)
        rand_col = random.randint(0, 8)
        dest_location = get_chess_notation((rand_row, rand_col))
        if move_checker(current_board, piece, dest_location):
            not_valid_move = False
    
    # Use to see if a piece is located at the destination location of the piece
    # If there is a piece it will always be a piece of the other colour, 
    # therefore a capture will take placein this situataion
    dest_Y = int(dest_location[1])-1
    dest_X = ord(dest_location[0])-97
    dest_pos = current_board.board[dest_Y][dest_X]

    # check colour of piece 
    if piece.is_black:
        # check if the move captured a piece
        if dest_pos != ' ':
            if(isinstance(piece, Pawn)):
                return piece.pos + 'x' + dest_location
            elif(isinstance(piece, Rook)):
                return 'r' + piece.pos + 'x' + dest_location
            elif(isinstance(piece, Knight)):
                return 'n' + piece.pos + 'x' + dest_location
            elif(isinstance(piece, Bishop)):
                return 'b' + piece.pos + 'x' + dest_location
            elif(isinstance(piece, Queen)):
                return 'q' + piece.pos + 'x' + dest_location
            elif(isinstance(piece, King)):
                return 'k' + piece.pos + 'x' + dest_location    
        else:
            if(isinstance(piece, Pawn)):
                return piece.pos + dest_location
            elif(isinstance(piece, Rook)):
                return 'r' + piece.pos + dest_location
            elif(isinstance(piece, Knight)):
                return 'n' + piece.pos + dest_location
            elif(isinstance(piece, Bishop)):
                return 'b' + piece.pos + dest_location
            elif(isinstance(piece, Queen)):
                return 'q' + piece.pos + dest_location
            elif(isinstance(piece, King)):
                return 'k' + piece.pos + dest_location
    else:
        if dest_pos != ' ':
            if(isinstance(piece, Pawn)):
                return piece.pos + 'x' + dest_location
            elif(isinstance(piece, Rook)):
                return 'R' + piece.pos + 'x' + dest_location
            elif(isinstance(piece, Knight)):
                return 'N' + piece.pos + 'x' + dest_location
            elif(isinstance(piece, Bishop)):
                return 'B' + piece.pos + 'x' + dest_location
            elif(isinstance(piece, Queen)):
                return 'Q' + piece.pos + 'x' + dest_location
            elif(isinstance(piece, King)):
                return 'K' + piece.pos + 'x' + dest_location    
        else:
            if(isinstance(piece, Pawn)):
                return piece.pos + dest_location
            elif(isinstance(piece, Rook)):
                return 'R' + piece.pos + dest_location
            elif(isinstance(piece, Knight)):
                return 'N' + piece.pos + dest_location
            elif(isinstance(piece, Bishop)):
                return 'B' + piece.pos + dest_location
            elif(isinstance(piece, Queen)):
                return 'Q' + piece.pos + dest_location
            elif(isinstance(piece, King)):
                return 'K' + piece.pos + dest_location

# take in array notation and return chess notation co-ordinates ( e.g. input : (2, 2) - output : d4
def get_chess_notation(coords):
    columns = "abcdefgh"
    row = str(coords[1])
    column = columns[coords[0] - 1]
    return column + row

    
    
    
