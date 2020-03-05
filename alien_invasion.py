## py -3 venv alien_venv
## alien_venv/scripts/activate
## pip install pygame

import sys ### use tools in this package to exit game when player quits
import pygame

#### First, we create a class to represent the game
class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800)) ## 1200px by 800px
        # Assigned ^ to self.screen so it's available in all methods in the class 
        pygame.display.set_caption("Alien INvasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Make the most recently drawn screen visible.
            pygame.display.flip()
if __name__ == "__main__":
    # Make a game instance, and run game.
    ai = AlienInvasion()
    ai.run_game()

