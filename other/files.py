#with open("bilgiler.txt","w") as f:
#   f.write("Yo,Whats up!")
#with open("bilgiler.txt","r") as ff:
#    print(ff.read())
#    print(ff.tell())
#    ff.seek(20)
#    print(ff.tell())
#with open("bilgiler.txt","r+") as f1:
#    icerik=f1.read()
#    icerik=icerik + "\nNissan GT-R"
#    f1.seek(0)
#    f1.write(icerik)
#    f1.seek(0)
#    icerik="AMG GT-R\n" + icerik
#    f1.write(icerik)
with open("other/bilgiler.txt","r+") as f2:
    liste=f2.readlines()
    liste.insert(1,"Bugatti Veyron\n")
    f2.seek(0)
    f2.writelines(liste)

