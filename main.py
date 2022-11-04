import re
import time
import random
import pygame
from sys import exit
import pandas as pd

def oyun():
    global content
    global quick
    global soruSayısı
    # with open ("QuizGame\soru\soru.txt", encoding="UTF-8") as f:
    #     content = f.readlines()
    # for i in content:
    #     a = i.strip("\n") #readlines her satırın sonuna \n koyuyuor onu sildik
    #     split = re.split("\? ", a) #soruları ve cevapları ayırdık
    #     sorularMain[split[0]] = split[1]

    print("Quiz Oyununa Hoş Geldiniz")
    quick = int(input("Hızlıca 10 tane soru cevaplamak için 1'e, kendi istediğiniz miktarda soru cevaplamak için 2'ye, süreye karşı (120sn) oynamak için 3e, Maraton (3 yanlış yapana kadar oynamak) için 4e basın: "))
    pygame.display.update()
    match quick:
        case 1:
            soruSayısı = 10
            hizliOyun()
        case 2:
            soruSayısı = int(input("Kaç tane soru cevapalamak istiyorsunuz? "))
            hizliOyun()
        case 3:
            timeRace()
        case 4:
            Marathon()
        case _:
            print("Yanlış tuşlama")
            quit()

def hizliOyun():
    global sorular
    global dogruCevap
    dogruCevap = 0
    sorular = sorularMain
    soruSorma()

def sonuçlar():
    global dogruSayisi
    global yanlışSayısı
    print(f"Puanınız: {puan}")
    print (f"Doğru cevap sayısı: {dogruSayisi}")
    print (f"Yanlış cevap sayısı: {yanlışSayısı}")
    print (f"Toplam soru sayısı: {dogruSayisi + yanlışSayısı}")
    


def cevap ():
    global yanlışSayısı
    global puan
    global dogruSayisi
    if answer.lower() == dogruCevap: 
        print("Doğru")
        puan += 1
        dogruSayisi += 1
    else:
        print("Yanlış")
        puan -= 0.25
        print(f"Doğru cevap: {dogruCevap}")
        yanlışSayısı += 1

def timeRace():
    global current_time
    global dogruCevap
    global sorular
    global answer
    global x
    global soruSayısı
    sorular = sorularMain
    start_time = pygame.time.get_ticks()
    soruSayısı = len(sorular)
    while current_time < 10000:
        for x in range(0,soruSayısı):
            pygame.display.update()
            current_time = pygame.time.get_ticks() - start_time
            screen.blit(currentTimeTimeRace_text,currentTimeTimeRace_textRect)
            soru, dogruCevap = random.choice(list(sorular.items()))
            answer = input(f"{soru}? ")
            if current_time > 10000:
                print("Soruyu zamanında cevaplandıramadınız")
                break
            cevap()
            sorular.pop(soru)
            if current_time > 10000:
                break
    print("Süre Bitti")
    sonuçlar()

def Marathon():
    global dogruCevap
    global sorular
    global answer
    global x
    global soruSayısı
    sorular = sorularMain
    soruSayısı = len(sorular)
    while yanlışSayısı != 3:
        for x in range(0,soruSayısı):
            soru, dogruCevap = random.choice(list(sorular.items()))
            answer = input(f"{soru}? ")
            cevap()
            if yanlışSayısı == 3:
                print("3 Tane yanlış cevap verdiniz")
                break
            sorular.pop(soru)
        print(f"Verdiğiniz doğru cevap sayısı = {dogruSayisi}")

WINDOW_WIDTH = 540
WINDOW_HEIGHT = 960
puan = 0
dogruSayisi = 0
yanlışSayısı = 0
soru = 0
current_time = 0
sorular = {}
sorularMain = {}
loginScreen_active= True
game_active = True
clicked = False
# pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
# pygame.display.set_caption("Genel Kültür Quiz")
# clock = pygame.time.Clock()
test_font = pygame.font.Font("QuizGame\Fonts\Anonymous_Pro.ttf",30)

# start_btn = pygame.image.load("QuizGame\Buttons\StartTheGame.jpg")
# start_btn_rect = start_btn.get_rect(center = (WINDOW_WIDTH / 2,400))
# quit_btn = pygame.image.load("QuizGame\Buttons\Quit.jpg")
# quit_btn_rect = quit_btn.get_rect(center = (WINDOW_WIDTH / 2,550))

# genelKültürQuiz_text = test_font.render("Genel Kültür Quiz", False, "white")
# genelKültürQuiz_textRect = genelKültürQuiz_text.get_rect(center = (WINDOW_WIDTH / 2 , 250))

currentTimeTimeRace_text = test_font.render(f"{current_time/1000}", False, "white")
currentTimeTimeRace_textRect = currentTimeTimeRace_text.get_rect(center = (WINDOW_WIDTH / 2 , 50))
oyun()

# quick = ""
# quick_surface = test_font.render(quick, False, "black")

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#         if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#             game_active = False
#             loginScreen_active = True 
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_BACKSPACE:
#                 quick = quick[:-1]
#             else:
#                 quick += event.unicode

#     if loginScreen_active:
#         screen.fill("gray7")
#         screen.blit(start_btn,start_btn_rect)
#         mouse_pos = pygame.mouse.get_pos()
#         if start_btn_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] == 1 and clicked == False:
#             clicked = True
#             loginScreen_active = False
#             game_active = True
#             # oyun()
#         if pygame.mouse.get_pressed()[0] == 0:
#             clicked = False
#         screen.blit(quit_btn,quit_btn_rect)
#         if quit_btn_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] == 1:
#             pygame.quit()
#             exit()
#         screen.blit(genelKültürQuiz_text,genelKültürQuiz_textRect)
#     elif game_active:
#         screen.fill("blue")
#         with open ("QuizGame\soru\soru.txt", encoding="UTF-8") as f:
#             content = f.readlines()
#             for i in content:
#                 a = i.strip("\n")
#                 split = re.split("\? ", a)
#                 sorularMain[split[0]] = split[1]

#         print("Quiz Oyununa Hoş Geldiniz")
#         screen.blit(quick_surface, (0,0))
#         # quick = int(input("Hızlıca 10 tane soru cevaplamak için 1'e, kendi istediğiniz miktarda soru cevaplamak için 2'ye, süreye karşı (120sn) oynamak için 3e, Maraton (3 yanlış yapana kadar oynamak) için 4e basın: "))
#         # match quick:
#         #     case 1:
#         #         soruSayısı = 10
#         #         hizliOyun()
#         #     case 2:
#         #         soruSayısı = int(input("Kaç tane soru cevapalamak istiyorsunuz? "))
#         #         hizliOyun()
#         #     case 3:
#         #         timeRace()
#         #     case 4:
#         #         Marathon()
#         #     case _:
#         #         print("Yanlış tuşlama")
#         #         time.sleep(5)
#         #         quit()


#     pygame.display.update()
#     clock.tick(60)