x={1,2,3}
print(type(x))
#set tipi kümeler gibidir aynı üyeden 2 tane olamaz.kümeler indexlerle ulaşılamaz.
y=[1,1,1,1,2,2,2,3,3,3]
z=set(y)
print(z)
for i in z:
    print(i)
#bu şekilde üyelere ulaşılabilir.
z.add(4)
print(x.difference(z))
x.difference_update(z)
print(x)
x.discard(3)
print(x.intersection(z))
print(x.isdisjoint(z))#kesişimleri yok ise true var ise false döner.


