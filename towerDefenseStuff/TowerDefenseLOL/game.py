import pygame
import sys

import buildings
import mob
import waves
import tower


PLAYER_HEARTS = 20
PLAYER_MONEY = 0


class Game:
    def __init__(self):

        # miscellaneous universal stuff
        self.screenSize = (800, 800)
        self.screen = pygame.display.set_mode(self.screenSize)
        self.clock = pygame.time.Clock()
        self.ticks = 0
        self.isRunning = True

        # background related stuff
        self.background = pygame.image.load("towerDefenseStuff/TowerDefenseLOL/pics/background.png")
        self.background = pygame.transform.scale(self.background, self.screenSize)

        #  mob related stuff
        self.wave_1 = waves.wave_1
        self.wave_2 = waves.wave_2()
        self.wave_3 = waves.wave_3()
        # currently in use:
        self.wave = self.wave_3

        # tower related stuff
        self.towers = buildings.towers

    def play(self):
        while self.isRunning:

            self.draw_screen()
            self.key_input()

            self.ticks += 1
            self.clock.tick(60)

    def key_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()

    def draw_screen(self):
        self.screen.blit(self.background, (0, 0))

        # help for developers, delete later
        self.draw_help_lines()

        self.waves()
        self.towers_func()
        self.write_stuff()

        pygame.display.update()

    """
    helpmethods for draw_screen()
    """
    def waves(self):
        for mob in self.wave:
            if mob.creep(self.screen, self.ticks):
                global PLAYER_HEARTS
                PLAYER_HEARTS -= mob.strength
                if PLAYER_HEARTS <= 0:
                    self.isRunning = False

    def towers_func(self):
        for i in range(0, len(buildings.towers)):
            buildings.towers[i].do_stuff(self.screen, self.wave, self.ticks)

    def write_stuff(self):
        fps = pygame.font.SysFont(None, 24)
        fps = fps.render("fps: "+str(int(self.clock.get_fps())), True, "black")
        self.screen.blit(fps, (20, 20))

        global PLAYER_HEARTS
        hearts = pygame.font.SysFont(None, 24)
        hearts = hearts.render("hearts: "+str(PLAYER_HEARTS), True, "red")
        self.screen.blit(hearts, (20, 40))

    """
    helpmethos for developers, irrelevant for gameplay
    """
    def draw_help_lines(self):
        for i in range(0, 8):
            pygame.draw.line(self.screen, "black", (0, i * 100), (800, i * 100))
            pygame.draw.line(self.screen, "black", (i * 100, 0), (i * 100, 800))
