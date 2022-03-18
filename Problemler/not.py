print("Birinci vize notunuzu girin: ")
a=int(input())
print("Ikinci vize notunuzu girin: ")
b=int(input())
print("Final notunuzu girin: ")
c=int(input())
d=(a*3+b*3+c*4)/10
print("Notunuz: ",d)
if(d>=90):
    print("Harf Notunuz: AA")
elif(d>=85):
    print("Harf Notunuz: BA")
elif(d>=80):
    print("Harf Notunuz: BB")
elif(d>=75):
    print("Harf Notunuz: CB")
elif(d>=70):
    print("Harf Notunuz: CC")
elif(d<70):
    print("Dersten kaldınız.")
else:
    print("Gecerli notlar giriniz.")


