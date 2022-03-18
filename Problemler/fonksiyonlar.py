def toplama(a,b,c):
    toplam=a+b+c
    return toplam
print(toplama(5,6,7))
def toplama1(*d):
    total=0
    for i in d:
        total=total+i
    return total
print(toplama1(1,2,34,5,7,78))
