import pygame
import random


class Arrow:
    def __init__(self, x_1, y_1, x_2, y_2):

        self.image = pygame.image.load("towerDefenseStuff/animation_test/pics/arrow.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (28, 9))

        self.start = (x_1, y_1)
        self.target = (x_2, y_2)
        self.random = 0

        self.x = x_1
        self.y = y_1
        self.slope = 0

        self.isFlying = False
        self.startTicks = 0

    def curve(self):
        y = (self.target[1] - self.start[1]) / (self.target[0] - self.start[0]) / 100 * \
            (self.x - self.start[0]) * (self.x - self.start[0]) * self.random / 2.3 + \
            self.start[1]
        return y

    def angle(self):
        dy = 0.14 * (self.x - self.start[0])
        return dy

    def start_animation(self, tick):
        if not self.isFlying:
            # for recycling old arrows
            self.x = self.start[0]
            self.y = self.start[1]

            # initialize flying variables
            self.random = round(random.uniform(0.8, 1.2), 2)
            self.startTicks = tick
            self.isFlying = True

    def fly(self, screen):
        if self.isFlying:

            screen.blit(self.image, (self.x, self.y))

            self.x += 10
            self.y = self.curve()
            self.slope += 0.1

    def stop(self):
        self.isFlying = False
