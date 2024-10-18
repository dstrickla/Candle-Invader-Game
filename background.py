from pygame import sprite

class Background(sprite.sprite)
    def __init__(self, image_file, location):
        sprite.sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location 