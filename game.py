import pygame
import pandas as pd
import random

def soruObj(x, y, rectNo):
    global answerBox_rect1
    global answerBox_rect2
    global answerBox_rect3
    global answerBox_rect4
    global answerBox_rectTrue
    boxsize = (225,150)
    current = random.choice(şıklar)
    if current == cevap:
        answerBox = pygame.image.load("QuizGame\photos\\answerbox.png").convert_alpha()
        answerBox = pygame.transform.scale(questionBox, boxsize)
        answerBox_rectTrue = answerBox.get_rect(topleft = (x,y))
        answerBox_rectText = answerBox.get_rect(topleft = (x+5,y+5))
        screen.blit(answerBox,answerBox_rectTrue)

    else:
        answerBox = pygame.image.load("QuizGame\photos\\answerbox.png").convert_alpha()
        answerBox = pygame.transform.scale(questionBox, boxsize)
        globals()["answerBox_rect" + str(rectNo)] = answerBox.get_rect(topleft = (x,y))
        answerBox_rectText = answerBox.get_rect(topleft = (x+5,y+5))
        screen.blit(answerBox,(x,y))


    drawText(screen, current, "#0D1821", answerBox_rectText, font, aa =True, bkg=None)
    şıklar.remove(current)

def drawText(surface, text, color, rect, font, aa=False, bkg=None):
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

def soruSorma(questionNumber):
        df = pd.read_excel("QuizGame\soru\sorular.xlsx")       #pull from excel
        sorulardf = df.sample(n = questionNumber)   #choose 10 random quesitons
        # screen.blit(questionBox, (20,50))

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

questionNumber = 10 #default amount of questions to be asked
WINDOW_WIDTH = 540
WINDOW_HEIGHT = 960 #screen size
clicked = False
questionBoxColor = "#F0F4EF"
doğruCevap = 0
yanlışCevap = 0
pygame.font.init()
font = pygame.font.Font("QuizGame\Fonts\Anonymous_Pro.ttf",20)

clock = pygame.time.Clock()
start_btn = pygame.image.load("QuizGame\Buttons\StartTheGame.jpg")
start_btn_rect = start_btn.get_rect(center = (WINDOW_WIDTH / 2,400))  #position of start button

 
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT)) 
background = pygame.image.load("QuizGame\photos\\background.png").convert_alpha() 
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT)) #scaling backgorund to fill the screen
screen.blit(background,(0,0))
screen.blit(start_btn,start_btn_rect)
pygame.font.init()
mainmenu = True
game = False
answered = True
doğruCevap = 0
yanlışCevap = 0 
while True:
    if mainmenu == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #close when you press the x button
                pygame.quit()
                exit()
        pygame.event.pump()
        mouse_pos = pygame.mouse.get_pos()


        if start_btn_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] == 1 and clicked == False: #checks if you click the button
            clicked = True
            screen.blit(background,(0,0))
            mainmenu = False
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

        if answered == False:
            if answerBox_rectTrue.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] == 1 and clicked == False:
                clicked = True
                answered = True
                doğruCevap += 1
                print(f"Doğru. Doğru sayınız: {doğruCevap}")
            elif (answerBox_rect1.collidepoint(mouse_pos) or answerBox_rect2.collidepoint(mouse_pos) or answerBox_rect3.collidepoint(mouse_pos) or answerBox_rect4.collidepoint(mouse_pos)) and pygame.mouse.get_pressed()[0] == 1 and clicked == False: # type: ignore
                clicked = True
                answered = True
                yanlışCevap += 1
                print(f"Yanlış. Yanlış sayınız: {yanlışCevap}")
            if pygame.mouse.get_pressed()[0] == 0:
                clicked = False
        if answered == True:
            soruSorma(questionNumber)
            if questionNumber > 0:
                questionNumber -=1
            answered = False


    pygame.display.update()
    clock.tick(60)
