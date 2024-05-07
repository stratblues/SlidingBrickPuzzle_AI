import time

import GameState
from SearchStrategy import SearchStrategy


class IterativeDeepeningSearch(SearchStrategy):

    def search(self, gameState: GameState) -> None:

        limit = 0
        startTime = time.time()

        while True:
            # closed list
            closedList = {}
            scan = self.depthLimitedSearch(gameState, limit, closedList, startTime)
            if scan is not None:
                return scan
            limit += 1

    def depthLimitedSearch(self, gameState, depthLimit, closedList, startTime):
        # open list of current state, path to that state
        stack = [(gameState.cloneState(), [])]
        nodesVisited = 0

        while stack:
            currentGameState, pathToState = stack.pop()
            currentDepth = len(pathToState)
            currentStateToTuple = gameState.dictionaryToTuple(currentGameState.board.blocks)
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
                        newGameState = gameState.dictionaryToTuple(newGame.board.blocks)
                        if (newGameState, currentDepth + 1) not in closedList:
                            # add newGameState and path to stack that includes new move
                            stack.append((newGame, pathToState + [(blockID, direction)]))
