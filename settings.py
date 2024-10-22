class Settings:
    """Class storage for game settings"""

    def __init__(self):
        """Game Setting initializer"""

        # Screen Settings
        self.screen_origin = 0
        self.screen_width = 672
        self.screen_height = 864
        
        # Background Settings
        self.background_path = r'assets\background_placeholder.bmp'
        self.background_cord = [0,0]

        # Player Settings
        self.player_path = r'assets\player_placeholder.bmp'
        self.p_horiz_speed = 10

        # Block Settings 
        self.block_path = r'assets\block_placeholder.bmp'
        self.block_dim = 96
