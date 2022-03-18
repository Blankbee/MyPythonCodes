class Pc():
    def __init__(self,cpu,gpu,ram):
        self.cpu=cpu
        self.gpu=gpu
        self.ram=ram
    def info(self):
        print("Information of device \n Cpu: {},Gpu: {},Ram: {}".format(self.cpu,self.gpu,self.ram))
    def __str__(self):
        return "Information of device \n Cpu: {},Gpu: {},Ram: {}".format(self.cpu,self.gpu,self.ram)
class Console(Pc):
    def __init__(self, cpu, gpu, ram, brand, model):
        super().__init__(cpu, gpu, ram)
        self.brand=brand
        self.model=model
    def info(self):
        super().info()
        print("Brand: {},Model: {}".format(self.brand,self.model))
mac=Pc("intel","RTX 3060","32 GB")
mac.info()
ps5=Console("AMD","RX 6800","32 GB","Sony","PlayStation")
ps5.info()
print(mac)
print(ps5)
