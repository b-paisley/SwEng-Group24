from Pieces import *

WHITE_POINTS = 0
BLACK_POINTS = 0

def UpdatePoints(board):
    for row in board:
        for square in row:
            piece = square.placedInSquare
            if piece.isBlack:
                BLACK_POINTS += piece.value
            else:
                WHITE_POINTS += piece.value
