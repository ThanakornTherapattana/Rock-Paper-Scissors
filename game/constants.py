import pygame
pygame.init()

#ไฟล์นี้ใช้กำหนดค่าต่าง ๆ ในเกมที่ไม่มีการเปลี่ยนแปลง
WIDTH, HEIGHT = 400, 500

WHITE = (255, 255, 255)
BLACK = (0,0,0)

LIST = ["rock", "paper", "scissors"]
#font
FONT = pygame.font.SysFont('Impact', 30)

#image 
ROCK = pygame.image.load("Assets/rock.png")
PAPER = pygame.image.load("Assets/paper.png")
SCISSORS = pygame.image.load("Assets/scissors.png")
BACK = pygame.image.load("Assets/back.png")
BACKGROUD = pygame.image.load("Assets/background.png")

#sound
KAKK = pygame.mixer.Sound("sound/kakk.wav")
CHOOSING = pygame.mixer.Sound("sound/choose.wav")
WINN = pygame.mixer.Sound("sound/winn.wav")
CLICK = pygame.mixer.Sound("sound/click.wav")