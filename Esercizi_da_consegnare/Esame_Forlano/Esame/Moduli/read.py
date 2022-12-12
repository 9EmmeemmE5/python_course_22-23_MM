'''
Questo modulo contiene diverse funzione per la lettura e apertura di file, 
immagini o input in base alla funzione scelta.
'''
# Importo le librerie
import sys
import cv2 as cv

def read_int(str_x):
    '''
    Questa funzione permette di prendere in input un numero intero, in caso di valore errato ci sarà un'eccezione.
    @param str_x: stringa da far visualizzare all'utente
    @return res: ritorna un intero
    '''

    letto = False # Condizione
    while not letto:
        # Gestione dell'errore
        try:
            res = int(input(str_x)) # Faccio il cast a intero
            # Verifico che l'input sia maggiore di zero
            if res >= 0:   
                letto = True
            else:
                print("Il numero inserito deve essere maggiore di zero..")
        except ValueError: # Valore non appropriato
            print("Bisonga inserire un numero interno...")
    return res


def read_txt(PATH_FILE):
    '''
    Questa funzione permette di leggere un file e ritornare una lista con 
    i nomi dei file all'interno del file txt.
    @param PATH_FILE: posizione del file
    @return name_splitted: ritorna una lista con i nomi dei file
    '''
    # Gestione dell'errore
    try:
        file = open(PATH_FILE, "r") # Apro il file in modalità di lettura
    except IOError: # File non esiste
        print(f'il file non esiste, controllare PATH_file {PATH_FILE}')
        sys.exit(1) # Printo l'errore ed esco

    # Operazione di lettura
    riga = file.read() # Leggo tutto il file
    name_splitted = riga.split("\n") # Splitto la lista con il separatore new line

    # Operazione di chiusura
    file.close()

    return name_splitted


def read_img(PATH_IMG, nome):
    '''
    Questa funzione permette di aprire un'immagine con OpenCV e 
    solleva un'eccezione di tipo ValueError in caso di file mancante.
    @param PATH_IMG: posizione del file
    @param nome: nome del file con estensione
    @return img: ritorna un array di due dimensioni
    '''
    # Operazione di lettura e conversione immagine in scala di grigi
    img = cv.imread(f'{PATH_IMG}{nome}', cv.IMREAD_GRAYSCALE)

    # Se l'array img è un NoneType sollevo un'eccezione
    if img is None:
        raise ValueError("L'immagine non esiste, controllare PATH_img e l'immagine")

    return img
