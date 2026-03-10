from typing import Protocol
from players import PlayerAction

class Bomb(Protocol):
    def __init__(self, timer: int) -> None:
        ...
    
    def tick(self) -> None:
        ...
    
    def explode(self, grid: list[list[str]]) -> None:
        ...

class Player(Protocol):
    def __init__(self) -> None:
        ...
    
    def action(self, choice: PlayerAction) -> None:
        ...

    def walk(self) -> None:
        ...

    def use_relic(self) -> None:
        ...
    
    def move_num(self) -> int:
        ...

class Tile(Protocol):
    ...