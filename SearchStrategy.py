from abc import ABC, abstractmethod

from GameState import GameState


class SearchStrategy(ABC):
    @abstractmethod
    def search(self, gameState: GameState) -> None:
        pass
