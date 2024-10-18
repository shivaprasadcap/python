import pygame

class Wizard:

    def __init__(self, rc_game):
        self.screen = rc_game.screen
        self.image = pygame.image.load("images\wizard.bmp")

        #get screen rect
        self.screen_rect = rc_game.screen.get_rect()

        #get image rect
        self.rect = self.image.get_rect()

        #put image rect to middbottom of screen_rect midbottom
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)