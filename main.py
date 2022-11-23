import pygame
import pandas as pd
import random
from pygame import mixer

textAlignLeft = 0
textAlignRight = 1
textAlignCenter = 2
textAlignBlock = 3
class Boxes:
    def __init__(self,screenname,name,xloc,yloc,width,height,color,aa,bkg):
        self.screenname = screenname
        self.name = name
        self.xloc = xloc
        self.yloc = yloc
        self.width = width
        self.height = height
        self.color = color
        self.aa = aa
        self.bkg = bkg

    def createBox(self,screenname,text, textcolor, fontsize, center = True, outline=None):
        if outline:
            pygame.draw.rect(screenname,outline,(self.xloc-2,self.yloc-2,self.width-4,self.height-4),0)
        self.name = pygame.draw.rect(screenname,self.color,(self.xloc,self.yloc,self.width,self.height),0)
        boxtext = pygame.draw.rect(screenname,self.color,(self.xloc+5,self.yloc+5,self.width-5,self.height-5),0)
        self.text = text
        match fontsize:
            case 1:
                fontbox = pygame.font.Font("QuizGame\Fonts\Anonymous_Pro.ttf",20)       
            case 2:
                fontbox = pygame.font.Font("QuizGame\Fonts\Anonymous_Pro.ttf",50)       
            case 3:
                fontbox = pygame.font.Font("QuizGame\Fonts\Anonymous_Pro.ttf",75)
        if text != "":
            if center:
                textscreen = fontbox.render(self.text, 1, textcolor)
                screen.blit(textscreen, ((self.xloc + (self.width/2 - textscreen.get_width()/2)), self.yloc + (self.height/2 - textscreen.get_height()/2)))
            else:
                drawText(screenname, text, textcolor, boxtext, fontbox, textAlignLeft, aa=self.aa, bkg=self.bkg)

    def isOver(self,pos):
        if pos[0] > self.xloc and pos[0] < self.xloc + self.width:
            if pos[1] > self.yloc and pos[1] < self.yloc + self.height:
                return True
        return False
    
def askQuestions(questionNumber):
    global answered,mainmenu,game,doğruCevap,yanlışCevap,sonuç,questions,rightAnswerBox,wrongAnswer1Box,wrongAnswer2Box,wrongAnswer3Box,soruNo

    choiceLocation = [(20,500),(275,500),(20,700),(275,700)]
    choiceLocationBack = [(20,500),(275,500),(20,700),(275,700)]

    question = sorulardf.iat[soruNo,0]
    rightAnswer = sorulardf.iat[soruNo,1] 
    wrongAnswer1 = sorulardf.iat[soruNo,2]
    wrongAnswer2 = sorulardf.iat[soruNo,3]
    wrongAnswer3 = sorulardf.iat[soruNo,4]   #take the question and the choices from df

    print(questionNumber)
    print(soruNo)

    currentRandom = random.sample(choiceLocation, 4) #randomize the places of the choices
    
    questionBox = Boxes(screen, "question", 20, 50, 500, 350, white, True, None)
    questionBox.createBox(screen, question, dark, 1, None, None)


    rightAnswerBox = Boxes(screen, "rightAnswerBox", currentRandom[0][0], currentRandom[0][1], 225,150, white, True, None)
    rightAnswerBox.createBox(screen, rightAnswer, dark, 1, None, None)

    wrongAnswer1Box = Boxes(screen, "wrongAnswer1Box", currentRandom[1][0], currentRandom[1][1], 225,150, white, True, None)
    wrongAnswer1Box.createBox(screen, wrongAnswer1, dark, 1, None, None)

    wrongAnswer2Box = Boxes(screen, " wrongAnswer2Box", currentRandom[2][0], currentRandom[2][1], 225,150, white, True, None)
    wrongAnswer2Box.createBox(screen, wrongAnswer2, dark, 1, None, None)

    wrongAnswer3Box = Boxes(screen, "wrongAnswer3Box", currentRandom[3][0], currentRandom[3][1], 225,150, white, True, None)
    wrongAnswer3Box.createBox(screen, wrongAnswer3, dark, 1, None, None)

    choiceLocation = choiceLocationBack #fill back the location of choices
    
    answered = False
    if answered == False:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rightAnswerBox.isOver(pos):
                pygame.mixer.music.load("QuizGame\sounds\\rightanswer.mp3") #plays a ding sound
                pygame.mixer.music.play(1)
                doğruCevap =+ 1
                questionNumber =- 1
                soruNo =+ 1
                answered = True
            if wrongAnswer1Box.isOver(pos) or wrongAnswer2Box.isOver(pos) or wrongAnswer3Box.isOver(pos):
                pygame.mixer.music.load("QuizGame\sounds\wronganswer.mp3")
                pygame.mixer.music.play(1)
                yanlışCevap =+ 1
                questionNumber =- 1
                soruNo =+ 1
                answered = True
                
    if questionNumber == 0:
        sonuçHesaplama()
        playAgainBox = Boxes(screen, "playAgainBox", 85.5, 600, 375, 100, white, True, None)
        playAgainBox.createBox(screen, "Tekrar Oyna", dark, 2, True, None)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if playAgainBox.isOver(pos):
                mainmenu = True #go back to the main menu
                game = False     #stop the game
                answered = True #reset the value
                doğruCevap = 0 #reset
                yanlışCevap = 0 #reset
                sonuç = 0 #reset
                soruNo = 0 #reset
                questionNumber = questionNumberMain



def drawText(surface, text, color, rect, font, align=textAlignLeft, aa=False, bkg=None):
    lineSpacing = -2
    spaceWidth, fontHeight = font.size(" ")[0], font.size("Tg")[1]

    listOfWords = text.split(" ")
    if bkg:
        imageList = [font.render(word, 1, color, bkg) for word in listOfWords]
        for image in imageList: image.set_colorkey(bkg)
    else:
        imageList = [font.render(word, aa, color) for word in listOfWords]

    maxLen = rect[2]
    lineLenList = [0]
    lineList = [[]]
    for image in imageList:
        width = image.get_width()
        lineLen = lineLenList[-1] + len(lineList[-1]) * spaceWidth + width
        if len(lineList[-1]) == 0 or lineLen <= maxLen:
            lineLenList[-1] += width
            lineList[-1].append(image)
        else:
            lineLenList.append(width)
            lineList.append([image])

    lineBottom = rect[1]
    lastLine = 0
    for lineLen, lineImages in zip(lineLenList, lineList):
        lineLeft = rect[0]
        if align == textAlignRight:
            lineLeft += + rect[2] - lineLen - spaceWidth * (len(lineImages)-1)
        elif align == textAlignCenter:
            lineLeft += (rect[2] - lineLen - spaceWidth * (len(lineImages)-1)) // 2
        elif align == textAlignBlock and len(lineImages) > 1:
            spaceWidth = (rect[2] - lineLen) // (len(lineImages)-1)
        if lineBottom + fontHeight > rect[1] + rect[3]:
            break
        lastLine += 1
        for i, image in enumerate(lineImages):
            x, y = lineLeft + i*spaceWidth, lineBottom
            surface.blit(image, (round(x), y))
            lineLeft += image.get_width() 
        lineBottom += fontHeight + lineSpacing

    if lastLine < len(lineList):
        drawWords = sum([len(lineList[i]) for i in range(lastLine)])
        remainingText = ""
        for text in listOfWords[drawWords:]: remainingText += text + " "
        return remainingText
    return ""
    
def sonuçHesaplama(): #calculating the marks of the player
    sonuç = doğruCevap-yanlışCevap*0.25
    sonuçText = f"Sonucunuz {sonuç}"
    screen.blit(background, (0,0))
    resultBox = Boxes(screen, "resultBox", 85.5, 300, 375, 100, dark, True, None)
    resultBox.createBox(screen,sonuçText, white, 2, True, outline=None)


#region variables and initialization

questionNumber = 10    #default amount of questions to be asked
questionNumberMain = questionNumber
WINDOW_WIDTH = 540      #screen width
WINDOW_HEIGHT = 960     #screen height
clicked = False
doğruCevap = 0
yanlışCevap = 0
soruNo = 0
ongoing = True
dark,red,green,white,silver = "#0D1821","#B3001B","#058C42","#F0F4EF","#ADA8B6"
colors = [dark,red,green,white,silver]
pygame.font.init()
font = pygame.font.Font("QuizGame\Fonts\Anonymous_Pro.ttf",20) 
clock = pygame.time.Clock()
 
pygame.init()
mixer.init()
pygame.font.init()

screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT)) 
background = pygame.image.load("QuizGame\photos\\background.png").convert_alpha() 
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT)) #scaling backgorund to fill the screen
mainmenu = True
game = False
answered = True
sonuç = 0
volume = 0.2
#endregion
while True:
    if mainmenu == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #close when you press the x button
                pygame.quit()
                exit()
        pygame.event.pump()
        pos = pygame.mouse.get_pos()

        screen.blit(background,(0,0))
        startButton = Boxes(screen, "startButtonrect", 50, 380, 450, 100, red, True, None)
        startButton.createBox(screen, "Oyuna Başla", dark, 2, True, None)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if startButton.isOver(pos):
                screen.blit(background, (0,0))
                mainmenu = False
                df = pd.read_excel("QuizGame\soru\sorular.xlsx") #pull from excel
                sorulardf = df.sample(n = questionNumber)   #choose 10 random quesitons
                game = True
    elif game == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #close when you press the x button
                pygame.quit()
                exit()
        if questionNumber > 0:
            askQuestions(questionNumber)


        pygame.event.pump()
        pos = pygame.mouse.get_pos()

    mixer.music.set_volume(volume) #general volume of the game
    pygame.display.update()
    clock.tick(60) #fps of the game