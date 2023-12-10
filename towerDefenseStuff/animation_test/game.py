import pygame
import sys

import animation
import tower


class Game:
    def __init__(self):
        self.isRunning = True
        self.clock = pygame.time.Clock()
        self.gameTick = 0

        self.screenSize = (500, 500)
        self.screen = pygame.display.set_mode(self.screenSize)

        self.background = pygame.image.load("towerDefenseStuff/animation_test/pics/background.png").convert(self.screen)
        self.background = pygame.transform.scale(self.background, self.screenSize)

        self.animation = animation.animation("towerDefenseStuff/animation_test/pics/arrows.png", 4, (8, 8), 16)
        self.animationCoordinates = (200, 200)

        self.tower = tower.Tower()

    def game(self):
        while self.isRunning:

            self.get_input()
            self.draw()

            self.gameTick += 1
            self.clock.tick(60)

    def draw(self):
        # background
        self.screen.blit(self.background, (0, 0))

        # draw tower
        self.tower.draw_tower(self.screen, self.gameTick)

        # draw fps
        font = pygame.font.Font('freesansbold.ttf', 32)

        # rotating arrows animation
        fps = str(int(self.clock.get_fps()))
        self.animation.draw_animation(self.screen, self.animationCoordinates, self.gameTick)
        text = font.render(fps, True, "green")
        textRect = text.get_rect()
        textRect.center = (200, 50)
        self.screen.blit(text, textRect)

        pygame.display.update()

    def get_input(self):
        for event in pygame.event.get():
            # clean exit
            if event.type == pygame.QUIT:
                # make a clean exit
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                elif event.key == pygame.K_SPACE:
                    #self.animation.start_animation(self.gameTick)
                    self.tower.makeShot = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.tower.makeShot = False
