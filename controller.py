from model import BomberModel
from view import BomberView
from time import sleep
from players import PlayerAction

class BomberController:
    def __init__(self, model: BomberModel, view: BomberView) -> None:
        self._model = model
        self._view = view
    
    def run(self) -> None:
        model = self._model
        view = self._view

        view.ask_where_to_place_player()
        model.place_player()
        view.print_grid()
        sleep(1)

        while not model.game_over_is_true:
            model.place_bombs()
            view.print_grid()

            chosen_action: PlayerAction = view.ask_action()
            
            match chosen_action:
                case PlayerAction.MOVE:
                    model.move_turn(chosen_action)
                
                case PlayerAction.USE_RELIC:
                    model.use_relic()
                
                case _:
                    pass
            
        view.win()


if __name__ == "__main__":
    ...
            
        
                
            