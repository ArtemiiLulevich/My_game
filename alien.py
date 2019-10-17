import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class that present one alian"""
    def __init__(self, ai_setting, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_setting = ai_setting

        self.image = pygame.image.load('img/Alien_ref.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitalien(self):
        self.screen.blit(self.image, self.rect)
