from pygame import sprite
from pygame import image

class Background(sprite.Sprite):
    def __init__(self, game):
        sprite.Sprite.__init__(self)
        self.game = game 
        self.screen = game.screen 
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings 

        self.image = image.load(self.settings.background_img_path)
        self.rect = self.image.get_rect()
        self.rect.left = self.settings.background_x_start 
        self.rect.top = self.settings.background_y_start 

    def blit_background(self):
        self.screen.blit(self.image, self.rect)
