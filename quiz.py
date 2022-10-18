import re
import random
import time

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
    

def soruSorma():
    global dogruCevap
    global sorular
    global answer
    global x
    for x in range(0,soruSayısı):
        soru, dogruCevap = random.choice(list(sorular.items()))
        answer = input(f"{soru}? ")
        cevap()
        sorular.pop(soru)
    sonuçlar()

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
    global dogruCevap
    global sorular
    global answer
    global x
    global soruSayısı
    sorular = sorularMain
    start_time = time.time()
    soruSayısı = len(sorular)
    current_time = 0
    while (current_time - start_time) < 10:
        for x in range(0,soruSayısı):
            soru, dogruCevap = random.choice(list(sorular.items()))
            answer = input(f"{soru}? ")
            current_time = time.time()
            if (current_time - start_time) > 120:
                print("Soruyu zamanında cevaplandıramadınız")
                break
            cevap()
            sorular.pop(soru)
            current_time = time.time()
            if (current_time - start_time) > 120:
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

puan = 0
dogruSayisi = 0
yanlışSayısı = 0
soru = 0
sorular = {}
sorularMain = {}

with open ("soru\soru.txt", encoding="UTF-8") as f:
    content = f.readlines()
for i in content:
    a = i.strip("\n")
    split = re.split("\? ", a)
    sorularMain[split[0]] = split[1]

print("Quiz Oyununa Hoş Geldiniz")
quick = int(input("Hızlıca 10 tane soru cevaplamak için 1'e, kendi istediğiniz miktarda soru cevaplamak için 2'ye, süreye karşı (120sn) oynamak için 3e, Maraton (3 yanlış yapana kadar oynamak) için 4e basın: "))
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

