import pygame

pygame.init()

class Krekhead():
    def __init__(self):

        self.main_x = 0
        self.main_y = 0
        self.window_width = 1100
        self.window_height = 900
        self.caption = "KREKHEAD"

    def initialize(self):
        win = pygame.display.set_mode((self.window_width,self.window_height))
        pygame.display.set_caption(self.caption)
        return win
    
    def check_for_close(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
    
class Krek():
    def __init__(self,main_x,main_y,x,y):

        self.x = x+main_x
        self.y = y+main_y
        self.width = 50
        self.height = 50
        self.color = (255,255,0)


    def create_character(self):
        rect = pygame.Rect(self.x,self.y,self.width,self.height)
        return rect


    def draw(self,win):
        rect = self.create_character()

        pygame.draw.rect(win,self.color,rect)

    def move(self,x,y):
        self.x += x
        self.y += y


krek = Krekhead()
win = krek.initialize()

player = Krek(krek.main_x,krek.main_y,500,400)


run = True
move_left = False
move_right = False
steps = 1


while run:
    win.fill((150,150,150)) 
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_RIGHT:
                    move_right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                elif event.key == pygame.K_RIGHT:
                    move_right = False
                
    if move_left:
        player.move(-steps,0)
    elif move_right:
        player.move(steps,0)

    player.draw(win)



    pygame.display.flip()

pygame.quit()
    

        




