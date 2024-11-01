from enum import Enum 
class Settings:
    """Class storage for game settings"""

    def __init__(self):
        """Game Setting initializer"""

        # Screen Settings
        self.screen_origin = 0
        self.screen_width = 672
        self.screen_height = 864
        
        # Background Settings
        self.background_img_path= r'assets\background_placeholder.bmp'
        self.background_x_start = 0
        self.background_y_start = 0 

        # Player Settings
        self.player_img_path = r'assets\player_placeholder.bmp'
        self.player_horizontal_speed = 10
        self.player_jump_count = 12
        self.player_jump_modifier = 0.3
        self.player_height = 96
        self.player_width = 96 
        self.player_x_start = self.screen_width / 2
        self.player_y_start = self.screen_height - (self.player_height * 1.5)

        # Player Fireball Settings
        self.fireball_speed = 20 
        self.fireball_path = r'assets\fireball_placeholder.bmp'

        # Generic Enemy Settings 

        # Flying Enemy Settings (Ghost)
        self.ghost_img_path = r'assets\ghost_placeholder.bmp'      
        self.ghost_horizontal_speed = 10 
        self.ghost_width = 96 
        self.ghost_height = 96

        # Ghost Swarm Settings
        self.swarm_horizontal_margin = self.ghost_width // 4 
        self.swarm_vertical_margin = self.ghost_height // 4

        # Walking Enemy Settings (Walker)
        self.walker_img_path = r'assets\walker_placeholder.bmp'
        self.walker_horizontal_speed = 10 

        # Block Settings 
        self.block_path = r'assets\block_placeholder.bmp'
        self.block_dim = 96

        # Floor Settings 
        self.floor_x_start = int(self.block_dim/2)
        self.floor_x_finish = self.screen_width + 1
        self.floor_y_height = self.screen_height - int(self.block_dim/2)

class Direction(Enum): 
    UP = 0 
    RIGHT = 1 
    DOWN = 2 
    LEFT = 3 
