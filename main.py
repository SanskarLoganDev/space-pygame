import pygame
import time
import random

WIDTH, HEIGHT = 1535, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge Space") # caption at the top of our window

BG = pygame.transform.scale(pygame.image.load("bg.png"), (WIDTH,HEIGHT)) # to scale

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL =5

def draw(player):
    WIN.blit(BG, (0, 0)) # used to draw an image or surface, (0,0) is the top left of the screen
    pygame.draw.rect(WIN, (255, 0, 0), player)
    pygame.display.update()

def main():
    run = True
    
    player =pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT )
    
    clock = pygame.time.Clock()
    
    while run: # game loop
        clock.tick(60)
        # when the player presses x on the window
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                run = False
                break
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: # code for left arrow key
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT]: # code for right arrow key
            player.x += PLAYER_VEL
        draw(player) # call the draw funciton in every single frame
            
    pygame.quit()

if __name__ == "__main__" : # __main__ is python inbuilt irrespective of the file nameewq
    main()