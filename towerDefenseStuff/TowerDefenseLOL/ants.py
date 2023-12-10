import pygame
import math


class Ant:
    def __init__(self, x, y, angle, screen):
        self.screen = screen
        self.angle = angle

        self.speed = 1.5
        self.size = 10

        self.coordinates = [x, y]
        self.direction = [math.cos(self.angle*math.pi/180), math.sin(self.angle*math.pi/180)]

    def turn(self, add):
        self.angle += add
        self.direction = [math.cos(self.angle*math.pi/180), math.sin(self.angle*math.pi/180)]

    def draw(self):
        self.move()
        # head
        pygame.draw.circle(self.screen, "black", (self.coordinates[0]+self.direction[0]*13,
                                              self.coordinates[1]+self.direction[1]*13), self.size*0.8)
        # torso
        pygame.draw.circle(self.screen, "black", self.coordinates, self.size)
        # back end
        pygame.draw.circle(self.screen, "black", (self.coordinates[0]-self.direction[0]*15,
                                                  self.coordinates[1]-self.direction[1]*15), self.size * 1.2)

    def move(self):
        self.coordinates[0] += self.direction[0] * self.speed
        self.coordinates[1] += self.direction[1] * self.speed
