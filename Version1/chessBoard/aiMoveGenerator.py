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

#def ai_move_generator(current_board, pieces_array):
def ai_move_generator(current_board, player_color):
    not_valid_move = True
    pieces_array = get_piece_array(current_board, player_color)
    # Continue looping until find a valid move
    while not_valid_move:
        rand_index = random.randint(0, len(pieces_array)-1)
        piece = pieces_array[rand_index]
        piece_name = current_board.board[piece[0]][piece[1]].placed_in_square
        piece_location = get_chess_notation((piece[0], piece[1]))
        
        # Check for valid pawn moves
        if (isinstance(piece_name, Pawn)):
            coords = get_coords(current_board, piece_location)
            pawn_moves = []
            if piece_name.is_black == True:
                if piece_name.has_moved == False:
                    move = get_chess_notation((coords[0][0]-2, coords[0][1]))
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
                move = get_chess_notation((coords[0][0]+1, coords[0][1]))
                pawn_moves.append(move)
                move = get_chess_notation((coords[0][0]+1, coords[0][1]-1))
                pawn_moves.append(move)
                move = get_chess_notation((coords[0][0]+1, coords[0][1]+1))
                pawn_moves.append(move)
                rand_index = random.randint(0, len(pawn_moves)-1)
                dest_location = pawn_moves[rand_index]
        else:
            rand_row = random.randint(0, 8)
            rand_col = random.randint(0, 8)
            dest_location = get_chess_notation((rand_row, rand_col))

        if move_checker(current_board, piece_location, dest_location):
            not_valid_move = False
    
    # Use to see if a piece is located at the destination location of the piece
    # If there is a piece it will always be a piece of the other colour, 
    # therefore a capture will take place in this situataion
    dest_coords = get_coords(current_board, dest_location)
    dest_pos = current_board.board[dest_coords[0][0]][dest_coords[0][1]]
    
    # Update the current board
    current_board.update_board(piece_location, dest_location)

    # check colour of piece 
    if piece_name.is_black:
        # check if the move captured a piece
        if dest_pos.placed_in_square != None:
            if(isinstance(piece_name, Pawn)):
                return piece_location + 'x' + dest_location
            elif(isinstance(piece_name, Rook)):
                return 'r' + piece_location + 'x' + dest_location
            elif(isinstance(piece_name, Knight)):
                return 'n' + piece_location + 'x' + dest_location
            elif(isinstance(piece_name, Bishop)):
                return 'b' + piece_location + 'x' + dest_location
            elif(isinstance(piece_name, Queen)):
                return 'q' + piece_location + 'x' + dest_location
            elif(isinstance(piece_name, King)):
                return 'k' + piece_location + 'x' + dest_location    
        else:
            if(isinstance(piece_name, Pawn)):
                return piece_location + dest_location
            elif(isinstance(piece_name, Rook)):
                return 'r' + piece_location + dest_location
            elif(isinstance(piece_name, Knight)):
                return 'n' + piece_location + dest_location
            elif(isinstance(piece_name, Bishop)):
                return 'b' + piece_location + dest_location
            elif(isinstance(piece_name, Queen)):
                return 'q' + piece_location + dest_location
            elif(isinstance(piece_name, King)):
                return 'k' + piece_location + dest_location
    else:
        if dest_pos.placed_in_square != None:
            if(isinstance(piece_name, Pawn)):
                return piece_location + 'x' + dest_location
            elif(isinstance(piece_name, Rook)):
                return 'R' + piece_location + 'x' + dest_location
            elif(isinstance(piece_name, Knight)):
                return 'N' + piece_location + 'x' + dest_location
            elif(isinstance(piece_name, Bishop)):
                return 'B' + piece_location + 'x' + dest_location
            elif(isinstance(piece_name, Queen)):
                return 'Q' + piece_location + 'x' + dest_location
            elif(isinstance(piece_name, King)):
                return 'K' + piece_location + 'x' + dest_location    
        else:
            if(isinstance(piece_name, Pawn)):
                return piece_location + dest_location
            elif(isinstance(piece_name, Rook)):
                return 'R' + piece_location + dest_location
            elif(isinstance(piece_name, Knight)):
                return 'N' + piece_location + dest_location
            elif(isinstance(piece_name, Bishop)):
                return 'B' + piece_location + dest_location
            elif(isinstance(piece_name, Queen)):
                return 'Q' + piece_location + dest_location
            elif(isinstance(piece_name, King)):
                return 'K' + piece_location + dest_location

# take in array notation and return chess notation co-ordinates ( e.g. input : (2, 2) - output : d4
def get_chess_notation(coords):
    row = int(coords[0]) + 1
    column = chr(coords[1]+65)
    return column + str(row)
    
def get_coords(current_board, notation):
    coords = []
    dest_Y = int(notation[1])-1
    dest_X = ord(notation[0])-65
    coords.append([dest_Y, dest_X])
    return coords

def get_piece_array(chess_board, player_color):
    piece_array = []
    index = 0
    pair = [4,7]
    if player_color == True:
        black = True
    else:
        black = False
    for i in range(8):
        for j in range(8):
            piece = chess_board.board[i][j].placed_in_square
            if piece != None:
                # Black Piece Array
                if piece.is_black == True and black == True:
                    # piece_array.append(chess_board.board[i][j].get_piece)
                    piece_array.append([i,j])

                # White Piece Array
                elif piece.is_black == False and black == False:
                   # piece_array.append(piece)
                   piece_array.append([i,j])

    return piece_array
    


    
    
    
