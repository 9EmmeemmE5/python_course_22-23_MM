"""test sul controllo della classe numero"""
from number import Number,ComplexNumber #non ha senso reinserire "from number import ComplexNumber"

my_number = Number() #implicitamente sto richiamando il metodo init e, in assenza di attributi come nelle funzioni, richiama un'eccezione
my_value= str(my_number)
#una cosa del genere è ammissibile? se eseguo il debug osservo che my_value è una stringa ed il suo elemento 0 è la parentesi quadra,
#quindi quando creo una stringa uso il metodo all'interno della mia classe che mi consente di convertire in stringa un numero

my_number.setNumber(4.0)
my_number2 = Number(5.0)
my_number3 = my_number2 + my_number
my_number4 = my_number2 + 4.0 #ritorna un eccezione di AttributeError perché nella classe float non esiste l'attributo 'getNumber', ma si può correggere con un isinstance()

#complex number.. 0+4i
my_complex_number=ComplexNumber(0.0, 4.0)
print(my_complex_number)
my_complex_number2=ComplexNumber(imgPart=4.0) #si può fare anche in questo modo qui, come nel caso in cui si abbiano molti argomenti, dove apunto conviene specificare l'attributo da usare e lasciare di default gli altri
# print(my_complex_number2.getValue()) #va in errore perche non ho un attributo richiamato nelle parentesi di getValue()
print(my_complex_number2.getValue("real"))
print(my_complex_number2.getValue("img"))
#python agisce in modo molto utile e potente ma allo stesso tempo pericolosissima: le variabili dell'oggetto vengono serializzate in memoria come un dizionario, quindi lo rende salvabile e modificabile da parte dall'utente, permettendo di derializzare e deserializzare l'oggetto, andando ad alterare lo stato dell'oggetto, ovviamente rispettando valori e tipi
print(my_complex_number2)

print(type(my_number3)) #ritorna number.Number ossia ritorna come tipo l'oggetto Number che fa parte della classe number
print(my_number)
# my_number._number = "nono..." #non si accede mai all'attributo, ma solamente con il SETTER
try: #eccezione messa in 
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
