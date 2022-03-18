print("****************ATM******************")
print("1.Para Çekme")
print("2.Para Yatırma")
print("3.Bakiye Sorgulama")
bakiye=1000
while True:
    print("İşlem seçiniz.")
    a=int(input())
    if(a==1):
        print("Çekmek istediğiniz miktarı girin: ")
        b=int(input())
        if(b>bakiye):
            print("Bakiye yetersiz")

            continue
        bakiye-=b
        print("{} miktarda para çektiniz kalan bakiyeniz {}".format(b,bakiye))
    elif(a==2):
        print("Yatırmak istediğiniz miktarı girin: ")
        b=int(input())
        bakiye+=b
    elif(a==3):
        print("Hesaptaki bakiye miktarı: {}".format(bakiye))
    else:
        print("Geçerli bir işlem seçiniz.")
