import sys
import pygame


# This will handle key presses and exiting the game
def check_events(ship):
    for event in pygame.event.get():
        # Exit's Game
        if event.type == pygame.QUIT:
            sys.exit()
        # When key is pressed right and left arrow key respond
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx += 1
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        # Makes sure we stop moving when key is not pressed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


# Handles the drawing and updates screen
def update_screen(settings, screen, ship):
    screen.fill(settings.bg_color)
    ship.blitme()
    pygame.display.flip()
