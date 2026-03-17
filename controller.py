from model import BomberModel
from view import BomberView
from random import Random
from bombs import BasicBomb


def clear():
    print("\033c", end="")

class BomberController:
    def __init__(self, model: BomberModel, view: BomberView) -> None:
        self._model = model
        self._view = view
    
    def run(self) -> None:
        model = self._model
        view = self._view

        model.move_player((0, 0))
        while True:
            clear()
            exploded = model.process_turn()
            view.print_grid(model.grid, exploded) 
            
            if model.is_game_over:
                break
            
            r_add, c_add = view.ask_move()
            if model.in_bounds(r_add, c_add):
                model.move_player((r_add, c_add))

        view.win()


if __name__ == "__main__":
    model = BomberModel(6, 7, 10, Random(), [BasicBomb], (0, 0))
    view = BomberView()
    controller = BomberController(model, view)
    controller.run()
        
                
            