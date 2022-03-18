while True:
    print("Fibonacci için bir terim sayısı giriniz: ")
    a=int(input())
    c=0
    b=1
    for i in range(0,a):
        r=b
        b+=c
        c=r
        print(c)

