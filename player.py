from pygame import image

class Player:
    """Class representing the playable character 'Phil'"""

    def __init__(self, game, image_path):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = image.load(image_path)
        self.rect = self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blit_player(self):
        """Blits the player onto the game screen"""
        self.screen.blit(self.image, self.rect)