import pygame
from pygame.sprite import Sprite


class Laser(Sprite):

    def __init__(self, settings, screen, ship):
        super(Laser, self).__init__()
        self.screen = screen
        # Create laser and set it to the top of the ship
        self.rect = pygame.Rect(0, 0, settings.laser_width, settings.laser_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = settings.laser_color
        self.speed_factor = settings.laser_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_laser(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
