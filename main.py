# Tetris Project





# Utiliser https://pyga.me/docs/ 



# UML : 
# diagramme de classe

from settings import *
from tetromino import *
from tetris import *


import pygame, sys, os, random
from pygame.locals import *


pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.set_num_channels(64)

pygame.display.set_caption('Pygame Window')
os.environ['SDL_VIDEODRIVER'] = 'directx'

flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED

screen = pygame.display.set_mode((WIDTH, HEIGHT), flags, vsync=True)

clock = pygame.time.Clock()


tetris = Tetris(screen)
tetronimo = Tetromino(tetris)


while True :

    screen.fill((BG_COLOR))

    tetris.draw_grid()

    tetris.draw()

    for event in pygame.event.get():  # event loop
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            pass
        if event.type == KEYUP:
            pass

    pygame.display.update()
    clock.tick(60)