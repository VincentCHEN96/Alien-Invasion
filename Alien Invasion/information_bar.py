import pygame.font
from pygame.sprite import Group

from ship import Ship


class InformationBar():
    '''Game Information Bar Class'''

    def __init__(self, settings, screen, statistics):
        '''Initialize the attributes of the information bar'''

        # The Information Bar Attributes
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self. settings = settings

        self.screen =screen
        self.screen_rect = self.screen.get_rect()

        self.statistics = statistics

        # Show the initial statistics information of the game
        self.render_score()
        self.render_highest_score()
        self.render_game_difficulty_level()
        self.render_left_ships()

    def render_score(self):
        '''Render the score as an image (update/refresh)'''

        rounded_score = int(round(self.statistics.score, 0))    # Keep 0 decimal place (next to int)
        str_score = "{:,}".format(rounded_score)    # Insert ',' when convert int to string
        self.score_image = self.font.render(
            str_score, True, self.text_color, self.settings.screen_bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 10
        self.score_image_rect.top = 10

    def render_highest_score(self):
        '''Render the highest score as an image (update/refresh)'''

        rounded_highest_score = int(round(self.statistics.highest_score, 0))
        str_highest_score = "{:,}".format(rounded_highest_score)
        self.highest_score_image = self.font.render(str_highest_score, True,
            self.text_color, self.settings.screen_bg_color)
        self.highest_score_image_rect = self.highest_score_image.get_rect()
        self.highest_score_image_rect.centerx = self.screen_rect.centerx
        self.highest_score_image_rect.top = self.score_image_rect.top

    def render_game_difficulty_level(self):
        '''Render the game difficulty level as an image (update/refresh)'''

        str_game_difficulty_level = "{:,}".format(self.statistics.game_difficulty_level)
        self.game_difficulty_level_image = self.font.render(
            str_game_difficulty_level, True, self.text_color,
            self.settings.screen_bg_color)
        self.game_difficulty_level_image_rect = self.game_difficulty_level_image.get_rect()
        self.game_difficulty_level_image_rect.right = self.score_image_rect.right
        self.game_difficulty_level_image_rect.top = self.score_image_rect.bottom + 10

    def render_left_ships(self):
        '''Render the left ships as images (update/refresh)'''

        self.left_ships = Group()
        for i in range(self.statistics.left_ships_quantity):
            ship = Ship(self.settings, self.screen)
            ship.rect.x = 10 + i * ship.rect.width
            ship.rect.y = 10
            self.left_ships.add(ship)

    def draw(self):
        '''Draw a information bar in a specific position of the screen'''

        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.highest_score_image, self.highest_score_image_rect)
        self.screen.blit(self.game_difficulty_level_image,
                         self.game_difficulty_level_image_rect)
        self.left_ships.draw(self.screen)
