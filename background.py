from pygame import sprite
from pygame import image

class Background(sprite.Sprite):
    def __init__(self, image_file, location):
        sprite.Sprite.__init__(self)
        self.image = image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location 