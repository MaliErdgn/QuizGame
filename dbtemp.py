import pandas as pd
import random

def soruSorma():
    global şıklar
    df = pd.read_excel("QuizGame\soru\sorular.xlsx")
    sorulardf = df.sample(n = 10)

    for i in range(10):
        soru = sorulardf.iat[i,0]
        cevap = sorulardf.iat[i,1]
        yanlışCevap1 = sorulardf.iat[i,2]
        yanlışCevap2 = sorulardf.iat[i,3]
        yanlışCevap3 = sorulardf.iat[i,4]
        şıklar = [cevap,yanlışCevap1,yanlışCevap2,yanlışCevap3]
        print(soru)
        soruText()


def soruText():
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


