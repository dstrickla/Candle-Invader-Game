from pygame import sprite 

class Block(sprite.Sprite):
    """Class representing a block element tile"""

    def __init__(self, game, location=(0,0)):
        """Block Constructor"""
        sprite.Sprite.__init__(self)
        self.screen = game.screen 
        self.screen_rect = game.screen.get_rect() 
        self.settings = game.settings 
        self.image = self.settings.BLOCK_IMG 
        self.rect = self.image.get_rect() 
        self.rect.center = location 

    def blit_block(self):
        """Blits the block instance to the screen"""
        self.screen.blit(self.image, self.rect)


class Floor(sprite.Group):
    """Class representing a floor generated from block sprites"""

    def __init__(self, game, x_start, x_finish, y_height):
        sprite.Group.__init__(self) 
        self.game = game 
        self.game_screen = game.screen.get_rect() 
        self.settings = game.settings 
        self.x_start = x_start 
        self.x_finish = x_finish
        self.y_height = y_height  
        self.block_spacing = self.settings.BLOCK_WIDTH
        self.block_locations = self._get_block_locations()
        self._create_floor_group()

    def _get_block_locations(self):
        """Generates and returns central coordinates of blocks in floor"""
        y = self.y_height 
        x_cords = [x for x in range(self.x_start, self.x_finish, self.block_spacing)]
        return [(x,y) for x in x_cords]

    def _create_floor_group(self):
        """Adds Block sprites to the Floor Sprite Group"""
        new_block = None 
        for location in self.block_locations: 
            new_block = Block(self.game, location=location)
            self.add(new_block)




