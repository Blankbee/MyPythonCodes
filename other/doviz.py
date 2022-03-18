import sys
import requests
url="https://data.fixer.io/api/latest"
birinci_doviz=input("Birinci doviz: ")
ikinci_doviz=input("İkinci doviz: ")

response=requests.get(url+birinci_doviz)
json_verisi=response.json()
print(json_verisi["rates"][ikinci_doviz])