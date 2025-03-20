import sys
import pygame 
import random 
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
class Player:
    def __init__(self, x, y, width, height, color, speed):
        self.x = x  
        self.y = y  
        self.width = width  
        self.height = height  
        self.color = color  
        self.speed = speed  
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)  #

    def move(self, keys):
        # Move left
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        # Move right
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        # Move up
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        # Move down
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

    