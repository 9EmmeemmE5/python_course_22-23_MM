"""test sul controllo della classe numero"""
from number import Number

my_number = Number() #implicitamente sto richiamando il metodo init e, in assenza di attributi come nelle funzioni, richiama un'eccezione
my_value= str(my_number)
#una cosa del genere è ammissibile? se eseguo il debug osservo che my_value è una stringa ed il suo elemento 0 è la parentesi quadra,
#quindi quando creo una stringa uso il metodo all'interno della mia classe che mi consente di convertire in stringa un numero
my_number.setNumber(4.0)
print(my_number)
# my_number._number = "nono..." #non si accede mai all'attributo, ma solamente con il SETTER
try:
    my_number.setNumber = "nono..." #restituisce TypeError : 'str' object is not callable
except TypeError as ex:
    print(f"numero sbagliato {ex}")
print(my_number)
#se viene passato number senza valori di default allora ho un'eccezione, se metto il valore di default, allora restituisce quello
#il metodo base di object quando converte a stringa, se si esegue il print e senza implementazioni di vario tipo, viene printata quella di default nelle built-in
#ossia viene printato il metodo.Classe object at INDIRIZZO, come nel caso in cui io sto scrivendo il codice durante la lezione "<number.Number object at 0x0000017E3ACDF340>"
#quando traduco un oggetto in stringa eseguo una serializzazione del mio oggetto, la print implicitamente chiama il metodo str e, con il metodo,
#se l'oggetto esiste allora usa quel metodo, se invece non esiste cammina a ritroso fino alla superclass default object e se anche li non esiste, allora si ha un exception raising da python
my_number.setNumber(8) #con l'implementazione del raise TypeError dal controlo isinstance()
print(my_number)
