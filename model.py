from protocols import Bomb, Player
from random import Random
from players import PlayerAction

class BomberModel:
    def __init__(self, bombset: set[Bomb], player: Player, dimension: tuple[int, int], rng: Random) -> None:
        self._row, self._col = dimension
        self._bombset = bombset
        self._player = player
        self._grid_string: list[list[str]] = [["." for _ in range(self._col)] for _ in range(self._row)]
        self._rng = rng
        self._turn = 1
        self._grid_items: list[list[None | Bomb]] = [[None for _ in range(self._col)] for _ in range(self._row)]
        self._is_game_over: bool = False
        
    @property
    def is_game_over(self) -> bool:
        return self._is_game_over
    
    @is_game_over.setter
    def game_over_is_true(self) -> None:
        self._is_game_over = True
    
    @property
    def rng(self) -> Random:
        return self._rng
    
    def next_turn(self) -> None:
        self._turn += 1
    
    def grid(self) -> list[list[None | Bomb]]:
        return self._grid_items

    def choose_bomb_loc(self) -> tuple[int, int]:
        return self._rng.randint(0, self._row - 1), self._rng.randint(0, self._col - 1)
    
    def move_turn(self, choice: PlayerAction):
        self._player.action(choice)
    
    def place_bombs(self):
        r, c = self.choose_bomb_loc()
        bomb: Bomb = self.rng.choice(list(self._bombset))
        self._grid_items[r][c] = bomb

    def place_player(self):
        ...
    
    def use_relic(self):
        ...



