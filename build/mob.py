import pygame

import paths


class Mob:
    def __init__(self, starting_point, spawn_time, path,
                 hp, speed, strength, spritesheet_path):

        # coordinates
        self.x = starting_point[0]
        self.y = starting_point[1]

        self.path = path
        self.age = 0

        """
        animation stuff here
        """
        # factor to scale the image to be bigger later
        self.sprite_scale = (128, 128)
        self.frame_pixel_size = (16, 16)
        self.sprite_sheet = pygame.image.load(spritesheet_path).convert_alpha()

        self.sheetIndex_walk = 0    # frames for walking to right is in first row -> index = 0
        self.frame_amount_walk = 4
        self.frame_cooldown = 32 * self.frame_amount_walk

        self.frames_walk = self.get_sprites(self.sheetIndex_walk)

        """ 
        stats and so on
        individualize this via init method later
        """
        self.spawn_time = spawn_time    # when to spawn the mob after starting the wave
        self.hp = hp
        self.speed = speed
        self.strength = strength

    def get_sprites(self, index):
        sprites = []
        for i in range(0, self.frame_amount_walk):
            image = pygame.Surface(self.frame_pixel_size, pygame.SRCALPHA)
            image.blit(self.sprite_sheet, (0, 0), (i * self.frame_pixel_size[0], index * self.frame_pixel_size[1],
                                                   self.frame_pixel_size[0], self.frame_pixel_size[1]))

            image = pygame.transform.scale(image, self.sprite_scale)
            sprites.append(image)

        return sprites

    def draw(self, screen):
        self.age += 1

        # import path from paths file
        dest = paths.path_1(self.path, self.x, self.y, self.speed)
        self.x = dest[0]
        self.y = dest[1]

        # draw frame dependent of index
        # maybe centralize get ticks method
        index = int(pygame.time.get_ticks() / self.frame_cooldown) % len(self.frames_walk)

        screen.blit(self.frames_walk[index], (self.x - self.sprite_scale[0] / 2,
                                              self.y - self.sprite_scale[1]))
        if self.x > 0:
            pygame.draw.circle(screen, "red", (self.x, self.y), 10)


"""
========================================================================================================================
To Do:



========================================================================================================================
"""
