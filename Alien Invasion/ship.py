import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    '''Ship Class'''

    def __init__(self, setting, screen):
        '''Initialize the attributes of the ship'''

        super().__init__()

        self.settings = setting

        # The Ship Attributes
        self.image_source = self.settings.ship_image
        self.speed_factor = self.settings.ship_speed_factor

        self.screen = screen
        self.screen_rect = self.screen.get_rect()   # Get the rectangular area of the Surface (return a Rect)

        self.image = pygame.image.load(self.image_source)   # Load an image from a file (return a Surface)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx    # Initialize the ship on the horizontal center of the screen
        self.rect.bottom = self.screen_rect.bottom  # Set the ship on the bottom of the screen
        self.centerx = float(self.rect.centerx) # Store the float horizontal position of the ship
        self.bottom = float(self.rect.bottom)   # Store the float vertical position of the ship

        self.moving_left = False    # Moving Left Flag
        self.moving_right = False   # Moving Right Flag
        self.moving_up = False  # Moving Up Flag
        self.moving_down = False    # Moving Down Flag
        # self.firing = False # Continuous Firing Flag

    def update(self):
        '''Update the position of the ship'''

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.bottom -= self.speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.speed_factor

        self.rect.centerx = self.centerx    # Still have a little bit value-loss but is not significant
        self.rect.bottom = self.bottom

    def reset(self):
        '''Reset the position of the ship'''

        self.centerx = self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom

    def draw(self):
        '''Draw a ship in a specific position of the screen'''

        self.screen.blit(self.image, self.rect) # Draw the Surface onto the Rect (return a Rect)
