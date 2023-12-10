import pygame
import mob


def init_slime(path, timing):
    #               name,    hp,  picture,                              speed, path, timing, strength, money
    slime = mob.Mob("Slime", 100, pygame.image.load("towerDefenseStuff/TowerDefenseLOL/pics/slime.png"), "slow", path, timing, 1, 10)
    return slime


def init_fast_slime(path, timing):
    #                     name,        hp, picture,                                   speed, path, timing, strength, money
    fast_slime = mob.Mob("fast_slime", 50, pygame.image.load("towerDefenseStuff/TowerDefenseLOL/pics/fast_slime.png"), "fast", path, timing, 1, 15)
    return fast_slime


def init_big_slime(path, timing):
    #                    name,         hp,  picture,                                 speed,      path, timing, strength, money
    fast_slime = mob.Mob("fast_slime", 350, pygame.image.load("towerDefenseStuff/TowerDefenseLOL/pics/big_slime.png"), "verySlow", path, timing, 2, 50)
    return fast_slime


wave_1 = [
    init_slime(1, 1),
    init_slime(2, 2),
    init_slime(1, 3),
    init_slime(2, 4),
    init_slime(1, 5),
    init_slime(2, 6)
]


def wave_2():
    wave_2 = []
    path = 1
    for i in range(1, 100):
        if i % 2 == 0:
            wave_2.append(init_slime(path, i))
        else:
            wave_2.append((init_fast_slime(path, i)))
    return wave_2


def wave_3():
    wave_3 = []
    for i in range(0, 5):
        wave_3.append(init_slime(0, i))
        wave_3.append(init_slime(1, i))

    # 5 seconds have passed
    for i in range(12, 20):
        path = int(i % 2)
        wave_3.append(init_fast_slime(path, i))

    # 19 seconds have passed
    wave_3.append(init_big_slime(1, 25))
    for i in range(25, 30):
        wave_3.append(init_slime(0, i))
        wave_3.append(init_slime(1, i))

    # 30 seconds have passed
    for i in range(35, 40):
        wave_3.append(init_slime(0, i))
        wave_3.append(init_slime(1, i))

    for i in range(50, 55):
        wave_3.append(init_big_slime(i % 2, i))

    return wave_3
