from os import path


class Settings():
    '''Game Settings Class'''

    def __init__(self):
        '''Define parameters of the game'''

        # Screen Parameters
        self.screen_width = 1200    # The Width of the Screen (pixel)
        self.screen_height = 800    # The Height of the Screen (pixel)
        self.screen_caption = "Alien Invasion (By VincentCHEN)" # The Caption of the Screen
        self.screen_bg_color = (230, 230, 230)  # The Background Color of the Screen (RGB)

        # Ship Parameters
        self.ship_image = 'images/ship.bmp' # The Image Resource of the Ship
        self.ship_speed_factor = 2  # The Moving Speed Factor of the Ship
        self.ship_quantity = 3  # The Quantity of the Ship can be Used in the Game

        # Bullet Parameters
        self.bullet_width = 5   # The Width of the Bullet
        self.bullet_height = 20 # The Height of the Bullet
        self.bullet_color = (255, 0, 0) # The Color of the Bullet
        self.bullet_speed_factor = 3    # The Moving Speed Factor of the Bullet
        self.bullet_max_quantity = 10   # The Max Quantity of the Bullets on the Screen at the Same Time

        # Alien Parameters
        self.alien_image = 'images/alien.bmp'   # The Image Resource of the Alien
        self.alien_horizontal_speed_factor = 1  # The Horizontal Moving Speed Factor of the Alien
        self.alien_vertical_speed_factor = 1    # The Vertical Moving Speed Factor of the Alien
        self.alien_score = 10   # The Score of an Alien

        # Game Speedup Parameters
        self.game_speedup = 1.5 # The Speedup of the Game Pace
        self.local_file_position = r"D:\alien_invasion.txt" # The Position of the File to Store the Highest Score of the Game
        # self.local_file_position = path.dirname(__file__)   # The Position of the File to Store the Highest Score of the Game (The Current File Directory)

    def reset_dynamic_settings(self):
        '''Reset the dynamic settings of the game'''

        self.ship_speed_factor = 2
        self.bullet_speed_factor = 3
        self.alien_horizontal_speed_factor = 1
        self.alien_vertical_speed_factor = 1
        self.alien_score = 10

    def increase_game_speed(self):
        '''Increase the speed of the game'''

        self.ship_speed_factor *= self.game_speedup
        self.bullet_speed_factor *= self.game_speedup
        self.alien_horizontal_speed_factor *= self.game_speedup
        self.alien_vertical_speed_factor *= self.game_speedup
        self.alien_score = int(self.alien_score * self.game_speedup)
