import pygame


class Chunk:
    def __init__(self, x, y, size, screen):

        # where to draw chunk
        self.x = x
        self.y = y
        self.screen = screen

        # surface
        self.surface = pygame.Surface(size, pygame.SRCALPHA)

    def draw(self):

        self.surface.fill("blue")

        self.screen.blit(self.surface, (self.x, self.y))
        self.surface.fill((255, 255, 255, 0))


# ==================================================================================================================== #


def create_chunk_path_15x10(screen):
    chunks = []

    for x in range(0, 15):
        chunk_column = []

        for y in range(0, 10):

            chunk_column.append(Chunk(x * 100, y * 100, (100, 100), screen))
        chunks.append(chunk_column)

    return chunks


def create_path_chunks_lv1(screen):

    chunks = [[
        Chunk(0 * 100, 1 * 100, (100, 100), screen),
        Chunk(1 * 100, 1 * 100, (100, 100), screen),
        Chunk(2 * 100, 1 * 100, (100, 100), screen),
        Chunk(3 * 100, 1 * 100, (100, 100), screen),
        Chunk(11 * 100, 1 * 100, (100, 100), screen),
        Chunk(12 * 100, 1 * 100, (100, 100), screen),
        Chunk(13 * 100, 1 * 100, (100, 100), screen),
        Chunk(14 * 100, 1 * 100, (100, 100), screen)
    ], [
        Chunk(3 * 100, 2 * 100, (100, 100), screen),
        Chunk(4 * 100, 2 * 100, (100, 100), screen),
        Chunk(10 * 100, 2 * 100, (100, 100), screen),
        Chunk(11 * 100, 2 * 100, (100, 100), screen)
    ], [
        Chunk(4 * 100, 3 * 100, (100, 100), screen),
        Chunk(5 * 100, 3 * 100, (100, 100), screen),
        Chunk(9 * 100, 3 * 100, (100, 100), screen),
        Chunk(10 * 100, 3 * 100, (100, 100), screen)
    ], [
        Chunk(5 * 100, 4 * 100, (100, 100), screen),
        Chunk(6 * 100, 4 * 100, (100, 100), screen),
        Chunk(7 * 100, 4 * 100, (100, 100), screen),
        Chunk(8 * 100, 4 * 100, (100, 100), screen),
        Chunk(9 * 100, 4 * 100, (100, 100), screen)
    ], [
        Chunk(5 * 100, 5 * 100, (100, 100), screen),
        Chunk(6 * 100, 5 * 100, (100, 100), screen),
        Chunk(7 * 100, 5 * 100, (100, 100), screen),
        Chunk(8 * 100, 5 * 100, (100, 100), screen),
        Chunk(9 * 100, 5 * 100, (100, 100), screen)
    ], [
        Chunk(4 * 100, 6 * 100, (100, 100), screen),
        Chunk(5 * 100, 6 * 100, (100, 100), screen),
        Chunk(9 * 100, 6 * 100, (100, 100), screen),
        Chunk(10 * 100, 6 * 100, (100, 100), screen)
    ], [
        Chunk(3 * 100, 7 * 100, (100, 100), screen),
        Chunk(4 * 100, 7 * 100, (100, 100), screen),
        Chunk(10 * 100, 7 * 100, (100, 100), screen),
        Chunk(11 * 100, 7 * 100, (100, 100), screen)
    ], [
        Chunk(0 * 100, 8 * 100, (100, 100), screen),
        Chunk(1 * 100, 8 * 100, (100, 100), screen),
        Chunk(2 * 100, 8 * 100, (100, 100), screen),
        Chunk(3 * 100, 8 * 100, (100, 100), screen),
        Chunk(11 * 100, 8 * 100, (100, 100), screen),
        Chunk(12 * 100, 8 * 100, (100, 100), screen),
        Chunk(13 * 100, 8 * 100, (100, 100), screen),
        Chunk(14 * 100, 8 * 100, (100, 100), screen)
    ]]

    return chunks


