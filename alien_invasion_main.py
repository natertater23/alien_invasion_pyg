import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button


def play():
    pygame.init()
    settings = Settings()
    # Create Window
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    button = Button(settings, screen, "Play")
    stats = GameStats(settings)
    ship = Ship(settings, screen)
    lasers = Group()
    aliens = Group()
    gf.create_aliens(settings, screen, ship, aliens)
    # Game loop
    while True:

        gf.check_user(settings, screen, stats, button, ship, aliens, lasers)

        if stats.game_active:
            ship.update()
            gf.update_lasers(settings, screen, ship, aliens, lasers)
            gf.update_aliens(settings, stats, screen, ship, aliens, lasers)
        gf.update_screen(settings, screen, stats, ship, aliens, lasers, button)


play()
