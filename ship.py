### for images in pygames, use .bmp files because pygame loads bitmaps by default
import pygame

## We treat the ship as a rectangle in this class, because it is easier to work with for when objects in the game collide, etc.

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen ## references to the alien invasion class so it can use all methods in tehre
        self.screen_rect = ai_game.screen.get_rect() # rect is rectangle. This command lets us place the rect where we want

        # load the ship image and get its rect.
        self.image = pygame.image.load("ship.bmp")
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom ## matches rectangle value to screen midbottom value. This way it's aligned

        # Movement flag
        self.moving_right = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """Draw the ship at its current lcoation."""
        self.screen.blit(self.image, self.rect)
