import sqlite3
con=sqlite3.connect("okutuphane.db")
cursor=con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS okitaplik (Isim TEXT,Yapimci TEXT,Firma TEXT,Tur TEXT)")
    con.commit()
def veri_ekle():
    cursor.execute("INSERT INTO okitaplik VALUES ('Half-Life 2','GabeN','Valve','Survival-Action')")
    con.commit()
def veri_ekle2(isim,yapimci,firma,tur):
    cursor.execute("INSERT INTO okitaplik VALUES (?,?,?,?)",(isim,yapimci,firma,tur))
    con.commit()
def verileri_al():
    cursor.execute("SELECT * FROM okitaplik")
    liste=cursor.fetchall()
    print("Oyun kitaplığı listesi: ")
    for i in liste:
        print(i)
def verileri_al2():
    cursor.execute("SELECT Isim,Yapimci FROM okitaplik")
    liste=cursor.fetchall()
    print("Oyun kitaplığı listesi: ")
    for i in liste:
        print(i)
def verileri_al3(firma):
    cursor.execute("SELECT * FROM okitaplik where Firma=?",(firma,))
    liste=cursor.fetchall()
    print("Oyun kitaplığı listesi: ")
    for i in liste:
        print(i)
def verileri_guncelle(x,y):
    cursor.execute("UPDATE okitaplik SET Firma=? where Firma=?",(x,y))
    con.commit()
def verileri_sil(x):
    cursor.execute("DELETE FROM okitaplik where Yapimci=?",(x,))
    con.commit()
verileri_sil("Houser Brothers")
con.close()