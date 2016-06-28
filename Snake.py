import pygame
import sys
from pygame.locals import *

pygame.init()

#set display
screen = pygame.display.set_mode((650, 467))
background = pygame.image.load("titlepage.png").convert_alpha()
screen.blit(background, (0,0))
pygame.display.set_caption("Tron")
font = pygame.font.SysFont(None, 36)

#initialize timer
main_clock = pygame.time.Clock()

#initialize P1's life status and movements
aliveP1 = True

p1 = pygame.Rect(0, 0, 25, 25)

p1Speed = 26

moveLeftP1 = False
moveRightP1 = False
moveUpP1 = False
moveDownP1 = False

snake1 = []

#initialize P2's life status and movements
aliveP2 = True

p2 = pygame.Rect(624, 443, 25, 25)

p2Speed = 26

moveLeftP2 = False
moveRightP2 = False
moveUpP2 = False
moveDownP2 = False

snake2 = []

#space
space = False
#methods
def drawScreen():
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))

def drawPlayer1(p1):
    p1= pygame.draw.rect(screen, (81, 167, 237), p1)
    snake1.append(p1)

def drawPlayer2(p2):
    p2= pygame.draw.rect(screen, (41, 227, 100), p2)
    snake2.append(p2)

def draw_text(display_string, font, surface, x, y):
    text_display = font.render(display_string, 1, (247, 132, 0))
    text_rect = text_display.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_display, text_rect)

drawScreen()
draw_text("Press Space to Begin", font, screen, 200, 50)
drawPlayer1(p1)
drawPlayer2(p2)
while True:
    
    
    #check for events
    for event in pygame.event.get():
        #Keyboard input for players
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_RETURN:

                aliveP1 = True
                p1 = pygame.Rect(0, 0, 25, 25)
                moveLeftP1 = False
                moveRightP1 = False
                moveUpP1 = False
                moveDownP1 = False
                snake1 = []

                aliveP2 = True
                p2 = pygame.Rect(624, 443, 25, 25)
                moveLeftP2 = False
                moveRightP2 = False
                moveUpP2 = False
                moveDownP2 = False
                snake2 = []

                drawScreen()
                drawPlayer1(p1)
                drawPlayer2(p2)

                draw_text("Press Space to Begin", font, screen, 200, 50)
                
            if event.key == K_SPACE:
                space = True
                
                drawScreen()

                p1= pygame.draw.rect(screen, (81, 167, 237), p1)
                p2= pygame.draw.rect(screen, (41, 227, 100), p2)
                
                moveLeftP1 = False
                moveRightP1 = True
                moveUpP1 = False
                moveDownP1 = False

                moveLeftP2 = True
                moveRightP2 = False
                moveUpP2 = False
                moveDownP2 = False
            #Player 1 keys
            if event.key == K_a and space:
                moveLeftP1 = True
                moveRightP1 = False
                moveUpP1 = False
                moveDownP1 = False
            if event.key == K_d and space:
                moveLeftP1 = False
                moveRightP1 = True
                moveUpP1 = False
                moveDownP1 = False
            if event.key == K_w and space:
                moveLeftP1 = False
                moveRightP1 = False
                moveUpP1 = True
                moveDownP1 = False
            if event.key == K_s and space:
                moveLeftP1 = False
                moveRightP1 = False
                moveUpP1 = False
                moveDownP1 = True
            #Player 2 keys
            if event.key == K_LEFT and space:
                moveLeftP2 = True
                moveRightP2 = False
                moveUpP2 = False
                moveDownP2 = False
            if event.key == K_RIGHT and space:
                moveLeftP2 = False
                moveRightP2 = True
                moveUpP2 = False
                moveDownP2 = False
            if event.key == K_UP and space:
                moveLeftP2 = False
                moveRightP2 = False
                moveUpP2 = True
                moveDownP2 = False
            if event.key == K_DOWN and space:
                moveLeftP2 = False
                moveRightP2 = False
                moveUpP2 = False
                moveDownP2 = True
                
    #Ensure consistent frames per second
    main_clock.tick(5)

    #Move the player
    if aliveP1 and aliveP2:
        if moveLeftP1:
            if p1.left < 0:
                aliveP1 = False
            else:
                p1.x -= p1Speed
                drawPlayer1(p1)
        if moveRightP1:
            if p1.right > 640:
                aliveP1 = False
            else:
                p1.x += p1Speed
                drawPlayer1(p1)
        if moveUpP1:
            if p1.top < 0:
                aliveP1 = False
            else:
                p1.y -= p1Speed
                drawPlayer1(p1)
        if moveDownP1:
            if p1.bottom > 460:
                alive = False
            else:
                p1.y += p1Speed
                drawPlayer1(p1)

        #snake1.append(p1)
            
        if moveLeftP2:
            if p2.left < 19:
                aliveP2 = False
            else:
                p2.x -= p2Speed
                drawPlayer2(p2)
        if moveRightP2:
            if p2.right > 640:
                aliveP2 = False
            else:
                p2.x += p2Speed
                drawPlayer2(p2)
        if moveUpP2:
            if p2.top < 19:
                aliveP2 = False
            else:
                p2.y -= p2Speed
                drawPlayer2(p2)
        if moveDownP2:
            if p2.bottom > 460:
                aliveP2 = False
            else:
                p2.y += p2Speed
                drawPlayer2(p2)

        #snake2.append(p2)

        #check for collisions P1
        for item in snake2:
            if p1.colliderect(item):
                aliveP1 = False     
        for i in range(0,len(snake1) -1):
            if p1.colliderect(snake1[i]):
                aliveP1 = False

        for item in snake1:
            if p2.colliderect(item):
                aliveP2 = False
        for i in range(0,len(snake2) -1):
            if p2.colliderect(snake2[i]):
                aliveP2 = False

    elif not aliveP1:
        draw_text("Player 2 wins!", font, screen, 255, 5)
        draw_text("Press Enter to Play Again", font, screen, 180, 50)
        space = False
    elif not aliveP2:
        draw_text("Player 1 wins!", font, screen, 255, 5)
        draw_text("Press Enter to Play Again", font, screen, 180, 50)
        space = False
    else:
        draw_text("Tie", font, screen, 255, 5)
        draw_text("Press Enter to Play Again", font, screen, 180, 50)
        space = False

    pygame.display.update()
