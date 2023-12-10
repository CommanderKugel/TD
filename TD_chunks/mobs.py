import pygame


pygame.init()


class Mob:
    def __init__(self, x, y, spawn_time,
                 sprites, frame_amount, sprite_scale,
                 screen,
                 hp, speed, strength
    ):
        # gaming - stuff
        self.hp = hp
        self.speed = speed
        self.strength = strength

        # coordinate stuff
        self.x = x
        self.y = y
        self.screen = screen

        self.spawn_time = spawn_time
        self.age = 0

        # animation stuff
        self.sprites = sprites
        self.chunks = None

        self.frame_cooldown = 60
        self.frame_amuont = frame_amount
        self.sprite_scale = sprite_scale

    def do_logic(self, all_chunks):

        # get mob chunk
        self.chunks = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    self.chunks.append(all_chunks[int(self.x / 100) + i][int(self.y / 100) + j])
                    all_chunks[int(self.x / 100) + i][int(self.y / 100) + j].surface.fill("red")
                except IndexError or TypeError:
                    pass

        self.creep()

        self.age += 1

    def creep(self):

        self.x += 2

        """
        add path stuff here
        """

    def draw(self):

        self.screen.blit(self.sprites[int(pygame.time.get_ticks() / self.frame_cooldown) % self.frame_amuont],
                         (
                         self.x - self.sprite_scale[0] / 2,
                         self.y - self.sprite_scale[1])
                         )


# ==================================================================================================================== #


def get_sprites(sprite_path, sprite_pixel_size, scale, frame_amount, rows):

    a = pygame.display.set_mode((0, 0))
    sprite_sheet = pygame.image.load(sprite_path).convert_alpha()
    sprites = []

    for j in range(rows):
        for i in range(frame_amount):

            image = pygame.Surface(sprite_pixel_size, pygame.SRCALPHA)
            image.blit(sprite_sheet, (0, 0),
                       (i * sprite_pixel_size[0], j * sprite_pixel_size[1],
                       sprite_pixel_size[0], sprite_pixel_size[1])
                       )
            image = pygame.transform.scale(image, scale)
            sprites.append(image)

    return sprites


skeleton_sprites = get_sprites("TD_chunks/sheets/skeleton_walk_16x16.png", (16, 16), (64, 64), 4, 2)


def create_skeleton(x, y, spawm_time, screen):
    return Mob(x, y, spawm_time,
               skeleton_sprites, 4, (64, 64), screen,
               100, 1, 1)


# ==================================================================================================================== #

def path_1_lvl1(x, y):

    pass
