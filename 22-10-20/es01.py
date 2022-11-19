##
# Liste
##

#TODO: creare una lista
my_list = []                                              #ho creato una lista vuota
my_list2 = [1,2,3,4]
my_list3 = [ "pippo" , 1.0, 2, 4, ["pippo", [1, 2, 3] ]]  #lista complessa
my_item = my_list3[4][1][1]                               #sono entrato nella mia lista 3 con il 4° indice, poi [1] per entrare nella sotto lista, poi [1] per prendere il 2
my_item = my_list3[-1][1][1]                              #in alternativa potevo entrare da destra con il [-1]
my_list2 [0] = -1                                         #cosi' sto cambiando il valore del primo elemento della lista da 1 a -1, rendendo le liste mutabili

try:                                                      #esempio di gestione delle eccezioni con il CS try, dove si risponde con except
    my_list[100]                                          #qui si genera un'eccezione del tipo index out of range, ma che puo' essere gestita
except Exception as ex:                                   #si crea la variabile di eccezione ex che richiama la Exception, in modo da poterla gestire
    print(str(ex))                                        # il programma non si e' bloccato per via della gestione dell'eccezione
print("done")

"""Somma di stringhe=Nuova stringa, Somma di liste=nuova lista"""
my_list4 = ["pippo", "one", "two"]
my_list5 = my_list4 + my_list2                            #l'aggancio della lista avviene alla coda del primo o del precedente addendo
my_list6 = my_list4 *10                                   #ripete la lista per 10VV

for item in my_list6:                                     #per ogni elemento presente nella lista 6, ossia 10vv la lista 4, stampa ogni elemento
    print(item)

for i in range(0,len(my_list6),2):                        #per ogni elemento che appartiene alla sequenza, printa gli [i] della lista my_list6
    print(my_list6[i])

#* Copiare una lista (dai valori in memoria)
my_copy_my_list4 = my_list4                               
"""
quello che normalmente uno pensa circa la copia delle funzioni, ma in realta' non e' cosi':
#in realta' sto solamente copiando gli ultimi valori registrati in memoria per quella lista, andando a copiare il riferimento di memoria
#creazione delle copie scorrelate dal codice:   dalla debug console pongo la #!my_copy_my_list4=list(my_list4)
#list e' un costruttore, ossia crea un nuovo oggetto da una lista preesistente, per dare poi vita ad una nuova lista, che ha vita propria rispetto alla
#precedentemente copiata
"""
#* Copiare una lista sfruttando il creatore e dando vita ad una lista vera e propria senza memory value copy
my_copy_my_list4 = list(my_list4)
print(my_list5)