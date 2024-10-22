from pygame import image

class Player:
    """Class representing the playable character 'Phil'"""

    def __init__(self, game, image_path):
        self.screen = game.screen # Game 
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        self.image = image.load(image_path) # Image and rect
        self.rect = self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.center

        self.moving_right = False # Horizontal Movement
        self.moving_left = False 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.is_jumping = False # Vertical Movement (Jumping)
        self.jump_count = 12 

    def jump(self):
        """Handles the logic of a player jump event"""
        if self.jump_count >= -12: 
            self.y -= (self.jump_count * abs(self.jump_count)) * 0.3
            self.jump_count -= 1
        else: 
            self.jump_count = 12
            self.is_jumping = False

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