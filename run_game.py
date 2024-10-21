import sys
import pygame

from settings import Settings
from background import Background
from player import Player

class CandleInvader:
    """Game Asset Management Class"""
     
    def __init__(self):
        """Game Constructor"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Candle Invader")

        self.background = Background(self, 
                                     self.settings.background_path,
                                     self.settings.background_cord)
        self.player = Player(self, self.settings.player_path)

    def run_game(self):
        """Main Loop Game Logic"""
        while True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.background.blit_background()
            self.player.blit_player()

            pygame.display.flip()

if __name__ == '__main__':
    game = CandleInvader()
    game.run_game()