import pygame.font


class Button():
    '''Game Button Class'''

    def __init__(self, screen, text, width=200, height=50,
                 button_color=(0, 0, 0), font_name=None, font_size=48,
                 font_color=(255, 255, 255),
                 position_offset_x=0, position_offset_y=0):
        ''' Initialize the attributes of the button'''

        # The Button Attributes
        self.width, self.height = width, height
        self.button_color = button_color
        self.font = pygame.font.SysFont(font_name, font_size)   # Create a font object from the system fonts (name, size)
        self.font_color = font_color

        self.screen = screen
        self.screen_rect  = self.screen.get_rect()

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx + position_offset_x
        self.rect.centery = self.screen_rect.centery + position_offset_y

        self.render_text(text)  # Render the text as an image

    def render_text(self, text):
        '''Render the text as an image'''

        self.text_image = self.font.render(
            text, True, self.font_color, self.button_color) # Draw the text on a new Surface (text, antialias, color, background=None)->Surface
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw(self):
        '''Draw a button in a specific position of the screen'''

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)
