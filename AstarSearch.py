import heapq
import time

import GameState
from SearchStrategy import SearchStrategy


class AstarSearch(SearchStrategy):
    def manhattanDistance(self, currentGame):
        masterBrick = currentGame.board.masterBrickPosition
        goalState = currentGame.board.goalPosition
        return abs(masterBrick[0] - goalState[0]) + abs(masterBrick[1] - goalState[1])

    def search(self, gameState: GameState) -> None:
        startTime = time.time()

        openList = []
        startState = gameState.cloneState()
        startState.g = 0
        startState.h = self.manhattanDistance(startState)
        startState.f = startState.g + startState.h
        closedList = set()
        counter = 0
        heapq.heappush(openList, (startState.f, counter, startState, []))
        counter += 1

        while openList:
            currentF, _, currentGameState, pathToState = heapq.heappop(openList)

            currentStateTuple = gameState.dictionaryToTuple(currentGameState.board.blocks)
            if currentStateTuple in closedList:
                continue

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

            closedList.add(currentStateTuple)

            for blockID, directions in currentGameState.availableMoves().items():
                for direction in directions:
                    newGame = currentGameState.cloneState()
                    newGame.applyMove(blockID, direction)

                    newGame.g = currentGameState.g + 1
                    newGame.h = self.manhattanDistance(newGame)
                    newGame.f = newGame.g + newGame.h

                    newGameState = gameState.dictionaryToTuple(newGame.board.blocks)
                    # If new state has been visited with a lower g value, skip adding to open list
                    if newGameState in closedList:
                        continue
                    heapq.heappush(openList, (newGame.f, counter, newGame,
                                              pathToState + [(blockID, direction)]))
                    counter += 1
        return None
