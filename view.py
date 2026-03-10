from players import PlayerAction

class BomberView:
    def ask_action(self) -> PlayerAction:
        ...
    
    def ask_where_to_move(self) -> tuple[str, int]:
        ...
    
    def ask_relic_to_use(self) -> None:
        ...
    
    def print_grid(self) -> None:
        ...
    
    def ask_where_to_place_player(self) -> None:
        ...
    
    def win(self) -> None:
        ...
    