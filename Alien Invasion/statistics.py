class Statistics():
    '''Game Statistics Information Class'''

    def __init__(self, settings):
        '''Initialize the statistics information of the game'''

        self.settings = settings

        self.game_status = False    # The Status of the Game (True means running and Fasle means stopped)
        self.game_over = False  # The Flag of Game Over (True means game over and False means pre-start)
        self.show_help_information = False  # The Flag of Show Help Information

        # The Game Statistics Information
        self.score = 0  # The Game Score
        self.highest_score = 0  # The Initially Highest Game Score
        self.game_difficulty_level = 1  # The Game Difficulty Level
        self.left_ships_quantity = self.settings.ship_quantity  # The Quantity of the Left Ships

    def reset_statistics(self):
        '''Reset the statistics information of the game'''

        self.score = 0
        self.game_difficulty_level = 1
        self.left_ships_quantity = self.settings.ship_quantity

    def set_highest_score(self):
        '''Read and set the highest score of the game from the file'''

        try:
            with open(self.settings.local_file_position, 'r') as file:
                try:
                    self.highest_score = int(file.read())
                except ValueError:
                    self.highest_score = 0
        except FileNotFoundError:
            self.highest_score = 0
