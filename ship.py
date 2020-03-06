### for images in pygames, use .bmp files because pygame loads bitmaps by default
import pygame
from pygame.sprite import Sprite

## We treat the ship as a rectangle in this class, because it is easier to work with for when objects in the game collide, etc.

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen ## references to the alien invasion class so it can use all methods in there
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect() # rect is rectangle. This command lets us place the rect where we want

        # load the ship image and get its rect.
        self.image = pygame.image.load("ship.bmp")
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom ## matches rectangle value to screen midbottom value. This way it's aligned

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current lcoation."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """ Center the ship on teh screen. """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)