###
#  Stringhe
###

print("**********")
print("*" * 40)  #l'operatore somma concatena le stringhe, mentre l'operatore di moltiplicazione le ripete 40 o n volte

my_str = "abc" * 40
print(my_str)

my_int = 22
my_str_from_num = str(my_int) 

"""
si sta costruendo un oggetto di tipo stringa usando il costruttore, ossia una funzione particolare che ci 
permette di creare un oggetto a partitre da un numero
"""

my_new_str_ = my_str_from_num.capitalize()

my_str_2 = "blablacar"
my_str_3 = my_str_2.replace("bla","", 1)

"""
con il comando replace si riesce a sostituire il contenuto vecchio di una stringa esistente con il contenuto che viene specificato come "new" nel comando,
opzionalmente si puo' aggiungere un counter, il quale indica quante occorrenze, a partire dalla prima, devono essere sostituite
"""

#print("ciao:"il mio nome e' Marco") #e' un errore perche si sta scrivendo una stringa con le double quotes andando a spezzare la stringa per via del simbolo "
print("ciao:\"il mio nome e' Marco\"") #stringa corretta per via dell'inserimento della sequenza di escape \"

"""
NB: se si inserisce solo un backslash si puo' incorrere in errore perche non si va a stampare il " fintanto che non viene inserito una sequenza completa \"
NB2: simboli occupati da python #\"
"""

print("Adriano\nMancini\nFondamenti\ndi\nInformatica") #\n e' il new line quindi va a capo
print("Adriano\tMancini\tFondamenti\tdi\tInformatica") #\t e' la tabulazione ossia coincide con una pressione del tasto Tab
print("Adriano\rMancini\rFondamenti\rdi\rInformatica") #\r restituisce solo l'ultima parola della stringa


my_float_num = 1.23456789
my_float_num2 = 121.23456789
print(my_float_num)
print(my_float_num2) #stampa i float allineati tutti a sinistra, poco desiderabile in terimini di formattazione
#print("%.2f" , my_float_num) #stampa i float allineati tutti a sinistra ma con 2 soli decimali, ancora poco desiderabile in terimini di formattazione

"""
NB: non i spuo' inserire la virgola quando si formatta, in quanto puo' essere interpretata come un elemento della formattazione, 
piuttosto che un separatore dei campi della variabile
"""

print("%.2f" % my_float_num)
print("%.2f" % my_float_num2)
print("%10.2f" % my_float_num) #stampa destinando 10 slot ai caratteri e 2 ai decimali del float 1
print("%10.2f" % my_float_num2) #stampa destinando 10 slot ai caratteri e 2 ai decimali del float 2
print("%10.2f %10.2f" % (my_float_num , my_float_num2)) # tuple 
print("%010.2f" % my_float_num2) #stampa facendo uno zero filling di una disponibilita' di 10 caratteri

"""
usare la formattazione con il comando %xxf, con x i relativi parametri desidedrati, si riesce a creare una formattazione che assume un senso se si 
generare un output tabulato, ad esempio:
"""

print("%10s %10s" % ( "rpm" , "temp" )) #ho printato una tuple
print("%10.2f %10.2f" % (my_float_num , my_float_num2)) 

my_tuple = ("rpm","temp") #la mia tuple
print(my_tuple[0][-1]) #con il primo [] si sceglie l'elemento della tuple, mentre invece con il secondo [] si va a scegliere il carattereù

"""
non si ha una concatenazione di stringhe, ma contenitori che possono contenere diverse tipologie di dati
"""

my_record = "1500;84.5;0.1;1.5"  #stringa di un CSV o comma separated value, in questo caso con separatore ;
my_list_of_values = my_record.split(";") #operazione di split della stringa del csv
print(my_list_of_values) #restituisce una lista di stringhe e non di numeri, perche dal terminale, nel print ho le single quote agli estrei del numero
print(my_list_of_values [3]) #restituisce 1.5
print(my_list_of_values [-1]) #restituisce 1.5 ma con lettura da destra
print(type(my_list_of_values[len(my_list_of_values)-1])) #restituisce il tipo dell'elemento corrispondente a 1.5 con la restituzione data dall'indice len-1
print(type(float(my_list_of_values[len(my_list_of_values)-1]))) #restituisce il float dell'elemento... in modo da convertirlo da str a float

print(f"il mio primo numero e': {my_float_num}; il mio secondo numero e': {my_float_num2}")  #f.string, ossia stringa formattata
print(f"il mio primo numero e': {my_float_num*2:10.2f}; il mio secondo numero e': {my_float_num2*5:10.2f}")  #f.string, dove si specifica come formattare la variabile singolarmente