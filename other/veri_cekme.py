import requests
from bs4 import  BeautifulSoup
url="https://www.imdb.com/chart/top/"
response=requests.get(url)
html_icerigi=response.content
soup=BeautifulSoup(html_icerigi,"html.parser")
basliklar=soup.find_all("td",{"class":"titleColumn"})
ratingler=soup.find_all("td",{"class","ratingColumn imdbRating"})
a=float(input("Min rating değerini giriniz: "))
#for baslik, rating in zip(basliklar,ratingler):
#    baslik=baslik.text
#    rating=rating.text
#
#    baslik=baslik.strip()
#    baslik=baslik.replace("\n","")

#    rating=rating.strip()
#    rating=rating.replace("\n","")

#   print("Başlık: ",baslik)
#    print("Rating: ",rating)
for baslik, rating in zip(basliklar,ratingler):
    baslik=baslik.text
    rating=rating.text

    baslik=baslik.strip()
    baslik=baslik.replace("\n","")

    rating=rating.strip()
    rating=rating.replace("\n","")
    if(float(rating)>a):
        print("Başlık: ",baslik)
        print("Rating: ",rating)
