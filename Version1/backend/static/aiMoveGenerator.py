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

#def AiMoveGenerator(currentBoard, piecesArray):
def AiMoveGenerator(currentBoard, playerColour):
    notValidMove = True
    piecesArray = GetPieceArray(currentBoard, playerColour)
    # Continue looping until find a valid move
    while notValidMove:
        randIndex = random.randint(0, len(piecesArray)-1)
        piece = piecesArray[randIndex]
        pieceName = currentBoard.board[piece[0]][piece[1]].placedInSquare
        pieceLocation = GetChessNotation((piece[0], piece[1]))
        
        # Check for valid pawn moves
        if (isinstance(pieceName, Pawn)):
            coords = GetCoords(currentBoard, pieceLocation)
            pawnMoves = []
            if pieceName.isBlack == True:
                if pieceName.hasMoved == False:
                    move = GetChessNotation((coords[0][0]-2, coords[0][1]))
                move = GetChessNotation((coords[0][0]-1, coords[0][1]))
                pawnMoves.append(move)
                move = GetChessNotation((coords[0][0]-1, coords[0][1]-1))
                pawnMoves.append(move)
                move = GetChessNotation((coords[0][0]-1, coords[0][1]+1))
                pawnMoves.append(move)
                randIndex = random.randint(0, len(pawnMoves)-1)
                destLocation = pawnMoves[randIndex]
            else:
                if pieceName.hasMoved == True:
                    move = GetChessNotation((coords[0][0]+2, coords[0][1]))
                move = GetChessNotation((coords[0][0]+1, coords[0][1]))
                pawnMoves.append(move)
                move = GetChessNotation((coords[0][0]+1, coords[0][1]-1))
                pawnMoves.append(move)
                move = GetChessNotation((coords[0][0]+1, coords[0][1]+1))
                pawnMoves.append(move)
                randIndex = random.randint(0, len(pawnMoves)-1)
                destLocation = pawnMoves[randIndex]
        else:
            randRow = random.randint(0, 8)
            randCol = random.randint(0, 8)
            destLocation = GetChessNotation((randRow, randCol))

        if MoveChecker(currentBoard, pieceLocation, destLocation, 0):
            notValidMove = False
    
    # Use to see if a piece is located at the destination location of the piece
    # If there is a piece it will always be a piece of the other colour, 
    # therefore a capture will take place in this situataion
    destCoords = GetCoords(currentBoard, destLocation)
    destPos = currentBoard.board[destCoords[0][0]][destCoords[0][1]]
    
    # check colour of piece 
    if pieceName.isBlack:
        # check if the move captured a piece
        ''' 
        if dest_pos.placed_in_square != None:
            if(isinstance(piece_name, Pawn)):
                notation = piece_location + 'x' + dest_location
            elif(isinstance(piece_name, Rook)):
                notation = 'r' + piece_location + 'x' + dest_location
            elif(isinstance(piece_name, Knight)):
                notation = 'n' + piece_location + 'x' + dest_location
            elif(isinstance(piece_name, Bishop)):
                notation = 'b' + piece_location + 'x' + dest_location
            elif(isinstance(piece_name, Queen)):
                notation = 'q' + piece_location + 'x' + dest_location
            elif(isinstance(piece_name, King)):
                notation = 'k' + piece_location + 'x' + dest_location    
        else:
        '''
        if(isinstance(pieceName, Pawn)):
            notation = pieceLocation + '_' + destLocation
        elif(isinstance(pieceName, Rook)):
            notation = 'r' + pieceLocation +  '_' + destLocation
        elif(isinstance(pieceName, Knight)):
            notation = 'n' + pieceLocation + '_' + destLocation
        elif(isinstance(pieceName, Bishop)):
            notation = 'b' + pieceLocation + '_' + destLocation
        elif(isinstance(pieceName, Queen)):
            notation = 'q' + pieceLocation + '_' + destLocation
        elif(isinstance(pieceName, King)):
            notation = 'k' + pieceLocation + '_' + destLocation
    else:
        # if dest_pos.placed_in_square != None:
        if(isinstance(pieceName, Pawn)):
            notation = pieceLocation + '_' + destLocation
        elif(isinstance(pieceName, Rook)):
            notation = 'R' + pieceLocation + '_' + destLocation
        elif(isinstance(pieceName, Knight)):
            notation = 'N' + pieceLocation + '_' + destLocation
        elif(isinstance(pieceName, Bishop)):
            notation = 'B' + pieceLocation + '_' + destLocation
        elif(isinstance(pieceName, Queen)):
            notation = 'Q' + pieceLocation + '_' + destLocation
        elif(isinstance(pieceName, King)):
            notation = 'K' + pieceLocation + '_' + destLocation    
        '''
        else:
            if(isinstance(piece_name, Pawn)):
                notation = piece_location + dest_location
            elif(isinstance(piece_name, Rook)):
                notation = 'R' + piece_location + dest_location
            elif(isinstance(piece_name, Knight)):
                notation = 'N' + piece_location + dest_location
            elif(isinstance(piece_name, Bishop)):
                notation = 'B' + piece_location + dest_location
            elif(isinstance(piece_name, Queen)):
                notation = 'Q' + piece_location + dest_location
            elif(isinstance(piece_name, King)):
                notation = 'K' + piece_location + dest_location
        '''
    
     # Update the current board
    currentBoard.UpdateBoard(pieceLocation, destLocation)
    return notation
    

# take in array notation and return chess notation co-ordinates ( e.g. input : (2, 2) - output : d4
def GetChessNotation(coords):
    row = int(coords[0]) + 1
    column = chr(coords[1]+65)
    return column + str(row)

# Takes in chess notation and retruns coords  
def GetCoords(currentBoard, notation):
    coords = []
    destY = int(notation[1])-1
    destX = ord(notation[0])-65
    coords.append([destY, destX])
    return coords

# This gets all the pieces of the colour of the ai player
def GetPieceArray(chessBoard, playerColour):
    pieceArray = []
    if playerColour.lower() == 'black':
        isBlack = True
    else:
        isBlack = False
    for i in range(8):
        for j in range(8):
            piece = chessBoard.board[i][j].placedInSquare
            if piece != None:
                # Black Piece Array
                if piece.isBlack == True and isBlack == True:
                    pieceArray.append([i,j])

                # White Piece Array
                elif piece.isBlack == False and isBlack == False:
                   pieceArray.append([i,j])

    return pieceArray
    


    
    
    
