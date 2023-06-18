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

    def rotate(self, pivot_pos):
        translated = self.pos - pivot_pos
        rotated = translated.rotate(90)
        return rotated + pivot_pos

    def set_rect_pos(self):
        self.rect.topleft = self.pos * TILE_SIZE

    def update(self):
        self.set_rect_pos()

    # def draw(self):
    def is_collide(self,pos):
        x, y = int(pos.x), int(pos.y)
        if 0 <= x < FIELD_W and y < FIELD_H and (y < 0 or not self.tetromino.tetris.field_array[y][x]):
            return False
        return True



class Tetromino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOES.keys()))
        self.landing = False
        self.blocks = [Block(self, pos) for pos in TETROMINOES[self.shape]]


    def move(self, direction):
        move_directions = MOVE_DIRECTIONS[direction]
        new_block_pos = [block.pos + move_directions for block in self.blocks]
        # print(new_block_pos)
        is_collide = self.is_collide(new_block_pos)

        # print(move_directions)
        if not is_collide:
            for block in self.blocks:
                block.pos += move_directions
        elif direction == 'down':
            self.landing = True

    def rotate(self):
        pivot_pos = self.blocks[0].pos
        new_block_positions = [block.rotate(pivot_pos) for block in self.blocks]

        if not self.is_collide(new_block_positions):
            for i, block in enumerate(self.blocks):
                block.pos = new_block_positions[i]



    def is_collide(self, block_pos):
        return any(map(Block.is_collide, self.blocks, block_pos))


    def update(self):
        self.move(direction = "down")


