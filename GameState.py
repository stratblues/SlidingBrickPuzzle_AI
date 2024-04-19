from Board import Board


class GameState:
    def __init__(self, filename):
        self.board = Board(0, 0, {})
        self.board.loadBoardFromFile(filename)

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

    # def __init__(self):
    #     self.goalState = -1
    #     self.emptyCell = 0
    #     self.wall = 1
    #     self.masterBrickPiece = 2
    #     self.rows = 0
    #     self.cols = 0
    #     self.game = []
    #     self.firstLine = [0, 0]

    # def loadLayoutFromFile(self, filename):
    #     with open(filename, 'r') as f:
    #         self.firstLine = [int(x) for x in f.readline().strip().split(',') if x]
    #         self.rows = int(self.firstLine[1])
    #         self.cols = int(self.firstLine[0])
    #         self.game = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
    #         for row in range(self.rows):
    #             line = f.readline().strip().split(',')
    #             rowVals = [int(x) for x in line if x.strip()]
    #             for col in range(self.cols):
    #                 self.game[row][col] = rowVals[col]

    # def printGame(self):
    #     print(f"{self.firstLine[0]},{self.firstLine[1]}")
    #     for row in self.game:
    #         for col in row:
    #             print(f"{col},", end=' ')
    #
    #         print()

    # def movesThisPieceCanDo(self, thisPiece):
    #     moves = []
    #     for i, row in enumerate(self.game):
    #         for j, col in enumerate(self.game[i]):
    #             if i > 0 and self.game[i][j] == thisPiece:
    #                 if self.game[i - 1][j] == self.emptyCell:
    #                     moves.append(f"({thisPiece},up)")
    #                 if self.game[i + 1][j] == self.emptyCell:
    #                     moves.append(f"({thisPiece},down)")
    #                 if self.game[i][j + 1] == self.emptyCell:
    #                     moves.append(f"({thisPiece},right)")
    #                 if self.game[i][j - 1] == self.emptyCell:
    #                     moves.append(f"({thisPiece},left)")
    #     return moves

    # def allAvailableMoves(self):
    #     uniquePieces = {self.game[i][j]
    #                     for i in range(self.rows)
    #                     for j in range(self.cols)
    #                     if self.game[i][j] != self.emptyCell
    #                     and self.game[i][j] != self.wall
    #                     and self.game[i][j] != self.goalState
    #                     }
    #     moves = []
    #     for piece in uniquePieces:
    #         moves += self.movesThisPieceCanDo(piece)
    #     return moves

    # def printAllMoves(self):
    #     moves = self.allAvailableMoves()
    #     for move in moves:
    #         print(move)
    #
    # def applyMove(self, move):
    #     piece, moveDirection = move.replace('(', '').replace(')', '').split(',')
    #     piece = int(piece.strip())
    #     moveDirection = moveDirection.strip()
    #     possibleMoves = self.movesThisPieceCanDo(piece)
    #     if move not in possibleMoves:
    #         print("You can't make that move.")
    #         return False
    #     for i in range(self.rows):
    #         for j in range(self.cols):
    #             if self.game[i][j] == piece:
    #                 try:
    #                     if moveDirection == "up" and i > 0 and self.game[i - 1][j] == 0:
    #                         self.game[i][j], self.game[i - 1][j] = self.game[i - 1][j], piece
    #                     elif moveDirection == "down" and i < self.rows - 1 and self.game[i + 1][j] == 0:
    #                         self.game[i][j], self.game[i + 1][j] = self.game[i + 1][j], piece
    #                     elif moveDirection == "left" and j > 0 and self.game[i][j - 1] == 0:
    #                         self.game[i][j], self.game[i][j - 1] = self.game[i][j - 1], piece
    #                     elif moveDirection == "right" and j < self.cols - 1 and self.game[i][j + 1] == 0:
    #                         self.game[i][j], self.game[i][j + 1] = self.game[i][j + 1], piece
    #                     else:
    #                         continue
    #                 except IndexError:
    #                     continue
    #     return True
    #
    # def returnNewStateAfterMove(self, move):
    #     newGame = self.cloneState()
    #     newGame.applyMove(move)
    #     newGame.printGame()
