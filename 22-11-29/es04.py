"""map round"""

#il reduce incapsula oggetti di tipo tuple dentro altre tuple, andando ad utilizzarlo per somme o divisioni, in genere calcoli aritmetici

#1
my_float = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

#TODO: attraverso il map creare il quadrato di tutti gli elementi arrotondato alla terza cifra decimale

map_results = list(map(lambda x: round(x**2,3), my_float)) #il round prende in ingresso l'oggetto di cui eseguire il round e come secondo elemento il numero di cifre decimali

print(map_results)

#2
my_list_to_be_filtered = ["Polonia","Korea del Nord","Brasile","Argentina","Giappone","Germania", "Uruguay","Italia","Togo"]

#TODO: attraverso il map stampare tutte le nazioni che hanno almeno 7 caratteri nel loro nome

filtered_results = list(filter(lambda word: len(word)>=7, my_list_to_be_filtered)) #applico il len della entry word della lambda function >=7 della lista my_list_to_be_filtered
print(filtered_results)

#3
from functools import reduce #da inserire per non andare in errore con il reduce
to_be_reduced_num_list = [5,7,8,9,2,6,7]

reduced_result = reduce(lambda x,y: x*y, to_be_reduced_num_list, ) #la reduce non richiede il cast, difatti se comprime un dato tipo, restituisce lo stesso tipo, inoltre, se si vuole inserire il valore iniziale da cui far iniziare la reduce, inserisco il numero, altrimenti, se vuoto, parte dal primo indice
print(reduced_result)