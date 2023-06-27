# Tetris Project


# TODO
# Rapport 
# PPT
# affichage : afficher le score OK
# mode timer : ajouter un timer et game over quand timer = 0 OK
# bouton restart OK
# user : input text + stocker user name dans CSV OK

# La vitesse de chute des blocs peut augmenter progressivement à mesure que le joueur marque des points ou atteint certains objectifs. OK
# mode powerup : ajouter des powerups OK
# commenter le code
# faire les boutons
# ajouter les sons + fx 
# fx : line completé 



from settings import *
from tetris import *
from button import Button
from database import Database
from score_box import ScoreBox


class App:
    def __init__(self):

        self.screen = screen
        self.database = Database()
        # self.database.display()
        self.clock = pygame.time.Clock()
        self.set_tetronimo_speed()
        
        self.play_button = Button(FIELD_RES[0] // 2 + 40, FIELD_RES[1] // 2 - 70, load_img('sprites/Button/play.png', [30,30]), 5)
        self.exit_button = Button(FIELD_RES[0] // 2 + 40, FIELD_RES[1] // 2 + 110, load_img('sprites/Button/quit.png', [30,30]), 5)

        self.next_button = Button(FIELD_RES[0] // 2 + 220, FIELD_RES[1] // 2 + 300, load_img('sprites/Button/next.png', [30,30]), 5)

        self.choose_mode_button = Button(FIELD_RES[0] // 2 + 40, FIELD_RES[1] // 2 - 140, load_img('sprites/Button/choosemode.png', [30,30]), 5)
        self.login_button = Button(FIELD_RES[0] // 2 - 140, FIELD_RES[1] // 2 + 290, load_img('sprites/Button/login.png', [30,30]), 5)
        self.score_button = Button(FIELD_RES[0] // 2 + 40, FIELD_RES[1] // 2 + 55, load_img('sprites/Button/score.png', [30,30]), 5)
        self.back_button = Button(FIELD_RES[0] // 2 - 140, FIELD_RES[1] // 2 + 290, load_img('sprites/Button/back.png', [30,30]), 5)


        self.normal_mode_button = Button(FIELD_RES[0] // 2 + 50, FIELD_RES[1] // 2 + - 240, load_img('sprites/Button/normal.png', [30,30]), 5)
        self.time_mode_button = Button(FIELD_RES[0] // 2 + 50, FIELD_RES[1] // 2 - 40, load_img('sprites/Button/time.png', [30,30]), 5)
        self.powerup_mode_button = Button(FIELD_RES[0] // 2 + 50, FIELD_RES[1] // 2 + 160, load_img('sprites/Button/powerup.png', [30,30]), 5)


        self.restart_button = Button(210,350, load_img('sprites/Button/restart.png', [30,30]), 5)
        self.back_menu_button = Button(210,510, load_img('sprites/Button/backmenu.png', [30,30]), 5)
        self.slowdown_button = Button(370,450, load_img('sprites/Button/slowdown.png', [30,30]), 5)

        # ------------------------ TEXT ---------------------------------------------

        self.title_text = font.render(str("Tetris"),  True, (255,255,255))
        self.register_text = font.render(str("Enter name"),  True, (255,255,255))
        self.choose_mode = font.render(str("choose mode"),  True, (255,255,255))
        self.score_text = font.render(str("Score"),  True, (255,255,255))
        
        self.game_over_text = font.render(str("Game Over"),  True, (255,0,0))

        self.mouse_img = pygame.image.load('sprites/mouse_cursor.png').convert_alpha()
        self.mouse_img = pygame.transform.scale(self.mouse_img, (int(self.mouse_img.get_width() * 4), int(self.mouse_img.get_height() * 4)))

        self.user_name = ""
        self.user_name_text = little_font.render(str(self.user_name), True, (255,255,255))

        self.show_game_title = True
        self.show_register = False
        self.show_menu = False
        self.show_mode = False
        self.show_score = False

        self.show_game = False
        self.show_game_over = False

        self.quit_game = False
        
        self.shade_surface = pygame.Surface((WIN_RES))
        self.shade_surface.fill((0,0,0))
        self.shade_surface.set_alpha(220)

    def set_tetronimo_speed(self, speed = 0, fast_speed = 0):
        self.user_event = pygame.USEREVENT + 0
        self.fast_user_event = pygame.USEREVENT + 1
        # self.timer_event = pygame.USEREVENT + 2 
        self.anim_trigger = False
        pygame.time.set_timer(self.user_event, anim_time_interval + speed)
        pygame.time.set_timer(self.fast_user_event, fast_anim_time_interval + fast_speed)
        # pygame.time.set_timer(self.timer_event, 1000)

    def set_timer_count_down(self):

        self.timer_event = pygame.USEREVENT + 2 
        pygame.time.set_timer(self.timer_event, 1000)


    def update_score_text(self):
        self.current_score_text = font.render((str(self.tetris.score)),  True, (255,255,255)) 

    def choose_page(self, page):

        if(page == "game_title"):
            self.show_game_title = True
            self.show_register = False
            self.show_menu = False
            self.show_mode = False
            self.show_score = False
            self.show_game = False
            self.show_game_over = False


        if(page == "register"):
            self.show_register = True
            self.show_game_title = False
            self.show_menu = False
            self.show_mode = False
            self.show_score = False
            self.show_game = False
            self.show_game_over = False

        if(page == "menu"):
            self.show_menu = True
            self.show_register = False
            self.show_game_title = False
            self.show_mode = False
            self.show_score = False
            self.show_game = False
            self.show_game_over = False

        if(page == "choose_mode"):
            self.show_mode = True
            self.show_game_title = False
            self.show_register = False
            self.show_menu = False
            self.show_score = False
            self.show_game = False
            self.show_game_over = False

        if(page == "score"):
            self.show_score = True
            self.show_mode = False
            self.show_game_title = False
            self.show_register = False
            self.show_menu = False
            self.show_game = False
            self.show_game_over = False

        if(page == "game"):
            self.show_game = True
            self.show_score = False
            self.show_mode = False
            self.show_game_title = False
            self.show_register = False
            self.show_menu = False
            self.show_game_over = False

        if(page == "gameover"):
            self.show_game_over = True
            self.show_score = False
            self.show_mode = False
            self.show_game_title = False
            self.show_register = False
            self.show_menu = False
            self.show_game = True
            
    def update(self):

        # print("counter : ", self.counter)
        # print("coutner max :", self.counter_max)

        self.mouse_pos = pygame.mouse.get_pos()


        press_play_button = self.play_button.update()
        press_quit_button = self.exit_button.update()

        press_next_button = self.next_button.update()

        press_score_button = self.score_button.update()
        press_login_button = self.login_button.update()
        press_choose_mode_button = self.choose_mode_button.update()
        press_back_button = self.back_button.update()
        
        press_normal_mode_button = self.normal_mode_button.update()
        press_time_mode_button = self.time_mode_button.update()
        press_powerup_mode_button = self.powerup_mode_button.update()

        press_restart_button = self.restart_button.update()
        press_slow_down_button = self.slowdown_button.update()


        back_menu_button = self.back_menu_button.update()


        if(press_play_button):
            self.choose_page("register")
            # self.tetris = Tetris(self)

        if(press_quit_button):
            self.quit_game = True

        if(press_next_button):
            if(len(self.user_name) != 0):
                self.user_name_text = little_font.render(str(self.user_name), True, (255,255,255))
                self.choose_page("menu")

        if(press_choose_mode_button):
            self.choose_page("choose_mode")
            pygame.time.wait(100)

        if(press_login_button):
            self.user_name = ""
            self.user_name_text = little_font.render(str(self.user_name), True, (255,255,255))
            self.choose_page("register")
            pygame.time.wait(70)

        if(press_score_button):
            self.best_score = self.database.get_best_score(str(self.user_name))
            self.choose_page("score")

        if(press_back_button):
            self.choose_page("menu")
            pygame.time.wait(100)

        if(press_normal_mode_button):
            # print("normal")
            self.tetris = Tetris(self)
            self.current_score_text = font.render((str(self.tetris.score)),  True, (255,255,255))
            self.update_score_text()
            self.choose_page("game")

        if(press_time_mode_button):
            self.tetris = Tetris(self, mode="time")
            # print("choose time")
            self.counter = TIME_COUNTER
            self.counter_max = self.counter
            self.timer_text = font.render(str(self.counter), True, (255, 255, 255))
            self.current_score_text = font.render((str(self.tetris.score)),  True, (255,255,255)) 
            self.update_score_text()
            self.choose_page("game")
            self.set_timer_count_down()

        if(press_powerup_mode_button):
            # print("powerup")
            self.tetris = Tetris(self, mode="powerup")
            self.current_score_text = font.render((str(self.tetris.score)),  True, (255,255,255))
            self.update_score_text()
            self.choose_page("game")

        if(press_slow_down_button):
            self.tetris.slow_down = not self.tetris.slow_down
            if(self.tetris.slow_down):
                speed = 150
                fast_speed = 15
            else:
                speed = 0
                fast_speed = 30
            self.set_tetronimo_speed(speed, fast_speed)

        if(press_restart_button):
            # create a new tetris with the same attribute of the previous one
            new_tetris = Tetris(self, mode=str(self.tetris.mode))
            restart_fx.play()
            self.tetris = new_tetris
            self.counter = TIME_COUNTER
            self.update_score_text()
            self.choose_page("game")
            # refresh text label of timer
            if(self.tetris.mode == "time"):
                self.timer_text = font.render(str(self.counter), True, (255, 255, 255))
            
            # print(self.tetris.score)

        if(back_menu_button):
            self.choose_page("menu")
            self.counter = TIME_COUNTER
            

        if(self.show_game): 
            self.tetris.update()


    def draw_game_title(self):
        self.screen.fill((255,255,255))
        self.screen.blit(background,(-300,0))
        self.screen.blit(self.title_text,(165,100))
        self.play_button.draw(self.screen)
        self.exit_button.draw(self.screen)

    def draw_register(self):
        self.screen.fill((0,0,0))
        self.screen.blit(background,(-300,0))
        self.screen.blit(self.register_text,(100,100))
        
        pygame.draw.rect(self.screen, (24,27,70), Rect(130,240,300,50))
        self.screen.blit(self.user_name_text, (138,250))
        self.next_button.draw(self.screen)
        # self.screen.blit(background,(-300,0))
        # self.screen.blit(self.title_text,(165,100))
        # self.play_button.draw(self.screen)
        # self.exit_button.draw(self.screen)

    def draw_menu(self):

        self.screen.fill((0,0,0))
        self.screen.blit(background,(-300,0))
        self.choose_mode_button.draw(self.screen)
        self.score_button.draw(self.screen)
        self.login_button.draw(self.screen)
        self.screen.blit(self.user_name_text,(420,700))


    def draw_choose_mode(self):
        self.screen.fill((0,0,0))
        self.screen.blit(background,(-300,0))
        self.screen.blit(self.user_name_text,(420,720))

        self.normal_mode_button.draw(self.screen)
        self.time_mode_button.draw(self.screen)
        self.powerup_mode_button.draw(self.screen)

        self.back_button.draw(self.screen)

    
    def draw_score(self):
        self.screen.fill((0,0,0))
        self.screen.blit(background,(-300,0))
        self.screen.blit(self.score_text,(180,40))
        self.screen.blit(self.user_name_text,(425,700))

        x = 40
        y = 120
        for i,score in enumerate(self.best_score):
            # print("score[2] ; ", score[2])
            scorebox = ScoreBox(self.screen, score[0], score[1], score[2])
            if(i == 0):
                offset = 1
            scorebox.draw(x,y*(i + offset))
                
                
        self.back_button.draw(self.screen)

    def draw_game(self):
        self.screen.fill((BG_COLOR))
        self.slowdown_button.draw(self.screen)
        self.tetris.draw()
        self.screen.blit(self.current_score_text,(395,20))
        self.screen.blit(self.user_name_text, (80,670))
        if(self.tetris.mode == "time"):
            self.screen.blit(self.timer_text, (410,655))
        if(self.tetris.pause == True):
            self.screen.blit(self.shade_surface, (0,0))
            self.screen.blit(font.render(str("Pause"),  True, (255,255,255)), (180,280))
        if(self.show_game_over):
            self.screen.blit(self.shade_surface, (0,0))
            self.screen.blit(self.game_over_text, (127,200))
            self.screen.blit(self.score_text, (140,280))
            self.screen.blit(self.current_score_text, (370,280))

            self.restart_button.draw(self.screen)
            self.back_menu_button.draw(self.screen)



    def draw(self):

        # print(self.counter)
       
        if(self.show_game_title):
            self.draw_game_title()

        if(self.show_register):
            self.draw_register()

        if(self.show_menu):
            self.draw_menu()

        if(self.show_mode):
            self.draw_choose_mode()

        if(self.show_score):
            self.draw_score()

        if(self.show_game):
            self.draw_game()

        screen.blit(self.mouse_img, (self.mouse_pos[0] - 30, self.mouse_pos[1] - 28))
        pygame.display.update()
        self.clock.tick(60)

    def check_events(self):
        self.anim_trigger = False
        self.fast_anim_trigger = False


        for event in pygame.event.get():
            if event.type == QUIT or self.quit_game:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                
                if(self.show_register):
                    if event.key == pygame.K_BACKSPACE:

                        # get text input from 0 to -1 i.e. end.
                        self.user_name = self.user_name[:-1]
        
                    # Unicode standard is used for string
                    # formation
                    else:
                        if(len(self.user_name) < 12):
                            self.user_name += event.unicode

                    self.user_name_text = little_font.render(str(self.user_name), True, (255,255,255))
                    # print(self.user_name)

                
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    if(self.show_game):
                        self.tetris.control(event)
                    
            elif event.type == self.user_event:
                self.anim_trigger = True

            elif event.type == self.fast_user_event:
                self.fast_anim_trigger = True

            elif(self.show_game == True and self.tetris.mode == "time"):
                # print("in")
                if event.type == self.timer_event:
                    if(self.counter != 0):
                        self.counter -= 1
                        timer_fx.play()
                    self.timer_text = font.render(str(self.counter), True, (255, 255, 255))


    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)


if __name__ == '__main__':
    app = App()
    app.run()

