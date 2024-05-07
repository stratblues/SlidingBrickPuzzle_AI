import time
from collections import deque

from GameState import GameState
from SearchStrategy import SearchStrategy


class BreadthFirstSearch(SearchStrategy):

    def search(self, gameState: GameState) -> None:
        startTime = time.time()
        # open list tuple of initial state and path to that state
        queue = deque([(gameState.cloneState(), [])])
        # closed list dictionary for expanded/searched nodes
        closedList = {}
        nodesVisited = 0

        while queue:
            # pop current state and path ( which is empty at first )
            currentGameState, pathToState = queue.popleft()
            currentStateToTuple = gameState.dictionaryToTuple(currentGameState.board.blocks)
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
                    newGameState = gameState.dictionaryToTuple(newGame.board.blocks)
                    if newGameState not in closedList:
                        # transition model, result state by taking action apply move
                        # append newGame (board with avail moves) to the openlist queue along with path to this state
                        queue.append((newGame, pathToState + [(blockID, direction)]))
