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
        pygame.display.set_caption("Alien Invasion")#

        # Set the background color:
        self.bg_color = (230, 230, 230)

    def run_game(self): ## this controls the game
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraw the screen during each pass thruogh the loop.
            self.screen.fill(self.bg_color)
            
            # Make the most recently drawn screen visible.
            pygame.display.flip() ## continually updates the display so it looks like there is smooth movement
if __name__ == "__main__":
    # Make a game instance, and run game.
    ai = AlienInvasion()
    ai.run_game()

