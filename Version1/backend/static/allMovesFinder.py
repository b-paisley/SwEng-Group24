from moveChecker import *

def allMovesFinder(chess_board, square):
    taking = ""
    valid_moves = []
    file = ord(square[0])-65
    row = int(square[1])-1
    piece = chess_board.board[row][file].placed_in_square
    
    # Brute Force approach for Pawn
    if (isinstance(piece, Pawn)):
        row_shift = [2, 1, 1, 1]
        file_shift = [0, -1, 0, 1]
        if (not piece.is_black):
            for x in range (4):
                if (move_checker(chess_board, square, positionsToNotation(file+file_shift[x], row+row_shift[x]))):
                    if(checkIfTaking(chess_board, positionsToNotation(file+file_shift[x], row+row_shift[x]))): taking = "x"
                    else: taking = ""
                    valid_moves.append(taking + positionsToNotation(file+file_shift[x], row+row_shift[x]))
        else:
            for x in range (4):
                if (move_checker(chess_board, square, positionsToNotation(file+file_shift[x], row-row_shift[x]))):
                    if(checkIfTaking(chess_board, positionsToNotation(file+file_shift[x], row-row_shift[x]))): taking = "x"
                    else: taking = ""
                    valid_moves.append(taking + positionsToNotation(file+file_shift[x], row-row_shift[x]))
    
    # Brute force also applicable for Knight  
    if (isinstance(piece, Knight)):
        row_shift = [2, 2, 1, 1, -1, -1, -2, -2]
        file_shift = [-1, 1, -2, 2, -2, 2, -1, 1]
        for x in range(8):
            if (move_checker(chess_board, square, positionsToNotation(file+file_shift[x], row+row_shift[x]))):
                if(checkIfTaking(chess_board, positionsToNotation(file+file_shift[x], row+row_shift[x]))): taking = "x"
                else: taking = ""
                valid_moves.append(taking + positionsToNotation(file+file_shift[x], row+row_shift[x]))
        
    if (isinstance(piece, Rook)):
        valid_moves = appendValidStraights(chess_board, square, file, row, valid_moves)
    
    if (isinstance(piece, Bishop)):
        valid_moves = appendValidDiagonals(chess_board, square, file, row, valid_moves)
    
    if (isinstance(piece, Queen)):
        valid_moves = appendValidStraights(chess_board, square, file, row, valid_moves)
        valid_moves = appendValidDiagonals(chess_board, square, file, row, valid_moves)
    
    valid_moves.sort()
    return valid_moves
    
def appendValidStraights(chess_board, square, file, row, valid_moves):
    taking = ""
    checked_row = 7
    while (checked_row > row):
        if move_checker(chess_board, square, positionsToNotation(file, checked_row)):
            while (checked_row > row):
                if(checkIfTaking(chess_board, positionsToNotation(file, checked_row))): taking = "x"
                else: taking = ""
                valid_moves.append(taking + positionsToNotation(file, checked_row))
                checked_row -= 1
        checked_row -= 1
    checked_row = 0
    while (checked_row < row):
        if move_checker(chess_board, square, positionsToNotation(file, checked_row)):
            while (checked_row < row):
                if(checkIfTaking(chess_board, positionsToNotation(file, checked_row))): taking = "x"
                else: taking = ""
                valid_moves.append(taking + positionsToNotation(file, checked_row))
                checked_row += 1
        checked_row += 1
        
    checked_file = 7
    while (checked_file > file):
        if move_checker(chess_board, square, positionsToNotation(checked_file, row)):
            while (checked_file > file):
                if(checkIfTaking(chess_board, positionsToNotation(checked_file, row))): taking = "x"
                else: taking = ""
                valid_moves.append(taking + positionsToNotation(checked_file, row))
                checked_file -= 1
        checked_file -= 1
    checked_file = 0
    while (checked_file < file):
        if move_checker(chess_board, square, positionsToNotation(checked_file, row)):
            while (checked_file < file):
                if(checkIfTaking(chess_board, positionsToNotation(checked_file, row))): taking = "x"
                else: taking = ""
                valid_moves.append(taking + positionsToNotation(checked_file, row))
                checked_file += 1
        checked_file += 1
    return valid_moves

def appendValidDiagonals(chess_board, square, file, row, valid_moves):
    checked_file = file
    checked_row = row
    while (checked_file > 0 and checked_row < 7):
        checked_file -= 1
        checked_row += 1
    while (checked_file < file):
        if move_checker(chess_board, square, positionsToNotation(checked_file, checked_row)):
            while (checked_file < file):
                if(checkIfTaking(chess_board, positionsToNotation(checked_file, checked_row))): taking = "x"
                else: taking = ""
                valid_moves.append(taking + positionsToNotation(checked_file, checked_row))
                checked_file += 1
                checked_row -= 1
        checked_file += 1
        checked_row -= 1
        
    checked_file = file
    checked_row = row
    while (checked_file < 7 and checked_row < 7):
        checked_file += 1
        checked_row += 1
    while (checked_file > file):
        if move_checker(chess_board, square, positionsToNotation(checked_file, checked_row)):
            while (checked_file > file):
                if(checkIfTaking(chess_board, positionsToNotation(checked_file, checked_row))): taking = "x"
                else: taking = ""
                valid_moves.append(taking + positionsToNotation(checked_file, checked_row))
                checked_file -= 1
                checked_row -= 1
        checked_file -= 1
        checked_row -= 1
        
    while (checked_file > 0 and checked_row > 0):
        checked_file -= 1
        checked_row -= 1
    while (checked_file < file):
        if move_checker(chess_board, square, positionsToNotation(checked_file, checked_row)):
            while (checked_file < file):
                if(checkIfTaking(chess_board, positionsToNotation(checked_file, checked_row))): taking = "x"
                else: taking = ""
                valid_moves.append(taking + positionsToNotation(checked_file, checked_row))
                checked_file += 1
                checked_row += 1
        checked_file += 1
        checked_row += 1
        
    checked_file = file
    checked_row = row
    while (checked_file < 7 and checked_row > 0):
        checked_file += 1
        checked_row -= 1
    while (checked_file > file):
        if move_checker(chess_board, square, positionsToNotation(checked_file, checked_row)):
            while (checked_file > file):
                if(checkIfTaking(chess_board, positionsToNotation(checked_file, checked_row))): taking = "x"
                else: taking = ""
                valid_moves.append(taking + positionsToNotation(checked_file, checked_row))
                checked_file -= 1
                checked_row += 1
        checked_file -= 1
        checked_row += 1
    
    return valid_moves

def positionsToNotation(file, row):
        return chr(file+65) + str(row+1)
    
def checkIfTaking(chess_board, square):
    file = ord(square[0])-65
    row = int(square[1])-1
    if (chess_board.board[row][file].placed_in_square == None): return False
    else: return True