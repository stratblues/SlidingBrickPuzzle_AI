from Board import Board


class GameState:
    def __init__(self, filename):
        # GameState has board, (board is blocks that move around)
        self.board = Board(0, 0, {})
        # load that board
        self.board.loadBoardFromFile(filename)

    # moves block, given id and direction
    def applyMove(self, blockID, direction):
        block = self.board.getBlock(blockID)
        if block:
            block.move(direction, self.board)

    def printGame(self):
        self.board.printBoard()

    def cloneState(self):
        newGame = GameState(None)
        newGame.board = self.board.cloneState()
        return newGame

    def identifySolutions(self):
        return self.board.identifySolutions()

    def availableMoves(self):
        return self.board.availableMoves()

    def getBlock(self, blockID):
        return self.board.getBlock(blockID)

