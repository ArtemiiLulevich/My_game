import pygame


class Ship:
    """Create ship"""
    def __init__(self, screen):
        self.screen = screen

        # Loading ship img and create rectangle
        self.image = pygame.image.load('img//ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitship(self):
        """Draw ship in position"""
        self.screen.blit(self.image, self.rect)
