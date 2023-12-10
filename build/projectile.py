import pygame
import math


class Projectile:
    def __init__(self, x, y, eye, sprites):

        # projectile will be ejected from "eye"
        self.x = x
        self.y = y
        self.z = 0
        self.eye = eye
        self.location = [x, y]

        # for parabola
        self.t = 0

        self.dist = None
        self.target = None

        # for drawing
        self.sprites = sprites

    def draw(self, screen):

        index = self.curve()
        screen.blit(self.sprites[index], self.location)

    def curve(self):
        self.t += 2

        index = 0
        slope = (self.dist - 2 * (self.t + 13)) * 0.04

        if slope >= 5:
            index = 0
        elif slope >= 2.4:
            index = 1
        elif slope >= 0.66:
            index = 2
        elif slope >= 0.19:
            index = 3
        elif slope >= -0.19:
            index = 4
        elif slope >= -0.66:
            index = 5
        elif slope >= -2.4:
            index = 6
        elif slope >= -5:
            index = 7
        elif slope < -5:
            index = 8

        if self.x > self.target.x:
            index += 8
            if index == 16:
                index = 8

        self.z = (self.t ** 2 - self.dist * self.t) * 0.04

        self.location = [
            self.x + self.t * (self.target.x - self.x) / self.dist,
            self.y + self.t * (self.target.y - self.y) / self.dist + self.z
        ]
        return index
