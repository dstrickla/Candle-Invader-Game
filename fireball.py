from pygame import sprite 
from pygame import image 
from settings import Direction

class Fireball(sprite.Sprite):
    """Class representing player fireball attack"""

    def __init__(self, game, player):
        sprite.Sprite.__init__(self) 
        # Game Attributes
        self.game = game
        self.screen = game.screen 
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings  

        # Fireball direction attribute
        self.shot_direction = player.look_direction

        # Fireball image and rect attributes
        self.image = image.load(self.settings.fireball_path)
        self.rect = self.image.get_rect() 
        self._set_rect_start() 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def _set_rect_start(self):
        """Sets start position based on direction fired in"""
        match(self.shot_direction):
            case Direction.LEFT.value: 
                 self.rect.midleft = self.game.player.rect.midleft
            case Direction.RIGHT.value: 
                self.rect.midright = self.game.player.rect.midright 
            case Direction.UP.value: 
                self.rect.midtop = self.game.player.rect.midtop 
            case Direction.DOWN.value: 
                self.rect.midbottom = self.game.player.rect.midbottom

    def update(self):
        """Updates the fireball's position on the screen"""
        match(self.shot_direction):
            case Direction.LEFT.value: 
                self.x -= self.settings.fireball_speed 
            case Direction.RIGHT.value: 
                self.x += self.settings.fireball_speed 
            case Direction.UP.value: 
                self.y -= self.settings.fireball_speed 
            case Direction.DOWN.value: 
                self.y += self.settings.fireball_speed 

        self.rect.x = self.x 
        self.rect.y = self.y  

    def blit_fireball(self):
        """Draws the fireball to the screen"""
        self.screen.blit(self.image, self.rect)


class FireballGroup(sprite.Group):
    """Class representing a group of active fireball sprites"""

    def __init__(self, game):
        sprite.Group.__init__(self) 

        self.game = game 
        self.screen = game.screen 
        self.settings = game.settings 
        self.left_screen_bound = self.settings.screen_origin  
        self.right_screen_bound = self.settings.screen_width 
        self.upper_screen_bound = self.settings.screen_origin
        self.lower_screen_bound = self.settings.screen_height 


    def clear_offscreen_fireballs(self):
        """Removes any fireballs that have left the game screen window"""
        for fireball in self:
            if (fireball.rect.bottom <= self.upper_screen_bound or \
                fireball.rect.top >= self.lower_screen_bound or \
                fireball.rect.right <= self.left_screen_bound or \
                fireball.rect.left >= self.right_screen_bound):
                self.remove(fireball)

    

    

