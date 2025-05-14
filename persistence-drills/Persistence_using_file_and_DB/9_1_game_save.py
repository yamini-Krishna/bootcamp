import pickle

class Game:
    def __init__(self, player, level=1, score=0):
        self.player = player
        self.level = level
        self.score = score

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
        print("Game saved!")

# Example usage
game = Game("Yamini", level=5, score=1200)
game.save("game_state.pkl")
