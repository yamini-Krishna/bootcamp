import pickle

class Game:
    def __init__(self, player, level=1, score=0):
        self.player = player
        self.level = level
        self.score = score

    @staticmethod
    def load(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)

# Load game from file
loaded_game = Game.load("game_state.pkl")
print(f"Player: {loaded_game.player}, Level: {loaded_game.level}, Score: {loaded_game.score}")
