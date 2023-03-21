from chessBoard import *
from PiecesPosDict import *

from app import app # Flask instance of the API

def test_index_route():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == '{"data":{"fen":"RNBQKBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbqkbnr"}}\n'

