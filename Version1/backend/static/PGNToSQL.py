import ReadPGNMoves
import mysql.connector


def PGNToSQL():
    db_passwd="Chess=iS@cooL174" # TODO: Make db_passwd environment variable

    # Database variable
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=db_passwd,
        database="pgn_database"
    )

    cursor = db.cursor()

    PGNData = ReadPGNMoves.PGNArray.PGNMoves() # List of PGN games

    for i in range(len(PGNData)):
        # Create a table for each PGN game in the list
        cursor.execute(
        f"""CREATE TABLE Game{i}
        (Move int PRIMARY KEY AUTO_INCREMENT,
        WhiteMoves varchar(10),
        BlackMoves varchar(10))
        """)

        # Insert the white and black moves into the table
        PGNGame = PGNData[i]
        for j in PGNGame.whitePieces:
            if j == len(PGNGame.BlackPieces):
                cursor.execute(
                f"""INSERT INTO Game{i}
                (WhiteMove. BlackMove)
                VALUES (%s,%s)
                """, (PGNGame.WhitePieces[j], None))
            else:
                cursor.execute(
                    f"""INSERT INTO Game{i}
                    (WhiteMove. BlackMove)
                    VALUES (%s,%s)
                    """, (PGNGame.WhitePieces[j], PGNGame.BlackPieces[j]))
                
    db.commit()