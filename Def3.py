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
    if c=="*": carp(a,b)
    if c=="/": bol(a,b)
    if c=="-": cıkar(a,b)

hesapla(4,5,"/")