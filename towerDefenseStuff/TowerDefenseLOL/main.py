import game
import pygame


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("CommanderKugel's Game")

    game = game.Game()
    game.play()
