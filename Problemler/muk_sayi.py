print("Bir sayi girin: ")
a=int(input())
b=0
for i in range(1,a):
    if(a%i==0):
        b+=i
if(b==a):
    print("Girdiğiniz sayi mükemmel")
else:
    print("Girdiğiniz sayı mük değil")