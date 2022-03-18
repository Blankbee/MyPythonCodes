def hesapla(liste):
    liste=liste[:-1]
    liste1=liste.split(",")
    isim=liste1[0]
    not1=int(liste1[1])
    not2=int(liste1[2])
    not3=int(liste1[3])
    print(isim,not1,not2,not3)
    ort=(not1*3+not2*3+not3*4)/10
    return ort
with open("notlar.txt","r") as f:
    l=f.readline()
    if(hesapla(l)>=70):
        print("Gectiniz.")
    else:
        print("Kaldiniz.")
    

