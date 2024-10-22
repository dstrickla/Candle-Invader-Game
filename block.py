from pygame import sprite 
from pygame import image

class Block(sprite.Sprite):
    """Class representing a block element tile"""

    def __init__(self, game, location=(0,0)):
        """Block Constructor"""
        self.screen = game.screen 
        self.screen_rect = game.screen.get_rect() 
        self.settings = game.settings 

        sprite.Sprite.__init__(self)
        self.image = image.load(self.settings.block_path)
        self.rect = self.image.get_rect() 
        self.rect.center = location 

    def blit_block(self):
        """Blits the block instance to the screen"""
        self.screen.blit(self.image, self.rect)

