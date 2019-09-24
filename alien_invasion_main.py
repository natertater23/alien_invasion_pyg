import pygame
from settings import Settings
from ship import Ship


def play():
    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    game_loop = True
    while game_loop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False

        ship.blitme()
        screen.fill(settings.bg_color)
        pygame.display.flip()


play()
pygame.quit()
