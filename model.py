from bombs import Bomb
from random import Random
from common_types import map_loc

class BomberModel:
    def __init__(self, rows: int, cols: int, max_rounds: int, rng: Random, bomb_set: list[type[Bomb]], player: map_loc) -> None:
        self._rows = rows
        self._cols = cols
        self._rng = rng
        self._max_round = max_rounds
        self._bomb_set = bomb_set
        self._player = player
        self._turn = 0
        self._map: list[list[str]] = [["." for _ in range(self._cols)] for _ in range(self._rows)]
        self._indexes: list[list[map_loc]] = [[(r, c) for c in range(self._cols)] for r in range(self._rows)]
        self._curr_bombs: list[Bomb] = []
        self._is_game_over: bool = False

    @property
    def turn(self) -> int:
        return self._turn
    
    @property
    def is_game_over(self) -> bool:
        return self._is_game_over
    
    @property
    def grid(self) -> list[list[str]]:
        return self._map
    
    def next_turn(self) -> None:
        self._turn += 1
        if self._turn >= self._max_round:
            self._is_game_over = True
    
    def random_index(self) -> map_loc:
        index_list: list[map_loc] = [index for row in self._indexes for index in row if index != self._player]
        return self._rng.choice(index_list)

    def plant_bomb(self, index: map_loc):
        bomb_class: type[Bomb] = self._rng.choice(self._bomb_set)
        bomb = bomb_class(self._rows, self._cols, index)
        self._map[index[0]][index[1]] = bomb.__str__()
        self._curr_bombs.append(bomb)
    
    def process_turn(self) -> set[map_loc]:
        if len(self._curr_bombs) <= 1:
            for _ in range(self._rng.randint(0, 3)):
                self.plant_bomb(self.random_index())

        explosions: set[map_loc] = set()
        placeholder: list[Bomb] = []
        
        for bomb in self._curr_bombs:
            bomb.tick()
            if bomb.time_end():
                explosions = explosions | bomb.explode()
                self._map[bomb.loc[0]][bomb.loc[1]] = "."
            else:
                placeholder.append(bomb)
        
        if self._player in explosions:
            self._is_game_over = True
        
        self._curr_bombs = placeholder
        self.next_turn()

        return explosions
    
    def move_player(self, new_index: map_loc):
        self._map[self._player[0]][self._player[1]] = "."
        self._player = (self._player[0] + new_index[0], self._player[1] + new_index[1])
        self._map[self._player[0]][self._player[1]] = "P"
    
    def in_bounds(self, r: int, c: int) -> bool:
        if 0 <= r + self._player[0] < self._rows and 0 <= self._player[1] + c < self._cols:
            return True
        else:
            return False
        
    @property
    def player(self) -> map_loc:
        return self._player
        
            

        



    
