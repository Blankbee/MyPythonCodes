from ornekvt import *
print("Islemler: \n[1]Oyunlari goster\n[2]Oyun sorgulama\n[3]Oyun ekle\n[4]Oyun sil\n[5]Oyun turu degistir")
print("Cikmak icin q tusuna basiniz.")
oyun=Library()
while True:
    a=input("Islem secin: ")
    if(a=="q"):
        break
    elif(a=="1"):
        oyun.oyunlari_goster()
    elif(a=="2"):
        b=input("Oyunun adi: ")
        oyun.oyun_sorgula(b)
    elif(a=="3"):
        print("Oyunun adini,yazarini,firmasini ve turunu girin: ")
        x=input()
        y=input()
        z=input()
        d=input()
        c=Oyun(x,y,z,d)
        oyun.oyun_ekle(c)
    elif(a=="4"):
        print("Silmek istediginiz oyunun adi: ")
        a=input()
        oyun.oyun_sil(a)
    elif(a=="5"):
        print("Turunu degistirmek istediginiz oyunun ismini ve yeni turunu girin: ")
        a=input()
        b=input()
        oyun.tur_degistir(b,a)
    else:
        print("Gecerli bir islem secin.")


