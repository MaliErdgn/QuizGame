import pandas as pd
import random
import pygame

questionNumber = 10
WINDOW_WIDTH = 540
WINDOW_HEIGHT = 960
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.font.init()
start_btn = pygame.image.load("QuizGame\Buttons\StartTheGame.jpg")
start_btn_rect = start_btn.get_rect(center = (WINDOW_WIDTH / 2,400))
font = pygame.font.Font("QuizGame\Fonts\Anonymous_Pro.ttf",20)

def soruSorma(questionNumber):
    global şıklar
    df = pd.read_excel("QuizGame\soru\sorular.xlsx")       #pull from excel
    sorulardf = df.sample(n = 10)   #choose 10 random quesitons
    # screen.blit(questionBox, (20,50))

    for i in range(0,questionNumber):   #ask amount of questions that was told to ask
        global questionBox
        global questionBox_rect
        global questionBox_rectText
        global cevap
        global soru

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
        soruObj(20,500)
        soruObj(275,500)
        soruObj(20,700)
        soruObj(275,700)
        soruCevap()
        # soruText()
        # soruCevap()


# def soruText():   #choose a random answer, print it as a choice and remove said item from list. Do it 4 times
#     global answerBox #20 500    275 500     20 700    275 700
#     global answerBox_rect

#     boxsize = (225,150)

#     current = random.choice(şıklar)
#     if current == cevap:
#         print(cevap)
#     answerBox = pygame.image.load("QuizGame\photos\\answerbox.png").convert_alpha()
#     answerBox = pygame.transform.scale(questionBox, boxsize)
#     answerBox_rect = answerBox.get_rect(topleft = (20,500))
#     answerBox_rectText = answerBox.get_rect(topleft = (25,505))
#     screen.blit(answerBox,answerBox_rect)

#     drawText(screen, current, "black", answerBox_rectText, font, aa =True, bkg=None)
#     şıklar.remove(current)

#     current = random.choice(şıklar)
#     if current == cevap:
#         print(cevap)
    
#     answerBox = pygame.image.load("QuizGame\photos\\answerbox.png").convert_alpha()
#     answerBox = pygame.transform.scale(questionBox, boxsize)
#     answerBox_rect = answerBox.get_rect(topleft = (275,500))
#     answerBox_rectText = answerBox.get_rect(topleft = (280,505))
#     screen.blit(answerBox,answerBox_rect)

#     drawText(screen, current, "black", answerBox_rectText, font, aa =True, bkg=None)
#     şıklar.remove(current)
    
#     current = random.choice(şıklar)
#     if current == cevap:
#         print(cevap)
    
#     answerBox = pygame.image.load("QuizGame\photos\\answerbox.png").convert_alpha()
#     answerBox = pygame.transform.scale(questionBox, boxsize)
#     answerBox_rect = answerBox.get_rect(topleft = (20,700))
#     answerBox_rectText = answerBox.get_rect(topleft = (25,705))
#     screen.blit(answerBox,answerBox_rect)

#     drawText(screen, current, "black", answerBox_rectText, font, aa =True, bkg=None)
#     şıklar.remove(current)
    
#     current = random.choice(şıklar)    
#     if current == cevap:
#         print(cevap)
    
#     answerBox = pygame.image.load("QuizGame\photos\\answerbox.png").convert_alpha()
#     answerBox = pygame.transform.scale(questionBox, boxsize)
#     answerBox_rect = answerBox.get_rect(topleft = (275,700))
#     answerBox_rectText = answerBox.get_rect(topleft = (280,705))
#     screen.blit(answerBox,answerBox_rect)

#     drawText(screen, current, "black", answerBox_rectText, font, aa =True, bkg=None)
#     şıklar.remove(current)


def soruObj(x, y):
    global answerBox_rect
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
        answerBox_rect = answerBox.get_rect(topleft = (x,y))
        answerBox_rectText = answerBox.get_rect(topleft = (x+5,y+5))
        screen.blit(answerBox,answerBox_rect)


    drawText(screen, current, "black", answerBox_rectText, font, aa =True, bkg=None)
    şıklar.remove(current)

def soruCevap():  # TRYING TO MAKE THIS FUNCTION WORK IN A WHILE LOOP????
    global doğruCevap
    global yanlışCevap

    mouse_pos = pygame.mouse.get_pos()
    doğruCevap = 0
    yanlışCevap = 0 

    print(mouse_pos)
    if answerBox_rectTrue.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] == 1 and clicked == False:
        clicked = True
        doğruCevap += 1
        print(doğruCevap)
    elif answerBox_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] == 1 and clicked == False:
        clicked = True
        yanlışCevap += 1
    if pygame.mouse.get_pressed()[0] == 0:
        clicked = False

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