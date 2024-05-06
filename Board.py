import copy

from Block import Block


class Board:
    def __init__(self, col, row, blocks, grid=None, goalPosition=None, masterBrickPosition=None):
        self.col = col
        self.row = row

        # dict of blocks with blockID to Block obj
        self.blocks = blocks
        #tuple
        self.masterBrickPosition = masterBrickPosition
        # tuple
        self.goalPosition = goalPosition
        if grid is None:
            self.grid = [[0 for _ in range(col)] for _ in range(row)]
        else:
            self.grid = [row[:] for row in grid]

    def loadBoardFromFile(self, filename):
        self.goalPosition = None
        with open(filename, 'r') as f:
            firstLine = [int(x) for x in f.readline().strip().split(',') if x]
            self.col = int(firstLine[0])
            self.row = int(firstLine[1])
            self.grid = [[0 for _ in range(self.col)] for _ in range(self.row)]
            # blocks dict
            blocks = {}
            for row, line in enumerate(f):
                for col, val in enumerate(line.strip().split(',')):
                    if val:
                        val = int(val)
                        # add items to grid here
                        self.grid[row][col] = val
                        if val == -1:
                            self.goalPosition = (row, col)
                        elif val > 1:
                            if val == 2:
                                self.masterBrickPosition = (row, col)
                            if val in blocks:
                                blocks[val].positions.append((row, col))
                            else:
                                # fill blocks dict with block object
                                blocks[val] = Block(val, [(row, col)])
            # make sure to set local dict to object dict
            self.blocks = blocks

    def cloneState(self):
        clonedGrid = [row[:] for row in self.grid]
        cloneGoalPosition = copy.deepcopy(self.masterBrickPosition)
        cloneMasterBrickPosition = copy.deepcopy(self.goalPosition)
        clonedBlocks = {id: block.clone() for id, block in self.blocks.items()}
        return Board(self.col, self.row, clonedBlocks, clonedGrid, cloneGoalPosition, cloneMasterBrickPosition)

    def getBlock(self, blockID):
        return self.blocks.get(blockID)

    def identifySolutions(self):
        if self.goalPosition is None:
            return False
        goalRow, goalCol = self.goalPosition
        if self.grid[goalRow][goalCol] == 2:
            return True
        return False

    def availableMoves(self):
        movesDict = {}
        for blockID, block in self.blocks.items():
            blockMoves = []
            for direction in ['up', 'down', 'left', 'right']:
                newPos = block.calcNewPositions(direction)
                if self.checkMove(newPos, blockID):
                    blockMoves.append(direction)
            if blockMoves:
                movesDict[blockID] = blockMoves
        return movesDict

    def checkMove(self, positions, blockID):
        if any(col < 0 or col >= self.col or row < 0 or row >= self.row for row, col in positions):
            return False
        for row, col in positions:
            cell = self.grid[row][col]
            if cell == -1 and blockID == 2:
                continue
            if cell != 0 and cell != blockID:
                return False

        return True

    def compareStates(self, board2):
        if len(self.blocks) == len(board2.blocks):
            return True
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j] != board2.grid[i][j]:
                    return False
        return True

    def normalize(self):
        nextIdx = 3
        indexMap = {}
        for i, row in enumerate(self.grid):
            for j, value in enumerate(row):
                if value > 2 and value not in indexMap:
                    indexMap[value] = nextIdx
                    nextIdx += 1

        for i, row in enumerate(self.grid):
            for j, value in enumerate(row):
                if value in indexMap:
                    self.grid[i][j] = indexMap[value]

    def swapIdx(self, idx1, idx2):
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                if self.grid[i][j] == idx1:
                    self.grid[i][j] = idx2
                elif self.grid[i][j] == idx2:
                    self.grid[i][j] = idx1

    def printBoard(self):
        print(f"{self.col},{self.row},")
        for row in self.grid:
            for col in row:
                print(f"{col},", end=' ')
            print()
