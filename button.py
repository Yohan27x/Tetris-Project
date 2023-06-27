from settings import *

pygame.mixer.init()

mouse_on_button_fx = pygame.mixer.Sound('audio/mouse_on_button.wav')
mouse_on_button_fx.set_volume(0.2)

click_on_button_fx = pygame.mixer.Sound('audio/click_on_button.wav')
click_on_button_fx.set_volume(0.6)


# Class and functions

class Button():
    def __init__(self, x, y, img, scale):

        self.width = img.get_width()
        self.height = img.get_height()

        self.mouse_pos = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)  # rendre invisible le curseur " de base "

        self.image = pygame.transform.scale(img, (int(self.width * scale), int(self.height * scale)))

        self.new_mouse_img = pygame.image.load('sprites/mouse_cursor.png').convert_alpha()
        self.new_mouse_img = pygame.transform.scale(self.new_mouse_img, (int(self.new_mouse_img.get_width() * 4), int(self.new_mouse_img.get_height() * 4)))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.clicked = False

        self.play_sound = 1

        self.is_active = False

    def draw(self, display):

        self.is_active = True

        display.blit(self.image, (self.rect.x, self.rect.y))
        # display.blit(self.new_mouse_img, (self.mouse_pos[0] - 30, self.mouse_pos[1] - 28))

        # pygame.draw.rect(display, color, self.rect)
        
    def update(self):

        if(self.is_active):

            action = False
            mouse_collide = False

            self.mouse_pos = pygame.mouse.get_pos()
            # get mouse position
    
            if self.rect.collidepoint(self.mouse_pos):
                if self.play_sound == 1:
                    # mouse_on_button_fx.play()
                    self.play_sound = 0

                mouse_collide = True

            else:
                self.play_sound = 1


            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and mouse_collide == True:
                click_on_button_fx.play()
                action = True
                self.clicked = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            if self.clicked == True:
                pass

            
            self.is_active = False
            return action



# ------------------------------------------------------------------------ #




# load buttons
#play
# image_play_button = load_img('sprites/Button/play.png', [83,38])

# #exit
# image_exit_button = load_img('sprites/Button/quit.png', [62,30])


# image_restart_button_unclick = pygame.image.load('Images/Buttons/Restart/0.png').convert_alpha()
# image_restart_button_mouse_on = pygame.image.load('Images/Buttons/Restart/1.png').convert_alpha()

# restart_button_list = [image_restart_button_unclick, image_restart_button_mouse_on]

# title_img = pygame.image.load('Images/Logo/title.png').convert_alpha()
# title_img = pygame.transform.scale(title_img,(title_img.get_width() * 5, title_img.get_height() * 5))


# play_button = Button(FIELD_RES[0] // 2 - 20, FIELD_RES[1] // 2 - 30, image_play_button, 5)
# exit_button = Button(FIELD_RES[0] // 2 - 20, FIELD_RES[1] // 2 + 170, image_exit_button, 5)
# restart_button = Button(SCREEN_WIDTH // 2 - 157, SCREEN_HEIGHT // 2 - 85, restart_button_list, 5)


