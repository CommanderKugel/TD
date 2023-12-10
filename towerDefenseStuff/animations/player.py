import pygame
import animation


class Player:
    def __init__(self, x, y):

        # animation stuff here
        self.standing_left = animation.Animation("pics/standing_left.png")
        self.standing_right = animation.Animation("pics/standing_right.png")
        self.hop_right = animation.Animation("pics/hop_right.png")
        self.hop_left = animation.Animation("pics/hop_left.png")

        # coordinate stuff here
        self.x = x
        self.y = y

        # keyboard input here
        self.isFacingLeft = False

        self.a_isPressed = False
        self.d_isPressed = False

        self.isAnimating = False
        self.isHopping_right = False
        self.isHopping_left = False

    def draw_player(self, screen, ticks, timePerFrame):

        if not self.isAnimating:
            if self.a_isPressed:
                self.isFacingLeft = True
                self.isAnimating = self.hop_left.full_animation(screen, 4, self.x, self.y)

            elif self.d_isPressed:
                self.isFacingLeft = False
                self.isAnimating = self.hop_right.full_animation(screen, 4, self.x, self.y)

            elif self.isFacingLeft and not self.a_isPressed and not self.d_isPressed:
                self.standing_left.draw_sprites(screen, ticks, timePerFrame, self.x, self.y)

            elif not self.isFacingLeft and not self.a_isPressed and not self.d_isPressed:
                self.standing_right.draw_sprites(screen, ticks, timePerFrame, self.x, self.y)

        else:
            if self.isHopping_left:
                self.isHopping_left = self.hop_left.full_animation(screen, 4, self.x, self.y)

            elif self.isHopping_right:
                self.isHopping_right = self.hop_right.full_animation(screen, 4, self.x, self.y)

        if not self.isHopping_left and not self.isHopping_right:
            self.isAnimating = False
