class Car():
    def __init__(self,brand,model,nation,hp):
        self.brand=brand
        self.model=model
        self.nation=nation
        self.hp=hp
    def info(self):
        print("Brand:{} , Model:{} , Nation:{} , HP:{} ".format(self.brand,self.model,self.nation,self.hp))

car1=Car("Ford","Mustang","American",500)
car2=Car("Chevrolet","Camaro","American",600)
car3=Car("Nissan","GTR","Japanese",600)
car1.info()
