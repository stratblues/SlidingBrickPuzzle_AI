class GameState:
    def __init__(self):
        self.goalState = -1
        self.emptyCell = 0
        self.wall = 1
        self.masterBrickPiece = 2
        self.rows = 0
        self.cols = 0
        self.game = []
        self.firstLine = [0, 0]

    def loadLayoutFromFile(self, filename):
        with open(filename, 'r') as f:
            self.firstLine = [int(x) for x in f.readline().strip().split(',') if x]
            self.rows = int(self.firstLine[1])
            self.cols = int(self.firstLine[0])
            self.game = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
            for row in range(self.rows):
                line = f.readline().strip().split(',')
                row_vals = [int(x) for x in line if x.strip()]
                for col in range(self.cols):
                    self.game[row][col] = row_vals[col]

    def printGame(self):
        print(self.firstLine[0], ",", self.firstLine[1])
        for row in self.game:
            for col in row:
                print(col, ",", end=' ')

            print()

    def cloneState(self):
        newGame = GameState()
        newGame.rows = self.rows
        newGame.columns = self.cols
        newGame.game = [[row[:] for row in self.game]]
        return newGame

    def identifySolutions(self):
        for row in self.game:
            for col in row:
                if col == -1:
                    return True
        return False

    def movesThisPieceCanDo(self, thisPiece):
        moves = []
        for i, row in enumerate(self.game):
            for j, col in enumerate(self.game[i]):
                if i > 0 and self.game[i][j] == thisPiece:
                    if self.game[i - 1][j] == self.emptyCell:
                        moves.append((thisPiece, "up"))
                    if self.game[i + 1][j] == self.emptyCell:
                        moves.append((thisPiece, "down"))
                    if self.game[i][j + 1] == self.emptyCell:
                        moves.append((thisPiece, "right"))
                    if self.game[i][j - 1] == self.emptyCell:
                        moves.append((thisPiece, "left"))
        return moves

    def allAvailableMoves(self):
        uniquePieces = {self.game[i][j]
                        for i in range(self.rows)
                        for j in range(self.cols)
                        if self.game[i][j] != self.emptyCell
                        and self.game[i][j] != self.wall
                        and self.game[i][j] != self.goalState
                        }
        moves = []
        for piece in uniquePieces:
            moves += self.movesThisPieceCanDo(piece)
        return moves

    def printAllMoves(self):
        moves = self.allAvailableMoves()
        for move in moves:
            print(move)

    def applyMove(self, move):
        move = move.replace('(', '').replace(')', '')
        arg = move.strip().split(',')
        piece = int(arg[0].strip())
        moveDirection = arg[1].strip()
        possibleMoves = self.movesThisPieceCanDo(piece)
        if (piece, moveDirection) not in possibleMoves:
            print("You can't make that move.")
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.game[i][j] == piece:
                    if moveDirection == "up" and i > 0 and self.game[i - 1][j] == 0:
                        self.game[i][j], self.game[i - 1][j] = self.game[i - 1][j], piece
                        return True
                    if moveDirection == "down" and i < self.rows - 1 and self.game[i + 1][j] == 0:
                        self.game[i][j], self.game[i + 1][j] = self.game[i + 1][j], piece
                        return True
                    if moveDirection == "left" and j > 0 and self.game[i][j - 1] == 0:
                        self.game[i][j], self.game[i][j - 1] = self.game[i][j - 1], piece
                        return True
                    if moveDirection == "right" and j < self.cols - 1 and self.game[i][j + 1] == 0:
                        self.game[i][j], self.game[i][j + 1] = self.game[i][j + 1], piece
                        return True
                    else:
                        return False
        return True

    def returnNewStateAfterMove(self, move):
        newGame = self.cloneState()
        newGame.applyMove(move)
        newGame.printGame()


