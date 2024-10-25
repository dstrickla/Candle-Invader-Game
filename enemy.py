from pygame import sprite 
from pygame import image 

class Enemy(sprite.Sprite):
    """Class representing the generic functionality of all enemies"""
    def __init__(self, game, _walker=True, _ghost=True):
        """Super enemy constructor"""
        sprite.Sprite.__init__() 
        self.game = game 
        self.screen = game.screen 
        self.settings = game.settings 
        self.walker = _walker 
        self.ghost = _ghost 
        self.horizontal_speed = self._get_enemy_horizontal_speed()
        self.image = image.load(self._get_enemy_img_path())
        self.rect = self.image.get_rect() 
        self.rect.x = self.rect.width # Start at top left of screen 
        self.rect.y = self.rect.height 

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)        

    def _get_enemy_horizontal_speed(self):
        """Returns the correct horizontal speed for selected enemy type"""
        if self.ghost: 
            return self.settings.ghost_horizontal_speed
        else: # self.walker 
            return self.settings.walker_horizontal_speed

    def _get_enemy_img_path(self):
        """Returns the correct img path for enemy type selected"""
        if self.ghost: 
            return self.settings.ghost_img_path 
        else: #self.walker
            return self.settings.walker_img_path

class Ghost(Enemy):
    """Class representing a flying Enemy"""
    def __init__(self, game):
        """Flying Enemy Constructor"""
        Enemy().__init__(game, _ghost=True)


class Walker(Enemy):
    """Class representing a walking Enemy"""
    def __init__(self, game):
        """Walking Enemy Constructor"""
        Enemy().__init__(game, _walker=True)
