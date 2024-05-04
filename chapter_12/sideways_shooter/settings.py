class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.scree_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 2.5

        # Bullet settings
        self.bullet_speed = 4.0
        self.bullet_width = 12
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 6