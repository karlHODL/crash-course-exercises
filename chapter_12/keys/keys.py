import pygame

class Key:
    """A class to manage the Key."""

    def __init__(self, kg_game):
        """Initialize the Key and set its starting position."""
        self.screen = kg_game.screen
        self.screen_rect = kg_game.screen.get_rect()
        self.font = pygame.font.Font(None, 36)
        self.text_color = (255, 255, 255)
        self.text = self.font.render("Press q to exit.", True, self.text_color)
        self.text_rect = self.text.get_rect(center=self.screen_rect.center)
        self.key_pressed = False

    def update_text(self, key_event):
        """Update the text based on the keyevent."""
        # if self.key_pressed:
        self.text = self.font.render(key_event, True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=self.screen_rect.center)

    def blitme(self):
        """Draw the key at its current location."""
        self.screen.blit(self.text, self.text_rect)
