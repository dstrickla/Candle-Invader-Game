from pygame import sprite 
from pygame import image 

class Fireball(sprite.Sprite):
    """Class representing player fireball attack"""

    def __init__(self, game, 
                 moving_left=False, 
                 moving_right=False, 
                 moving_up=False):
        
        sprite.Sprite.__init__(self) #
        self.game = game
        self.screen = game.screen 
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings  

        self.image = image.load(self.settings.fireball_path)
        self.rect = self.image.get_rect() 
        
        self.moving_left = moving_left 
        self.moving_right = moving_right 
        self.moving_up = moving_up  
        self.set_rect_start() 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def set_rect_start(self):
        """Sets start position depending on direction fired"""
        if self.moving_left:
            self.rect.midright = self.game.player.rect.midright
        elif self.moving_right:
            self.rect.midleft = self.game.player.rect.midleft  
        elif self.moving_up:
            self.rect.midtop = self.game.player.rect.midtop 

    def update(self):
        """Updates the fireball's position on the screen"""
        if self.moving_left:
            self.x -= self.settings.fireball_speed 
        elif self.moving_right:
            self.x += self.settings.fireball_speed 
        else: #self.moving_up 
            self.y -= self.settings.fireball_speed 

        self.rect.x = self.x 
        self.rect.y = self.y  

    def blit_fireball(self):
        """Draws the fireball to the screen"""
        self.screen.blit(self.image, self.rect)


