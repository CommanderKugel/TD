import pygame
import sys
import math

import buildings
import mob
import paths


class Game:
    def __init__(self):

        # big main screen
        self.screen_size = (1200, 800)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.background = pygame.Rect((0, 0), self.screen_size)

        # miscellaneous stuff
        self.clock = pygame.time.Clock()
        self.tick = 1
        self.isRunning = True

        # input variables
        self.SPACE_INPUT = False
        self.click = False

        """
        buildings to be put here
        """
        self.all_buildings = [
            buildings.Buiding(200, 400),
            buildings.Buiding(1000, 400)
        ]

        """
        waves, mobs & paths
        """
        # path surfaces
        self.path_1_surfaces = paths.path_1_surfaces()

        # this is the ~wave
        self.wave = paths.wave()
        # check for towerrange here
        self.spawned_mobs = []

    def play(self):
        while self.isRunning:

            """
            REMOVE THIS LATER!!
            """

            self.get_input()

            self.draw()

            self.tick += 1
            self.clock.tick(60)

    def draw(self):
        """
        background
        """
        pygame.draw.rect(self.screen, "dark green", self.background)

        # draw help lines, delete later, just for developer help
        for i in range(0, 12):
            pygame.draw.line(self.screen, "black", (i * 100, 0), (i * 100, 800))
            pygame.draw.line(self.screen, "black", (0, i * 100), (1200, i * 100))

        """
        mobs
        """
        time = pygame.time.get_ticks()
        for mob in self.wave:
            if time > mob.spawn_time and mob.age == 0:
                self.spawned_mobs.append(self.wave.pop(self.wave.index(mob)))

                for building in self.all_buildings:

                    # do this with chunks later
                    building.all_visible_mobs.append(mob)

        for mob in self.spawned_mobs:
            mob.draw(self.screen)

            # remove when outside of map
            if -100 < mob.x > self.screen_size[0] + 100 or -100 < mob.y > self.screen_size[1] + 100:
                self.spawned_mobs.remove(mob)

        """
        buildings
        """
        for building in self.all_buildings:
            building.draw(self.screen, self.tick)

            # draw projectiles and return them after target hit
            for projectile in building.projectiles_shot:
                projectile.draw(self.screen)

                # when target is hit:
                try:
                    if buildings.dist(projectile.location, building.target) <= 10:

                        building.target.hp -= building.dmg

                        # if target died
                        if building.target.hp <= 0:
                            try:
                                self.spawned_mobs.remove(building.target)
                                building.mobs_in_range.remove(building.target)

                                for tower in self.all_buildings:
                                    if building.target in tower.mobs_in_range:
                                        tower.mobs_in_range.remove(building.target)
                                    if building.target in tower.all_visible_mobs:
                                        tower.all_visible_mobs.remove(building.target)
                            except ValueError:
                                pass

                        # recycle projectile
                        projectile.t = 0
                        building.projectiles_loaded.append(projectile)
                        building.projectiles_shot.remove(projectile)

                except AttributeError:
                    pass

                if projectile.z > 0 and projectile.t != 0:
                    # recycle projectile
                    projectile.t = 0
                    building.projectiles_loaded.append(projectile)
                    building.projectiles_shot.remove(projectile)

        """
        miscellanous
        """
        fps_font = pygame.font.SysFont("monospace", 15)
        fps = fps_font.render("fps: "+str(int(self.clock.get_fps())), False, "grey")
        self.screen.blit(fps, (10, 10))

        pygame.display.update()

    def get_input(self):
        # make a clean exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                # do some stuff when pressed
                elif event.key == pygame.K_SPACE:
                    print("space was pressed." + "\n"
                          "lets say a new wave is triggered now")

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    print("space was let go")

            mouse_presses = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            if mouse_presses[0]:

                # figure out collision by dist from circle center
                for building in self.all_buildings:
                    if math.sqrt((building.x - mouse_pos[0]) * (building.x - mouse_pos[0])
                                 + (building.y - mouse_pos[1]) * (building.y - mouse_pos[1])) \
                                 <= building.click_radius:
                        building.build()
