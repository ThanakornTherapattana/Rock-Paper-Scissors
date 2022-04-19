#รันไฟล์นี้ผ่าน vscode

import pygame
from game.constants import  WIDTH, HEIGHT
from game.game import Game

#set caption and icon
WIN = pygame.display.set_mode((WIDTH, HEIGHT))#set resolution
pygame.display.set_caption('Rock Paper Scissors')#set title

programIcon = pygame.image.load('Assets/back.png')#set icon
pygame.display.set_icon(programIcon)


#main loop
def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    
    while run:
        clock.tick(60)#set fps
        
        #การออกเกมเมื่อกดกากะบาด
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
        
        game.update()
          
    pygame.quit()
  
#call function   
if __name__ == '__main__' :
    main()