class ReadPGNMoves():

    def __init__(self, whitePieces, blackPieces):
        self.whitePieces = whitePieces
        self.blackPieces = blackPieces

class PGNArray():
    '''
       This class returns an array of games and the white and black 
       moves associated with each game
    '''

    def PGNMoves():
        whitePieces = []
        blackPieces = []
        
        with open("Version1\\backend\\static\\Adams.pgn", "r") as image2string:
            convertedString = image2string.read()
        print(convertedString)
        gamesArray = []
        j = 0
        splits = convertedString.split() 
        while(j != (len(splits)-1)):
            prevWord = ''
            result = ''
            game = ReadPGNMoves(whitePieces, blackPieces)
            while(j != len(splits)):
                split = splits[j]
                if(prevWord == 'Result'):
                    split = split.replace("\"", "")
                    split = split.replace("]", "")
                    result = split
                    prevWord = ''
                    break
                if(split.__contains__('Result')):
                    prevWord = 'Result'
                j += 1
            split = ''
            whiteMove = 1
            numberCounter = 1
            oppMove = 1
            j += 1

            while(j != len(splits)):
                split = splits[j]
                if result == split:
                    break
                elif(split.__contains__(str(numberCounter) + ".") or oppMove == 0):
                        if whiteMove == 1:
                            split = split.replace(str(numberCounter), "")
                            split = split.replace(".", "")
                            game.whitePieces.append(split)
                            whiteMove = 0
                            numberCounter += 1
                            oppMove = 0
                        elif whiteMove == 0:
                            game.blackPieces.append(split)
                            whiteMove = 1
                            oppMove = 1
                j += 1

            gamesArray.append(game)
        return gamesArray
