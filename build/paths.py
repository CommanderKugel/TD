import mob
import pygame


"""
init methods for different mobs
"""


def init_skeleton(starting_point, spawn_time, path):
    return mob.Mob(starting_point, spawn_time, path,
                   # hp, speed, strength, spritesheet_path
                   100, 2, 1, "build/pics/skeleton_walk_16x16.png")


"""
wave creation here
"""


def wave():
    spawn_point = (-50, 700)
    # spawn point, spawn time, path
    wave = []
    for i in range(1, 50):
        wave.append(init_skeleton(spawn_point, 1500 * i + 2000, 0))

    return wave


"""
path functions here
"""


def path_1_surfaces():
    path_1_surfaces = [
        pygame.Surface((700, 200), pygame.SRCALPHA),
        pygame.Surface((200, 700), pygame.SRCALPHA),
        pygame.Surface((700 + 200, 200), pygame.SRCALPHA)
    ]
    return path_1_surfaces


def path_1(path, x, y, speed):

    if path == 0:

        if x < 600:
            return x + speed, y

        elif x == 600:
            return x + 1, 700

        elif x > 600 and y > 200:
            return x, y - speed

        elif x >= 600 and y < 300:
            return x + speed, y
