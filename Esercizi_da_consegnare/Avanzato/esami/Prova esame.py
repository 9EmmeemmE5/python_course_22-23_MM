import requests
import json


url="https://s3.amazonaws.com/vrai.univpm/FI/2021/11/geodata_cdp.json"
response=requests.get(url)
my_dict=json.loads(response.text)
#print(my_dict)

#!stampa lista soggetti unici
#estrai lista soggetti e crei col costruttore il set per rendere unici i soggetti
# data={
#     "type":[],
#     "properties":{},
#     "geometry":{},
# }
soggetti=[]
for i in range(len(my_dict)):
    soggetti.append(my_dict[i]["properties"]["Soggetto"])
print(soggetti)
soggetti_unici=set(soggetti)
print(len(soggetti_unici))
print(soggetti_unici)

#!stampare il numero di contratti per ogni soggetto unico
for element in soggetti_unici:
    numero_contratti=0
    for item in soggetti:
        if item==element:
            numero_contratti+=1
    print(f"Soggetto unico:{element} - numero di contratti {numero_contratti}")

#!