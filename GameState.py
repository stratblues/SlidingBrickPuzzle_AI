import copy
import time
from collections import deque
from Board import Board
import heapq


class GameState:
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
        newGame.g = self.g
        newGame.h = self.h
        newGame.f = self.f
        newGame.board = copy.deepcopy(self.board)
        return newGame

    def identifySolutions(self):
        return self.board.identifySolutions()

    def availableMoves(self):
        return self.board.availableMoves()

    def getBlock(self, blockID):
        return self.board.getBlock(blockID)

    def dictionaryToTuple(self, d):
        return tuple((blockID, block.getState()) for blockID, block in d.items())

    def manhattanDistance(self, currentGame):
        masterBrick = currentGame.board.masterBrickPosition
        goalState = currentGame.board.goalPosition
        return abs(masterBrick[0] - goalState[0]) + abs(masterBrick[1] - goalState[1])

    def breadthFirstSearch(self):
        startTime = time.time()
        # open list tuple of initial state and path to that state
        queue = deque([(self.cloneState(), [])])
        # closed list dictionary for expanded/searched nodes
        closedList = {}
        nodesVisited = 0

        while queue:
            # pop current state and path ( which is empty at first )
            currentGameState, pathToState = queue.popleft()
            currentStateToTuple = self.dictionaryToTuple(currentGameState.board.blocks)
            if currentStateToTuple in closedList:
                continue
            closedList[currentStateToTuple] = None
            # cost
            nodesVisited += 1

            # check if goal
            if currentGameState.identifySolutions():
                endTime = time.time()
                for move in pathToState:
                    print(f"({move[0]},{move[1]})")
                print()
                currentGameState.printGame()
                print()
                print(nodesVisited)
                print(f"{endTime - startTime:.2f}")
                print(len(pathToState))
                return

            # actions
            availableMoves = currentGameState.availableMoves()
            for blockID, directions in availableMoves.items():
                for direction in directions:
                    newGame = currentGameState.cloneState()
                    newGame.applyMove(blockID, direction)
                    newGameState = self.dictionaryToTuple(newGame.board.blocks)
                    if newGameState not in closedList:
                        # transition model, result state by taking action apply move
                        # append newGame (board with avail moves) to the openlist queue along with path to this state
                        queue.append((newGame, pathToState + [(blockID, direction)]))

    def depthFirstSearch(self):
        startTime = time.time()
        stack = [(self.cloneState(), [])]
        closedList = {}
        nodesVisited = 0
        while stack:
            currentGameState, pathToState = stack.pop()
            currentStateToTuple = self.dictionaryToTuple(currentGameState.board.blocks)
            if currentStateToTuple in closedList:
                continue
            closedList[currentStateToTuple] = None

            nodesVisited += 1

            # check if goal
            if currentGameState.identifySolutions():
                endTime = time.time()
                for move in pathToState:
                    print(f"({move[0]},{move[1]})")
                print()
                currentGameState.printGame()
                print()
                print(nodesVisited)
                print(f"{endTime - startTime:.2f}")
                print(len(pathToState))
                return

            availableMoves = currentGameState.availableMoves()

            for blockID, directions in reversed(availableMoves.items()):
                for direction in directions:
                    newGame = currentGameState.cloneState()
                    newGame.applyMove(blockID, direction)
                    newGameState = self.dictionaryToTuple(newGame.board.blocks)
                    if newGameState not in closedList:
                        # transition model, result state by taking action apply move
                        # append newGame (board with avail moves) to the openlist queue along with path to this state
                        stack.append((newGame, pathToState + [(blockID, direction)]))

    def iterativeDeepeningSearch(self):
        limit = 0
        startTime = time.time()

        while True:
            # closed list
            closedList = {}
            scan = self.depthLimitedSearch(limit, closedList, startTime)
            if scan is not None:
                return scan
            limit += 1

    def depthLimitedSearch(self, depthLimit, closedList, startTime):
        # open list of current state, path to that state
        stack = [(self.cloneState(), [])]
        nodesVisited = 0

        while stack:
            currentGameState, pathToState = stack.pop()
            currentDepth = len(pathToState)
            currentStateToTuple = self.dictionaryToTuple(currentGameState.board.blocks)
            if currentDepth > depthLimit:
                continue
            closedList[(currentStateToTuple, currentDepth)] = None
            nodesVisited += 1
            if currentGameState.identifySolutions():
                endTime = time.time()
                for move in pathToState:
                    print(f"({move[0]},{move[1]})")
                print()
                currentGameState.printGame()
                print()
                print(nodesVisited)
                print(f"{endTime - startTime:.2f}")
                print(len(pathToState))
                return pathToState
            if currentDepth < depthLimit:
                availableMoves = currentGameState.availableMoves()
                for blockID, directions in reversed(availableMoves.items()):
                    for direction in directions:
                        newGame = currentGameState.cloneState()
                        newGame.applyMove(blockID, direction)
                        newGameState = self.dictionaryToTuple(newGame.board.blocks)
                        if (newGameState, currentDepth + 1) not in closedList:
                            # add newGameState and path to stack that includes new move
                            stack.append((newGame, pathToState + [(blockID, direction)]))

    def aStarSearch(self):
        startTime = time.time()

        openList = []
        startState = self.cloneState()
        startState.g = 0
        startState.h = self.manhattanDistance(startState)
        startState.f = startState.g + startState.h
        closedList = {}
        counter = 0
        heapq.heappush(openList, (startState.f, counter, startState, []))
        counter += 1

        while openList:
            currentF, _, currentGameState, pathToState = heapq.heappop(openList)

            if currentGameState.identifySolutions():
                endTime = time.time()
                for move in pathToState:
                    print(f"({move[0]}, {move[1]})")
                print()
                currentGameState.printGame()
                print(len(closedList))
                print(f"{endTime - startTime:.2f} ")
                print(f"{len(pathToState)}")
                return pathToState

            currentStateTuple = self.dictionaryToTuple(currentGameState.board.blocks)
            if currentStateTuple in closedList:
                continue
            closedList[currentStateTuple] = None

            for blockID, directions in currentGameState.availableMoves().items():
                for direction in directions:
                    newGame = currentGameState.cloneState()
                    newGame.applyMove(blockID, direction)

                    newGame.g = currentGameState.g + 1
                    newGame.h = self.manhattanDistance(newGame)
                    newGame.f = newGame.g + newGame.h

                    newGameState = self.dictionaryToTuple(newGame.board.blocks)
                    # If new state has been visited with a lower g value, skip adding to open list
                    if newGameState in closedList:
                        continue
                    heapq.heappush(openList, (newGame.f, counter, newGame,
                                              pathToState + [(blockID, direction)]))
                    counter += 1
        return None
