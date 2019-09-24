import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def play():
    pygame.init()
    settings = Settings()
    # Create Window
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(settings, screen)
    lasers = Group()

    # Game loop
    while True:

        gf.check_events(settings, screen, ship, lasers)
        ship.update()
        lasers.update()

        for laser in lasers.copy():
            if laser.rect.bottom <= 0:
                lasers.remove(laser)
        # print(len(lasers))

        gf.update_screen(settings, screen, ship, lasers)


play()
