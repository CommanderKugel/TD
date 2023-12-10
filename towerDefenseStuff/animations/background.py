import pygame


class Background:
    def __init__(self, image, screenSize, screen):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, screenSize)

        self.screen = screen

    def draw_bg(self):
        self.screen.blit(self.image, (0, 0))

        # maybe play with player coordinates here later for moving background
