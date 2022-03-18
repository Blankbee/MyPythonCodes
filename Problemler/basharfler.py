a=""
y=""
x=""
with open("siir.txt","r",encoding="utf-8") as f:
    for i in f:
        a+=i[0]
print(a)
with open("siir.txt","r",encoding="utf-8") as f1:
    y=f1.read()
print(y)
for i in range(0,len(y)):
    print(y[i])

