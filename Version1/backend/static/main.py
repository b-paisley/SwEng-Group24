from chessBoard import *
from Points import *
from Pieces import *
from moveChecker import *
from aiMoveGenerator import *
from PiecesPosDict import *
from Game import *
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import json

app = Flask(__name__)
api = Api(app)
CORS(app)

# board = ChessBoard()
# board.draw()
game = Game()

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/', methods=['GET'])
def giveFEN():
    fenVal = game.getBoard().giveFEN()
    return {'data':fenVal}

@app.route('/move/<move>', methods=['GET'])
def makeMove(move):
    game.playMove(move)
    move = ''
    fenVal = game.getBoard().giveFEN()
    return {'data':fenVal}

if __name__ == '__main__':
    app.run()  # run our Flask app

# Quick Example Game - Player V Person
'''
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

#Testing AI Move Generator Function - black pieces
black_pieces_array = [Knight(True,'f2',point), Pawn(True,'f2',point), Pawn(True,'d7',point)]
print(ai_move_generator(board, black_pieces_array))

#Testing AI Move Generator Function - white pieces
white_pieces_array = [Knight(False,'f2',point), Pawn(False,'d2',point), Pawn(False,'b7',point)]
print(ai_move_generator(board, white_pieces_array))
'''

# In this prototype chess game, the game ends when black or white lose all of their
# pieces.
