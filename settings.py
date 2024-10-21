class Settings:
    """Class storage for game settings"""

    def __init__(self):
        """Game Setting initializer"""

        # Screen Settings
        self.screen_width = 600
        self.screen_height = 800
        
        # Background Settings
        self.background_path = r'assets\background_placeholder.png'
        self.background_cord = [0,0]