import pygame


speed_conversion = {"veryFast": 2, "fast": 1.5, "medium": 1, "slow": 0.75, "verySlow": 0.5}


class Mob:
    def __init__(self, name, hp, pic, speed, path, spawntime, strength, money):
        self.out_of_range = [False]
        self.travelled = 0

        self.x = -2000
        self.y = -2000
        self.dx = 0
        self.dy = 0

        self.name = name
        self.hp = hp
        self.pic = pygame.transform.scale(pic, (50, 50))
        self.speed = speed_conversion[speed]
        self.path = path
        self.spawntime = spawntime * 60
        self.strength = strength
        self.money = money

    def creep(self, screen, time):
        if self.spawntime <= time:
            if self.hp <= 0:
                self.x = -1000
                self.y = -1000
                self.dx = 0
                self.dy = 0
                self.travelled = 0
                return

            screen.blit(self.pic, (self.x, self.y - 25))

            if self.path == 0:
                if self.x == -2000 and self.y == -2000:
                    self.x = 700
                    self.y = 100
                if self.x == 700 and self.y == 100:
                    self.dx = self.speed * -1
                    self.dy = self.speed * 0.15
                elif self.x == 100 and self.y <= 200:
                    self.dx = self.speed * 0
                    self.dy = self.speed * 1
                elif self.x == 100 and self.y >= 363:
                    self.dx = self.speed * 0.9
                    self.dy = self.speed * 0.25
                elif self.x >= 649 and 515 < self.y < 547:
                    self.dx = self.speed * 0
                    self.dy = self.speed * 1
                elif self.x >= 640 and self.y >= 600:
                    self.dx = self.speed * -0.9
                    self.dy = self.speed * 0.25
                elif self.x <= 360 and self.y >= 700:
                    self.dx = self.speed * -1.05
                    self.dy = self.speed * 0

            elif self.path == 1:
                if self.x == -2000 and self.y == -2000:
                    self.x = 750
                    self.y = 150
                elif self.x == 750 and self.y == 150:
                    self.dx = self.speed * -1
                    self.dy = self.speed * 0.15
                elif 100 <= self.x <= 200 and 400 >= self.y >= 200 and self.dx != 0:
                    self.dx = self.speed * 0
                    self.dy = self.speed * 0.5
                    self.travelled += 100
                elif 100 <= self.x <= 200 and 500 >= self.y >= 330 and self.dx == 0:
                    self.dx = self.speed * 0.9
                    self.dy = self.speed * 0.25
                    self.travelled += 100
                elif self.x >= 680 and self.y >= 450 and self.dx == self.speed * 0.9:
                    self.dx = self.speed * 0
                    self.dy = self.speed * 1
                elif self.x >= 600 and self.y >= 600:
                    self.dx = self.speed * -0.65
                    self.dy = self.speed * 0.45
                elif self.x <= 800 and self.y >= 750:
                    self.dx = self.speed * -1.05
                    self.dy = self.speed * 0

            self.x += self.dx
            self.y += self.dy
            self.travelled += self.dy + self.dy

            if self.x < -10 and self.y > 699:
                self.x = -1000
                self.y = -1000
                self.dx = 0
                self.dy = 0
                return True
