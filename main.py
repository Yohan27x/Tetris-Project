# Tetris Project
import pygame as pygame

# Utiliser https://pyga.me/docs/

# UML : 
# diagramme de classe


from settings import *
from tetris import *


class App:
    def __init__(self):
        pygame.init()
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.set_num_channels(64)
        pygame.display.set_caption('Tetris')
        os.environ['SDL_VIDEODRIVER'] = 'directx'
        flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), flags, vsync=True)
        self.clock = pygame.time.Clock()
        self.set_timer()
        self.tetris = Tetris(self)

    def set_timer(self):
        self.user_event = pygame.USEREVENT + 0
        self.anim_trigger = False
        pygame.time.set_timer(self.user_event, ANIM_TIME_INTERVAL)

    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)


    def draw(self):
        self.screen.fill((BG_COLOR))
        self.tetris.draw()
        pygame.display.update()

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