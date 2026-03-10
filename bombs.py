from protocols import Bomb

class BasicBomb(Bomb):
    def __init__(self, timer: int) -> None:
        self._timer = timer
        self._radius: int = 1
        self._hollow: int = False
        self._damage: int = 1
    
    def tick(self) -> None:
        self._timer -= 1
    
    def explode(self, grid: list[list[str]]) -> None:
        if self._timer <= 0:
            ...