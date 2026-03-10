from protocols import Player
from enum import Enum, auto

class PlayerAction(Enum):
    MOVE = auto()
    USE_RELIC = auto()

class BasicPlayer(Player):
    def __init__(self, location: tuple[int, int]) -> None:
        self._base_hp: int = 3
        self._base_move_num: int = 1
        self._location = location

    def action(self, choice: PlayerAction) -> None:
        match choice:
            case PlayerAction.MOVE:
                self.walk()
            case PlayerAction.USE_RELIC:
                self.use_relic()
            case _:
                pass

    def walk(self, ) -> None:
        ...
        
    
    def use_relic(self) -> None:
        ...
    
    def move_num(self) -> int:
        return self._base_move_num
