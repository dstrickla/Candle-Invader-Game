import sys
import pygame

from settings import Settings

class CandleInvader:
    """Game Asset Management Class"""
     
    def __init__(self):
        """Game Constructor"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Candle Invader")

    def run_game(self):
        """Main Loop Game Logic"""
        while True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()

if __name__ == '__main__':
    game = CandleInvader()
    game.run_game()