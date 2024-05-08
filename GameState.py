import copy

from Board import Board


class GameState:
    board: Board
    f: int
    g: int
    h: int

    def __init__(self, filename=None):
        # GameState has board, (board is blocks that move around)
        self.board = Board(0, 0, {})
        self.f = 0
        self.g = 0
        self.h = 0
        # load that board
        if filename:
            self.board.loadBoardFromFile(filename)
            self.board.normalize()

    # moves block, given id and direction
    def applyMove(self, blockID, direction):
        block = self.board.getBlock(blockID)
        if block:
            block.move(direction, self.board)

    def printGame(self):
        self.board.printBoard()

    def cloneState(self):
        newGame = GameState()
        newGame.board = copy.deepcopy(self.board)
        newGame.g = self.g
        newGame.h = self.h
        newGame.f = self.f
        return newGame

    def identifySolutions(self):
        return self.board.identifySolutions()

    def availableMoves(self):
        return self.board.availableMoves()

    def getBlock(self, blockID):
        return self.board.getBlock(blockID)

    def dictionaryToTuple(self, d):
        return tuple(sorted((blockID, block.getState()) for blockID, block in d.items()))
