import pygame
import math

import mob
import projectile


class Buiding:
    def __init__(self, x, y):

        self.dmg = 50
        self.attack_speed = 25

        # coordinates
        self.x = x
        self.y = y
        self.eye = (self.x, self.y - 140)

        # determine what building it is here
        self.upgrade_level = 0

        # radius to trigger building method
        self.click_radius = 100

        """
        now all the animation stuff
        make sprites list of lists for animations
        """
        self.sprite_sheet = pygame.image.load("build/pics/tower_1.1.png")
        self.sprite_amount = 2
        self.sprite_pixel_size = (32, 64)
        self.size = (256, 512)

        # floor: index = 0, tower_1: index = 1
        self.sprites = self.get_sprites()

        """
        now all the shooting and range stuff
        """
        self.range = 450
        self.all_visible_mobs = []
        self.mobs_in_range = []

        self.projectiles_spritesheet = pygame.image.load("build/pics/angled_arrows.png")
        self.projectiles_sprites = []

        for i in range(16):
            image = pygame.Surface((8, 8), pygame.SRCALPHA)
            image.blit(self.projectiles_spritesheet, (0, 0), ((i * 8, 0), (8, 8)))
            image = pygame.transform.scale(image, (32, 32))
            self.projectiles_sprites.append(image)

        self.projectiles_loaded = []
        self.projectiles_shot = []

        self.target = None

    def get_sprites(self):
        sprites = []

        for i in range(0, self.sprite_amount):
            image = pygame.Surface(self.sprite_pixel_size, pygame.SRCALPHA)

            image.blit(self.sprite_sheet, (0, 0), ((i * self.sprite_pixel_size[0], 0), self.sprite_pixel_size))

            image = pygame.transform.scale(image, self.size).convert_alpha()
            sprites.append(image)

        return sprites

    def build(self):

        if self.upgrade_level == 0:
            # change picture and start shooting
            self.upgrade_level = 1

            # initialize the projectiles
            for i in range(0, 3):
                self.projectiles_loaded.append(projectile.Projectile(self.x, self.y, self.eye, self.projectiles_sprites))

        elif self.upgrade_level == 1:
            print("lol maxed out!")

    def draw(self, screen, tick):

        # drawing is level dependent
        if self.upgrade_level == 0:
            screen.blit(self.sprites[0], (self.x - self.size[0] / 2, self.y - self.size[1] * 5 / 6))

        elif self.upgrade_level == 1:
            screen.blit(self.sprites[1], (self.x - self.size[0] / 2, self.y - self.size[1] * 5 / 6))
            # the EYE
            pygame.draw.circle(screen, "red", (self.x, self.y - self.size[1] / 3 + 15), 10)
            # not shoot
            self.shoot(tick)

        # visualize @ (x, y) delete later, just help for developers
        pygame.draw.circle(screen, "red", (self.x, self.y), 10)

    def shoot(self, tick):

        if tick % self.attack_speed == 0:

            for mob in self.all_visible_mobs:
                if dist((self.x, self.y), (mob.x, mob.y)) <= self.range and mob not in self.mobs_in_range:
                    self.mobs_in_range.append(mob)

            # remove mobs out of range
            for mob in self.mobs_in_range:
                if dist((self.x, self.y), (mob.x, mob.y)) > self.range:
                    self.mobs_in_range.remove(mob)

            try:
                self.target = self.mobs_in_range[0]

                for i in range(1, len(self.mobs_in_range)):
                    if self.mobs_in_range[i].age > self.target.age:
                        self.target = self.mobs_in_range[i]

                if len(self.projectiles_loaded) > 0:

                    self.projectiles_loaded[0].x = self.eye[0]
                    self.projectiles_loaded[0].y = self.eye[0]
                    self.projectiles_loaded[0].t = 0

                    self.projectiles_loaded[0].target = self.target
                    self.projectiles_loaded[0].dist = dist((self.x, self.y), self.eye)

                    self.projectiles_shot.append(self.projectiles_loaded.pop(0))

            except IndexError:
                pass


"""
========================================================================================================================
To Do:

- projectiles & animation
- gold cost for building

optional:
- maybe tower animations (wind & flags?)

========================================================================================================================
"""


def dist(self, target):
    try:
        return math.sqrt((target[0] - self[0]) ** 2 + (target[1] - self[1]) ** 2)
    except TypeError:
        return math.sqrt((target.x - self[0]) ** 2 + (target.y - self[1]) ** 2)
