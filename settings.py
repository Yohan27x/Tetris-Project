import pygame, sys, os, random
from pygame.locals import *
from helperFunction import load_img

pygame.init()
pygame.mixer.init()
pygame.font.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.set_num_channels(64)
pygame.display.set_caption('Tetris')

font = pygame.font.Font("font/8-BIT WONDER.TTF", size=40)
os.environ['SDL_VIDEODRIVER'] = 'directx'
flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED

BG_COLOR = (0,0,0)
FPS = 60

TILE_SIZE = 32



FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

FIELD_SCALE_W, FIELD_SCALE_H = 1.8, 1.2
WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * FIELD_SCALE_W, FIELD_RES[1] * FIELD_SCALE_H

screen = pygame.display.set_mode(WIN_RES, flags, vsync=True)

vec = pygame.math.Vector2
INIT_POS_OFFSET = vec(FIELD_W//2 -1 , 0)
NEXT_POS_OFFSET = vec(FIELD_W * 1.3,  FIELD_H * 0.45)


anim_time_interval = 150
fast_anim_time_interval = 15

TETROMINOES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}

MOVE_DIRECTIONS = {'left': vec(-1, 0), 'right': vec(1, 0), 'down': vec(0, 1)}


blocks_color = ["blue", "lightblue", "red", "yellow", "purple", "green"]

blocks = {}
for color in blocks_color:
    blocks[color] = load_img(f"sprites/Block/{color}.png", [TILE_SIZE, TILE_SIZE])

background = load_img("sprites/bg.png", [1500,1000])
