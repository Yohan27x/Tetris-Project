import pygame

BG_COLOR = (0,0,0)


TILE_SIZE = 32
GRID_OFFSET = 32 * 5

vec = pygame.math.Vector2

SCREEN_SIZE = WIDTH, HEIGHT = 700, TILE_SIZE * 22
FIELD_SIZE = FIELD_W, FIELD_H = int((WIDTH / TILE_SIZE)), int((HEIGHT / TILE_SIZE))
FIELD_SIZE = FIELD_W, FIELD_H = 10,50

TETROMINOES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}