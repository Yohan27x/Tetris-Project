# Tetris Project

#TODO

# UML :
# diagramme de classe

# functions : 
# - vitesse réglable par le joueur -> AnimTimeInterval -> bouton slow mode 
# - boutton pause dans instance tetris
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
        self.restart_button = Button(130,350, load_img('sprites/Button/restart.png', [62,30]), 5)
        self.slowdown_button = Button(370,20, load_img('sprites/Button/fill.png', [30,30]), 5)

        self.title_text = font.render(str("Tetris"),  True, (255,255,255))
        self.score_text = font.render(str("Score"),  True, (255,255,255))
        self.game_over_text = font.render(str("Game Over"),  True, (255,255,255))

        
        self.user_name = "yohan"

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


        press_play_button = self.play_button.update()
        press_quit_button = self.exit_button.update()
        press_restart_button = self.restart_button.update()
        press_slow_down_button = self.slowdown_button.update()

        if(press_slow_down_button):
            self.tetris.slow_down = not self.tetris.slow_down
            print(self.tetris.slow_down)
            if(self.tetris.slow_down):
                speed = 150
            else:
                speed = 0
            self.set_timer(speed)


        if(press_play_button):
            print("in")
            self.choose_page("game")
            self.tetris = Tetris(self)

        if(press_quit_button):
            self.quit_game = True

        if(self.show_game): 
            self.tetris.update()

    def draw_game_title(self):
        self.screen.fill((255,255,255))
        self.screen.blit(background,(-300,0))
        self.screen.blit(self.title_text,(165,100))
        self.play_button.draw(self.screen)
        self.exit_button.draw(self.screen)


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
        
        elif(self.show_game):
            self.draw_game()

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

