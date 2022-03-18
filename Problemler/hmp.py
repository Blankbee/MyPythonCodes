print("******************HMP***********************\n")
print("Işlem seçiniz:\n")
print("1.Toplama\n")
print("2.Cikarma\n")
print("3.Carpma\n")
print("4.Bolme\n")
a=int(input(" "))
if(a==1):
    print("Birinci sayiyi girin: \n")
    b=int(input())
    print("Ikinci sayiyi girin: \n"),
    c=int(input())
    print("Sayilarin toplami: {}".format(b+c))
elif(a==2):
    print("Buyuk sayiyi girin: \n")
    b = int(input())
    print("Kucuk sayiyi girin: \n"),
    c = int(input())
    print("Sayilarin farki: {}".format(b - c))
elif(a==3):
    print("Birinci sayiyi girin: \n")
    b = int(input())
    print("Ikinci sayiyi girin: \n"),
    c = int(input())
    print("Sayilarin carpimi: {}".format(b*c))
elif(a==4):
    print("Bolunen sayiyi girin: \n")
    b = int(input())
    print("Bolen sayiyi girin: \n"),
    c = int(input())
    print("Sayilarin bolumu: {}".format(b/c))
else:
    print("Gecerli bir islem secin\n")

