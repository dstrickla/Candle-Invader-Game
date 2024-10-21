from pygame import sprite
from pygame import image

class Background(sprite.Sprite):
    def __init__(self, game, image_file, location):
        sprite.Sprite.__init__(self)

        self.screen = game.screen 
        self.screen_rect = game.screen.get_rect()

        self.image = image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location 

    def blit_background(self):
        self.screen.blit(self.image, self.rect)
