class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0
        self.load_high_score()  # Call the method to load high score on initialization

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 0

    def load_high_score(self):
        try:
            with open(r"C:\Users\jayad\Desktop\PYTHON\ALIENSPACE\HIGHSCORE.txt", 'r') as high_score_file:
                self.high_score = int(high_score_file.read())
        except FileNotFoundError:
            # Handle the case where the file is not found
            print("High score file not found.")
        except ValueError:
            # Handle the case where the file content is not a valid integer
            print("Error reading high score from file.")

    def save_high_score(self):
        with open(r"C:\Users\jayad\Desktop\PYTHON\ALIENSPACE\HIGHSCORE.txt", 'w') as high_score_file:
            high_score_file.write(str(self.high_score))
