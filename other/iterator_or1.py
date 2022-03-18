def asal():
    c=0
    for i in range(3,1001):
        c=0
        for j in range(2,i):
            if(i%j==0):
                c=1
                break
        if(c!=1):
            yield i
for k in asal():
    print(k)