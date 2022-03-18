class User():
    def __init__(self,id,pw,auth,name,sname):
        self.id=id
        self.pw=pw
        self.auth=auth
        self.name=name
        self.sname=sname
    def change(self,b):
        while True:
            print("You wanna change id(1) or pw(2): ")
            a=int(input())
            if(a==1):
                self.id=b
                break
            elif(a==2):
                self.pw=b
                break
            else:
                print("Please choose a valid process")
    def login(self):
        while True: 
            print("Enter your id and pw :")
            a=input()
            b=input()
            if(a==self.id and b==self.pw):
                print("Succesfully logged in")
                break
            else:
                print("Your id or pw is wrong try again")
class Admin(User):
    def __init__(self, id, pw, auth, name, sname,):
        super().__init__(id, pw, auth, name, sname)

a=User("1","1234",2,"Esad","Sen")
a.login()