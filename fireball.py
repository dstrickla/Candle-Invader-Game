from pygame import sprite 
from pygame import image 

class Fireball(sprite.Sprite):
    """Class representing player fireball attack"""

    def __init__(self, game, 
                 left_fireball=False, 
                 right_fireball=False, 
                 up_fireball=False,
                 down_fireball=False):
        
        sprite.Sprite.__init__(self) #
        self.game = game
        self.screen = game.screen 
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings  

        self.image = image.load(self.settings.fireball_path)
        self.rect = self.image.get_rect() 
        
        self.left_fireball = left_fireball 
        self.right_fireball = right_fireball 
        self.up_fireball = up_fireball  
        self.down_fireball = down_fireball

        self._set_rect_start() 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def _set_rect_start(self):
        """Sets start position depending based on direction fired"""
        if self.left_fireball:
            self.rect.midleft = self.game.player.rect.midleft
        elif self.right_fireball:
            self.rect.midright = self.game.player.rect.midright  
        elif self.up_fireball:
            self.rect.midtop = self.game.player.rect.midtop 
        else: # self.down_fireball 
            self.rect.midbottom = self.game.player.rect.midbottom

    def update(self):
        """Updates the fireball's position on the screen"""
        if self.left_fireball:
            self.x -= self.settings.fireball_speed 
        elif self.right_fireball:
            self.x += self.settings.fireball_speed
        elif self.up_fireball: 
            self.y -= self.settings.fireball_speed 
        else: #self.down_fireball 
            self.y += self.settings.fireball_speed 

        self.rect.x = self.x 
        self.rect.y = self.y  

    def blit_fireball(self):
        """Draws the fireball to the screen"""
        self.screen.blit(self.image, self.rect)


