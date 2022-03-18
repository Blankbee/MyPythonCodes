a=3.14
b=int(a)
print(b)
a=3
b=float(a)
print(b)
c=str(a) #stringe dönüştürür.
print(c)
print(type(3.14))
print(type("hey"))
print(type(3))
print(26,6,2021,sep="/")
print("26","06","2021",sep="/")
print(*"Python")
print(*"Python",sep=".")
print("{} + {} = {} ".format(2,3,5))
print("{1} {0} {2}".format("station","play",5))#süslü parantez içindeki numaralar yer belirtir.
##################Listeler##############################
liste=[1,2,3,4,5,6,7,8,"qwe"]
print(liste)
print(liste[4:])
print(liste[:5])
liste1=list("Merhaba")
print(liste1)
print(liste1+liste)
liste2=[1,3,5]
liste2[1]=7#bu listelerde yapılabilirken stringlerde yapılamaz.
print(liste2)
liste2[:2]=[10,11]
print(liste2)
liste2.append("deneme")
print(liste2)
liste2.pop()
print(liste2)
liste2.pop(0)
print(liste2)
liste3=[3,7,2,4,9,1]
liste3.sort()
print(liste3)
liste3.sort(reverse=True)
print(liste3)
liste4=["b","a","d","c"]
liste4.sort()
print(liste4)
liste5=[[1,2],[3,4],[5,6]]
print(liste5[1][1])
a = input("a:")
b = input("b:")

print("Değiştirilmeden Önce Değerler\na: {} b: {}\n".format(a,b))

a,b = b,a

print("Değiştirildikten Sonraki Değerler\na: {} b: {}\n".format(a,b))