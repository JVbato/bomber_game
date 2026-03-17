from typing import Protocol
from common_types import map_loc

class Bomb(Protocol):
    def __init__(self, row: int, col: int, loc: map_loc) -> None:
        ...

    def __str__(self) -> str:
        ...

    @property
    def loc(self) -> map_loc:
        ...

    def time_end(self) -> bool:
        ...

    def tick(self) -> None:
        ...
    
    def explode(self) -> set[map_loc]:
        ...
    
    def in_bounds(self, r: int, c: int) -> bool:
        ...


class BasicBomb:
    def __init__(self, row: int, col: int, loc: map_loc) -> None:
        self._time: int = 4
        self._loc = loc
        self._rows = row
        self._cols = col

    def __str__(self) -> str:
        return "S"

    @property
    def loc(self) -> map_loc:
        return self._loc

    def tick(self) -> None:
        self._time -= 1
    
    def time_end(self) -> bool:
        return True if self._time <= 0 else False
    
    def in_bounds(self, r: int, c: int) -> bool:
        if 0 <= r < self._rows and 0 <= c < self._cols:
            return True
        else:
            return False
    
    def explode(self) -> set[map_loc]:
        row, col = self._loc
        row_adder: set[int] = {-1, 0, 1}
        col_adder: set[int] = {-1, 0, 1}

        affected: set[map_loc] = set()

        for r in row_adder:
            for c in col_adder:
                if self.in_bounds(row + r, col + c) and (row + r, col + c) != self._loc:
                    affected.add((row + r, col + c))

        return affected
        

from typing import Protocol
from common_types import map_loc

class DiamondBomb():
    def __init__(self, row: int, col: int, loc: map_loc) -> None:
        self._time: int = 2
        self._loc = loc
        self._rows = row
        self._cols = col

    def __str__(self) -> str:
        return "D"

    @property
    def loc(self) -> map_loc:
        return self._loc

    def tick(self) -> None:
        self._time -= 1
    
    def time_end(self) -> bool:
        return True if self._time <= 0 else False
    
    def in_bounds(self, r: int, c: int) -> bool:
        if 0 <= r < self._rows and 0 <= c < self._cols:
            return True
        else:
            return False
    
    def explode(self) -> set[map_loc]:
        row, col = self._loc
        

        affected: set[map_loc] = set()
        
        for idx in range(3):
            if self.in_bounds(row + idx, col + idx - 2):
                affected.add((row + idx, col + idx - 2))
            if self.in_bounds(row + idx, col - idx + 2):
                affected.add((row + idx, col - idx + 2))
            if self.in_bounds(row - idx, col + idx - 2):
                affected.add((row - idx, col + idx - 2))
            if self.in_bounds(row - idx, col - idx + 2):
                affected.add((row - idx, col - idx + 2))
        return affected