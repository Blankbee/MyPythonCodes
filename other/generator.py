def kare_al():
    for i in range(1,6):
        yield i**2 #yield fonksiyonu değerleri sürekli bellekte tutmaktansa sadece kullanacağımız zaman onları
                   #üretip kullanmamızı sağlar.
generator=kare_al()
iterator=iter(generator)
for i in range(1,6):
    print(next(iterator))