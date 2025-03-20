import pygame
import sys
import random
from char import Char
import sprites 
from sprites import walking_1


pygame.init()
#display diminsions 
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (125, 0, 0)
RED = (255, 0 ,  0)
BLUE= (0, 0, 255)
YELLOW= (255,255,0)

#game variables 

intro_count = 3 
last_count_update = pygame.time.get_ticks()

#display 
screen= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("stinky game")

#framerate 
clock = pygame.time.Clock()
FPS = 60


# load background image
bg_image = pygame.image.load("/home/csd-cs/Documents/Coding Projects/Pygame/characters/background /background.jpeg").convert_alpha()

#load sprites 

fighter_1 = Char(1, 200, 310)
fighter_2 = Char(2, 700, 310)

sprites_1 = pygame.sprite.Group()
sprites_1.add(fighter_1, fighter_2)


#number of steps in animation 


def draw_bg():
   scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
   screen.blit(scaled_bg, (0,0))

#func for health bar 
def draw_health_bar(health, x, y):
   ratio = health / 100 
   pygame.draw.rect(screen, WHITE, (x - 1, y - 1, 404, 34))
   pygame.draw.rect(screen, RED, (x, y, 400, 30))
   pygame.draw.rect(screen, YELLOW,(x, y, 400 * ratio, 30) )




#playersettings

player_width = 150
player_height = 150
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height - 10


#fighters 


#game loop 
run = True 
while run: 
   clock.tick(FPS)
   
   #draw background 

   draw_bg()

   

   #show health stats 
   draw_health_bar(fighter_1.health, 20, 20)
   draw_health_bar(fighter_2.health, 580, 20)


   #char move 
   fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
   fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1)

   #draw fighters 

   #fighter_1.draw(screen)
   #fighter_2.draw(screen)


   sprites_1.draw(screen)
   #eventhandler 

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         run = False 

   #update display 
   pygame.display.update()
   pygame.display.flip
   