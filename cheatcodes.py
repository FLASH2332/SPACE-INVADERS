import pygame

class Cheatcodes:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.cheatstr = ""
        self.ship = ai_game.ship

    def cheats(self):
        print("Cheatcodes: Entering cheats method")
        print("Cheatcodes: Cheat string =", self.cheatstr)
        if self.cheatstr == "increaselife":
            print("Cheatcodes: Increasing life")
            self.ai_game.ship.ship_limit += 1
            print("Cheatcodes: New ship limit =", self.ai_game.ship.ship_limit)
