import pygame


class Ship:
    """Create ship"""
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        # Loading ship img and create rectangle
        self.image = pygame.image.load('img//Ship_png.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitship(self):
        """Draw ship in position"""
        self.screen.blit(self.image, self.rect)
