import time

import GameState
from SearchStrategy import SearchStrategy


class DepthFirstSearch(SearchStrategy):
    def search(self, gameState: GameState) -> None:
        startTime = time.time()
        stack = [(gameState.cloneState(), [])]
        closedList = {}
        nodesVisited = 0
        while stack:
            currentGameState, pathToState = stack.pop()
            currentStateToTuple = gameState.dictionaryToTuple(currentGameState.board.blocks)
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
                    newGameState = gameState.dictionaryToTuple(newGame.board.blocks)
                    if newGameState not in closedList:
                        # transition model, result state by taking action apply move
                        # append newGame (board with avail moves) to the openlist queue along with path to this state
                        stack.append((newGame, pathToState + [(blockID, direction)]))
