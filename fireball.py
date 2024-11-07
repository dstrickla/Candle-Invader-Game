from pygame import sprite 
from pygame import image 
from settings import Direction
from math import atan2 
from math import cos 
from math import sin 

class Fireball(sprite.Sprite):
    """Class representing player fireball attack"""

    def __init__(self, game):
        sprite.Sprite.__init__(self) 
        # Game Attributes
        self.game = game
        self.screen = game.screen 
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings  
        self.mouse_position = game.mouse.get_pos() 

        # Fireball image and rect attributes
        self.image = image.load(self.settings.FIREBALL_IMG_PATH)
        self.rect = self.image.get_rect() 
        self.starting_position = game.player.rect.midtop 
        self.rect.midtop = self.starting_position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Get fireball path angle and speed 
        self.angle = self._get_fireball_angle()
        self.speed_x = self._get_x_speed()
        self.speed_y = self._get_y_speed() 

    def _get_fireball_angle(self): 
        """Returns the arc tangent angle of rise and run"""
        x1, y1 = self.starting_position 
        x2, y2 = self.mouse_position 
        return atan2((y2-y1), (x2-x1))

    def _get_x_speed(self):
        """Returns the cosine of slope angle"""
        return self.settings.FIREBALL_SPEED * cos(self.angle) 
    
    def _get_y_speed(self):
        """Returns the sine of slope angle"""
        return self.settings.FIREBALL_SPEED * sin(self.angle)

    def update(self):
        """Updates the fireball's position on the screen"""
        self.x += self.speed_x 
        self.y += self.speed_y
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
        self.left_screen_bound = self.settings.SCREEN_ORIGIN  
        self.right_screen_bound = self.settings.SCREEN_WIDTH 
        self.upper_screen_bound = self.settings.SCREEN_ORIGIN
        self.lower_screen_bound = self.settings.SCREEN_HEIGHT 


    def clear_offscreen_fireballs(self):
        """Removes any fireballs that have left the game screen window"""
        for fireball in self:
            if (fireball.rect.bottom <= self.upper_screen_bound or \
                fireball.rect.top >= self.lower_screen_bound or \
                fireball.rect.right <= self.left_screen_bound or \
                fireball.rect.left >= self.right_screen_bound):
                self.remove(fireball)

    

    

