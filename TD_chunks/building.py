import math

import pygame


class Building:
    def __init__(self, x, y, sprites, screen):

        # ingame stuff
        self.dmg = 0
        self.attack_speed = 0
        self.range = 400

        # coordinates
        self.x = x
        self.y = y
        self.eye = self.x, self.y - 150

        # determine building
        self.upgrade_lvl = 0

        # click on it
        self.click_raius = 100

        #animation stuff
        self.screen = screen
        self.sprites = sprites
        self.size = 64, 128
        # original 32x64, scaled 64x128, 2 frames - floor & tower, 0 rows

        # shooting
        self.mobs_in_range = []

        self.target = None
        self.projectiles_loaded = []
        self.projectiles_shot = []

    def build(self):

        if self.upgrade_lvl == 0:
            self.upgrade_lvl = 1

            # initialize ürojectiles aka ability to shoot
            self.projectiles_loaded = None

        elif self.upgrade_lvl == 1:
            print("lol already maxed out?")

    def draw(self, tick):

        if self.upgrade_lvl == 0:
            # draw floor
            self.screen.blit(self.sprites[0],
                             (self.x - self.size[0] / 2, self.y - self.size[1] * 5 / 6))

        elif self.upgrade_lvl == 1:
            # draw building
            self.screen.blit(self.sprites[1],
                             (self.x - self.size[0] / 2, self.y - self.size[1] * 5 / 6))
            # draw the EYE
            pygame.draw.circle(self.screen, "red", self.eye, 10)

            # draw projectiles
            for projectile in self.projectiles_shot:
                projectile.draw()

        # draw center, just for developer help
        pygame.draw.circle(self.screen, "red", (self.x, self.y), 10)

    def do_logic(self, tick):

        if tick % self.attack_speed == 0:

            """
            mobs_in_range will be updated by chunk logic (adding & deleting)
            """
            try:
                if self.mobs_in_range[0] and self.projectiles_loaded[0]:

                    self.target = self.mobs_in_range[0]
                    # find target first
                    for mob in self.mobs_in_range:
                        if mob.age > self.target:
                            self.target = mob

                    self.projectiles_loaded[0].t = 0
                    self.projectiles_loaded[0].target = self.target
                    self.projectiles_loaded[0].dist = dist(self.target, self.eye)

                    self.projectiles_shot.append(
                        self.projectiles_loaded.pop(0)
                    )

            except IndexError:
                pass


# ==================================================================================================================== #


class Projectile:
    def __init__(self, eye, screen):

        self.eye = eye
        self.t = 0

        self.screen = screen

        self.target = None
        self.dist = None

        self.location = eye

    def draw(self):
        self.t += 2

        slope = (self.dist - 2 * (self.t + 13)) * 0.04

        index = 0
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

        if self.eye[0] > self.target.x:
            index += 8
            if index == 16:
                index = 8

        z = (self.t ** 2 - self.dist * self.t) * 0.04

        self.location = [
            self.eye[0] + self.t * (self.target.x - self.eye[0]) / self.dist,
            self.eye[1] + self.t * (self.target.y - self.eye[1]) / self.dist + z
        ]

        self.screen.blit(projectile_sprites[index], (self.eye[0] + self.t * (self.target.x - self.eye[0]) / self.dist,
                                                     self.eye[1] + self.t * (self.target.y - self.eye[1]) / self.dist+z)
                         )


# ==================================================================================================================== #


def get_sprites(sprite_path, sprite_pixel_size, scale, frame_amount, rows):

    a = pygame.display.set_mode((0, 0))
    sprite_sheet = pygame.image.load(sprite_path).convert_alpha()
    sprites = []

    for j in range(rows):
        for i in range(frame_amount):

            image = pygame.Surface(sprite_pixel_size, pygame.SRCALPHA)
            image.blit(sprite_sheet, (0, 0),
                       (i * sprite_pixel_size[0], j * sprite_pixel_size[1],
                       sprite_pixel_size[0], sprite_pixel_size[1])
                       )
            image = pygame.transform.scale(image, scale)
            sprites.append(image)

    return sprites


building_sprites = get_sprites("sheets/tower_1.1_32x64.png", (32, 64), (64, 128), 2, 1)
projectile_sprites = get_sprites("sheets/angled_arrows_8x8.png", (8, 8), (16, 16), 16, 1)


def create_building(x, y, screen):
    return Building(x, y, building_sprites, screen)


def create_arrow(eye, screen):
    return Projectile(eye, screen)


# ==================================================================================================================== #


def dist(a, b):
    try:
        return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    except TypeError:
        return math.sqrt((a.x - b[0]) ** 2 + (a.x - b[1]) ** 2)
