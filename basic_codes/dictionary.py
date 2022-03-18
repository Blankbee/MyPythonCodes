sozluk1={"bir":1,"iki":2,"üç":3,"liste":[1,2,3,4],"touple":(3,2,1),"float":3.6}
print(sozluk1["bir"])
print(sozluk1["touple"])
print(sozluk1["liste"])
print(sozluk1["float"])
print(sozluk1["liste"][2])
a={"sayilar":{"bir":1,"iki":2,"üç":3},"meyveler":{"portakal":"kis","kiraz":"yaz",}}
print(a["sayilar"]["bir"])
print(a["meyveler"]["portakal"])
print(sozluk1.keys())
print(sozluk1.values())
print(sozluk1.items())
for n,m in sozluk1.items():
    print(n,m)