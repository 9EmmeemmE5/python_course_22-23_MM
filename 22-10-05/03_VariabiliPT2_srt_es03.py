##
# Stringhe
##

from operator import le


my_str= "hello world"
print(len(my_str)) # printo la lunghezza della stringa, ossia il numero di caratteri che la compongono
print(my_str[0]) # con la [] vado a specificare cosa prendere dal contenitore, dalla  mia stringa: parto da 0, ossia il primo elemento che è la h
print(my_str[10]) # per printare l'ultimo elemento della stringa non devo inserire 11, perche si parte dallo 0 e non dall'1, quindi metto 10
print(len(my_str)-1) # alternativamente, per printare l'ultimo carattere della str, posso printare la len, ma a cui devo tolgo 1 per via della partenza dallo 0
# inserendo 11 ottengo un errore definito come "IndexError: string indedx out of range"

"""
in python è possibile usare indici negativi per pescare l'elemento della stringa corrispondente al modulo dell'indice negativo, ma da DX e non da SX, 
ma partendo da -1, per poi andare a SX ed avere indice -2, poi -3 ...
"""

my_str2 = "tre"
print(my_str2[2])
#my_str2[0] = "p" # Si è verificata un'eccezione: TypeError 'str' object does not support item assignment
"""
non si può riassegnare un carattere di una stringa
"""
print(my_str2)

print(my_str2.upper()) # ritorna una copia della stringa in UPPERCASE, mantenendo inalterata la stringa
"""
un metodo è una funzione applicabile a tutte le variabili di un dato tipo, come una stringa, 
difatti tutte le variabili di tipo stringa possono essere metodizzate
"""
print(input("inserisci una stringa...").lower()) # è possibile programmare in maniera asincrona dando all'utente la possibilità di scrivere una stringa
print("due" == "DUE") # restituisce un False perché non si è normalizzata la coppia di stringhe in lower case od upper case
print("due".lower() == "DUE".lower()) # restituisce un True perche si è normalizzata la coppia di stringhe in lowercase
"""
l'operatore == ci permette di chiedere a python di confrontare due stringhe per controllare che esse siano uguali oppure no
"""
my_str3 = "supermario"
# prendere i primi due elementi di my_str3
my_sub_str = my_str3[0] + my_str3[1] # metodo base
print(my_sub_str) #print della sub str
my_sub_str1 = my_str3[0:2] # operazione di slice
print(my_sub_str1) # ci si aspetta "sup" ma in realtà si va ad escludere l'ultimo carattere dell'indice finale dato dallo slice, ossia l'indice di stop
"""
nello slice l'indice di star viene considerato
mentre invece l'indice di stop no e si va a considerare quello precedente
"""
my_sub_str2 = my_str3[0:6:2] # logica dello slice: indice di start, indice di stop, step incrementale usato per lo slice, ossia un intervallo regolare
print(my_sub_str2)
"""
in questo caso se si printa per step di 2, quindi 0,2,4, non il 6 perché è quello di stop
"""