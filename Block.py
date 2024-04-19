class Block:
    def __init__(self, blockID, positions):
        #block id from val in enumerate grid logic
        self.blockID = blockID

        # tuples list of (x,y) spot in grid
        self.positions = positions

    def move(self, direction, board):
        newPositions = self.calcNewPositions(direction)
        if board.checkMove(newPositions, self.blockID):
            for row, col in self.positions:
                board.grid[row][col] = 0
            for row, col in newPositions:
                board.grid[row][col] = self.blockID
            self.positions = newPositions

    def calcNewPositions(self, direction):
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

