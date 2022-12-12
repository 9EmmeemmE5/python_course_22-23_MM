"""sim d'esame su learn gestione dati"""

"""
Dataset: https://s3.amazonaws.com/vrai.univpm/FI/2021/11/geodata_cdp.json
(i dati rappresentano i contratti/cantieri e sono derivati da 
http://opencantieri.mit.gov.it/contratti )
"""
import requests
import json

#1 Memorizzare il dataset e poi convertitolo in dizionario mediante la libreria 
# requests e json (vedicodice di esempio svolto a lezione 
# https://learn.univpm.it/mod/folder/view.php?id=177642 ) 

url="https://s3.amazonaws.com/vrai.univpm/FI/2021/11/geodata_cdp.json"
response=requests.get(url)
my_dict=json.loads(response.text)
print(type(my_dict))

#2 Calcolare e stampare il numero di soggetti unici

soggetti=[]
for i in range(len(my_dict)):
    soggetti.append(my_dict[i]["properties"]["Soggetto"])
print(soggetti)
print(type(soggetti))
soggetti_unici=set(soggetti)
print(len(soggetti_unici))
print(soggetti_unici)

#3 Calcolare e stampare per ogni soggetto il numero di contratti associati

for element in soggetti_unici:
    numero_contratti=0
    for item in soggetti:
        if item==element:
            numero_contratti+=1
    print(f"Soggetto unico:{element} - numero di contratti {numero_contratti}")

#4 Importare da file un bounding box; un bounding box è un insieme di 4 valori che corrispondono a
# TL_x, TL,y, BR_x e BR_y dove TL è angolo top-left e BR è angolo bottom-right (es. 9.14; 45.48; 9.15;
# 45.38); il nome del file è specificato dall’utente (mediante input() o sys.argv). L’utente crea
# autonomamente (manualmente tale file) prima di avviare l’esecuzione.

#5 Chiedere all’utente di fornire mediante la funzione input() una porzione della descrizione (es. BIS 
# TIBERINA) fornendo poi all’utente la lista dei cantieri che hanno un “match” con la stringa fornita (si
# consiglia di uniformare le liste mediante lower case);

lista_cantieri_corrispondenti=[]
descrizioni_da_controllare=[]
nome_cantiere=str(input("inserire le parole chiavi per la ricerca dei cantieri:..."))

for i in my_dict:
    cantiere=i["properties"]["Descrizione Completa"]
    descrizioni_da_controllare.append(cantiere.lower())
#6 Se i bounding box hanno una intersezione si utilizzi il buonding box risultante dall’intersezione;

#7 Per ogni bounding box calcolare il numero di contratti / progetti presenti; si richiede di effettuare il
# calcolo distinguendo per il soggetto

#8 Salvare in un file di testo in formato json (si può utilizzare la libreria json ed il metodo json.dumps; il
# nome del file è specificato dall’utente mediante input() o sys.argv) quanto creato al passo
# precedente

#9 La codifica del JSON è a libera scelta da parte dello studente

#10 Visualizzare mediante matplotlib (si consiglia di usare il plot di tipo bar) il numero di
# progetti/cantieri per ogni soggetto

#11 Devono essere presenti almeno due test

#12 Il codice deve essere opportunamente commentato e si chiede di organizzare il codice in modo più 
# “modulare” possibile

#13 Il codice deve gestire eventuali eccezioni che potranno avvenire durante l’esecuzione del codice