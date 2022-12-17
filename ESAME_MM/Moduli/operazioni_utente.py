"""Questo modulo implementa funzioni relative alle operazioni compiute dall'utente"""
#import unittest
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

# def scelta_metodo_creazione_roi():
#     """
#     Questa funzione implementa la scelta che deve compiere l'utente in merito a come vuole
#     impostare la bounding box per determinare la regione di interesse dell'immagine sulla quale
#     eseguire la compilazione.
#     Parametri in ingresso:
#     Parametri inuscita: metodo_roi
#     """
#     print("Scegliere il metodo di inserimento dei limiti della bounding box:\n\
# la scelta avviene tra metodo manuale e metodo automatizzato.\n\n\
# Si ricorda che la bounding box viene inserita nell'algoritmo con logica\n\
# \"Top-Left to Bottom-Right\", ossia inserendo prima i dati del punto\n\
# in alto a sinistra del rettangolo di ritaglio e poi del punto in basso a destra")
#     scelta_metodo_roi=inserimento_valori_numerici("Scegliere tra metodo manuale e\n\
# metodo automatizzato digitando rispettivamente \"0\" o \"1\": ")
#     print(f"Si è scelto {scelta_metodo_roi}: esecuzione controllo...")
#     if scelta_metodo_roi==0 or scelta_metodo_roi==1:
#         return scelta_metodo_roi
#     raise TypeError("Type Error:Inserimento errato, si può inserire solamente \"0\" o \"1\"")
