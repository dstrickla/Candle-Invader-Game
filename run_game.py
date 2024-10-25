import sys
import pygame

from settings import Settings
from background import Background
from player import Player
from floor import Floor
from enemy import Ghost 
from enemy import Walker 

class CandleInvader:
    """Game Asset Management Class"""
     
    def __init__(self):
        """Game Constructor"""
        pygame.init()
        pygame.display.set_caption("Candle Invader")

        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        
        self.background = Background(self)
        self.player = Player(self)
        self.floor_group = Floor(self, self.settings.floor_x_start, 
                                 self.settings.floor_x_finish, 
                                 self.settings.floor_y_height)

    def _check_keydown_events(self, event):
        """Checks and handles pygame.KEYDOWN game events"""
        if event.key == pygame.K_w:
            self.player.set_look_direction_up()
        elif event.key == pygame.K_a:
            self.player.is_moving_left = True 
            self.player.set_look_direction_left()
        elif event.key == pygame.K_s: 
            self.player.set_look_direction_down()
        elif event.key == pygame.K_d:
            self.player.is_moving_right = True 
            self.player.set_look_direction_right()
        elif event.key == pygame.K_SPACE:
            self.player.is_jumping = True
            self.player.set_look_direction_up()
        elif event.key == pygame.K_LSHIFT:
            self.player.shoot_fireball()
    
    def _check_keyup_events(self, event):
        """Checks and handles pygame.KEYUP game events"""
        if event.key == pygame.K_d:
            self.player.is_moving_right = False 
        elif event.key == pygame.K_a:
            self.player.is_moving_left = False

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
        self.floor_group.draw(self.screen)
        for fireball in self.player.fireball_group:
            fireball.blit_fireball()

        pygame.display.update()

    def run_game(self):
        """Main Loop Game Logic"""
        while True: 
            self.clock.tick(60)
            self._check_events()
            self.player.update()
            self.player.fireball_group.update()
            self.player.fireball_group.clear_offscreen_fireballs()
            self._update_screen()

if __name__ == '__main__':
    game = CandleInvader()
    game.run_game()