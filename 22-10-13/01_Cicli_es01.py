##
#   CICLO FOR
##

"""
Il ciclo for esegue il codice all'interno di contenitori, ossia la stringa e la tuple 
"""

my_string = "SuperPython"
for item in my_string:      #per ogni elemento in my_string genera item e printalo 
    print("carattere", item, sep='|', end='\t')   
"""
il comando end con il tabulatore separa le lettere con una tabulazione (pressione tasto TAB),
mentre con sep='|' e con carattere, item inserisco prima del separatore la stringa carattere
Se volessi estrarre il singolo carattere occorre inserire il corrispettivo indice tra [], 
ponendo attenzione al fatto che per l'ultimo non occorre mettere len(...) ma len(...)-1 
perche altrimenti si incapperebbe in un errore, dato che si va fuori range 
"""

print(my_string[0])
print(my_string[1])
print(my_string[2])
print(my_string[3])
print(my_string[4])
print(my_string[5])
print(my_string[6])
print(my_string[7])
print(my_string[8])
print(my_string[9])
print(my_string[10])
print(my_string[len(my_string)-1])

#* che nella versione for è

for i in range(len(my_string)):
    print(my_string[i])

for i in range(4):
    print(i)

for i in range(0,len(my_string),2):              #imposto un for che parte da 0, ha passo 2 e termina alla fine della stringa, considerando il ciclo nel range della stringa
    print(f"indice {i} valore = {my_string[i]}") #printa formattando gli indici richiamati dalla i, quindi parto dallo 0, con passo 2, fino alla fine

for i in range(len(my_string)-1,-1,-1):             #imposto un for che va in errore perche non ho inserito il -1 dopo il len per partire dall'ultima, correggo 
    print(f"indice {i} valore = {my_string[i]}")    #inserendolo con l'esclusione dello stop a -1

#TODO: stampare dall'ultimo al primo usando indici negativi

for i in range(-1,-len(my_string)-1,-1):            #parto da -1, arrivo a -len(my_str)-1 perche viene escluso lo STOP, con step negativo di -1
    print(f"indice {i} valore = {my_string[i]}")    #Se fosse stato {my_string[-i]}, sarebe andato da 1 al finale, ma avrebbe continnuato perché sarebbe andato a len(my_string)+1

#! Inserendo il -1 forzo il ciclo a partire dall'ultimo indice, altrimenti lo avrebbe escluso con un eccezione "Index_out_of_range" se fosse stato range(-len(my_string)-1,-1,-1)

my_list_of_value = ["ciao", "mondo", 1, 2, 3.0, True, ["pippo", "pluto"]]   #La tuple è scritta con le (,) ed il separatore è la virgola , mentre, se le parentesi sono [] ho una lista

"""
come per le liste e la tuple si accede allo stesso modo con lo stesso metodo, ossia il len(...)-1, -1 per l'elemento finale;
quello che è particolare in python è che dentro una lista posso mischiare diversi tipi, come int, float, str, boole, ma anche una lista stessa (sub-lista).
Se volessi stampare gli oggetti o volessi iterare su questo contenitore, posso farlo come per i contenitori visti in precedenza
"""
for item in my_list_of_value:
    print(item)

#sopra abbiamo fatto un for per una lista, qui per una stringa, ma aanche sopra abbiamo fatto un "range", quindi 
#! un for è applicabile ad una qualsiasi collezione iterabile

print(my_list_of_value[6][1]) #ho stampato esattamente pluto, perche la prima [] individua l'elemento 7 (parto dallo 0) della lista, che è una lista, poi la 2° [] prende il 2°el.

my_identity = [[1,0],[0,1]] #[1,0,0,1] è la matrice identità scritta in notazione informatica 2x2, ma posso modellarla andando ad inserire 2 liste, una per ogni riga

#* gli oggetti che sono collezione sono iterabili come quanto visto in precedenza con il ciclo for, quindi ogni contenitore (liste, tuple, stringhe, risultato del range...)

#TODO: scrivere un codice che, senza un reshape della matrice [1, 2, 1, -1], somma ogni elemento della matrice e restituisce il risultato della somma
#creo una variabile somma s; per ogni riga-i: per ogni colonna-j: s+=A[i][j]; la parte esterna [i] gira molto lentamente, mentre l'interna, ossia la [j] gira più velocemente

#

n_rows = 100

n_cols = 50

#per ogni riga
#per ogni colonna
#stampa indice di riga e colonna...
for i in range(0, n_rows):
    for j in range(0, n_cols):
        print(f"A[{i}][{j}]")   #quando il for si concatena come in questo caso, ho 100 operazioni concatenate con 50 interne, quindi esegue 5000 iterazioni

#! nel caso di operazioni con immagini, per applicare un filtro blur o di sfocamento su un'immagine 1000X1000 con un kernel 11x11, eseguo 4 for concatenati da
#! 1000x1000x11x11 = 121.000.000 iterazioni; in MatLab nel for con le istruzioni di start e stop + intervallo, non si ha esclusione dello stop, con indici che sono positivi, quindi non si parte dallo 0
