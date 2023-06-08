
from settings import *
from tetromino import Tetromino

class Tetris:
    def __init__(self,screen):
        self.screen = screen
        self.sprite_group = pygame.sprite.Group()
        self.tetromino = Tetromino(self)

    def draw_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pygame.draw.rect(self.screen, (30,30,30),
                             (x * TILE_SIZE + GRID_OFFSET, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
                
    
    def update(self):
        self.tetromino.update()
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.screen)