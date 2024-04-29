import pygame
import sys

from settings import Settings
from keys import Key

class KeyGame:
    """A class to manage the game."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height
            ))
        
        # self.font = pygame.font.Font(None, 36)
        pygame.display.set_caption("Key Game")
        self.text = Key(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()
        self.text.key_pressed = True
        key_event = pygame.key.name(event.key)
        self.text.update_text(key_event)

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        self.text.key_pressed = False
        self.text.update_text("")

    def _update_screen(self):
        """Update screen image, and flip to new screen."""
        self.screen.fill(self.settings.bg_color)
        self.text.blitme()
            
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    kg = KeyGame()
    kg.run_game()