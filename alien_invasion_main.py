import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def play():
    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(settings, screen)

    while True:

        gf.check_events(ship)
        ship.update()
        gf.update_screen(settings, screen, ship)


play()

