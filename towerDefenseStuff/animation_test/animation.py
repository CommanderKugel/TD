import pygame


class animation:
    def __init__(self, image, frameAmount, dim, scale):
        self.spriteSheet = pygame.image.load(image).convert()
        self.frameAmount = frameAmount
        self.frameDim = dim
        self.scale = (dim[0] * scale, dim[1] * scale)

        self.sheet = self.get_sprites()

        self.isAnimating = False
        self.startTime = 0
        self.animationSpeed = 16

    def get_sprites(self):
        sprites = []
        for i in range(0, self.frameAmount):
            image = pygame.Surface(self.frameDim).convert()
            image.blit(self.spriteSheet, (0, 0), (i * self.frameDim[0], 0, self.frameDim[0], self.frameDim[1]))
            image = pygame.transform.scale(image, self.scale)

            sprites.append(image)
        return sprites

    """
    draw_gif works properly if called constantly, good for default animation
    """
    def draw_gif(self, screen, gameTicks, frameSpeed, spriteCoordinates):
        screen.blit(self.sheet[int(int(gameTicks / frameSpeed) % len(self.sheet))], spriteCoordinates)
    """
    start_animation is to be called @ button input to setup the drawing function
    draw_animation is to be called in the draw method 
    """
    def start_animation(self, gameTick):
        if not self.isAnimating:
            self.startTime = gameTick
            self.isAnimating = True

    def draw_animation(self, screen, coordinates, currentGameTick):
        if self.isAnimating:
            if currentGameTick - self.startTime >= self.frameAmount * (self.animationSpeed):
                self.isAnimating = False
                print("break animation!")
            else:
                screen.blit(self.sheet[int(int(self.startTime - currentGameTick - 1) /
                                           self.animationSpeed % len(self.sheet))], coordinates)
