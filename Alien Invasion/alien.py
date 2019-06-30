import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''Aline Class'''

    def __init__(self, settings, screen, row=0):
        '''Initialize the attributes of the alien'''

        super().__init__()

        self.settings = settings

        # The Alien Attributes
        self.image_source = self.settings.alien_image
        self.horizontal_speed_factor = self.settings.alien_horizontal_speed_factor
        self.vertical_speed_factor = self.settings.alien_vertical_speed_factor
        self.row = row  # The row the alien on

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(self.image_source)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width   # Initialize the alien on the screen diagonal
        self.rect.y = self.rect.height  # Initialize the alien on the screen diagonal
        self.x = float(self.rect.x) # Store the float horizontal position of the alien
        self.y = float(self.rect.y) # Store the float vertical position of the alien

        # The aliens on the odd and even rows have the different initial moving direction
        if self.row % 2 == 0:
            self.moving_direction = False   # Moving Direction Flag (True means left and False means right)
        else:
            self.moving_direction = True
        self.moving_down = False    # Moving Down Flag

    def update(self):
        '''Update the position of the alien'''

        if not self.moving_direction and self.rect.right < self.screen_rect.right:  # Moving Right Actions
            self.x += self.horizontal_speed_factor
            self.moving_down = True
        elif self.rect.left > self.screen_rect.left:    # Moving left Actions
            self.x -= self.horizontal_speed_factor
            if self.moving_down:
                self.y += self.vertical_speed_factor * self.rect.height * 2
                self.moving_down = False
            self.moving_direction = True
        else:   # Reset moving
            self.y += self.vertical_speed_factor * self.rect.height * 2
            self.moving_direction = False   # Reset moving direction flag
            self.moving_down = False    # Reset moving down flag

        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        '''Draw an alien in a specific position of the screen'''

        self.screen.blit(self.image, self.rect)
