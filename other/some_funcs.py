from functools import reduce
def double(x):
    return x*2
print(list(map(double,[1,2,3,4,5,6])))
a=list(map(lambda x : x**2,(1,2,3,4,5,6,7,8,9)))
print(a)
b="Mer,haba"
print(b.split(","))
liste1=[1,3,5,7,9]
liste2=[2,4,6,8,10]
c=list(map(lambda x,y : x*y,liste1,liste2))
print(c)
def topla(x,y):
    return x+y
print(reduce(topla,(1,2,3,4,5)))
print(reduce(lambda x,y: x*y,[1,2,3,4,5]))
def tek(x):
    if(x%2==0):
        return False
    elif(x%2!=0):
        return True
print(list(filter(tek,range(0,100))))