## py -3 venv alien_venv
## alien_venv/scripts/activate
## pip install pygame

import sys ### use tools in this package to exit game when player quits
import pygame
from settings import Settings ## the file with the class we made
from ship import Ship

#### First, we create a class to represent the game
class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()


        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)) ## 1200px by 800px. From the settings class
        # Assigned ^ to self.screen so it's available in all methods in the class 
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self) # this gives ship access to the games resources

        # Set the background color:
        self.bg_color = (230, 230, 230)

    def run_game(self): ## this controls the game
        """Start the main loop for the game."""
        while True:
            self._check_events() #single leading underscore indicates helper method
            self._update_screen()

            # Watch for keyboard and mouse events.
    def _check_events(self):
        """ Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #Move the ship to the right.
                    self.ship.rect.x += 1
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass thruogh the loop.
        self.screen.fill(self.settings.bg_color) ## taken from settings.py file
        self.ship.blitme() # this draws the ship
        
        # Make the most recently drawn screen visible.
        pygame.display.flip() ## continually updates the display so it looks like there is smooth movement

if __name__ == "__main__":
    # Make a game instance, and run game.
    ai = AlienInvasion()
    ai.run_game()

