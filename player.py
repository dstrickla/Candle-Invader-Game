from pygame import image

class Player:
    """Class representing the playable character 'Phil'"""

    def __init__(self, game):
        self.screen = game.screen # Game 
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        self.image = image.load(game.settings.player_path) # Image and rect
        self.rect = self.rect = self.image.get_rect()
        self.x_start = self.screen.get_width()/2 
        self.y_start = self.screen.get_height() - self.settings.block_dim * 1.5
        self.rect.center = (self.x_start, self.y_start)

        self.moving_right = False # Horizontal Movement
        self.moving_left = False 
        self.is_jumping = False # Vertical Movement (Jumping)
        self.jump_count = 12 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.looking_up = False
        self.looking_down = False 
        self.looking_left = False 
        self.looking_right = False

    def jump(self):
        """Handles the logic of a player jump event"""
        if self.jump_count >= -12: 
            self.y -= (self.jump_count * abs(self.jump_count)) * 0.3
            self.jump_count -= 1
        else: 
            self.jump_count = 12
            self.is_jumping = False

    def set_look_direction(self, up=False, down=False, left=False, right=False):
        """Updates the look direction of the player"""
        self.looking_up = up
        self.looking_down = down  
        self.looking_left = left 
        self.looking_right = right        

    def update(self):
        """Updates the player's rect position on game screen"""
        if self.moving_right and self.rect.right + self.settings.p_horiz_speed < self.screen_rect.right:
            self.x += self.settings.p_horiz_speed
        if self.moving_left and self.rect.left - self.settings.p_horiz_speed >= self.settings.screen_origin:
            self.x -= self.settings.p_horiz_speed
        if self.is_jumping: 
            self.jump()

        self.rect.y = self.y
        self.rect.x = self.x

    def blit_player(self):
        """Blits the player onto the game screen"""
        self.screen.blit(self.image, self.rect)