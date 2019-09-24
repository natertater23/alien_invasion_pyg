import sys
import pygame
from laser import Laser


# This will handle key presses and exiting the game
def check_events(settings, screen, ship, lasers):
    for event in pygame.event.get():
        # Exit's Game
        if event.type == pygame.QUIT:
            sys.exit()
        # When key is pressed right and left arrow key respond and space bar shoots lasers
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.key == pygame.K_SPACE:
                if len(lasers) < settings.lasers_allowed:
                    new_laser = Laser(settings, screen, ship)
                    lasers.add(new_laser)
        # Makes sure we stop moving when key is not pressed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


# Handles the drawing and updates screen
def update_screen(settings, screen, ship, lasers):
    screen.fill(settings.bg_color)
    for laser in lasers.sprites():
        laser.draw_laser()
    ship.blitme()
    pygame.display.flip()


def update_lasers(lasers):
    lasers.update()
    # Remove excess lasers
    for laser in lasers.copy():
        if laser.rect.bottom <= 0:
            lasers.remove(laser)
