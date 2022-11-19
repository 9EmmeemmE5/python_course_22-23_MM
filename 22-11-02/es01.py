##
# LETTURA E SCRITTURA
##

# con le liste si creano delle tabelle, con numpy si creano delle matrici
# un file binario necessita di un algoritmo o una libreria per essere codificato, altrimenti, ad esempio un'immagine, se aperto con un editor testuale,
# un file binario e' composto da caratteri che non hanno molto senso se non decodificati con un apposito algoritmo

# fisicamente, sul disco si ha una serie di codici binari, che possono essere letti con appositi software che permettono di decodificare e codificare il codice:
# se ad esempio scriviamo 12, troviamo come sequenze memorizzate 31 e 32, ossia le codificazioni dei caratteri 1 e 2, piuttosto che 1100, ossia un numero.
# se voglio convertire la stringa "12", allora devo usare la funzione int, altrimenti rimane codificato come successione di caratteri 1 e 2.

# se volessi scrivere 3 float a 10 numeri dopo la virgola, per questi tre numeri utilizzo 28 byte, notando anche una sequenza particolare che si ripete, ossia la 0D 0A,
# che rappresenta la sequenza per andare a capo.
# se avessi un numero molto lungo con decine di migliaia di cifre decimali, se si salva il file in formato testuale, la sua dimensione sara' molo grande,
# mentre in binario sara' molto più piccola, ma con l'handicap di andare a capire come sono stati codificati i file binari in modo da poterli poi decodificare per l' utlizzo.

# se interpreto la sequenza 3F 9E 71 24 come testo ottengo ?zq$, che non ha senso, ma se lo codifico come float, ottengo 1.2378277776825,
# che e' quello che e' stato usato per generare la combinazione in binario dello stesso (il prof ha fatto un check per osservare la dimensione); il rapporto di dimensione tra 
# binario e testuale e' di 1:4.

# se chiedo di aprire un file con la funzione open, allora dovro' anche chiuderlo per poterne permettere l'uso ad altri utenti,
# altrimenti rimane aperto solo per me che sto scrivendo

"""Codice per la gestione dei file"""

def main():
    """Entry-point"""
    #apertura di un file...
    my_file = open("esempio_open_funct.txt")    #in grigetto perche non vi e' accesso, inoltre rimane aperto, non viene chiuso
    # my_line = my_file.readline()    #cerca la terminazione 0D 0A per definire la fine della linea, cercando la srtringa
    # my_line = my_file.readline()
    # my_line = my_file.readline()
    # print(my_line, my_line =="")    #controllo della lettura oltre la fine del file se restituisce il True, allora python ha raggiunto la fine del file senza eccezione
    
    my_line = 0
    
    #versione senza while true
    
    # while my_line != "":
    #     my_line = my_file.readline().rstrip()
    #     print(my_line)
    # else:
    #     break
    
    #versione while true
    
    while True:
        my_line = my_file.readline().rstrip() # nel print si denota \end \n come se si stesse codificando una f.string, quindi per pulire la stringa si usa il ".rstrip()"
        if (my_line == ""):             
            break
        print(my_line)
    my_file.close()
    my_line = my_file.readline() #va in eccezione perche sto operando su un file chiuso, distruggendo le connessioni logiche con lo stesso, quindi #!CHIUDERE SEMPRE IL FILE DOPO
main()                           #! AVERCI OPERATO SOPRA

# se volessi creare una tabella in python con la struttura riportata nel file di testo che si sta usando in questo file python, vedi es02.py