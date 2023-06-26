from settings import *

class ScoreBox:
    def __init__(self, screen, name, score, mode):

        self.screen = screen

        self.name = little_font.render(name, True, (255,255,255))
        self.score = little_font.render(str(score), True, (255,255,255))
        self.mode = little_font.render(mode, True, (255,255,255))
        

    def draw(self, x,y):
        pygame.draw.rect(self.screen, (24,27,70), Rect(x,y,490,50))
        self.screen.blit(self.name, (x + 15 ,y + 10))
        self.screen.blit(self.score, (x*5.6,y + 10))
        self.screen.blit(self.mode, (x*8.7,y + 10))