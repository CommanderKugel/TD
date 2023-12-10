import pygame
import sys

import wheatfield

pygame.init()

# build a screen
screen_size = 1200, 800
screen = pygame.display.set_mode(screen_size)
screen.fill("light green")

clock = pygame.time.Clock()
tick = 0

# ==================================================================================================================== #
# wheatfield here

top = wheatfield.plant_wheat(-10, -10, 1210, 300, screen)

bottom = wheatfield.plant_wheat(-10, 500, 1210, 350, screen)

path_top_wheat = []
for x in range(0, 12):
    quad = wheatfield.plant_wheat(x * 100, 300, 100, 110, screen)
    path_top_wheat.append(quad)

path_bottom_wheat = []
for x in range(0, 12):
    quad = wheatfield.plant_wheat(x * 100, 400, 100, 110, screen)
    path_bottom_wheat.append(quad)

# ==================================================================================================================== #
# mobs here

mobs = [
    [200, 400]
]

# ==================================================================================================================== #


def draw():
    screen.fill((180, 130, 45))

    for mob in mobs:
        bend_wheat(mob)

        pygame.draw.circle(screen, (100, 100, 100), (mob[0], mob[1] + 50), 50)
        mob[0] += 1

    for plant in top:
        plant.draw(tick)

    for quad in path_top_wheat:
        for plant in quad:
            plant.draw(tick)

    for quad in path_bottom_wheat:
        for plant in quad:
            plant.draw(tick)

    for plant in bottom:
        plant.draw(tick)


    fps_font = pygame.font.SysFont("monospace", 15)
    fps = fps_font.render("fps: " + str(int(clock.get_fps())), False, "grey")
    screen.blit(fps, (10, 10))

    for i in range(0, 12):
        pygame.draw.line(screen, "black", (i * 100, 0), (i * 100, 800))
        pygame.draw.line(screen, "black", (0, i * 100), (1200, i * 100))

    pygame.display.update()


def bend_wheat(mob):

    square = int(mob[0] / 100), int(mob[1] / 100)

    for i in range(-1, 2):
        try:
            for plant in path_bottom_wheat[square[0] + i]:

                if 0 <= plant.x - mob[0] <= 50 and 0 <= plant.y - mob[1] <= 75 and not plant.isAnimating:
                    plant.isAnimating = 1

                elif 0 > plant.x - mob[0] >= -75 and plant.isAnimating == 1:
                    plant.isAnimating = 2

                elif -75 >= plant.x - mob[0] and plant.isAnimating == 2:
                    plant.isAnimating = 0

        except IndexError:
            pass


def get_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


# ==================================================================================================================== #

while True:

    get_input()
    draw()

    tick += 1
    clock.tick(60)
