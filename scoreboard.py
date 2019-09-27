import pygame.ftfont


class Scoreboard:

    def __init__(self, settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        self.txt_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_imgae = self.font.render(score_str, True, self.txt_color, self.settings.bg_color)

        self.score_rect = self.score_imgae.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20