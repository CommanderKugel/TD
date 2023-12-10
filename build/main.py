import pygame

import game

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()

    level = game.Game()
    level.play()
