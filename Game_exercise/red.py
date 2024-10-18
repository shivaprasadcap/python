import pygame
from settings import Settings
from wizard import Wizard
import sys

class Red:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Red Chronicals")

        self.wizard = Wizard(self)

    def run_game(self):
        while True:
            self._check_event()
            self._update_screen()
            self.clock.tick(60)

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.wizard.blitme()

        pygame.display.flip()       

if __name__ == '__main__':
    rc = Red()
    rc.run_game()


