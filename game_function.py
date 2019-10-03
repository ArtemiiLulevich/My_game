import sys

import pygame


def check_events():
    """Check mouse and keypad events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """Refreshes the image on the screen and displays a new screen."""
    screen.fill(ai_settings.bg_color)
    ship.blitship()
    # Displays the last screen drawn.
    pygame.display.flip()
