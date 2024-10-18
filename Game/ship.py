import pygame

class Ship:
    """A class to manage Ship"""

    def __init__(self, ai_game):
        """Initializing Ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load Ship image and get its rect
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()

        #Start each Ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a float foer the ship's exat horizontal position
        self.x = float(self.rect.x)

        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Update rect object from self.x
        self.rect.x = self.x


    def blitme(self):
        """Draw the Ship at it's current location. The Pygame blit() method is one of the methods to place an image onto the screens of pygame applications. It intends to put an image on the screen. It just copies the pixels of an image from one surface to another surface just like that"""
        self.screen.blit(self.image, self.rect)