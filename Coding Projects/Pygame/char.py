#imports 
import pygame
import sys
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

#character class one 

class Char(pygame.sprite.Sprite): 
 def __init__(self, player,  x, y, ):
  self.player = player
  self.flip = False 
  super().__init__()
 
  self.vel_y = 0
  self.jump = False 
  self.attacking = False 
  self.attack_type = 0
  self.health = 100
  self.alive = True
  self.attack_delay = 500
  self.frame_delay = 100
  self.last_update = pygame.time.get_ticks()
  self.dir = "/home/csd-cs/Documents/Coding Projects/Pygame/sprites/"
  #sprite files 
  self.current_frame = 0
  self.animation_idle_1 = pygame.image.load(f"{self.dir}idle/idle.png")
  self.animation_walking_1 = [pygame.image.load(f"{self.dir}walking_1/walking{i}.png") for i in range(1,10)]
  self.animation_attack_1_char_1 = [pygame.image.load(f"{self.dir}crowgun/crowgun{i}.png")for i in range (1, 9)]
  self.image = self.animation_idle_1
  self.rect = self.image.get_rect()
  self.rect.x = x




 def move(self, screen_width, screen_height, surface, target):
  SPEED = 2.5
  GRAVITY = 2
  dx = 0
  dy = 0
  now = pygame.time.get_ticks()
  
  print(self.attacking)
  #keyrec

  key = pygame.key.get_pressed()

  #attack limit
  if self.alive == True:
    if self.health == 0 :
        self.alive = False
  #checks player 1 controls 
  
    if self.player == 1:
     #self.animation_idle_1.draw(screen)
     
        #movement 
     if key[pygame.K_a]:
                dx = -SPEED
                if now - self.last_update > self.frame_delay:
                    self.current_frame = (self.current_frame -1) % len(self.animation_walking_1)
                    self.image = self.animation_walking_1[self.current_frame]
                    self.last_update = now

     if key[pygame.K_d]:
                dx = SPEED 
                if now - self.last_update > self.frame_delay:
                    self.current_frame = (self.current_frame + 1) % len(self.animation_walking_1)
                    self.image = self.animation_walking_1[self.current_frame]
                    self.last_update = now          

     #jump
     if key[pygame.K_w] and self.jump == False:
                self.vel_y = - 30
                self.jump = True 

            #attack 
     if key[pygame.K_r] :

         if now - self.last_update > self.attack_delay and not self.attacking :
          self.attack(surface, target , self.attack_type)
          self.attacking = True
          self.last_update = now
     else:
        self.attacking = False

                #which attack type 
    if key[pygame.K_r]: 
            if now - self.last_update > self.attack_delay and not self.attacking :
             self.attack_type
            
            
     #elif key[pygame.K_t]:
        #if now - self.last_update > self.attack_delay and not self.attacking:
        # self.attack_type == 2  
        # self.attacking = True
       #  self.last_update = now
    else:
        self.attacking = False

        #checks player 2 controls 
    if self.player == 2:
    #movement 
        if key[pygame.K_LEFT]:
            dx = -SPEED 
            if now - self.last_update > self.frame_delay:
                    self.current_frame = (self.current_frame + 1) % len(self.animation_walking_1)
                    self.image = self.animation_walking_1[self.current_frame]
                    self.last_update = now          
        if key[pygame.K_RIGHT]:
            dx = SPEED 
            if now - self.last_update > self.frame_delay:
                    self.current_frame = (self.current_frame + 1) % len(self.animation_walking_1)
                    self.image = self.animation_walking_1[self.current_frame]
                    self.last_update = now          

        #jump
        if key[pygame.K_UP] and self.jump == False:
            self.vel_y = - 30
            self.jump = True 

        #attack 
        if key[pygame.K_m]: 
         if now - self.last_update > self.attack_delay and not self.attacking :
          self.attack(surface, target , self.attack_type)
          self.attacking = True
          self.last_update = now
        else:
            self.attacking = False

        


            #which attack type 
        if key[pygame.K_m]:
            self.attack_type == 1 
            if now - self.last_update > self.attack_delay and not self.attacking :
             self.attack_type
        




    #gravity 
  self.vel_y += GRAVITY 
  dy += self.vel_y

  #screen frame 
  if self.rect.left + dx < 0:
    dx = -self.rect.left
  if self.rect.right + dx > screen_width :
    dx = screen_width - self.rect.right 
  if self.rect.bottom + dy > screen_height - 110: 
    self.vel_y = 0 
    self.jump = False 
    dy = screen_height - 110 - self.rect.bottom

   #ensure players face eachother 
  if target.rect.centerx > self.rect.centerx:
     self.flip = False 
  else :
     self.flip = True 
     self.image = pygame.transform.flip(self.animation_walking_1[self.current_frame], True, False)
     

 #update player postion 
  self.rect.x += dx 
  self.rect.y += dy


 def attack(self, surface, target, type):
     now = pygame.time.get_ticks() 

     if now - self.last_update > self.frame_delay :
             self.current_frame = (self.current_frame + 1) % len(self.animation_attack_1_char_1)
             self.image = self.animation_attack_1_char_1[self.current_frame]
             self.last_update = now
     attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip ), self.rect.y, 2 * self.rect.width, self.rect.height)
     if attacking_rect.colliderect(target.rect):
       target.health -= 10 

     pygame.draw.rect(surface, (0, 255, 0), attacking_rect)


 def draw(self, surface):
  pygame.draw.rect(surface, (255, 0, 0 ), self.rect)