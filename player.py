from pygame import image

from fireball import Fireball 
from fireball import FireballGroup
from settings import Direction

class Player:
    """Class representing the playable character 'Phil'"""

    def __init__(self, game):
        # Game attributes
        self.game = game
        self.screen = game.screen 
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        # Player image and rect attributes
        self.image = image.load(game.settings.PLAYER_IMG_PATH)
        self.rect = self.image.get_rect()
        self.rect.center = (self.settings.PLAYER_X_START,
                            self.settings.PLAYER_Y_START)

        # Player Motion attributes
        self.is_moving_right = False 
        self.is_moving_left = False 
        self.is_jumping = False 
        self.jump_count = self.settings.PLAYER_JUMP_COUNT
        self.jump_modifier = self.settings.PLAYER_JUMP_MODIFIER
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Player Fireball Group 
        self.fireball_group = FireballGroup(game)

    def jump(self):
        """Handles the logic of a player jump event"""
        if self.jump_count >= -12: 
            self.y -= (self.jump_count * abs(self.jump_count)) * self.jump_modifier
            self.jump_count -= 1
        else: 
            self.jump_count = 12
            self.is_jumping = False

    def shoot_fireball(self,):
        """Adds a new fireball to the players group"""
        new_fireball = Fireball(self.game)
        self.fireball_group.add(new_fireball)

    def update(self):
        """Updates the player's rect position on game screen"""
        right_bound = self.settings.SCREEN_WIDTH 
        left_bound = self.settings.SCREEN_ORIGIN
        if self.is_moving_right and self.rect.right < right_bound:
            self.x += self.settings.PLAYER_HORIZONTAL_SPEED
        if self.is_moving_left and self.rect.left > left_bound:
            self.x -= self.settings.PLAYER_HORIZONTAL_SPEED
        if self.is_jumping: 
            self.jump()

        self.rect.y = self.y
        self.rect.x = self.x

    def blit_player(self):
        """Blits the player onto the game screen"""
        self.screen.blit(self.image, self.rect)