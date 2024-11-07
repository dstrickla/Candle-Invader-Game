from enum import Enum 
class Settings:
    """Class storage for game settings"""

    def __init__(self):
        """Game Setting initializer"""

        # Screen Settings
        self.SCREEN_ORIGIN = 0
        self.SCREEN_WIDTH = 672
        self.SCREEN_HEIGHT = 864
        
        # Background Settings
        self.BACKGROUND_IMG_PATH= r'assets\background_placeholder.bmp'
        self.BACKGROUND_X_START = 0
        self.BACKGROUND_Y_START = 0 

        # Player Settings
        self.PLAYER_IMG_PATH = r'assets\player_placeholder.bmp'
        self.PLAYER_HORIZONTAL_SPEED = 10
        self.PLAYER_JUMP_COUNT = 12
        self.PLAYER_JUMP_MODIFIER = 0.3
        self.PLAYER_HEIGHT = 96
        self.PLAYER_WIDTH = 96 
        self.PLAYER_X_START = self.SCREEN_WIDTH / 2
        self.PLAYER_Y_START = self.SCREEN_HEIGHT - (self.PLAYER_HEIGHT * 1.5)

        # Player Fireball Settings
        self.FIREBALL_SPEED = 20 
        self.FIREBALL_IMG_PATH = r'assets\fireball_placeholder.bmp'

        # Generic Enemy Settings 

        # Flying Enemy Settings (Ghost)
        self.GHOST_IMG_PATH = r'assets\ghost_placeholder.bmp'      
        self.GHOST_HORIZONTAL_SPEED = 1.5 
        self.GHOST_WIDTH = 96 
        self.GHOST_HEIGHT = 96

        # Ghost Swarm Settings
        self.SWARM_HORIZONTAL_MARGIN = self.GHOST_WIDTH // 4 
        self.SWARM_VERTICAL_MARGIN = self.GHOST_HEIGHT // 8
        self.SWARM_VERTICAL_DROP_SPEED = 5

        # Walking Enemy Settings (Walker)
        self.WALKER_IMG_PATH = r'assets\walker_placeholder.bmp'
        self.WALKER_HORIZONTAL_SPEED = 10 

        # Block Settings 
        self.BLOCK_PATH = r'assets\block_placeholder.bmp'
        self.BLOCK_DIM = 96

        # Floor Settings 
        self.FLOOR_X_START = int(self.BLOCK_DIM/2)
        self.FLOOR_X_FINISH = self.SCREEN_WIDTH + 1
        self.FLOOR_Y_HEIGHT = self.SCREEN_HEIGHT - int(self.BLOCK_DIM/2)

class Direction(Enum): 
    UP = 0 
    RIGHT = 1 
    DOWN = 2 
    LEFT = 3 
