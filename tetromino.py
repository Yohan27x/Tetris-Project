from settings import *

class Block:
    def __init__(self):
        self.surface = pygame.Surface(32,32)
        self.surface.fill((200,120,100))
        self.rect = self.image.get_rect()

