# Tetris Project
import pygame as pygame

# Utiliser https://pyga.me/docs/

# UML :
# diagramme de classe

# Tetris normal, avec en plus :
# - vitesse réglable par le joueur
# - plusieurs mode de jeu


from settings import *
from tetris import *
from button import play_button, exit_button


class App:
    def __init__(self):

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), flags, vsync=True)
        self.clock = pygame.time.Clock()
        self.set_timer()
        self.tetris = Tetris(self)

        self.in_menu = True
        self.play_button = play_button
        self.exit_button = exit_button
        self.title = font.render(str("Tetris"),  True, (0,0,0))


    def set_timer(self):
        self.user_event = pygame.USEREVENT + 0
        self.anim_trigger = False
        pygame.time.set_timer(self.user_event, ANIM_TIME_INTERVAL)

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.tetris.control(event)
            elif event.type == self.user_event:
                self.anim_trigger = True

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)


if __name__ == '__main__':
    app = App()
    app.run()






# pygame.init()
# pygame.mixer.pre_init(44100, -16, 2, 512)
# pygame.mixer.set_num_channels(64)

# pygame.display.set_caption('Pygame Window')
# os.environ['SDL_VIDEODRIVER'] = 'directx'

# flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED

# screen = pygame.display.set_mode((WIDTH, HEIGHT), flags, vsync=True)

# clock = pygame.time.Clock()

# tetris = Tetris(screen)

# user_event = pygame.USEREVENT + 0
# anim_trigger = False
# pygame.time.set_timer(user_event, ANIM_TIME_INTERVAL)


# while True :

#     screen.fill((BG_COLOR))

#     tetris.draw()
#     tetris.update()

#     for event in pygame.event.get():  # event loop
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()

#         if event.type == KEYDOWN:
#             tetris.control(event)

#         if event.type == KEYUP:
#             pass

#         if event.type == user_event:
#             anim_trigger = True

#     pygame.display.update()
#     clock.tick(60)