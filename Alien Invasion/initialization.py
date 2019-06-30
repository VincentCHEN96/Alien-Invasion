import pygame


def initialize_game(settings):
    '''Initialize the game'''

    pygame.init()   # Initialize all imported pygame modules
    pygame.display.set_caption(settings.screen_caption) # Set the caption of the screen
