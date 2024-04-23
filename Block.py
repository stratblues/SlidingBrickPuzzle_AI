class Block:
    def __init__(self, blockID, positions):
        #block id from val in enumerate grid logic
        self.blockID = blockID

        # tuples list of (x,y) spot in grid
        self.positions = positions

    def move(self, direction, board):
        newPositions = self.calcNewPositions(direction)
        if board.checkMove(newPositions, self.blockID):
            # set old grid positions now to equal 0
            for row, col in self.positions:
                board.grid[row][col] = 0
            # set new grid positions to equal new blockID val
            for row, col in newPositions:
                board.grid[row][col] = self.blockID
            # update block positions list
            self.positions = newPositions

    def calcNewPositions(self, direction):
        # given a move direction, loop through all the block positions and adjust that position
        if direction == "up":
            return [(row-1, col) for row, col in self.positions]
        elif direction == "down":
            return [(row+1, col) for row, col in self.positions]
        elif direction == "left":
            return [(row, col-1) for row, col in self.positions]
        elif direction == "right":
            return [(row, col+1) for row, col in self.positions]

    def availableMoves(self, board):
        directions = ["up", "down", "left", "right"]
        validMoves = []
        for direction in directions:
            if board.checkMove(self.calcNewPositions(direction)):
                validMoves.append((self.blockID, direction))
        return validMoves

