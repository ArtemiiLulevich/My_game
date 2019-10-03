import pygame

from settings import Settings
from ship import Ship
import game_function as gf


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
    ship = Ship(ai_settings, screen)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
