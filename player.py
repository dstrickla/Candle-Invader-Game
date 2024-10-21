from pygame import image

class Player:
    """Class representing the playable character 'Phil'"""

    def __init__(self, game, image_path):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        self.image = image.load(image_path)
        self.rect = self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Updates the player's rect position on game screen"""
        if self.moving_right and (self.x + self.rect.width) < self.settings.screen_width:
            self.x += self.settings.p_horiz_speed
        elif self.moving_left and self.x > self.settings.screen_origin:
            self.x -= self.settings.p_horiz_speed

        self.rect.x = self.x

    def blit_player(self):
        """Blits the player onto the game screen"""
        self.screen.blit(self.image, self.rect)