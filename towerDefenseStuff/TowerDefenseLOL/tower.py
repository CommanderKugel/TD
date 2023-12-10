import pygame
import math


class Tower:
    def __init__(self, name, id, x, y, pic, dmg, attack_speed):
        self.id = id
        self.name = name
        self.x = x
        self.y = y

        self.range = 300
        self.dmg = dmg
        self.attack_speed = attack_speed * 60

        self.pic = pic
        self.target = False
        self.laser_fired = 6

    def do_stuff(self, screen, wave, tick):
        # draw the tower
        screen.blit(self.pic, (self.x, self.y - 25))
        pygame.draw.lines(screen, "red", True, ((self.x + self.range, self.y + self.range),
                                                (self.x + self.range, self.y - self.range),
                                                (self.x - self.range, self.y - self.range),
                                                (self.x - self.range, self.y + self.range)))

        # find enemy in range with biggest mob.travelled
        if tick % self.attack_speed == 0:
            for mob in wave:
                dist = math.sqrt((self.x - mob.x) * (self.x - mob.x) + (self.y - mob.y) * (self.y - mob.y))
                if dist <= self.range:
                    # mob is in range
                    if not self.target or self.target.travelled < mob.travelled:
                        self.target = mob

            # now draw laser attacking the target
            if self.target and self.laser_fired == 0:
                self.laser_fired = 4

        if self.target and self.laser_fired > 0:
            if self.target.x < 0:
                return
            pygame.draw.line(screen, "red", (self.x, self.y), (self.target.x, self.target.y), 15)
            self.laser_fired -= 1
            if self.laser_fired == 0:
                self.target.hp -= self.dmg
                self.target = None
