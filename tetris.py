from settings import *
from tetromino import Tetromino


class Tetris:
    def __init__(self,app):
        self.app = app
        self.sprite_group = pygame.sprite.Group()
        self.field_array = self.get_field_array()
        self.tetromino = Tetromino(self)
        self.next_tetromino = Tetromino(self, current=False)
        self.speed_up = False

        self.score = 0
        self.full_lines = 0
        self.point_per_lines = {0:0, 1:100, 2:300, 3:700, 4:2000}


    def get_score(self):
        self.score += self.point_per_lines[self.full_lines]
        self.full_lines = 0

    def get_field_array(self):
        # return an empty array that represent the tetris field
        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]
    
    def is_game_over(self):
        if self.tetromino.blocks[0].pos.y == INIT_POS_OFFSET[1]:
            pygame.time.wait(300)
            return True

    
    def check_full_lines(self):
        row = FIELD_H - 1
        for y in range(FIELD_H - 1, -1, -1):
            for x in range(FIELD_W):
                self.field_array[row][x] = self.field_array[y][x]

                if self.field_array[y][x]:
                    self.field_array[row][x].pos = vec(x, y)

            if sum(map(bool, self.field_array[y])) < FIELD_W:
                row -= 1
            else:
                for x in range(FIELD_W):
                    self.field_array[row][x].alive = False
                    self.field_array[row][x] = 0

                self.full_lines += 1
    
    def put_tetromino_block_in_array(self):
        # when tetromino land, add it to the field list with the right coordinates

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
        elif(event.key == pygame.K_DOWN):
            self.speed_up = True

    def check_tetromino_landing(self):
        # if the active tetromino land, then put in the array and create a new one that will then fall 
        if self.tetromino.landing:
            if self.is_game_over():
                self.__init__(self.app)
            else:
                self.put_tetromino_block_in_array()
                self.next_tetromino.current = True
                self.tetromino = self.next_tetromino
                self.next_tetromino = Tetromino(self, current=False)
                self.speed_up = False

    def draw_grid(self):
        # draw the grid
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pygame.draw.rect(self.app.screen, (30,30,30),
                             (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
                
    
    def update(self):
        trigger = None
        if self.speed_up == True:
            trigger = self.app.fast_anim_trigger
        else:
            trigger = self.app.anim_trigger

        if trigger:
            self.check_full_lines()
            self.tetromino.update()
            self.check_tetromino_landing()
            self.get_score()
            print(self.score)
        self.sprite_group.update()

    def draw(self):
        # draw the grid and the sprites
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)