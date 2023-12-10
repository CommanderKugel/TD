import pygame


class Animation:
    def __init__(self, spriteSheet):
        self.spriteSheet = pygame.image.load(spriteSheet)
        self.frameAmount = 4
        self.spriteSize = (16, 16)
        self.scale = (8 * self.spriteSize[0], 8 * self.spriteSize[1])

        self.spriteList = self.get_spriteList()

    def get_spriteList(self):
        spriteList = []
        for i in range(0, self.frameAmount):
            sprite = pygame.Surface(self.spriteSize)
            sprite.blit(self.spriteSheet, (0, 0), (i * self.spriteSize[0], 0, self.spriteSize[0], self.spriteSize[1]))
            sprite = pygame.transform.scale(sprite, self.scale)
            spriteList.append(sprite)
        return spriteList

    def draw_sprites(self, screen, ticks, timePerFrame, x, y):
        screen.blit(self.spriteList[int(int(ticks / timePerFrame) % len(self.spriteList))],
                    (x - self.spriteSize[0] / 2, y - self.spriteSize[1] / 2))

    def full_animation(self, screen, animationLength, x, y):

        i =
        screen.blit(self.spriteList[i], (x - self.spriteSize[0] / 2, y - self.spriteSize[1] / 2))


