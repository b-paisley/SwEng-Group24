from Points import *
from Pieces import *
import random
from chessBoard import *
from moveChecker import *
from square import *

'''
This function takes in the current state of the board (current_board) and an 
array of piece objects which relate to the colour whose go it is (pieces_array).
It is used to generate random moves for the AI player anf returns in the forms:
1) Non-capture -> nf2h3 (knight at starting postion f2 moves to h3) 
2) Capture -> nf2xh3 (knight at starting position f2 moves to and takes at h3)
 ->
'''

def ai_move_generator(current_board, player_colour):
    not_valid_move = True
    pieces_array = get_piece_array(current_board, player_colour)
    # Continue looping until find a valid move
    while not_valid_move:
        rand_index = random.randint(0, len(pieces_array)-1)
        piece = pieces_array[rand_index]
        piece_name = current_board.board[piece[0]][piece[1]].placed_in_square
        piece_location = get_chess_notation((piece[0], piece[1]))
        
        # Check for valid pawn moves
        if (isinstance(piece_name, Pawn)):
            dest_location = valid_pawn_move(piece_name, current_board, piece_location)
        else:
            rand_row = random.randint(0, 8)
            rand_col = random.randint(0, 8)
            dest_location = get_chess_notation((rand_row, rand_col))

        if move_checker(current_board, piece_location, dest_location):
            not_valid_move = False
    
    # Use to see if a piece is located at the destination location of the piece
    # If there is a piece it will always be a piece of the other colour, 
    # therefore a capture will take place in this situataion
    dest_coords = get_coords(dest_location)
    dest_pos = current_board.board[dest_coords[0][0]][dest_coords[0][1]]
    
    # check colour of piece 
    if piece_name.is_black:
        if(isinstance(piece_name, Pawn)):
            notation = piece_location + '_' + dest_location
        elif(isinstance(piece_name, Rook)):
            notation = 'r' + piece_location +  '_' + dest_location
        elif(isinstance(piece_name, Knight)):
            notation = 'n' + piece_location + '_' + dest_location
        elif(isinstance(piece_name, Bishop)):
            notation = 'b' + piece_location + '_' + dest_location
        elif(isinstance(piece_name, Queen)):
            notation = 'q' + piece_location + '_' + dest_location
        elif(isinstance(piece_name, King)):
            notation = 'k' + piece_location + '_' + dest_location
    else:
        if(isinstance(piece_name, Pawn)):
            notation = piece_location + '_' + dest_location
        elif(isinstance(piece_name, Rook)):
            notation = 'R' + piece_location + '_' + dest_location
        elif(isinstance(piece_name, Knight)):
            notation = 'N' + piece_location + '_' + dest_location
        elif(isinstance(piece_name, Bishop)):
            notation = 'B' + piece_location + '_' + dest_location
        elif(isinstance(piece_name, Queen)):
            notation = 'Q' + piece_location + '_' + dest_location
        elif(isinstance(piece_name, King)):
            notation = 'K' + piece_location + '_' + dest_location    
    
     # Update the current board
    current_board.update_board(piece_location, dest_location)
    return notation
    

# take in array notation and return chess notation co-ordinates ( e.g. input : (2, 2) - output : C4
def get_chess_notation(coords):
    row = int(coords[0]) + 1
    column = chr(coords[1]+65)
    return column + str(row)

# Takes in chess notation and retruns coords  
def get_coords(notation):
    coords = []
    dest_Y = int(notation[1])-1
    dest_X = ord(notation[0])-65
    coords.append((dest_Y, dest_X))
    return coords

# This gets all the pieces of the colour of the ai player
def get_piece_array(chess_board, player_colour):
    piece_array = []
    if player_colour.lower() == 'black':
        is_black = True
    else:
        is_black = False
    for i in range(8):
        for j in range(8):
            piece = chess_board.board[i][j].placed_in_square
            if piece != None:
                # Black Piece Array
                if piece.is_black == True and is_black == True:
                    piece_array.append([i,j])

                # White Piece Array
                elif piece.is_black == False and is_black == False:
                   piece_array.append([i,j])

    return piece_array
    
def valid_pawn_move(piece_name, current_board, piece_location):
     # Check for valid pawn moves
    coords = get_coords(piece_location)
    pawn_moves = []
    if not piece_name.has_moved:
        if piece_name.is_black == True:
            if piece_name.has_moved == False:
                move = get_chess_notation((coords[0][0]-2, coords[0][1]))
                pawn_moves.append(move)
            move = get_chess_notation((coords[0][0]-1, coords[0][1]))
            pawn_moves.append(move)
            rand_index = random.randint(0, len(pawn_moves)-1)
            dest_location = pawn_moves[rand_index]
        else:
            if piece_name.has_moved == True:
                move = get_chess_notation((coords[0][0]+2, coords[0][1]))
                pawn_moves.append(move)
            move = get_chess_notation((coords[0][0]+1, coords[0][1]))
            pawn_moves.append(move)
            rand_index = random.randint(0, len(pawn_moves)-1)
            dest_location = pawn_moves[rand_index]
    else:
        if piece_name.is_black == True:
            if piece_name.has_moved == False:
                move = get_chess_notation((coords[0][0]-2, coords[0][1]))
                pawn_moves.append(move)
            move = get_chess_notation((coords[0][0]-1, coords[0][1]))
            pawn_moves.append(move)
            move = get_chess_notation((coords[0][0]-1, coords[0][1]-1))
            pawn_moves.append(move)
            move = get_chess_notation((coords[0][0]-1, coords[0][1]+1))
            pawn_moves.append(move)
            rand_index = random.randint(0, len(pawn_moves)-1)
            dest_location = pawn_moves[rand_index]
        else:
            if piece_name.has_moved == True:
                move = get_chess_notation((coords[0][0]+2, coords[0][1]))
                pawn_moves.append(move)
            move = get_chess_notation((coords[0][0]+1, coords[0][1]))
            pawn_moves.append(move)
            move = get_chess_notation((coords[0][0]+1, coords[0][1]-1))
            pawn_moves.append(move)
            move = get_chess_notation((coords[0][0]+1, coords[0][1]+1))
            pawn_moves.append(move)
            rand_index = random.randint(0, len(pawn_moves)-1)
            dest_location = pawn_moves[rand_index]
    return dest_location

    
    
    
