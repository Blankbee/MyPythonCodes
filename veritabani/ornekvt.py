import sqlite3
import time
class Oyun():
    def __init__(self,isim,yazar,firma,tur):
        self.isim=isim
        self.yazar=yazar
        self.firma=firma
        self.tur=tur
    def __str__(self):
        return "Oyun adi: {}\nYazar: {}\nFirma: {}\nTur: {}\n".format(self.isim,self.yazar,self.firma,self.tur)
class Library():
    def __init__(self):
        self.baglanti_olustur()
    def baglanti_olustur(self):
        self.con=sqlite3.connect("library.db")
        self.cursor=self.con.cursor()
        sorgu="CREATE TABLE IF NOT EXISTS olibrary (isim TEXT,yazar TEXT,firma TEXT,tur TEXT)"
        self.cursor(sorgu)
        self.con.commit()
    def baglantiyi_kes(self):
        self.con.close()
    def oyunlari_goster(self):
        sorgu="SELECT * FROM olibrary"
        self.cursor.execute(sorgu)
        liste=self.cursor.fetchall()
        if(len(liste)==0):
            print("Kutuphanede oyun yok.")
        else:
            for i in liste:
                a=Oyun(i[0],i[1],i[2],i[3])
                print(a)
    def oyun_sorgula(self,isim):
        sorgu="SELECT * FROM olibrary WHERE isim=?"
        self.cursor.execute(sorgu,(isim,))
        liste=self.cursor.fetchall()
        if(len(liste)==0):
            print("Boyle bir oyun bulunmuyor.")
        else:
            a=Oyun(liste[0][0],liste[0][1],liste[0][2],liste[0][3])
    def oyun_ekle(self,oyun):
        sorgu="INSERT INTO olibrary VALUES(?,?,?,?)"
        self.cursor.execute(sorgu,(oyun.isim,oyun.yazar,oyun.firma,oyun.tur))
        self.con.commit()
    def oyun_sil(self,isim):
        sorgu="DELETE FROM olibrary WHERE isim=?"
        self.cursor.execute(sorgu,(isim,))
        self.con.commit()
    def tur_degistir(self,tur,isim):
        sorgu="UPDATE olibrary SET tur=? WHERE isim=?"
        self.cursor.execute(sorgu,(tur,isim))
        self.con.commit()
    
