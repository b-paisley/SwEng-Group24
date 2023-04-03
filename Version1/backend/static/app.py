from flask import Flask, request
from chessBoard import *
from PiecesPosDict import *
from Game import *
from flask_restful import Resource, Api
from flask_cors import CORS
from MoveSearch import playPrune
# from main import game

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r'/api/*': {'origins': 'http://localhost:4200'}})

game = Game()
app = Flask(__name__)
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/fen')
def getFen():
    fenVal = ChessBoard.GiveFEN(game.GetBoard())
    return {
        "data": {
            "fen": fenVal,
        }
    }


@app.route('/')
def runGame():
    # game.play()
    fenVal = ChessBoard.GiveFEN(game.GetBoard())
    return {
        "data": {
            "fen": fenVal,
        }
    }

@app.route('/api/move/<move>')
def movePiece(move):
    move = game.PlayMove(move)
    if move == "error":
        return {
            "data": {
                "fen": "error",
                "gameOver": False
            }
        }
    fenVal = ChessBoard.GiveFEN(game.GetBoard())
    if game.black:
        playerColour='black'
    else:
        playerColour='white'
    if CheckmateChecker(game.board, playerColour):
        game.gameOver = True
        return {
            "data": {
                "fen": fenVal,
                "gameOver": True
            }
        }
    return {
        "data": {
            "fen": fenVal,
            "gameOver": False
        }
    }

@app.route('/api/reset')
def reset():
    game.Restart()
    fenVal = ChessBoard.GiveFEN(game.GetBoard())
    return {
        "data": {
            "fen":fenVal,
        }
    }

@app.route('/api/setBoard1')
def MakeBoard1(): 
    game.Restart()
    game.black = False
    board = game.GetBoard()
    for i in range(8):
        for j in range(8):
            board.board[i][j].ResetSquare()
    for i in range(10):
        pieceToDraw = list(piecesPosDict1.keys())[i]
        squareToFill = piecesPosDict1[pieceToDraw]
        board.OriginalDraw(pieceToDraw, squareToFill)

@app.route('/api/mitch')
def callMitch():
    move = playPrune(game)
    game.PlayMove(move)
    fenVal = ChessBoard.GiveFEN(game.GetBoard())
    return {
        "data": {
            "fen":fenVal,
        }
    }
