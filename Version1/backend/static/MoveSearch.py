import random
import chess
import chess.polyglot
import os
from copy import deepcopy
from NetComponents import NetVal
from GetTrainingData import State
from chessBoard import ChessBoard

Evaluator = NetVal()
'''
p = os.getcwd()
if os.path.isfile(os.path.join(p, '/openings/baron30.bin')):
    p = p + '/openings/baron30.bin'
elif os.path.isfile(p + '\\openings\\baron30.bin'): 
    p = '\\openings\\baron30.bin'
'''
q = 'openings/baron30.bin'
p = os.path.abspath(__file__).removesuffix(os.path.basename(__file__)) 
r = p + q
if not os.path.isfile(r):
    r = r.removeprefix(p)
reader = chess.polyglot.open_reader(r)
del p
scoring = {'p':-1,
           'r':-3,
           'b':-4,
           'n':-5,
           'q':-10,
           'k':0,
           'P':1,
           'R':3,
           'B':4,
           'N':5,
           'Q':10,
           'K':0}


def playPrune(GAME):
    b = GAME.GetBoard().ProperFen(True)
    BOARD = chess.Board(b)
    return MoveFromUCI(basePrune(BOARD, 4, True).uci())

def basePrune(BOARD, N, playerMax):
    maxN = N
    currentN = N
    opening = reader.get(BOARD)
    if opening == None:
        pass
    else:
        return opening.move

    moves = list(BOARD.legal_moves)
    random.shuffle(moves)

    bestVal = -9999
    bestMovefinal = None
    for move in moves:
        temp = deepcopy(BOARD)
        temp.push(move)
        val = max(bestVal, MinMaxAlphaBeta(temp, 
                            not playerMax,
                            maxN,
                            currentN - 1,
                            -10000,
                            10000))
        temp.pop()
        if (val > bestVal):
            bestVal = val
            bestMovefinal = chess.Move.from_uci(str(move))
    return bestMovefinal

def MinMaxAlphaBeta(board, playerMax, maxN, currentN, alpha, beta):
    if currentN == 0:
        return -NewEval(board)
    moves = list(board.legal_moves)
    random.shuffle(moves)
    if (playerMax):
        bestVal = -9999
        for move in moves:
            board.push(move)
            bestVal = max(bestVal, MinMaxAlphaBeta(board, not playerMax, maxN, currentN-1, alpha, beta))
            board.pop()
            alpha = max(alpha, bestVal)
            if beta <= alpha:
                return bestVal
        return bestVal
    else:
        bestVal = 9999
        for move in moves:
            board.push(move)
            bestVal = min(bestVal, MinMaxAlphaBeta(board, not playerMax, maxN, currentN-1, alpha, beta))
            board.pop()
            beta = min(bestVal, beta)
            if beta <= alpha:
                return bestVal
        return bestVal

def NewEval(BOARD):
    s = State(BOARD)
    return Evaluator(s)

def MoveFromUCI(moveIn):
    moveOut = moveIn[:2] + "_" + moveIn[2:]
    return moveOut
