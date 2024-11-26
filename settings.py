from enum import Enum 
from pygame import image 
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
        self.PLAYER_IMG = image.load(self.PLAYER_IMG_PATH)
        self.PLAYER_INITIAL_LIVES = 1
        self.PLAYER_WIDTH = self.PLAYER_IMG.get_width()  
        self.PLAYER_HEIGHT = self.PLAYER_IMG.get_height() 
        self.PLAYER_X_START = self.SCREEN_WIDTH / 2
        self.PLAYER_Y_START = self.SCREEN_HEIGHT - (self.PLAYER_HEIGHT * 1.5)
        self.PLAYER_HORIZONTAL_SPEED = 10
        self.PLAYER_JUMP_COUNT = 12
        self.PLAYER_JUMP_MODIFIER = 0.3
        

        # Player Fireball Settings
        self.FIREBALL_IMG_PATH = r'assets\fireball_placeholder.bmp'
        self.FIREBALL_IMG = image.load(self.FIREBALL_IMG_PATH)
        self.FIREBALL_WIDTH = self.FIREBALL_IMG.get_width()
        self.FIREBALL_HEIGHT = self.FIREBALL_IMG.get_height() 
        self.FIREBALL_SPEED = 25 

        # Generic Enemy Settings 

        # Flying Enemy Settings (Ghost)
        self.GHOST_IMG_PATH = r'assets\ghost_placeholder.bmp' 
        self.GHOST_IMG = image.load(self.GHOST_IMG_PATH)     
        self.GHOST_WIDTH = self.GHOST_IMG.get_width() 
        self.GHOST_HEIGHT = self.GHOST_IMG.get_height() 
        self.GHOST_HORIZONTAL_SPEED = 1.5 

        # Ghost Swarm Settings
        self.SWARM_HORIZONTAL_MARGIN = self.GHOST_WIDTH // 4 
        self.SWARM_VERTICAL_MARGIN = self.GHOST_HEIGHT // 8
        self.SWARM_VERTICAL_DROP_SPEED = 10
        self.SWARM_VERTICAL_MS_DROP_TIME = 500

        # Walking Enemy Settings (Walker)
        self.WALKER_IMG_PATH = r'assets\walker_placeholder.bmp'
        self.WALKER_IMG = image.load(self.WALKER_IMG_PATH)
        self.WALKER_WIDTH = self.WALKER_IMG.get_width() 
        self.WALKER_HEIGHT = self.WALKER_IMG.get_height() 
        self.WALKER_HORIZONTAL_SPEED = 10 

        # Block Settings 
        self.BLOCK_IMG_PATH = r'assets\block_placeholder.bmp'
        self.BLOCK_IMG = image.load(self.BLOCK_IMG_PATH)
        self.BLOCK_WIDTH = self.BLOCK_IMG.get_width() 
        self.BLOCK_HEIGHT = self.BLOCK_IMG.get_height() 

        # Floor Settings 
        self.FLOOR_X_START = int(self.BLOCK_WIDTH/2)
        self.FLOOR_X_FINISH = self.SCREEN_WIDTH + 1
        self.FLOOR_Y_HEIGHT = self.SCREEN_HEIGHT - int(self.BLOCK_HEIGHT/2)

class Direction(Enum): 
    UP = 0 
    RIGHT = 1 
    DOWN = 2 
    LEFT = 3 
