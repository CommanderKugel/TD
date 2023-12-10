import pygame
import sys


import chunks
import mobs


class Level:
    def __init__(self):

        self.screen = pygame.display.set_mode((0, 0,), pygame.FULLSCREEN)
        self.screen_size = self.screen.get_size()
        print(self.screen_size)

        # screen stuff
        self.clock = pygame.time.Clock()
        self.tick = 1
        self.is_running = True

        # player input
        self.SPACE = False
        self.MOUSE_RIGHT = False

        # all buildings here
        self.all_buildings = []

        # mobs & waves
        self.wave = []
        self.spawned_mobs = []

        # paths & chunks
        self.chunks_inFront = chunks.create_path_chunks_lv1(self.screen)
        self.chunks_behind = []
        self.all_chunks = self.chunks_inFront

    def play(self):
        while self.is_running:

            self.get_player_input()

            self.do_logic()
            self.draw()

            self.tick += 1
            self.clock.tick(60)

    def draw(self):

        # background
        self.screen.fill("light green")

        for mob in self.spawned_mobs:
            mob.draw()

        for row in self.all_chunks:
            for chunk in row:
                chunk.draw()

        for building in self.all_buildings:
            building.draw()
        """
        for row in self.chunks_inFront:
            for chunk in row:
                chunk.draw()
        """

        self.draw_help_lines()

        pygame.display.update()

    def do_logic(self):

        for mob in self.wave:
            if self.tick >= mob.spawn_time:

                self.spawned_mobs.append(
                    self.wave.pop(self.wave.index(mob))
                )

        for mob in self.spawned_mobs:
            mob.do_logic(self.all_chunks)

    def get_player_input(self):

        # make a clean exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # keyboard presses
            elif event.type == pygame.KEYDOWN:

                # another clean exit
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                # do some stuff when pressed
                elif event.key == pygame.K_SPACE:
                    print("space was pressed.")

            # keyboard let go's
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    print("space was let go")

            # right mousebutton presses
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:

                # figure out collision by dist from circle center
                for building in self.all_buildings:

                    # make building be clicked
                    # coming soon
                    pass

# ==================================================================================================================== #

    def draw_help_lines(self):
        for x in range(1, 16):
            for y in range(1, 11):

                pygame.draw.line(self.screen, "black", (x * 100, 0), (x * 100, 1000))
                pygame.draw.line(self.screen, "black", (0, y * 100), (1500,  y * 100))
