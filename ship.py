import pygame


class Ship:

    def __int__(self, screen):

        self.screen = screen

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
