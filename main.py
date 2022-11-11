import pygame
import pandas as pd
import random
import time
from pygame import mixer

def soruObj(x, y, rectNo):    #get the placement arguments and blit the questionbox on the screen
    global answerBox_rect1
    global answerBox_rect2
    global answerBox_rect3
    global answerBox_rect4
    global answerBox_rectTrue
    global boxsize
    global rightBox
    global rightBox_rect
    global rightBox_rectText
    global wrongBox
    global wrongBox_rect
    global wrongBox_rectText


    boxsize = (225,150)
    current = random.choice(şıklar)            #choose a random choice


    if current == cevap:                              #if true mark it as true and render it on the screen
        rightBox = pygame.image.load("QuizGame\photos\\rightanswer.png").convert_alpha()    
        rightBox = pygame.transform.scale(rightBox,boxsize)
        rightBox_rect = rightBox.get_rect(topleft = (x,y))
        rightBox_rectText = rightBox.get_rect(topleft = (x+5,y+5))
        answerBox = pygame.image.load("QuizGame\photos\\answerbox.png").convert_alpha()
        answerBox = pygame.transform.scale(questionBox, boxsize)
        answerBox_rectTrue = answerBox.get_rect(topleft = (x,y))
        answerBox_rectText = answerBox.get_rect(topleft = (x+5,y+5))
        screen.blit(answerBox,answerBox_rectTrue)

    else:               #if its wrong create wrong variables and blit it
        wrongBox = pygame.image.load("QuizGame\photos\wronganswer.png").convert_alpha()
        wrongBox = pygame.transform.scale (wrongBox,boxsize) 
        globals()["wrongBox_rect" + str(rectNo)] = wrongBox.get_rect(topleft = (x,y))
        globals()["wrongBox_rectText" + str(rectNo)] = wrongBox.get_rect(topleft = (x+5,y+5))
        answerBox = pygame.image.load("QuizGame\photos\\answerbox.png").convert_alpha()
        answerBox = pygame.transform.scale(questionBox, boxsize)                                
        globals()["answerBox_rect" + str(rectNo)] = answerBox.get_rect(topleft = (x,y))         #creating the differernt variables 
        answerBox_rectText = answerBox.get_rect(topleft = (x+5,y+5))
        screen.blit(answerBox,(x,y))


    drawText(screen, current, "#0D1821", answerBox_rectText, font, aa =True, bkg=None)
    şıklar.remove(current)        #remove that choice after blitting it on the screen

def drawText(surface, text, color, rect, font, aa=False, bkg=None):   #make sure that the texts in the given rects dont overstep the boundaries of the rect
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text

def soruSorma(questionNumber):   #get the questions and answers from the database and store them


        for i in range(questionNumber):   #ask amount of questions that was told to ask
            global questionBox
            global questionBox_rect
            global questionBox_rectText
            global cevap
            global soru
            global şıklar

            soru = sorulardf.iat[i,0]
            cevap = sorulardf.iat[i,1] 
            yanlışCevap1 = sorulardf.iat[i,2]
            yanlışCevap2 = sorulardf.iat[i,3]
            yanlışCevap3 = sorulardf.iat[i,4]   #take the question and the choices from df

            questionBox = pygame.image.load("QuizGame\photos\\answerbox.png").convert_alpha() #background of the question
            questionBox = pygame.transform.scale(questionBox, (500,350)) #resizing the bg
            questionBox_rect = questionBox.get_rect(topleft = (20,50)) #getting the rect
            questionBox_rectText = questionBox.get_rect(topleft = (25,55)) #rect of the text
            screen.blit(questionBox,questionBox_rect) #blitting the said rect

            drawText(screen, soru, "black", questionBox_rectText, font, aa =True, bkg=None) #writing the question in screen

            şıklar = [cevap,yanlışCevap1,yanlışCevap2,yanlışCevap3]  #put choices in a list for randomness
            soruObj(20,500,1)
            soruObj(275,500,2)
            soruObj(20,700,3)
            soruObj(275,700,4)

def sonuçHesaplama(): #calculating the marks of the player
    sonuçSize = (400,500)
    sonuç =doğruCevap - (yanlışCevap*0.25)
    sonuçText = f"Sonucunuz {sonuç}"
    sonuçKutusu = pygame.image.load("QuizGame\photos\\background.png").convert_alpha()
    sonuçKutusu = pygame.transform.scale(sonuçKutusu, sonuçSize)
    sonucKutusu_rect = sonuçKutusu.get_rect(center = (WINDOW_WIDTH/1.75,WINDOW_HEIGHT/1.5))
    screen.blit(background, (0,0))
    screen.blit(sonuçKutusu, sonucKutusu_rect)
    drawText(screen, sonuçText, "#F0F4EF", sonucKutusu_rect, fontBigger, aa=True, bkg= None)

questionNumber = 11     #default amount of questions to be asked + 1
questionNumberMain = questionNumber
WINDOW_WIDTH = 540      #screen width
WINDOW_HEIGHT = 960     #screen height
clicked = False
questionBoxColor = "#F0F4EF"
doğruCevap = 0
yanlışCevap = 0
pygame.font.init()
font = pygame.font.Font("QuizGame\Fonts\Anonymous_Pro.ttf",20) #general font of the program
fontBigger = pygame.font.Font("QuizGame\Fonts\Anonymous_Pro.ttf",50) 

clock = pygame.time.Clock()
start_btn = pygame.image.load("QuizGame\Buttons\StartTheGame.jpg")
start_btn_rect = start_btn.get_rect(center = (WINDOW_WIDTH / 2,400))  #position of start button

 
pygame.init()
mixer.init()
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT)) 
background = pygame.image.load("QuizGame\photos\\background.png").convert_alpha() 
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT)) #scaling backgorund to fill the screen
pygame.font.init()
mainmenu = True
game = False
answered = True
doğruCevap = 0
yanlışCevap = 0
sonuç = 0
volume = 0.2
while True:
    if mainmenu == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #close when you press the x button
                pygame.quit()
                exit()
        pygame.event.pump()
        mouse_pos = pygame.mouse.get_pos()

        screen.blit(background,(0,0))
        screen.blit(start_btn,start_btn_rect)

        if start_btn_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] == 1 and clicked == False: #checks if you click the button
            clicked = True
            screen.blit(background,(0,0))
            mainmenu = False
            df = pd.read_excel("QuizGame\soru\sorular.xlsx")       #pull from excel
            sorulardf = df.sample(n = questionNumber)   #choose 10 random quesitons
            game = True
            if pygame.mouse.get_pressed()[0] == 0:
                clicked = False
    elif game == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #close when you press the x button
                pygame.quit()
                exit()


        pygame.event.pump()
        mouse_pos = pygame.mouse.get_pos()

        if questionNumber > 0:
            if answered == False:
                if answerBox_rectTrue.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] == 1 and clicked == False: #checks if you pressed the right option
                    pygame.mixer.music.load("QuizGame\sounds\\rightanswer.mp3") #plays a ding sound
                    pygame.mixer.music.play(1)
                    clicked = True
                    answered = True
                    doğruCevap += 1 #adds +1 to right answers
                elif (answerBox_rect1.collidepoint(mouse_pos) or answerBox_rect2.collidepoint(mouse_pos) or answerBox_rect3.collidepoint(mouse_pos) or answerBox_rect4.collidepoint(mouse_pos)) and pygame.mouse.get_pressed()[0] == 1 and clicked == False: # type: ignore #checks if you pressed one of the wrong options
                    pygame.mixer.music.load("QuizGame\sounds\\wronganswer.mp3") #plays a buzzer sound
                    pygame.mixer.music.play(1)
                    clicked = True
                    answered = True
                    yanlışCevap += 1 #adds +1 to wrong answers
                if pygame.mouse.get_pressed()[0] == 0:
                    clicked = False
            if answered == True:
                soruSorma(questionNumber) 
                questionNumber -=1
            answered = False
        
        elif questionNumber == 0:
            sonuçHesaplama()
            playAgainBox = pygame.image.load("QuizGame\photos\\answerbox.png").convert_alpha()
            playAgainBox = pygame.transform.scale(playAgainBox, (375,100))
            playAgain_rect = playAgainBox.get_rect(topleft = (100,600))
            playAgain_rectText = playAgainBox.get_rect(topleft = (155,620))
            screen.blit(playAgainBox,playAgain_rect)
            drawText(screen, "Play Again", "#0D1821", playAgain_rectText, fontBigger, aa =True, bkg=None)
            if playAgain_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] == 1 and clicked == False:
                mainmenu = True #go back to the main menu
                game = False     #stop the game
                answered = True #reset the value
                doğruCevap = 0 #reset
                yanlışCevap = 0 #reset
                sonuç = 0 #reset
                clicked = True 
                clicked = False
                questionNumber = questionNumberMain #load back the amount of questions
            if pygame.mouse.get_pressed()[0] == 0:
                clicked = False

    mixer.music.set_volume(volume) #general volume of the game
    pygame.display.update()
    clock.tick(60) #fps of the game