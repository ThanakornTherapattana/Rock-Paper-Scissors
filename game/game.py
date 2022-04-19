#ไฟล์นี้เป็นไฟล์ที่จะประมวลผล logic ต่าง ๆ ในเกม

import pygame
import random
from .constants import (WHITE, BACK, ROCK, PAPER, SCISSORS, WIDTH, HEIGHT, LIST, BACKGROUD, BLACK, FONT
                        , KAKK, WINN)
from .card import Card, cards



class Game:
    #ประกาศปุ่ม การ์ดและวัตถุต่าง ๆ
    def __init__(self, win):
        self.win = win
        self.win_score = 5
        self.__init()
        self.rock = Card(75, 375, ROCK, 0.1)
        self.paper = Card(200, 375, PAPER, 0.1)
        self.scissors = Card(325, 375, SCISSORS, 0.1)
        self.enemy = Card(WIDTH//2, 100, BACK, 0.08)
        
    
    #ทำไว้ใช้รีเซ็ตเริ่มเกมใหม่
    def __init(self):
        self.player_score = 0
        self.bot_score = 0
        
    def reset(self):#reset the game when win or lose
        self.__init()
        
        
    #สุ่มว่าบอทจะเลือกออกอะไรและรีเทินค่า
    def bot_choose(self):
        global bot_random
        bot_random = random.choice(LIST)
        return bot_random
    
    #เปลี่ยนรูปการ์ดของbot
    def change(self):
        print(bot_random)
        bot = bot_random
        if bot == "scissors":
            self.enemy = Card(WIDTH//2, 100, SCISSORS, 0.08)
        elif bot == "rock":
            self.enemy = Card(WIDTH//2, 100, ROCK, 0.08)
        elif bot == "paper":
            self.enemy = Card(WIDTH//2, 100, PAPER, 0.08)
        
    
    #player choose card
    def player_choose(self):
        
        if self.rock.check_mouse_click():
            player_card = LIST[0]
            self.change()
            return player_card
        
        elif self.paper.check_mouse_click():
            player_card = LIST[1]
            self.change()
            return player_card
        
        elif self.scissors.check_mouse_click():
            player_card = LIST[2]
            self.change()
            return player_card
        
    
    #ตรวจคะแนนและเพิ่มคะแนนในแต่ละรอบ
    def check_win(self):
        bot = self.bot_choose()
        x = self.player_choose()
        #ตรวจผล
        if (x=='rock' and bot=='scissors') or (x=='paper' and bot=='rock') or (x=='scissors' and bot=='paper'):
            self.player_score += 1
              
        elif (x=='rock' and bot=='paper') or (x=='paper' and bot=='scissors') or (x=='scissors' and bot=='rock'):
            self.bot_score += 1
            
        else:
            pass
 
    #เช็คว่าคะแนนครบตามที่กำหนดหรือยัง      
    def check_big_win(self):
        if self.player_score == self.win_score:
            WINN.play()
            self.draw_text("WINN", FONT, BLACK, WIDTH//2 - self.txt.get_width()//2, HEIGHT//2 - self.txt.get_height()//2)#แจ้งเตือนว่าชนะ
            pygame.display.update()
            pygame.time.delay(3000)
            self.reset()#reset the game
            
        elif self.bot_score == self.win_score:
            KAKK.play()
            self.draw_text("KAKK", FONT, BLACK, WIDTH//2 - self.txt.get_width()//2, HEIGHT//2 - self.txt.get_height()//2)#แจ้งเตือนว่าแพ้
            pygame.display.update()
            pygame.time.delay(3000)
            self.reset()#reset the game

            
    def draw_text(self,text, font, text_col, x, y) :#draw the text
        self.txt = font.render(text, True, text_col)
        self.win.blit(self.txt, (x, y))
        
    
    #ฟังชั่นต่าง ๆ ด้านบนจะถูกนำมาใช้ด้านล่างนี้    
    def update(self):
        self.win.blit(BACKGROUD, (0,0))#draw background
        
        #draw cards in the list
        for i in cards:
            i.draw(self.win)
        
            
            
        #draw texts
        self.draw_text(f"Player : {self.player_score}", FONT, BLACK, 10, 10)
        self.draw_text(f"Bot : {self.bot_score}", FONT, BLACK, 10, 50)
        
        #เรียกใช้ฟังค์ชั่นเช็คเรื่องการแพ้ชนะ
        self.check_big_win()
        self.check_win()

        pygame.display.update()