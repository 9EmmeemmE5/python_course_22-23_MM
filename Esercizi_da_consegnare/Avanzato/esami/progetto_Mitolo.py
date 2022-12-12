import requests
import json
import matplotlib.pyplot as plt

#1
#per prima cosa andiamo a creare la nostra variabile
#uso global per rendere global la var my_text
#contenente il testo da utilizzare
#utilizziamo un'eccezione in modo che se l'url sia errato
#il programma sia pronto

def creazione_testo(url):
    "this function import the text from the url"
    response = requests.request("GET",url)   
    global my_text                          
    my_text = json.loads(response.text)     
    return my_text                          

#uso un ciclo for per scorrere ogni elemento della lista (my_text)
#grazie all'accesso posizionale accedo ai valori della chiave soggetto
#se il soggetto non è nel diz lo aggiungo e gli do valore 1
#se il soggetto è nel diz incremento di 1 il suo valore

def operazioni_lista(diz_soggetti_contratti,n):
    "questa funzione svolge i punti 2,3 e 4 provando"
    for i in my_text:
        soggetto = i["properties"]["Soggetto"]  
        if soggetto not in diz_soggetti_contratti: 
            diz_soggetti_contratti[soggetto] = n   
        else:
            diz_soggetti_contratti[soggetto] += 1
    print(f"il seguente dizionario mostra i soggetti unici ed i contratti associati: {diz_soggetti_contratti},\
    il numero di soggetti unici è {len(diz_soggetti_contratti)}")

#6• Chiedere all’utente di fornire mediante la funzione input() una porzione della descrizione (es. BIS
#TIBERINA) fornendo poi all’utente la lista dei cantieri che hanno un “match” con la stringa fornita (si
#consiglia di uniformare le liste mediante lower case)

def ricerca_cantiere(descrizioni,str1,lista_matchata):
    
    for i in my_text:
        descrizione = i["properties"]["Descrizione Completa"]
        descrizioni.append(descrizione.lower())
    for elem in descrizioni:
        valore = elem.find(str1)
        if valore != -1:
            lista_matchata.append(elem)
    print(f"{lista_matchata}")
    #print(descrizioni)

#11 • Visualizzare mediante matplotlib (si consiglia di usare il plot di tipo bar) il numero di
#progetti/cantieri per ogni soggetto
#con la funzione bar creo il grafico passando sulle x il numero di soggetti presenti,
#sulle y i cantieri associati ad ognuno
#il metodo xticks permette di mostrare graficamente i soggetti uno ad uno sull'asse delle x
#range(len(diz_soggetti_contratti)) passa uno ad uno tutti i numeri fino a 44,
#list(diz_soggetti_contratti.keys()) passa tutti i nomi dei soggetti
#permette di mostrare il grafico in output

def my_plot(diz_soggetti_contratti):
    """questa funzione rappresenta un grafico che mostra il numero di cantieri per soggetto"""
    plt.bar(range(len(diz_soggetti_contratti)), list(diz_soggetti_contratti.values()), align='center')
    plt.xticks(range(len(diz_soggetti_contratti)), list(diz_soggetti_contratti.keys()))
    #plt.show()
    



#capire come migliorare output del grafico
#aggiungere unittest
#fare punti bounding box    
