import sys

import pygame

from settings import Settings
from ship import Ship


def run_game():
    # Start the game and create screen obj.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption('Alien Invasion')
    # bg_color = (230, 230, 230)

    # Create ship
    ship = Ship(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            screen.fill(ai_settings.bg_color)
            ship.blitship()
        pygame.display.flip()


run_game()
