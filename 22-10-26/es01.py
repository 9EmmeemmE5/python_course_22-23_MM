##
#   FUNZIONI ED OPERATORI SULLE LISTE
##


my_list = []                                                        #creo una lista vuota
my_list.append(0)                                                   #comando append permette di aggiungere un elemento alla lista vuota
print(my_list)                                                      #print
my_list.append(2)                                                   #appendo un secondo elemento
print(my_list)                                                      #print

#TODO: Creare una lista di valori da 1 a 10 estremi inclusi...

my_list_of_values = []                                              #creo la lista vuota

for i in range(1,11):                                               #iterazione  for per elem. i nel range che va da 1 a 10 estremo escluso, quindi 11
    my_list_of_values.append(i)                                     #append elemento i nel range
my_list_of_values.insert(3,-1)                                      #inserisce alla posizione 3 l'elemento -1
my_list_of_values.insert(3,-100)                                    #come sopra ma con -100
#my_list_of_values.remove(1000)                                     #rimuove alla posizione 1000, quindi qualcosa che non esiste, ma genera eccezione

#TODO: Rimuovere valore dalla lista... senza la gestione delle eccezioni...

item_to_remove = 1000                                               #variabilizzando l'elemento da rimuovere
if(item_to_remove in my_list_of_values):                            #CS if che dice che se e' presente, allora rimuovi la variabile item_to_remove,
    my_list_of_values.remove(item_to_remove)                         
else:                                                                         #altrimenti
    print(f"l'elemento {item_to_remove} non presente in {my_list_of_values}") #printa la f string qui a sinistra

try:
    my_list_of_values.remove(1000)
except Exception as ex:
    print(f"Ahi Ahi Ahi... I got a {ex} puncture")                  #Carlos Sainz in (S)Pain
print(my_list_of_values)                                            #printa la lista di 10 elementi da 1 a 10 come se fossero 10 append

print(my_list_of_values.sort())                                     #la funzione sort ritorna un None, ma ha lo scopo di ordinare, nonostante nel bene o nel male vada a modificare la lista
print(my_list_of_values.sort(reverse=True))                         #difatti il sort agisce nella funzione di partenza, andando a sovrascrivere, quindi occorre prima creare la copia della lista con il list per poi andare ad operare con il sort

if(-101 in my_list_of_values):
    index_of_value = my_list_of_values.index(-101)                  #ritorna il primo indice della lista, ma se fosse stato -101 avrebbe ritornato un eccezione
print(my_list_of_values)

my_deleted_value = my_list.pop(100)                                 #rimuove e ritorna l'item all'index specificato dallo user
print(my_deleted_value)                                             #print

#! TEST DI UGUAGLIANZA
#! Due liste sono uguali/non uguali se e solo se hanno la stessa lunghezza e gli stessi elementi/se hanno lunghezza e/o elementi diversi

#! min, max, ... VEDI SLIDE

print(my_list_of_values[4:6])                                       #come in MatLab ma senza l'ultimo indice come per il range, quindi 4 e 5
print(my_list_of_values[4:8:2])                                     #printa 2 elementi dal 4 all'8 con step da 2, quindi 4, 6, 8 e si esclude l'ultimo, quindi 8,; risultato 4 e 6 