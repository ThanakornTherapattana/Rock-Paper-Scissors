import pygame
from .constants import CHOOSING, CLICK

cards = []#list
class Card:
    #สร้างการ์ดแต่ละใบกำหนดค่าเริ่มต้น
    def __init__(self, x, y, image, scale):
        self.width, self.height = image.get_width(), image.get_height()
        self.scale = scale
        self.image = image
        self.image = pygame.transform.scale(self.image, (int(self.width*self.scale)
                                                         , int(self.height*self.scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False
        self.sound = True
        self.y_limit = self.rect.y - 30
        self.y_original = self.rect.y
        cards.append(self)#add card to list
        
    #วาดการ์ด
    def draw(self, win):
        #(image, (x position, y position))
        win.blit(self.image, (self.rect.x, self.rect.y))
        
        
    #check when clicked or collide with mouse
    def check_mouse_click(self):
        action = False
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos) :
            if self.sound == True:#sound control
                CHOOSING.play()
                self.sound = False
                
            #card animation(เลื่อนขึ้น)
            if self.rect.y > self.y_limit:
                self.rect.y -= 5
                
            #check clicked
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False :
                CLICK.play()
                action = True
                self.clicked = True
                
        else:#พอเมาส์ไม่ซ้อนกับการ์ดแล้วการ์ดเลื่อนลง
            self.sound = True
            if self.rect.y <= self.y_original:
                self.rect.y += 5

                
        if pygame.mouse.get_pressed()[0] == 0 :
            self.clicked = False
            
        return action