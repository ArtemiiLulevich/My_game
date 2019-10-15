class Settings:
    """Class for store settings"""

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 250)

        self.ship_speed_factor = 0.75

        # bullet parameters
        self.bullet_speed_factor = 0.5
        self.bullet_width = 4
        self.bullet_height = 20
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 3
