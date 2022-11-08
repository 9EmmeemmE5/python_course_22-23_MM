##
# CICLI 3
##

#TODO: chiedere all'utente un numero > = 0; uscire dal ciclo se numero == -1 o comunque se <=0; calcolare min, max, media

#* CALCOLO DELLA MEDIA

my_sum = 0 #codifica la somma
num_count = 0 #codifica quanti numeri ho inserito
min_val = None #codifica il minimo: potrebbe potenzialmente essere codificato come infinito, mentre invece 0 è errato perche non so quanto può valere il minimo, quindi partendo da
max_val = None #una conoscenza nulla posso impostare come minimo il primo valore inserito; possiamo inserire il "None" ossia un valore speciale che significa letteralemente"non lo so"

while True:
    my_num = float(input("Inserisci un numero > 0 ..."))
    if (my_num > 0):
        my_sum += my_num
        num_count +=1
        # al primo numero aggiorno il valore minimo..
        if(num_count == 1):     # baseline, linea di riferimento per il confronto
            min_val = my_num    # se inserisco un solo numero allora il minimo coincide con l'unico numero inserito
            max_val = my_num    # se inserisco solo un numero allora il min ed il max coincidono
        elif(min_val < my_num): # faccio un confronto senza una base, al primo gior eseguo il confronto; se invece ho inserito un numero nuovo e, 
            min_val = my_num    # qualora fosse minore di 1, ossia quello relativo a riga 20-21, allora aggiorna min con il numero più basso di 1 appena inserito
        elif(my_num > max_val): # devo inserire un altro elif per la condizione del massio, ossia se il mio numero inserito dopo il primo inserimento è maggiore del max,
            max_val = my_num    # allora il massimo coincide con il numero appena inserito dopo il primo valore massimo registrato
    else:
        break                   #CHIUSURA WHILE TRUE, senza non sarebbe raggiungible il codice sottostante
avg_val = my_sum / num_count
print(f"La media è: {avg_val:.3f}, il valore minimo è {min_val}, mentre il valore massimo è {max_val}")