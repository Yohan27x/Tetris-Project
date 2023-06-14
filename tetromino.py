from settings import *

class Block(pygame.sprite.Sprite):
    def __init__(self,tetromino,pos):
        self.tetromino = tetromino

        self.pos = vec(pos) + INIT_POS_OFFSET
        # print("pos : ", self.pos)

        super().__init__(tetromino.tetris.sprite_group)
        self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.image.fill(('orange'))
        self.rect = self.image.get_rect()
        # self.rect.topleft = pos[0] * TILE_SIZE + GRID_OFFSET, pos[1] *TILE_SIZE     
        self.rect.topleft = self.pos * TILE_SIZE
        # print(self.rect.topleft)

    def set_rect_pos(self):
        self.rect.topleft = self.pos * TILE_SIZE

    def update(self):
        self.set_rect_pos()

    # def draw(self):


class Tetromino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOES.keys()))
        self.blocks = [Block(self,pos) for pos in TETROMINOES[self.shape]]

    def move(self, direction):
        move_directions = MOVE_DIRECTIONS[direction]
        # print(move_directions)
        for block in self.blocks:
            block.pos += move_directions


    def update(self):
        self.move(direction = "down")
        pygame.time.wait(200)

