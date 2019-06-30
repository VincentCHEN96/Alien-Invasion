import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    '''Bullet Class'''

    def __init__(self, settings, screen, ship):
        '''Initialize the attributes of the bullet'''

        super().__init__()

        self.settings = settings

        # The Bullet Attributes
        self.width = self.settings.bullet_width
        self.height = self.settings.bullet_height
        self.color = self.settings.bullet_color
        self.speed_factor = self.settings.bullet_speed_factor

        self.screen = screen

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = ship.rect.centerx   # Set the bullet on the center of the ship
        self.rect.top = ship.rect.top   # Initialize the bullet on the top and inside of the ship
        self.y = float(self.rect.y) # Store the float vertical position of the bullet

    def update(self):
        '''Update the position of the bullet'''

        self.y -= self.speed_factor # The y axe are pointing down of the screen
        self.rect.y = self.y

    def draw(self):
        '''Draw a bullet in a specific position of the screen'''

        pygame.draw.rect(self.screen, self.color, self.rect)    # Draw a rectangle shape on the Surface using the solide color (return a Rect)
