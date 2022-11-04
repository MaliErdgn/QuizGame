import pygame
import pandas as pd
import dbtemp


questionNumber = 1
WINDOW_WIDTH = 540
WINDOW_HEIGHT = 960
clicked = False
questionBoxColor = "#F0F4EF"
doğruCevap = 0
yanlışCevap = 0

clock = pygame.time.Clock()
start_btn = pygame.image.load("QuizGame\Buttons\StartTheGame.jpg")
start_btn_rect = start_btn.get_rect(center = (WINDOW_WIDTH / 2,400))


pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
background = pygame.image.load("QuizGame\photos\\background.png").convert_alpha()
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT)) #scaling backgorund to fill the screen
screen.blit(background,(0,0))
screen.blit(start_btn,start_btn_rect)
pygame.font.init()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.event.pump()
    mouse_pos = pygame.mouse.get_pos()


    if start_btn_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] == 1 and clicked == False:
        clicked = True
        screen.blit(background,(0,0))
        dbtemp.soruSorma(questionNumber)
        if pygame.mouse.get_pressed()[0] == 0:
            clicked = False

    pygame.display.update()
    clock.tick(60)
