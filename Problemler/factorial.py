while True:
    print("Faktöryelini almak istediğiniz sayıyı seçiniz:")
    print("Çıkmak için q tuşuna basınız.")
    a=int(input())
    b=1
    for i in range(1,a+1):
        print(i)
        b=i*b
    print("Sonuç: {}".format(b))


