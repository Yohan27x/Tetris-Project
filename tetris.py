from settings import *
from tetromino import Tetromino, Block



class Tetris:
    def __init__(self,app, mode="normal"):
        self.app = app
        self.mode = mode
        self.sprite_group = pygame.sprite.Group()
        self.field_array = self.get_field_array()
        self.tetromino = Tetromino(self)
        self.next_tetromino = Tetromino(self, current=False)
        self.speed_up = False
        self.slow_down = False

        self.score = 0
        self.full_lines = 0
        self.point_per_lines = {0:0, 1:100, 2:300, 3:700, 4:2000}

        self.speed_change = True



    def get_score(self):
        
        win_point = self.point_per_lines[self.full_lines]
        self.score += win_point

        if(win_point != 0):
            self.app.update_score_text()

        self.full_lines = 0

       

    def get_field_array(self):
        # return an empty array that represent the tetris field
        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]
    
    def is_game_over(self, check_on_landing=True):


        # print("self.app.counter : ", self.app.counter)

        if(self.mode == "time"):
            if(self.app.counter == 0):
                print("in")
                return True
            
        if(check_on_landing):
            if (self.tetromino.blocks[0].pos.y == INIT_POS_OFFSET[1]):
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

    
    def close_tetris(self):
        self.app.choose_page("gameover")
        self.app.database.append(self.app.user_name, self.score, self.mode)



    def control(self, event):

        if(self.app.show_game_over == False):


            if(event.key == pygame.K_LEFT):
                self.tetromino.move(direction = "left")
            elif (event.key == pygame.K_RIGHT):
                self.tetromino.move(direction = "right")
            elif(event.key == pygame.K_UP):
                self.tetromino.rotate()
            elif(event.key == pygame.K_DOWN):
                self.speed_up = True
            elif(event.key == pygame.K_p):
                self.app.set_timer(-149)
            # elif(event.key == pygame.K_p):
            #     for x in range(FIELD_W): 
            #         for y in range(FIELD_H):
            #             # print(self.field_array[y][x])
            #             # print(type(self.field_array[y][x]))
            #             if(isinstance(self.field_array[y][x], Block)):
            #                 # print(self.field_array[y][x].tetromino.color)
            #                 if self.field_array[y][x].tetromino.color == "red":
            #                     self.field_array[y][x].tetromino.clear()
            #                     self.field_array[y][x] = 0
                                


    def check_tetromino_landing(self):
        # if the active tetromino land, then put in the array and create a new one that will then fall 
        if self.tetromino.landing:
            # print("enter game over check")
            # print(self.is_game_over())
            if self.is_game_over():
                if(self.app.show_game_over == False):
                    self.close_tetris()
                    
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
        if(self.app.show_game_over == False):

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
                # print(self.score)

        
            if(self.mode == "time"):
                if self.is_game_over(check_on_landing=False):
                    if(self.app.show_game_over == False):
                        self.close_tetris()
                        
        


        


        # if((self.score == 300 or self.score == 1000 or self.score == 2000) and self.speed_change == False):
        #     self.speed_change = True

        # if(self.slow_down == False):
        #     if(self.speed_change):
        #         if(self.score == 300):
        #             self.app.set_timer(anim_time_interval - 200)

        #         elif(self.score == 1000):
        #             self.app.set_timer(anim_time_interval - 250)

        #         elif(self.score == 2000):
        #             self.app.set_timer(anim_time_interval - 299)


        #         self.speed_change = not self.speed_change
        
        
        self.sprite_group.update()

    def draw(self):
        # draw the grid and the sprites
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)