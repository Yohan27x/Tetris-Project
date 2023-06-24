# Tetris Project

#TODO

# UML :
# diagramme de classe

# functions : 
# - vitesse réglable par le joueur -> AnimTimeInterval
# - boutton pause dans instance tetris
# demander nom -> stocker dans csv



from settings import *
from tetris import *
from button import play_button, exit_button


class App:
    def __init__(self):

        self.screen = screen
        self.clock = pygame.time.Clock()
        self.set_timer()
        self.tetris = Tetris(self)

        self.in_menu = True
        self.play_button = play_button
        self.exit_button = exit_button
        self.title = font.render(str("Tetris"),  True, (0,0,0))


    def set_timer(self):
        self.user_event = pygame.USEREVENT + 0
        self.fast_user_event = pygame.USEREVENT + 1
        self.anim_trigger = False
        pygame.time.set_timer(self.user_event, ANIM_TIME_INTERVAL)
        pygame.time.set_timer(self.fast_user_event, FAST_ANIM_TIME_INTERVAL)

    def update(self):
        if(self.in_menu):
             press_button = self.play_button.update()
             self.exit_button.update()
             if(press_button == True):
                 self.in_menu = False
        else:
            self.tetris.update()

    def draw(self):

        if(self.in_menu):
            self.screen.fill((255,255,255))
            self.screen.blit(self.title,(100,120))
            self.play_button.draw(self.screen)
            self.exit_button.draw(self.screen)
        else:
            self.screen.fill((BG_COLOR))
            self.tetris.draw()

        pygame.display.update()
        self.clock.tick(60)

    def check_events(self):
        self.anim_trigger = False
        self.fast_anim_trigger = False

        for event in pygame.event.get():
            if event.type == QUIT:
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

