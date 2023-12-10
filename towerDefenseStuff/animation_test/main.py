import pygame

import game

if __name__ == "__main__":

    pygame.init()
    pygame.font.init()
    game = game.Game()
    game.game()
