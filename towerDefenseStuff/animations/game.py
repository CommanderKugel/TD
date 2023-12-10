import pygame
import sys

import background
import player


class Game:
    def __init__(self):
        self.isRunning = True
        self.clock = pygame.time.Clock()
        self.gameTicks = 0

        self.screenSize = (1200, 800)
        self.screen = pygame.display.set_mode(self.screenSize)

        self.bg = background.Background("pics/background.png", self.screenSize, self.screen)
        self.playerStartX = 550
        self.playerStartY = 650
        self.player = player.Player(self.playerStartX, self.playerStartY)

    def game(self):
        while self.isRunning:

            self.getInput()
            self.draw()
            self.tick()

    def draw(self):

        self.bg.draw_bg()
        self.player.draw_player(self.screen, self.gameTicks, 8)
        self.draw_help_lines()

        pygame.display.update()

    def getInput(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                # make a clean exit
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # make another clean exit
                    pygame.quit()
                    sys.exit()

                elif event.key == pygame.K_a and not event.key == pygame.K_d:
                    self.player.a_isPressed = True
                    self.player.isFacingLeft = True

                elif event.key == pygame.K_d and not event.key == pygame.K_a:
                    self.player.d_isPressed = True
                    self.player.isFacingLeft = False

            elif event.type == pygame.KEYUP:
                # stop moving when letting go of a key

                if event.key == pygame.K_a:
                    self.player.a_isPressed = False

                if event.key == pygame.K_d:
                    self.player.d_isPressed = False

    def tick(self):
        self.gameTicks += 1
        if self.gameTicks >= 60:
            self.gameTicks = 0
        self.clock.tick(60)

    def draw_help_lines(self):
        # helplines for developer
        for i in range(0, 12):
            pygame.draw.line(self.screen, "black", (i * 100 + 100, 0), (i * 100 + 100, 800))
        for i in range(0, 8):
            pygame.draw.line(self.screen, "black", (0, i * 100 + 100), (1200, i * 100 + 100))
