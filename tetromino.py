from settings import *

class Block(pygame.sprite.Sprite):
    def __init__(self,tetromino,pos):
        self.tetromino = tetromino


        super().__init__(tetromino.tetris.sprite_group)
        self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.image.fill(('orange'))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos[0] * TILE_SIZE + GRID_OFFSET, pos[1] *TILE_SIZE     

    # def update(self):
    #     pass

    # def draw(self):


class Tetromino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape='T'
        self.blocks = [Block(self,pos) for pos in TETROMINOES [self.shape]]

    def update(self):
        pass