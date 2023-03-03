# from flask import Flask
# from flask_restful import Resource, Api
# from PiecesPosDict import *
# from flask_cors import CORS
# from chessBoard import ChessBoard
# import json

# app = Flask(__name__)
# api = Api(app)
# CORS(app)

# board = ChessBoard()

# @app.after_request
# def after_request(response):
#   response.headers.add('Access-Control-Allow-Origin', '*')
#   response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#   response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#   return response

# class PieceLocation(Resource):
#     def get(self):
#         mylist = []
#         for i in range(32):
#             piece_to_draw = list(pieces_pos_dict.keys())[i]
#             square_to_fill = pieces_pos_dict[piece_to_draw]
#             piece_str = str(list(pieces_pos_dict.keys())[i])
#             mylist.append({"piece": piece_str,
#                            "position": square_to_fill,
#                            "isBlack": str(piece_to_draw.is_black),
#                            "value": str(piece_to_draw.value)}
#                           )
#         mylist = json.loads(json.dumps(mylist))

#         return {'data': mylist}, 200  # return data and 200 OK

# class FenString(Resource):
#     def get(self):
#         fenVal = ChessBoard.giveFEN(board)
#         return {'data':fenVal}, 200

# api.add_resource(PieceLocation, '/pieces')  # add endpoints
# api.add_resource(ChessBoard, '/fen')  # add endpoints


# if __name__ == '__main__':
#     app.run()  # run our Flask app
from flask import Flask, request
from chessBoard import *
from PiecesPosDict import *
from Game import *
from main import game


app = Flask(__name__)
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/fen')
def getFen():
    fenVal = ChessBoard.giveFEN(game.getBoard())
    return {'data':fenVal}, 200


@app.route('/')
def runGame():
    # game.play()
    fenVal = ChessBoard.giveFEN(game.getBoard())
    return {'data':fenVal}, 200

@app.route('/move/<move>')
def movePiece(move):
    game.playMove(move)
    fenVal = ChessBoard.giveFEN(game.getBoard())
    return {'data': fenVal}, 200