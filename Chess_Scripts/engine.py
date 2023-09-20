"""
Stores information about current state of chess game. Determines valid moves at current state.
Stores a move log.
"""

class GameState():
    def __init__(self):
        # Board is an 8x8 2D list, each element of the list has 2 characters.
        # The first character represents the color of the piece.
        # The second character represents the type of the piece.
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        
        self.whiteToMove = True
        self.moveLog = []

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move) # log the move so we can undo it later
        self.whiteToMove = not self.whiteToMove # swap players


class Move():

    # maps keys to values
    # key : value
    ranksToRows = {"1":7, "2":6, "3":5, "4":4, 
                   "5":3, "6":2, "7":1, "8":0}
    rowsToRanks = dict([(value, key) for key, value in ranksToRows.items()]) # reverses the dictionary
    filesToCols = {"a":0, "b":1, "c":2, "d":3, 
                   "e":4,"f":5, "g":6, "h":7}
    colToFiles = dict([(value, key) for key, value in filesToCols.items()])

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        pass

    def getChessNotation(self):
        # print(self.startRow)
        # print(self.startCol)
        # print(self.ranksToRows)
        # print(self.rowsToRanks)
        # #print(self.rowsToRanks[self.startRow])
        # #print(self.filesToCols[self.startCol])
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colToFiles[c] + self.rowsToRanks[r]

