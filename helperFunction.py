from settings import *


def load_img(path, img_size, scale = 1,colorkey=(255,255,255)):

    type = path.split("/")[-1]
    type = type.split(".")[-1]
    if type == "png":
        img = pygame.image.load(path).convert_alpha()
    else:
        img = pygame.image.load(path).convert()
    img.set_colorkey(colorkey)
    img = pygame.transform.scale(img, (img_size[0], img_size[1]))

    return img