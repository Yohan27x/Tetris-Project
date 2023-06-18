from settings import *
from tetromino import Tetromino


class Tetris:
    def __init__(self,app):
        self.app = app
        self.sprite_group = pygame.sprite.Group()
        self.field_array = self.get_field_array()
        self.tetromino = Tetromino(self)

    def get_field_array(self):
        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]
    
    def put_tetromino_block_in_array(self):
        for block in self.tetromino.blocks:
            x,y = int(block.pos.x), int(block.pos.y)
            self.field_array[y][x] = block


    def control(self, event):
        if(event.key == pygame.K_LEFT):
            self.tetromino.move(direction = "left")
        elif (event.key == pygame.K_RIGHT):
            self.tetromino.move(direction = "right")
        elif(event.key == pygame.K_UP):
            self.tetromino.rotate()

    def check_tetromino_landing(self):
        if self.tetromino.landing:
            self.put_tetromino_block_in_array()
            self.tetromino = Tetromino(self)

    def draw_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pygame.draw.rect(self.app.screen, (30,30,30),
                             (x * TILE_SIZE + GRID_OFFSET, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
                
    
    def update(self):
        if self.app.anim_trigger:
            self.tetromino.update()
            # for block in self.tetromino.blocks:
            #     print(block.pos)
            self.check_tetromino_landing()
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)