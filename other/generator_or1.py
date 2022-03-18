class Kareler():
    def __init__(self,max):
        self.max=max
        self.sayac=1
    def __iter__(self):
        return self
    def __next__(self):
        if(self.sayac<=self.max):
            sonuc=self.sayac**2
            self.sayac+=1
            return sonuc
        else:
            self.sayac=1
            raise StopIteration
kare=iter(Kareler(10))
for i in kare:
    print(i)
