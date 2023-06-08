# Tetris Project





# Utiliser https://pyga.me/docs/ 



# UML : 
# diagramme de classe

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

screen = pygame.display.set_mode((700,750), flags, vsync=True)

clock = pygame.time.Clock()


tetris = Tetris(screen)

sprite_group = pygame.sprite.Group()
block1 =  Block()

sprite_group.add(block1)

while True :

    screen.fill((200, 50, 150,))

    tetris.draw_grid()

    sprite_group.draw(screen)

    pygame.draw.rect(screen, (0, 100, 255), (50, 50, 162, 100), 1)

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