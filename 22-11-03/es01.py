##
# EXCEPTION HANDLIG
##
#exception handling: occorre gestire le eccezioni; si può volontariamente sollevare
#un'eccezione con l'apposita keyword "raise" a cui si aggiunge la classe di eccezione
#che si vuole sollevare, come ad esempio l'eccezione di TypeError, ossia quella legata a ...
#oppure l'eccezione ValueError, ossia quella legata a ...

#pylint ed il linting: libreria che fornisce uno scoring del codice scritto in python
#sulla base di un certo livello stilistico qualitativo, assegnando un punteggio in
#decimi e definendo le possibili correzioni applicabili al codice in analisi.
#Per operare il pylint, occorre, da terminale, andare con il comando "cd" nel path
#di lavoro del file python, per poi digitare la combinazione "pylint nomefile.py"

#quando si gestiscono le eccezioni si inserisce prima l'eccezione particolare, per
#poi inserire la generale, quindi si mette prima quella al più basso livello di
#dettaglio o gerarchia, per poi andare a salire fino a quella al più alto livello

#la clausola finally in generale viene messa in esecuzione sia nel caso in cui
#l'eccezione venga sollevata, che nel caso in cui essa non venga sollevata; funge
#come blocco di codice di chiusura a valle dell'esecuzione ed ha delle casistiche di
#utilizzo particolari: non è buono codificare con l'ordine try, finally, except,
#ma un try-except, che contiene un try-finally.

#con il construtto with si ha l'unione del try-finally, codificandolo come:
#"with open(filename, "w+") as alias" occorre definire un alias
""" test del raise e gestione del try-except"""

def input_poistive_number():
    """function that raises ValueError if number is >= 0, otherwise it returns the number"""
    my_number = float(input("inserisci un numero maggiore di 0..."))
    if my_number >0:
        return my_number
    raise ValueError("devi inserire un numero maggiore di 0...")#consente di sollevare un'eccezione

def main():
    """Entrypoint"""
    while True:           #eseguo un while true per poter permettere il reinserimento
        try:              #ci consente di intercettare l'eccezione sollevata
            my_number = input_poistive_number()
            print(f"{my_number}")                               
            # dà un secondo errore di Unbound Local Error, perche la variabile viene referenziata
            # prima del suo utilizzo, risolvibile spostando questo print sopra dato che posso già
            # far comparire l'eccezione quando sto digitando e non dopo quando printo
            break #metto il break qui perche se io inserisco un numero positivo, allora non sollevo un'eccezione, quindi breako
        except ValueError as ex:                            #se avessi messo il break sotto...
            print(f"{ex}")                                  #CS dell'exception handler
        print("Done")
main()
