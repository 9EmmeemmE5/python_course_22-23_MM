"""TRY-EXCEPT-FINALLY"""
# TRY-EXCEPT-FINALLY
##

#nel momento che ho un'eccezione, salto nella clausola finally, raiso l'eccezione
# e poi richiamo l'eccezione
def main():
    """Entry point"""
    print("hello")
    try:
        my_file=open("./22-11-03/miofile.txt","w+")
        try:    #NB: se si mette un path, sempre quello relativo e mai l'assoluto con "./..."
            my_file.write("hello world\n")
            a_value = 5 / 0 #inserisco un'operazione errata
            print(a_value)  #printo la variabile
        finally:
            print("sono nella clausola finally") #NB: può accadere che in caso di eccezioni
            my_file.close()                      #    le scritture non vengano finalizzate
    except OSError as ex:   #ho inserito l'OSError per via dello snippet della doc di open
        print(f"Ahi, Ahi, errore nella gestione del file.. {ex}")
    except Exception as ex:
        print(f"Ahi, Ahi... {ex}")
main()
