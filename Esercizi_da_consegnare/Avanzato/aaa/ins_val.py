def inserimento_valori_numerici(stringa_numerica):
    """
    Questa funzione implementa l'input utente dei valori numerici che devono essere sempre
    maggiori di 0 ed interi in diversi contesti:
    -nel caso di un'immagine è formata da pixel che, a livello matriciale, sono
    identificati da indici maggiori di 0
    -nel caso di inserimento delle coordinate dei punti della regione di interesse (pixel)
    -nel caso di scelta del valore di riferimento dell'immagine sogliata 0 o 255 per la
    sogliatura adattativa
    Parametri in ingresso: stringa_numerica
    Parametri in uscita: numero_intero
    """
    stato=0
    while stato==0:
        try:
            numero_intero=int(input(stringa_numerica))
            if numero_intero >=0:
                stato=1
                return numero_intero
            print("Si deve inserire un numero maggiore di 0!")
        except ValueError as ve_ex: # Valore non appropriato
            print(f"{ve_ex}: Bisogna inserire un numero intero!")