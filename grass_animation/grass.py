import pygame


class GrassBlade:
    def __init__(self, x, y, frames, screen):

        self.x = x
        self.y = y

        # "static" stuff for drawing
        # dunno why they are here and not in an Interface lol
        self.sprite_size = 32, 96
        self.frames = frames
        self.screen = screen

        # determine the frame and duration
        # different animation based on position
        # standard animation here
        self.animation_ticks = self.x / 20 - self.y / 50
        self.animation_cooldown = 8

        self.index = 0
        self.translator = None
        self.frame_amount = None

        # special animation here
        # when mob is walking through -> blades are bent
        self.isAnimating = False

        self.translator_ani_1 = None
        self.frame_amount_ani_1 = None
        self.translator_ani_2 = None
        self.frame_amount_ani_2 = None



    def draw(self, tick):
        self.animation_ticks += 1

        if not self.isAnimating:
            self.index = int(self.animation_ticks / self.animation_cooldown) % self.frame_amount
            self.screen.blit(self.frames[self.translator[self.index]],
                             (self.x - self.sprite_size[0] / 2, self.y - self.sprite_size[1]))

        elif self.isAnimating == 1:
            self.screen.blit(self.frames[4], (self.x - self.sprite_size[0] / 2, self.y - self.sprite_size[1]))

        elif self.isAnimating == 2:
            self.screen.blit(self.frames[5], (self.x - self.sprite_size[0] / 2, self.y - self.sprite_size[1]))


    def set_translators(self, translator_1):
        self.translator = translator_1
        self.frame_amount = len(translator_1)
