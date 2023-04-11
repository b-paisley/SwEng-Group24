# install chess
import os
import chess.pgn
import numpy as np

def GetDataset(N = None):
    X, Y = [], []
    gameN = 0
    vals = {'1/2-1/2':0,'0-1':-1,'1-0':1}
    for file in os.listdir("data"):
        pgn = open(os.path.join("data", file))
        while True:
            game = chess.pgn.read_game(pgn)
            if game is None:
                break
            result = game.headers['Result']
            if result not in vals:
                continue
            value = vals[result]
            board = game.board()
            for i, move in enumerate(game.mainline_moves()):
                board.push(move)
                ser = State(board).serialize()
                X.append(ser)
                Y.append(value)
            print("Game Num: %d, got %d examples" % (gameN, len(X)))
            if N is not None and len(X) > N:
                return X, Y
            gameN += 1
    return np.array(X), np.array(Y)

class State(object):
    def __init__(self, board=None):
        if board is None:
            self.board = chess.Board()
        else:
            self.board = board

    def key(self):
        return (self.board.board_fen(), self.board.turn, self.board.castling_rights, self.board.ep_square)

    def serialize(self):
        import numpy as np
        assert self.board.is_valid()

        bstate = np.zeros(64, np.uint8)
        for i in range(64):
            pp = self.board.piece_at(i)
            if pp is not None:
                bstate[i] = {"P": 1, "N": 2, "B": 3, "R": 4, "Q": 5, "K": 6, \
                                "p": 9, "n":10, "b":11, "r":12, "q":13, "k": 14}[pp.symbol()]
        if self.board.has_queenside_castling_rights(chess.WHITE):
            assert bstate[0] == 4
            bstate[0] = 7
        if self.board.has_kingside_castling_rights(chess.WHITE):
            assert bstate[7] == 4
            bstate[7] = 7
        if self.board.has_queenside_castling_rights(chess.BLACK):
            assert bstate[56] == 8+4
            bstate[56] = 8+7
        if self.board.has_kingside_castling_rights(chess.BLACK):
            assert bstate[63] == 8+4
            bstate[63] = 8+7

        if self.board.ep_square is not None:
            assert bstate[self.board.ep_square] == 0
            bstate[self.board.ep_square] = 8
        bstate = bstate.reshape(8,8)

        state = np.zeros((5,8,8), np.uint8)

        state[0] = (bstate>>3)&1
        state[1] = (bstate>>2)&1
        state[2] = (bstate>>1)&1
        state[3] = (bstate>>0)&1

        state[4] = (self.board.turn*1.0)

        return state

    def edges(self):
        return list(self.board.legal_moves)

if __name__ == "__main__":
    X, Y = GetDataset(2000000)
    np.savez("processed/dataset_9M", X, Y)