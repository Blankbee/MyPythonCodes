with open("mail.txt","r",encoding="utf-8") as f:
    for i in f:
        i=i[:-1]
        if(i.find("@")!=-1 and i.endswith(".com")):
            print(i)
        else:
            print("Geçersiz email")