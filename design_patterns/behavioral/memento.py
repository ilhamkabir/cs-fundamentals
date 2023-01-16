import pickle
from dataclasses import dataclass

class Memento:

    def __init__(self):
        self._caretaker = None

    def set_state(self, state):
        self._caretaker = pickle.dumps(state) # convention to call state "caretaker"

    def get_state(self):
        return pickle.loads(self._caretaker)

@dataclass
class GameState:
    level: int

class MarioCart:

    def __init__(self):
        self.game_state = GameState(1)
        self.memento = Memento()

    def level_up(self):
        self.game_state.level += 1
        print('leveled up | current level:', self.game_state.level)

    def level_down(self):
        if self.game_state.level == 1:
            print("can't level down. you're at level 1")
            return
        self.game_state.level -= 1 
        print('leveled down | current level:', self.game_state.level)

    def save_progress(self):
        self.memento.set_state(self.game_state)
        print('>> PROGRESS SAVED')
    
    def restore_progress(self):
        self.game_state = self.memento.get_state()
        print('>> PROGRESS RESTORED')
        
game = MarioCart()

game.level_up()
game.level_up()
game.level_up()
game.level_down()

game.save_progress()

print('Game crashed!')
game.game_state.level = 1 # game crashed

game.level_down()

game.restore_progress()

game.level_down()
