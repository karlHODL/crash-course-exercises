import pygame

class Rocket:
    """A class to manage the rocket."""

    def __init__(self, rg_game):
        """Initialize the rocket and set its starting position."""
        self.screen = rg_game.screen
        self.settings = rg_game.settings
        self.screen_rect = rg_game.screen.get_rect()

        # Load the rocket image and get its rect.
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()

        # Start each new rocket at the center of the screen
        self.rect.center = self.screen_rect.center

        # Store a float value for the rocket's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags; start with a rocket that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the rocket's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed

        # Update rect object from self.x and self.y.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)