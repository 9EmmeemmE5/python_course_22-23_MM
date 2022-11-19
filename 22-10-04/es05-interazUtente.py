"""Interazione con lo user"""

# Chiedere all'utente di inserire un numero
my_num = float(input("inserisci un numero"))
print(type(my_num))

# programmazione sincrona, ossia l'utente inserisce gli input,
# ossia non posso stampare la riga 7 prima che venga inserito da parte dello user un numero
# se si inserirre un numero float verrebbe restituita la classe stringa dal comando print
# a meno che non venga inserito a monte di my_num il comando float()
# infine, se si inserisce "pippo" esce fuori un'eccezione TypeError dato che si e' inserita
# una stringa in input che non e' convertibile in numero: a tal proposito 
# occorre gestire le eccezioni, altrimenti il programma smette di funzionare,
# quindi va circoscritta la modalita' con cui agisce 
