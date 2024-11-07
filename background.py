from pygame import sprite
from pygame import image

class Background(sprite.Sprite):
    def __init__(self, game):
        sprite.Sprite.__init__(self)
        self.game = game 
        self.screen = game.screen 
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings 

        self.image = image.load(self.settings.BACKGROUND_IMG_PATH)
        self.rect = self.image.get_rect()
        self.rect.left = self.settings.BACKGROUND_X_START 
        self.rect.top = self.settings.BACKGROUND_Y_START 

    def blit_background(self):
        self.screen.blit(self.image, self.rect)
