"""Questo modulo implementa funzioni relative alle operazioni compiute dall'utente"""

def inserimento_valori_numerici(stringa_numerica):
    """
    Questa funzione implementa l'input utente dei valori numerici che devono essere sempre
    maggiori o uguali a 0 ed interi in diversi contesti:
    -nel caso di un'immagine è formata da pixel che, a livello matriciale, sono
    identificati da indici maggiori di 0
    -nel caso di inserimento delle coordinate dei punti della regione di interesse (pixel)
    -nel caso di scelta del valore di riferimento dell'immagine sogliata 0 o 255 per la
    sogliatura adattativa
    Parametri in ingresso: stringa_numerica
    Parametri in uscita: numero_intero
    """
# ---------------------------------------------------------------------------------------------- #
# Variabile sentinella dello stato di inserimento del numero
# ---------------------------------------------------------------------------------------------- #
    stato=0
# ---------------------------------------------------------------------------------------------- #
# Fintanto che lo stato non cambia dallo 0
# ---------------------------------------------------------------------------------------------- #
    while stato==0:
# ---------------------------------------------------------------------------------------------- #
# Si prova l'inserimento del numero intero
# ---------------------------------------------------------------------------------------------- #
        try:
            numero_intero=int(input(stringa_numerica))
# ---------------------------------------------------------------------------------------------- #
# Se il numero inserito è maggiore o uguale a zero
# ---------------------------------------------------------------------------------------------- #
            if numero_intero >=0:
# ---------------------------------------------------------------------------------------------- #
# Uscita dal ciclo while con restituzione dell'inserimento
# ---------------------------------------------------------------------------------------------- #
                stato=1
                return numero_intero
# ---------------------------------------------------------------------------------------------- #
# Altrimenti viene stampato un errore se viene inserito un numero minore di zero
# ---------------------------------------------------------------------------------------------- #
            print("Si deve inserire un numero maggiore di 0!")
# ---------------------------------------------------------------------------------------------- #
# Eccezione del tipo ValueError se si inseriscono stringhe
# ---------------------------------------------------------------------------------------------- #
        except ValueError as ve_ex: # Valore non appropriato
            print(f"{ve_ex}: Bisogna inserire un numero intero!")

def inserimento_valori_float(stringa_numerica):
    """
    Questa funzione implementa l'input utente dei valori numerici di tipo float
    che devono essere sempre maggiori di 0 nel contesto dell'inserimento dell' epsilon per
    l'algoritmo di clusterizzazione con il DBSCAN.
    Parametri in ingresso: stringa_numerica
    Parametri in uscita: numero_float
    """
# ---------------------------------------------------------------------------------------------- #
# Variabile sentinella dello stato di inserimento del numero
# ---------------------------------------------------------------------------------------------- #
    stato=0
# ---------------------------------------------------------------------------------------------- #
# Fintanto che lo stato non cambia dallo 0
# ---------------------------------------------------------------------------------------------- #
    while stato==0:
# ---------------------------------------------------------------------------------------------- #
# Si prova l'inserimento del numero float
# ---------------------------------------------------------------------------------------------- #
        try:
            numero_float=float(input(stringa_numerica))
# ---------------------------------------------------------------------------------------------- #
# Se il numero inserito è maggiore di zero
# ---------------------------------------------------------------------------------------------- #
            if numero_float >0:
# ---------------------------------------------------------------------------------------------- #
# Uscita dal ciclo while con restituzione dell'inserimento
# ---------------------------------------------------------------------------------------------- #
                stato=1
                return numero_float
# ---------------------------------------------------------------------------------------------- #
# Altrimenti viene stampato un errore se viene inserito un numero >=0
# ---------------------------------------------------------------------------------------------- #
            print("Si deve inserire un numero intero o float maggiore di 0!")
# ---------------------------------------------------------------------------------------------- #
# Eccezione del tipo ValueError se si inseriscono stringhe
# ---------------------------------------------------------------------------------------------- #
        except ValueError as ve_ex: # Valore non appropriato
            print(f"{ve_ex}: Bisogna inserire un numero float od intero!")
