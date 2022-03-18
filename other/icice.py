def argsf(isim,*args):
    print(isim)
    for i in args:
        print(i)
def kwargsf(**kwargs):
    print(kwargs)
argsf("hello",(1,3,5,6,8))
kwargsf(isim="Jack",soyisim="Walker",numara=1234)
def kwargs1(**kwargs):
    for i,j in kwargs.items():
        print("Arguman adi: {},Arguman degeri: {}".format(i,j))
kwargs1(isim="Paul",soyisim="Walker",numara=12345)
def anafonk(islem_adi):
    def topla(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam
    def carpma(*args):
        carpim=1
        for i in args:
            carpim*=i
        return  carpim
    if(islem_adi=="topla"):
        return topla
    elif(islem_adi=="carpma"):
        return carpma
def toplama(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam
def carpma(*args):
    carpim=1
    for i in args:
        carpim*=i
    return carpim
def cikarma(a,b):
    return a-b
def bolme(a,b):
    return a/b
fonk=anafonk("topla")
print(fonk(1,2,3,4,5))
def anafonk1(fonk1,fonk2,fonk3,fonk4,islem):
    if(islem=="toplama"):
        print(fonk1(1,3))
    elif(islem=="carpma"):
        print(fonk2(3,4))
    elif(islem=="cikarma"):
        print(fonk3(10,5))
    elif(islem=="bolme"):
        print(fonk4(8,2))
    else:
        print("Gecersiz islem.")
anafonk1(toplama,cikarma,carpma,bolme,"toplama")


