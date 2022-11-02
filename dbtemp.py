import pandas as pd
import random

def soruSorma(questionNumber):
    global şıklar
    df = pd.read_excel("QuizGame\soru\sorular.xlsx")       #pull from excel
    sorulardf = df.sample(n = 10)       #choose 10 random quesitons

    for i in range(questionNumber):   #ask amount of questions that was told to ask
        soru = sorulardf.iat[i,0]
        cevap = sorulardf.iat[i,1] 
        yanlışCevap1 = sorulardf.iat[i,2]
        yanlışCevap2 = sorulardf.iat[i,3]
        yanlışCevap3 = sorulardf.iat[i,4]   #take the question and the choices from df
        şıklar = [cevap,yanlışCevap1,yanlışCevap2,yanlışCevap3]  #put choices in a list for randomness
        print(soru) 
        soruText()


def soruText():   #choose a random answer, print it as a choice and remove said item from list. Do it 4 times
    current = random.choice(şıklar)
    print(f"A){current}",end="  ")
    şıklar.remove(current)
    current = random.choice(şıklar)
    print(f"B){current}",end="  ")
    şıklar.remove(current)
    current = random.choice(şıklar)
    print(f"C){current}",end="  ")
    şıklar.remove(current)
    current = random.choice(şıklar)
    print(f"D){current}")
    şıklar.remove(current)


