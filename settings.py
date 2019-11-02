class Settings:
    """Class for store settings"""

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 250)

        self.ship_speed_factor = 0.75
        self.ship_limit = 3

        # bullet parameters
        self.bullet_speed_factor = 0.75
        self.bullet_width = 4
        self.bullet_height = 20
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 3

        self.alien_speed_factor = 0.1
        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

        # 1 is right, -1 - left
        self.fleet_direction = 1

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 0.75
        self.bullet_speed_factor = 0.75
        self.alien_speed_factor = 0.1

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)
