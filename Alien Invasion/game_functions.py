import sys
import pygame
from time import sleep

from ship import Ship
from alien import Alien
from bullet import Bullet


def create_aliens(settings, screen, aliens):
    '''Create aliens'''

    # Get the max quantity of the aliens the screen can accommodate
    quantity_information = get_alien_quantity(settings, screen)
    single_line_quantity = quantity_information['single_line_quantity']
    max_lines = quantity_information['max_lines']

    # Create aliens
    for j in range(max_lines):
        for i in range(single_line_quantity):
            alien = Alien(settings, screen, j)
            calculate_alien_position(settings, alien, i, j)
            aliens.add(alien)


def get_alien_quantity(settings, screen):
    '''Get the quantity information of the aliens the screen can accommodate'''

    # Load the attributes for calculating
    screen_width = settings.screen_width
    screen_height = settings.screen_height
    ship = Ship(settings, screen)
    ship_height = ship.rect.height
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height

    # Calculate the max quantity of the aliens the single line can accommodate
    single_line_quantity = int(
        (screen_width - 2 * alien_width) / (2 * alien_width))

    # Calculate the max alien lines the screen can accommodate
    max_lines = int(
        (screen_height - 3 * alien_height - ship_height) / (2 * alien_height))

    # Encapsulate and return results
    quantity_information = {}
    quantity_information['single_line_quantity'] = single_line_quantity
    quantity_information['max_lines'] = max_lines
    return quantity_information


def calculate_alien_position(settings, alien, i, j):
    '''Calculate the position of the alien'''

    # Load the attributes for calculating
    screen_width = settings.screen_width
    alien_width = alien.rect.width
    alien_height = alien.rect.height

    # The aliens on odd and even rows have the different initially horizontal position
    if j % 2 == 0:
        alien.x = (2 * i + 1) * alien_width # On the left part of the screen
    else:
        alien.x = screen_width - (2 * i + 1) * alien_width  # On the right part of the screen
    alien.y = (2 * j + 1) * alien_height
    alien.rect.x = alien.x
    alien.rect.y = alien.y


def check_events(settings, screen, ship, aliens, bullets,
                 statistics, play_button, help_button, game_over_information):
    '''Check events'''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            store_highest_score(settings, statistics)
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_mouse_button_down_event(settings, screen, ship, aliens, bullets,
                                          statistics, play_button, help_button,
                                          game_over_information)
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(settings, event, screen, ship, aliens, bullets,
                                  statistics)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)


def store_highest_score(settings, statistics):
    '''Store the highest score of the game into a file'''

    try:
        with open(settings.local_file_position, 'w') as file:
            try:
                file.write(str(statistics.highest_score))
            except ValueError:
                file.write('0')
    except FileNotFoundError:
        pass


def check_mouse_button_down_event(settings, screen, ship, aliens, bullets,
                                  statistics, play_button, help_button,
                                  game_over_information):
    '''Actions of MOUSEBUTTONDOWN Event'''

    mouse_x, mouse_y = pygame.mouse.get_pos()   # Get the mouse cursor position (return x, y)
    if not statistics.game_status:
        if play_button.rect.collidepoint(mouse_x, mouse_y) and not statistics.game_over and not statistics.show_help_information:
            start_game(settings, screen, ship, aliens, bullets, statistics)
        elif help_button.rect.collidepoint(mouse_x, mouse_y) and not statistics.game_over and not statistics.show_help_information:
            statistics.show_help_information = True
        elif game_over_information.rect.collidepoint(mouse_x, mouse_y) and statistics.game_over:
            statistics.game_over = False


def check_key_down_events(settings, event, screen, ship, aliens, bullets, statistics):
    '''Actions of KEYDOWN Event'''

    if event.key == pygame.K_p and not statistics.game_status and not statistics.game_over:
        start_game(settings, screen, ship, aliens, bullets, statistics)
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire(settings, screen, ship, bullets)
    elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
        store_highest_score(settings, statistics)
        sys.exit()


def check_key_up_events(event, ship):
    '''Actions of KEYUP Event'''

    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def start_game(settings, screen, ship, aliens, bullets, statistics):
    '''Start the game'''

    pygame.mouse.set_visible(False) # Set the visibility of the mouse
    initialize_game(settings, screen, ship, aliens, bullets, statistics)
    statistics.game_status = True
    statistics.game_over = True


def fire(settings, screen, ship, bullets):
    '''Fire Actions'''

    if len(bullets) < settings.bullet_max_quantity:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def initialize_game(settings, screen, ship, aliens, bullets, statistics):
    '''Initialize the game content'''

    settings.reset_dynamic_settings()
    statistics.reset_statistics()
    reset_game_environment(settings, screen, ship, aliens, bullets)


def reset_game_environment(settings, screen, ship, aliens, bullets):
    '''Reset the environment of the game'''

    ship.reset()
    ship.update()
    aliens.empty()
    bullets.empty()
    create_aliens(settings, screen, aliens)


def detect_collision(settings, screen, ship, aliens, bullets, statistics):
    '''Detect the various collision in the game'''

    # Check the collision between bullets and aliens
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)    # Return a dictionary consisted of crashed bullets and aliens, True means delete the correspondingly crashed elements
    if collisions:
        update_score(settings, statistics, collisions)

    # If no alien on the screen, reproduce some
    if len(aliens) == 0:
        reproduce_aliens(settings, screen, aliens, bullets, statistics)

    # Check the collision between ship and aliens
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_crash(settings, screen, ship, aliens, bullets, statistics)

    # Check the aliens have or not reached the edge of the screen
    aliens_reach(settings, screen, ship, aliens, bullets, statistics)


def update_score(settings, statistics, collisions):
    '''Update the score and the highest score of the game'''

    # Update the score
    for crashed_aliens in collisions.values():
        statistics.score += settings.alien_score * len(crashed_aliens)

    # Update the highest score
    if statistics.score > statistics.highest_score:
        statistics.highest_score = statistics.score


def reproduce_aliens(settings, screen, aliens, bullets, statistics):
    '''Reproduce aliens'''

    bullets.empty()
    settings.increase_game_speed()
    statistics.game_difficulty_level += 1
    create_aliens(settings, screen, aliens)


def ship_crash(settings, screen, ship, aliens, bullets, statistics):
    '''Ship Crash Actions'''

    statistics.left_ships_quantity -= 1 # Reduce the quantity of the left ships
    if statistics.left_ships_quantity > 0:
        reset_game_environment(settings, screen, ship, aliens, bullets)
        sleep(0.5)  # Sleep 0.5 seconds (delay 0.5 seconds to restart the game)
        # print(statistics.left_ships_quantity)   # Testing code
    else:
        game_over(settings, screen, ship, aliens, bullets, statistics)


def aliens_reach(settings, screen, ship, aliens, bullets, statistics):
    '''The Actions of Aliens have Reached the Bottom of the Screen'''

    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_crash(settings, screen, ship, aliens, bullets, statistics)
            break


def game_over(settings, screen, ship, aliens, bullets, statistics):
    '''Game Over Actions'''

    statistics.game_status = False
    initialize_game(settings, screen, ship, aliens, bullets, statistics)
    pygame.mouse.set_visible(True)


def update_screen(settings, screen, ship, aliens, bullets,
                  statistics, information_bar,
                  play_button, help_button, game_over_information):
    '''Update the screen (redraw all content)'''

    screen.fill(settings.screen_bg_color)   # Fill the screen with the solid color

    if not statistics.game_status:
        refresh_stopped_screen(statistics, play_button, help_button,
                               game_over_information)
    else:
        refresh_running_screen(screen, ship, aliens, bullets, information_bar)

    pygame.display.flip()   # Update the full display Surface to the screen (refresh)


def refresh_stopped_screen(statistics, play_button, help_button,
                           game_over_information):
    '''Refresh the stopped screen'''

    if not statistics.show_help_information:
        if not statistics.game_over:    # "Pre-start" Status
            play_button.draw()  # Draw a "PLAY" button
            help_button.draw()  # Draw a "HELP" button
        else:   # "Game Over" Status
            game_over_information.draw()  # Show the game over information
    else:
        show_help_information()


def refresh_running_screen(screen, ship, aliens, bullets, information_bar):
    '''Refresh the running screen'''

    # Update ship
    ship.update()  # Update the position of the ship
    ship.draw()  # Redraw the ship

    # Update aliens
    aliens.update()  # Update the position of all the aliens
    aliens.draw(screen)  # Redraw all the aliens using the Surface and Rect of each Sprite

    # Update bullets
    bullets.update()  # Update the position of all the bullets
    delete_bullet(bullets)  # Delete the bullets out range of the screen
    # Redraw all the bullets
    for bullet in bullets.sprites():
        bullet.draw()

    # Show the game statistics information
    information_bar.render_score()
    information_bar.render_highest_score()
    information_bar.render_game_difficulty_level()
    information_bar.render_left_ships()
    information_bar.draw()


def show_help_information():
    '''Show help information'''




def delete_bullet(bullets):
    '''Delete the bullets out range of the screen'''

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets)) # Testing code
