from pygame import sprite 
from pygame import image 

class Fireball(sprite.Sprite):
    """Class representing player fireball attack"""

    def __init__(self, game, 
                 is_shot_left=False, 
                 is_shot_right=False, 
                 is_shot_up=False,
                 is_shot_down=False):
        
        sprite.Sprite.__init__(self) 
        # Game Attributes
        self.game = game
        self.screen = game.screen 
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings  

        # Fireball direction attributes
        self.is_shot_left = is_shot_left 
        self.is_shot_right = is_shot_right 
        self.is_shot_up = is_shot_up  
        self.is_shot_down = is_shot_down

        # Fireball image and rect attributes
        self.image = image.load(self.settings.fireball_path)
        self.rect = self.image.get_rect() 
        self._set_rect_start() 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)



    def _set_rect_start(self):
        """Sets start position depending based on direction fired"""
        if self.is_shot_left:
            self.rect.midleft = self.game.player.rect.midleft
        elif self.is_shot_right:
            self.rect.midright = self.game.player.rect.midright  
        elif self.is_shot_up:
            self.rect.midtop = self.game.player.rect.midtop 
        else: # self.down_fireball 
            self.rect.midbottom = self.game.player.rect.midbottom

    def update(self):
        """Updates the fireball's position on the screen"""
        if self.is_shot_left:
            self.x -= self.settings.fireball_speed 
        elif self.is_shot_right:
            self.x += self.settings.fireball_speed
        elif self.is_shot_up: 
            self.y -= self.settings.fireball_speed 
        else: #self.down_fireball 
            self.y += self.settings.fireball_speed 

        self.rect.x = self.x 
        self.rect.y = self.y  

    def blit_fireball(self):
        """Draws the fireball to the screen"""
        self.screen.blit(self.image, self.rect)


