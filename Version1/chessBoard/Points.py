from Pieces import *

white_points = 0
black_points = 0

def update_points(board):
    for row in board:
        for square in row:
            piece = square.placed_in_square
            if piece.is_black:
                black_points += piece.value
            else:
                white_points += piece.value