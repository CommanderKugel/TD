import random
import pygame
import arrow


class Tower:
    def __init__(self):
        # put all coordinates here
        self.x = 50
        self.y = 236
        self.eye = (self.x + 80, self.y + 50)
        self.target = (400, 410)

        # image for the tower is here
        self.image = pygame.image.load("towerDefenseStuff/animation_test/pics/tower_1.png").convert()
        self.image = pygame.transform.scale(self.image, (100, 200))
        # make a dummy
        self.rect = pygame.Rect(self.target, (25, 25))

        # the arrow to be shot
        self.makeShot = False

        self.arrow_A = arrow.Arrow(self.eye[0], self.eye[1], self.target[0], self.target[1])
        self.arrow_B = arrow.Arrow(self.eye[0], self.eye[1], self.target[0], self.target[1])
        self.arrow_C = arrow.Arrow(self.eye[0], self.eye[1], self.target[0], self.target[1])
        self.arrow_D = arrow.Arrow(self.eye[0], self.eye[1], self.target[0], self.target[1])
        self.arrow_E = arrow.Arrow(self.eye[0], self.eye[1], self.target[0], self.target[1])
        self.arrow_F = arrow.Arrow(self.eye[0], self.eye[1], self.target[0], self.target[1])

        self.freeArrows = [self.arrow_A, self.arrow_B, self.arrow_C, self.arrow_D, self.arrow_E, self.arrow_F]
        self.shotArrows = []

    def draw_tower(self, screen, tick):
        # draw tower
        screen.blit(self.image, (self.x, self.y))
        # draw dummy
        pygame.draw.rect(screen, "red", self.rect)
        # draw "eye"
        pygame.draw.rect(screen, "green", (self.eye, (5, 5)))

        # add an arrow to shot arrows array every time one is shot
        # and vice versa when it lands
        if self.makeShot and self.freeArrows and tick % 6 == 0:
            self.shotArrows.append(self.freeArrows[0])
            self.freeArrows.remove(self.freeArrows[0])

            """
            if you want to only shoot once when triggered:
            self.makeShot = False
            """

        # shootanimation for every arrow
        for arrow in self.shotArrows:
            arrow.start_animation(tick)
            arrow.fly(screen)

            if arrow.y > 600:

                self.freeArrows.append(arrow)
                self.shotArrows.remove(arrow)
                arrow.stop()
