import pygame
import tower


def init_floor(x, y, i):
    floor = tower.Tower("floor", i, x, y, "towerDefenseStuff/TowerDefenseLOL/pics/floor.png", 0, 0)
    floor.pic = pygame.image.load(floor.pic)
    return floor


def init_basic_tower(x, y, i):
    #                          name,        id, x, y, pic                dmg, AS
    basic_tower = tower.Tower("basic tower", i, x, y, "towerDefenseStuff/TowerDefenseLOL/pics/tower_1.png", 50, 1)
    basic_tower.pic = pygame.image.load(basic_tower.pic)
    return basic_tower


tower_1 = init_basic_tower(350, 250, 0)
tower_2 = init_basic_tower(550, 500, 1)

towers = [tower_1, tower_2]
