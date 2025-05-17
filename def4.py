def hesapla(a,b,c):

    def topla(a,b):
        print("Toplam:", a+b)

    def carp(a,b):
        print("Carpma:", a*b)


    def bol(a,b):
        print("Bolme:", a/b)

    def cıkar(a,b):
        print("Cıkarma:", a-b)

    if c=="+": topla(a,b)
    elif c=="*": carp(a,b)
    elif c=="/": bol(a,b)
    elif c=="-": cıkar(a,b)
    else:
        print("Böyle Bir İşlem Yok")
        exit()

hesapla(4,5," ")