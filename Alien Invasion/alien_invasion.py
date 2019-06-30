import pygame
from pygame.sprite import Group

from settings import Settings
from initialization import initialize_game
from ship import Ship
import game_functions as gf
from statistics import Statistics
from information_bar import InformationBar
from button import Button


def run_game():
    '''Game Main Function'''

    settings = Settings()   # Load the game settings

    initialize_game(settings)   # Initialize the game

    screen_mode = (settings.screen_width, settings.screen_height)   # Store the size of the screen for game display
    screen = pygame.display.set_mode(screen_mode)   # Create a screen for game display (return a Surface)

    ship = Ship(settings, screen)   # Game Ship

    aliens = Group()    # Aliens Group
    gf.create_aliens(settings, screen, aliens)  # Create a group of aliens

    bullets = Group()   # Bullets Group

    statistics = Statistics(settings)   # Game Statistics Information
    statistics.set_highest_score()  # Read and set the highest score of the game from the file

    information_bar = InformationBar(settings, screen, statistics)  # The Information Bar of the Game

    play_button = Button(screen, "PLAY", button_color=(0, 255, 0),
                         position_offset_y=-25) # The "PLAY" Button for Start the Game
    help_button = Button(screen, "HELP", button_color=(150, 150, 255),
                         font_size=45, position_offset_y=25)    # The "HELP" Button to Notice the Rules of the Game
    # help_information = Button(screen, help)
    game_over_information = Button(screen, "GAME OVER (click to restart)",
                                   width=500, button_color=(255, 0, 0)) # The "GAME OVER" Information for Notice the Game Status

    # Game Main Loop
    while True:
        gf.check_events(settings, screen, ship, aliens, bullets, statistics,
                        play_button, help_button, game_over_information)    # Check the game events
        if statistics.game_status:
            gf.detect_collision(settings, screen, ship, aliens, bullets,
                                statistics) # Detect the various collision in the game
        gf.update_screen(settings, screen, ship, aliens, bullets, statistics,
                         information_bar, play_button, help_button,
                         game_over_information) # Refresh the screen to update the latest game content


run_game()  # Run the game
