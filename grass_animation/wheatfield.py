import pygame
import random

import grass


def get_frames(path, frame_amount, rows, frame_size, scale):
    sheet = pygame.image.load(path)
    sprites = []

    for j in range(rows):
        row = []
        for i in range(frame_amount):
            image = pygame.Surface(frame_size, pygame.SRCALPHA)
            image.blit(sheet, (0, 0), (i * frame_size[0], j * frame_size[1], frame_size[0], frame_size[1]))
            image = pygame.transform.scale(image, scale)
            row.append(image)

        sprites.append(row)

    return sprites


wheat_frames = get_frames("grass_animation/wheat_1_16x32.png", 6, 3, (16, 32), (32, 96))

# ==================================================================================================================== #


def plant_wheat(start_x, start_y, length, height, surface):
    """
    returns list of wheat objects
    need to be drawn onto a surface
    """
    wheat = []

    for j in range(int(height / 30)):
        for i in range(int(length / 15)):

            x = 15 * i + j % 2 * 15 - random.randint(0, 10) + start_x
            y = 30 * j + i % 3 * 10 + random.randint(0, 10) + start_y + 15
            z = random.randint(0, 2)

            blade = grass.GrassBlade(x, y, wheat_frames[z], surface)
            blade.set_translators([0, 1, 2, 1, 0, 3, 0, 1, 0, 0, 0])

            wheat.append(blade)

    return wheat
