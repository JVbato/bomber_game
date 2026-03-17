from common_types import map_loc
from copy import deepcopy


class BomberView:
    def print_grid(self, grid: list[list[str]], explosions: set[map_loc]) -> None:
        
        grid_copy = deepcopy(grid)
        for r, c in explosions:
            grid_copy[r][c] = "x"
        
        for row in grid_copy:
            print(*row)
    
    def ask_move(self) -> map_loc:
        my_dic = {"A": (0, -1), "D": (0, 1), "W": (-1, 0), "S": (1, 0)}
        shit = input("where you movin ").upper()
        if shit in my_dic.keys():
            return my_dic[shit]
        else:
            return (0, 0)

    def win(self) -> None:
        print("you won! ")
    
    def print_turn(self, turn: int):
        print(f"Turn: {turn}")
    
