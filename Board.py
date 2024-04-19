import copy

from Block import Block


class Board:
    def __init__(self, col, row, blocks):
        self.col = col
        self.row = row
        self.blocks = blocks  # dict blockID to Block obj
        self.goalPosition = None  # tuple(x,y)
        self.grid = [[0 for _ in range(col)] for _ in range(row)]

    def loadBoardFromFile(self, filename):
        with open(filename, 'r') as f:
            firstLine = [int(x) for x in f.readline().strip().split(',') if x]
            self.col = int(firstLine[0])
            self.row = int(firstLine[1])
            self.grid = [[0 for _ in range(self.col)] for _ in range(self.row)]
            blocks = {}
            for row, line in enumerate(f):
                for col, val in enumerate(line.strip().split(',')):
                    if val:
                        val = int(val)
                        self.grid[row][col] = val
                        if val == -1:
                            self.goalPosition = (row, col)
                        elif val > 1:
                            if val in blocks:
                                blocks[val].positions.append((row, col))
                            else:
                                blocks[val] = Block(val, [(row, col)])
            self.blocks = blocks

    def cloneState(self):
        return copy.deepcopy(self)

    def checkMove(self, positions, blockID):
        for row, col in positions:
            if col < 0 or col >= self.col or row < 0 or row >= self.row:
                return False
            if self.grid[row][col] == -1 and blockID == 2:
                continue
            if self.grid[row][col] != 0 and self.grid[row][col] != blockID:
                return False
        return True

    def getBlock(self, blockID):
        return self.blocks.get(blockID)

    def identifySolutions(self):
        for row in self.grid:
            for col in row:
                if col == -1:
                    return False
        return True

    def availableMoves(self):
        moves = []
        for blockID, block in self.blocks.items():
            for direction in ['up', 'down', 'left', 'right']:
                newPos = block.calcNewPositions(direction)
                if self.checkMove(newPos, blockID):
                    moves.append((blockID, direction))
        return moves

    def compareStates(self, board2):
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j] != board2.grid[i][j]:
                    return False
        return True

    def normalize(self, board):
        nextIdx = 3
        for i, row in enumerate(board.grid):
            for j, col in enumerate(row):
                if board.grid[i][j] == nextIdx:
                    nextIdx = nextIdx + 1
                elif board.grid[i][j] > nextIdx:
                    self.swapIdx(nextIdx, board.grid[i][j])
                    nextIdx = nextIdx + 1

    def swapIdx(self, idx1, idx2):
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                if self.grid[i][j] == idx1:
                    self.grid[i][j] = idx2
                elif self.grid[i][j] == idx2:
                    self.grid[i][j] = idx1

    def printBoard(self):
        print(f"{self.col},{self.row}")
        for row in self.grid:
            for col in row:
                print(f"{col},", end=' ')
            print()
