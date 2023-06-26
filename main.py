# Tetris Project

#TODO

# UML :
# diagramme de classe

# functions : 
# - vitesse réglable par le joueur -> AnimTimeInterval -> bouton slow mode 
# La vitesse de chute des blocs peut augmenter progressivement à mesure que le joueur marque des points ou atteint certains objectifs.
# demander nom -> stocker dans csv


from settings import *
from tetris import *
from button import Button


class App:
    def __init__(self):

        self.screen = screen
        self.clock = pygame.time.Clock()
        self.set_timer()
        
        self.play_button = Button(FIELD_RES[0] // 2 - 200, FIELD_RES[1] // 2 - 30, load_img('sprites/Button/play.png', [83,38]), 5)
        self.exit_button = Button(FIELD_RES[0] // 2 - 20, FIELD_RES[1] // 2 + 170, load_img('sprites/Button/quit.png', [62,30]), 5)

        self.next_button = Button(FIELD_RES[0] // 2 + 220, FIELD_RES[1] // 2 + 300, load_img('sprites/Button/next.png', [30,30]), 5)

        self.choose_mode_button = Button(FIELD_RES[0] // 2 + 40, FIELD_RES[1] // 2 - 120, load_img('sprites/Button/choosemode.png', [30,30]), 5)
        self.score_button = Button(FIELD_RES[0] // 2 + 40, FIELD_RES[1] // 2 + 80, load_img('sprites/Button/score.png', [30,30]), 5)
        self.back_button = Button(FIELD_RES[0] // 2 - 130, FIELD_RES[1] // 2 + 320, load_img('sprites/Button/back.png', [30,30]), 5)


        self.normal_mode_button = Button(FIELD_RES[0] // 2 + 50, FIELD_RES[1] // 2 + - 240, load_img('sprites/Button/normal.png', [30,30]), 5)
        self.time_mode_button = Button(FIELD_RES[0] // 2 + 50, FIELD_RES[1] // 2 - 40, load_img('sprites/Button/time.png', [30,30]), 5)
        self.powerup_mode_button = Button(FIELD_RES[0] // 2 + 50, FIELD_RES[1] // 2 + 160, load_img('sprites/Button/powerup.png', [30,30]), 5)


        self.restart_button = Button(130,350, load_img('sprites/Button/restart.png', [62,30]), 5)
        self.slowdown_button = Button(370,20, load_img('sprites/Button/fill.png', [30,30]), 5)

        # ------------------------ TEXT ---------------------------------------------

        self.title_text = font.render(str("Tetris"),  True, (255,255,255))
        self.register_text = font.render(str("Enter name"),  True, (255,255,255))
        self.choose_mode = font.render(str("choose mode"),  True, (255,255,255))
        self.score_text = font.render(str("Score"),  True, (255,255,255))
        self.game_over_text = font.render(str("Game Over"),  True, (255,255,255))

        self.mouse_img = pygame.image.load('sprites/mouse_cursor.png').convert_alpha()
        self.mouse_img = pygame.transform.scale(self.mouse_img, (int(self.mouse_img.get_width() * 4), int(self.mouse_img.get_height() * 4)))

        self.user_name = ""
        self.user_name_text = font.render(str(self.user_name), True, (255,255,255))
        # self.user_name = ""

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
        self.shade_surface.set_alpha(120)

    def set_timer(self, speed = 0):
        self.user_event = pygame.USEREVENT + 0
        self.fast_user_event = pygame.USEREVENT + 1
        self.anim_trigger = False
        pygame.time.set_timer(self.user_event, anim_time_interval + speed)
        pygame.time.set_timer(self.fast_user_event, fast_anim_time_interval + speed)

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

        self.mouse_pos = pygame.mouse.get_pos()


        press_play_button = self.play_button.update()
        press_quit_button = self.exit_button.update()

        press_next_button = self.next_button.update()

        press_score_button = self.score_button.update()
        press_choose_mode_button = self.choose_mode_button.update()
        press_back_button = self.back_button.update()

        press_restart_button = self.restart_button.update()
        press_slow_down_button = self.slowdown_button.update()

        press_normal_mode_button = self.normal_mode_button.update()
        press_time_mode_button = self.time_mode_button.update()
        press_powerup_mode_button = self.powerup_mode_button.update()



        if(press_play_button):
            # print("in")
            self.choose_page("register")
            # self.tetris = Tetris(self)


        if(press_quit_button):
            self.quit_game = True

        if(press_next_button):
            self.user_name = "yohan" # recuperer l'input
            self.user_name_text = font.render(str(self.user_name), True, (255,255,255))
            self.choose_page("menu")

        if(press_choose_mode_button):
            self.choose_page("choose_mode")
            pygame.time.wait(100)

        if(press_score_button):
            self.choose_page("score")

        if(press_back_button):
            self.choose_page("menu")

        if(press_normal_mode_button):
            print("normal")
            self.tetris = Tetris(self)
            self.choose_page("game")

        if(press_time_mode_button):
            print("time")
            self.tetris = Tetris(self, mode="time")
            self.choose_page("game")

        if(press_powerup_mode_button):
            print("powerup")
            self.tetris = Tetris(self, mode="powerup")
            self.choose_page("game")


        if(press_slow_down_button):
            self.tetris.slow_down = not self.tetris.slow_down
            print(self.tetris.slow_down)
            if(self.tetris.slow_down):
                speed = 150
            else:
                speed = 0
            self.set_timer(speed)


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
        self.screen.blit(self.user_name_text,(40,700))


    def draw_choose_mode(self):
        self.screen.fill((0,0,0))
        self.screen.blit(background,(-300,0))
        self.screen.blit(self.user_name_text,(350,700))

        self.normal_mode_button.draw(self.screen)
        self.time_mode_button.draw(self.screen)
        self.powerup_mode_button.draw(self.screen)

        self.back_button.draw(self.screen)

    
    def draw_score(self):
        self.screen.fill((0,0,0))
        self.screen.blit(background,(-300,0))
        self.screen.blit(self.score_text,(180,40))
        self.screen.blit(self.user_name_text,(350,700))
        self.back_button.draw(self.screen)


    def draw_game(self):
        self.screen.fill((BG_COLOR))
        self.slowdown_button.draw(self.screen)
        self.tetris.draw()
        if(self.show_game_over):
            self.screen.blit(self.shade_surface, (0,0))
            self.screen.blit(self.game_over_text, (130,200))
            # self.screen.blit(self.restart_button, (130,140))
            self.restart_button.draw(self.screen)

        

    def draw(self):

       


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
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    self.tetris.control(event)
                    
            elif event.type == self.user_event:
                self.anim_trigger = True

            elif event.type == self.fast_user_event:
                self.fast_anim_trigger = True

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)


if __name__ == '__main__':
    app = App()
    app.run()

