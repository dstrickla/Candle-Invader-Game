from pygame import sprite 
from pygame import image 

class Enemy(sprite.Sprite):
    """Class representing the generic functionality of all enemies"""
    def __init__(self, game, _walker=False, _ghost=False):
        """Super enemy constructor"""
        sprite.Sprite.__init__(self) 
        self.game = game 
        self.screen = game.screen 
        self.settings = game.settings 
        self.walker = _walker 
        self.ghost = _ghost 
        self.is_moving_right = False  
        self.is_moving_left = False 
        self.image = image.load(self._get_enemy_img_path())
        self.rect = self.image.get_rect() 
        self.rect.x = self.rect.width // 2 # Start at top left of screen 
        self.rect.y = self.rect.height // 4 

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)        

    def _get_enemy_img_path(self):
        """Returns the correct img path for enemy type selected"""
        if self.ghost: 
            return self.settings.ghost_img_path 
        else: #self.walker
            return self.settings.walker_img_path

class Ghost(Enemy):
    """Class representing a flying Enemy"""
    def __init__(self, game, row_num, col_num):
        """Flying Enemy Constructor"""
        super().__init__(game, _ghost=True)
        self.horizontal_speed = self.settings.ghost_horizontal_speed
        self.is_moving_right = True  
        self.is_moving_left = False  
        self.row_num = row_num  
        self.col_num = col_num 

    def check_edge(self):
        screen_rect = self.screen.get_rect() 
        if self.rect.right >= screen_rect.right or self.rect.left <= 0: 
            return True 
        return False

    def switch_moving_direction(self):
        """Switches ghost moving direction"""
        if self.is_moving_right:
            self.is_moving_right = False 
            self.is_moving_left = True 
        else: 
            self.is_moving_left = False 
            self.is_moving_right = True

    def _update_horizontal_position_even_row(self):
        """Updates the horizontal position of ghosts in an even row"""
        if self.is_moving_right: 
            self.x += self.settings.ghost_horizontal_speed 
        elif self.is_moving_left:
            self.x -= self.settings.ghost_horizontal_speed 
        self.rect.x = self.x 

    def _update_horizontal_position_odd_row(self):
        """Updates the horizontal position of ghosts in an odd row"""
        if self.is_moving_right: 
            self.x += self.settings.ghost_horizontal_speed 
        elif self.is_moving_left:
            self.x -= self.settings.ghost_horizontal_speed 
        self.rect.x = self.x 

    def _update_horizontal_position(self):
        """Updates ghost horizontal position"""
        if self.row_num % 2 == 0: 
            self._update_horizontal_position_even_row() 
        else: 
            self._update_horizontal_position_odd_row()

    def update(self):
        """Updates the position of the ghost object"""
        self._update_horizontal_position()


class Walker(Enemy):
    """Class representing a walking Enemy"""
    def __init__(self, game):
        """Walking Enemy Constructor"""
        super().__init__(game, _walker=True)
        self.horizontal_speed = self.settings.walker_horizontal_speed 


class GhostSwarmGroup(sprite.Group):
    """Class representing a swarm of ghosts at the top of the game screen"""

    def __init__(self, game):
        sprite.Group.__init__(self)
        self.game = game 
        self.screen = game.screen 
        self.settings = game.settings 
        self.swarm_horizontal_margin = self.settings.swarm_horizontal_margin
        self.swarm_vertical_margin = self.settings.swarm_vertical_margin
        self.available_horizontal_space = self._get_available_horizontal_space()
        self.available_vertical_space = self._get_available_vertical_space()  
        self.ghosts_per_row = self._get_ghosts_per_row()
        self.rows_of_ghosts = self._get_rows_of_ghosts()
        self._create_flying_swarm()

    def _get_available_horizontal_space(self):
        """Returns the length of the row in which ghosts may be fit"""
        return self.settings.screen_width - self.swarm_horizontal_margin
    
    def _get_available_vertical_space(self):
        """Returns the height of the vertical space in which ghosts may fit"""
        return (self.settings.screen_height //2) - self.settings.player_height
    
    def _get_ghosts_per_row(self): 
        """Returns how many ghosts can fit in a row"""
        spacing = self.settings.ghost_width + self.swarm_horizontal_margin
        return self.available_horizontal_space // (spacing)
    
    def _get_rows_of_ghosts(self):
        """Returns how many rows of ghosts can fit on the screen"""
        return self.available_vertical_space // self.settings.ghost_height 
    
    def _get_ghost_y_start(self, new_ghost): 
        """Returns the new y cord for a ghost based upon row placement"""
        ghost_height = self.settings.ghost_height  
        offset = (self.swarm_vertical_margin + ghost_height) * new_ghost.row_num 
        return self.swarm_vertical_margin + offset 

    def _get_ghost_x_start(self, new_ghost):
        """Returns the x cord for a ghost based on col_num and row_num"""
        ghost_width = self.settings.ghost_width 
        offset = (self.swarm_horizontal_margin + ghost_width) * new_ghost.col_num 
        if new_ghost.row_num % 2 == 0: 
            return self.swarm_horizontal_margin + offset 
        else: 
            offset += ghost_width + self.settings.swarm_horizontal_margin
            return self.settings.screen_width - offset 

    def _create_and_add_ghost(self, row_num, col_num): 
        """Creates a ghost with position in row according to col_num"""
        new_ghost = Ghost(self.game, row_num, col_num)
        new_ghost.x = self._get_ghost_x_start(new_ghost)
        new_ghost.rect.x = new_ghost.x 
        new_ghost.y = self._get_ghost_y_start(new_ghost)
        new_ghost.rect.y = new_ghost.y
        self.add(new_ghost)
        
    def _create_flying_swarm(self): 
        """Generates and add the swarm of ghosts at the top of the screen """
        for row_num in range(self.rows_of_ghosts):
            for col_num in range(self.ghosts_per_row): 
                self._create_and_add_ghost(row_num, col_num)

    def _change_ghost_list_direction(self, ghosts):
        """Changes the directions of all ghosts in the list"""
        for ghost in ghosts: 
            ghost.switch_moving_direction()

    def _check_even_ghost_row_edges(self):
        """Checks if even ghost rows must change direction"""
        ghosts = [ghost for ghost in self.sprites() if ghost.row_num % 2 == 0]
        for ghost in ghosts: 
            if ghost.check_edge():
                self._change_ghost_list_direction(ghosts)
                break

    def _check_odd_ghost_row_edges(self):
        """Checks if odd ghost rows must change direction"""
        ghosts = [ghost for ghost in self.sprites() if ghost.row_num % 2 != 0]
        for ghost in ghosts: 
            if ghost.check_edge():
                self._change_ghost_list_direction(ghosts)
                break

    def check_swarm_direction_change(self):
        """Checks if swarm row needs to change direction"""
        self._check_even_ghost_row_edges() 
        self._check_odd_ghost_row_edges() 

