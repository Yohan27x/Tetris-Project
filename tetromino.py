from settings import *

class Block(pygame.sprite.Sprite):
    def __init__(self,tetromino,pos, img):
        # reference to the tetromino it belongs to
        self.tetromino = tetromino
        
        self.alive = True
        self.pos = vec(pos) + INIT_POS_OFFSET
        self.next_pos = vec(pos) + NEXT_POS_OFFSET
        # print("pos : ", self.pos)

        super().__init__(tetromino.tetris.sprite_group)
        self.image = img
        # self.image.fill(('orange'))
        self.rect = self.image.get_rect()
        # self.rect.topleft = pos[0] * TILE_SIZE + GRID_OFFSET, pos[1] *TILE_SIZE     
        self.rect.topleft = self.pos * TILE_SIZE
        # print(self.rect.topleft)

    def is_alive(self):
        if(not self.alive):
           self.kill()
           

    def rotate(self, pivot_pos):
        translated = self.pos - pivot_pos
        rotated = translated.rotate(90)
        return rotated + pivot_pos

    def set_rect_pos(self):
        pos = None
        if(self.tetromino.current == True):
            pos = self.pos
        else:
            pos = self.next_pos
        self.rect.topleft = pos * TILE_SIZE

    def update(self):
        self.is_alive()
        self.set_rect_pos()


    # def draw(self):
    def is_collide(self,pos):
        x, y = int(pos.x), int(pos.y)

        if 0 <= x < FIELD_W and y < FIELD_H and (y < 0 or not self.tetromino.tetris.field_array[y][x]):
            return False
        return True



class Tetromino:
    def __init__(self, tetris, current=True):
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOES.keys()))
        self.color = random.choice(list(blocks.values()))
        self.landing = False
        self.blocks = [Block(self, pos, self.color) for pos in TETROMINOES[self.shape]]
        self.current = current

    def move(self, direction):
        move_directions = MOVE_DIRECTIONS[direction]
        # calculte the next position of the block in the tetromino
        new_block_pos = [block.pos + move_directions for block in self.blocks]
        # check if one of the block of the current tetromino enter in collision
        is_collide = self.is_collide(new_block_pos)

        
        if not is_collide:
            for block in self.blocks:
                block.pos += move_directions
        elif direction == 'down':
            self.landing = True

    def rotate(self):
        # rotation in 3 steps ...
        pivot_pos = self.blocks[0].pos
        new_block_positions = [block.rotate(pivot_pos) for block in self.blocks]

        if not self.is_collide(new_block_positions):
            for i, block in enumerate(self.blocks):
                block.pos = new_block_positions[i]



    def is_collide(self, block_pos):
        return any(map(Block.is_collide, self.blocks, block_pos))


    def update(self):
        self.move(direction = "down")


