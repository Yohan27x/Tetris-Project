from settings import *

class Block(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()
        self.image = pygame.Surface((32,32))
        self.image.fill((200,120,100))
        self.rect = self.image.get_rect()

    # def update(self):
    #     pass

    # def draw(self):


