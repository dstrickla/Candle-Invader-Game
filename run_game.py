import sys
import pygame

from settings import Settings
from background import Background
from player import Player
from floor import Floor
from enemy import GhostSwarmGroup

class CandleInvader:
    """Game Asset Management Class"""
     
    def __init__(self):
        """Game Constructor"""
        pygame.init()
        pygame.display.set_caption("Candle Invader")

        self.settings = Settings() 
        self.mouse = pygame.mouse 
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((
            self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
        
        self.background = Background(self)
        self.player = Player(self)
        self.enemy_group = GhostSwarmGroup(self)
        self.floor_group = Floor(self, self.settings.FLOOR_X_START, 
                                 self.settings.FLOOR_X_FINISH, 
                                 self.settings.FLOOR_Y_HEIGHT)

    def _check_keydown_events(self, event):
        """Checks and handles pygame.KEYDOWN game events"""
        if event.key == pygame.K_a:
            self.player.is_moving_left = True 
        elif event.key == pygame.K_d:
            self.player.is_moving_right = True 
        elif event.key == pygame.K_SPACE:
            self.player.is_jumping = True
    
    def _check_keyup_events(self, event):
        """Checks and handles pygame.KEYUP game events"""
        if event.key == pygame.K_d:
            self.player.is_moving_right = False 
        elif event.key == pygame.K_a:
            self.player.is_moving_left = False

    def _check_mouse_events(self, event):
        """Checks and handles pygame mouse related events"""
        if event.button == 1: 
            self.player.shoot_fireball()

    def _check_events(self):
        """Checks and responds to any new game events"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.constants.MOUSEBUTTONDOWN: 
                self._check_mouse_events(event) 
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def _update_screen(self):
        """Update the main game screen display"""
        self.background.blit_background()
        self.player.blit_player()
        self.floor_group.draw(self.screen)
        self.player.fireball_group.draw(self.screen)
        self.enemy_group.draw(self.screen)

        pygame.display.update()

    def run_game(self):
        """Main Loop Game Logic"""
        while True: 
            self.clock.tick(60)
            self._check_events()
            self.player.update()
            self.player.fireball_group.update()
            self.player.fireball_group.clear_offscreen_fireballs()
            self.enemy_group.remove_shot_ghosts(self.player.fireball_group)
            self.enemy_group.update()
            self.enemy_group.check_swarm_direction_change()
            self._update_screen()

if __name__ == '__main__':
    game = CandleInvader()
    game.run_game() 