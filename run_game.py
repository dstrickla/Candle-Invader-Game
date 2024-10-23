import sys
import pygame

from settings import Settings
from background import Background
from player import Player
from block import Block 
from fireball import Fireball

class CandleInvader:
    """Game Asset Management Class"""
     
    def __init__(self):
        """Game Constructor"""
        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Candle Invader")

        self.background = Background(self, 
                                     self.settings.background_path,
                                     self.settings.background_cord)
        self.player = Player(self, self.settings.player_path)
        self.floor = self.get_floor_group()

        

        self.left_fireball = Fireball(self, moving_left=True)
        self.right_fireball = Fireball(self, moving_right=True)
        self.up_fireball = Fireball(self, moving_up=True)

    def get_floor_group(self):
        floor = pygame.sprite.Group() 
        y = self.settings.screen_height - (abs(self.settings.block_dim/2))
        locations = [(x, y) for x in range(48, self.settings.screen_width+1, 96)]

        for location in locations:
            floor.add(Block(self, location))

        return floor

    def _check_keydown_events(self, event):
        """Checks and handles pygame.KEYDOWN game events"""
        if event.key == pygame.K_d:
            self.player.moving_right = True 
        elif event.key == pygame.K_a:
            self.player.moving_left = True 
        elif event.key == pygame.K_SPACE:
            self.player.is_jumping = True 
    
    def _check_keyup_events(self, event):
        """Checks and handles pygame.KEYUP game events"""
        if event.key == pygame.K_d:
            self.player.moving_right = False 
        elif event.key == pygame.K_a:
            self.player.moving_left = False

    def _check_events(self):
        """Checks and responds to any new game events"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def _update_screen(self):
        """Update the main game screen display"""
        self.background.blit_background()
        self.player.blit_player()
        self.floor.draw(self.screen)

        self.up_fireball.blit_fireball()
        self.right_fireball.blit_fireball()
        self.left_fireball.blit_fireball()

        pygame.display.update()

    def run_game(self):
        """Main Loop Game Logic"""
        while True: 
            self.clock.tick(60)
            self._check_events()
            self.player.update()

            self.up_fireball.update()
            self.left_fireball.update() 
            self.right_fireball.update()

            self._update_screen()

if __name__ == '__main__':
    game = CandleInvader()
    game.run_game()