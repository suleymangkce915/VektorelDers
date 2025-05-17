import random

puan = 0
while True:
    s1 = random.randitnt(1,100)
    s2 = random.randitnt(1,100)

    cevap = input(f"{s1}+{s2} toplamı kaç?")

    if cevap == " " :
        print(f"Hoşçakal, seni {puan} puan ile uğurluyorum")
        break
    if int(cevap) == s1 + s2:
        puan += 10
        print("Bildin, puanın:", puan)
    else:
        puan -=10
        print("Bilemedin, puanın:", puan)
