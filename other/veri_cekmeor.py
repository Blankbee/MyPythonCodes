import requests
from bs4 import BeautifulSoup
url="https://www.metacritic.com/browse/games/score/metascore/all/pc/filtered"
response=requests.get(url)
html_icerigi=response.content
soup=BeautifulSoup(html_icerigi,"html.parser")
basliklar=soup.find_all("a href",{"class":"title"})
for i in basliklar:
    print(str(i))
#ratingler=soup.find_all({"class","metascore_w large game positive"})
#for baslik, rating in zip(basliklar,ratingler):
#    baslik=baslik.text
#    rating=rating.text

#    baslik=baslik.strip()
#    baslik=baslik.replace("\n","")

#    rating=rating.strip()
#    rating=rating.replace("\n","")

#    print("Başlık: ",baslik)
#    print("Rating: ",rating)