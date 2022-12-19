"""Questo modulo implementa funzioni di lettura e di input"""
import sys
import cv2 as cv
import numpy as np
# ---------------------------------------------------------------------------------------------- #
#funzione lettura file testo
# ---------------------------------------------------------------------------------------------- #
def lettura_input_testo(percorso_lista_file):
    """
    Questa funzione permette di caricare la lista dei file di testo aprendolo in lettura.
    La funzione ritorna una lista contenente i nomi dei file.
    Variabili in ingresso: PERCORSO_LISTA_FILE
    Variabili in uscita: testo_diviso
    """
# ---------------------------------------------------------------------------------------------- #
# Apertura del file con gestione dell'eccezione relativa all'assenza del file
# o percorso errato
# ---------------------------------------------------------------------------------------------- #
    testo_diviso=[]     # lista vuota per appendere i nomi dei file divisi
# ---------------------------------------------------------------------------------------------- #
# Tentativo di apertura file ed esecuzione operazioni
# ---------------------------------------------------------------------------------------------- #
    try:
        with open(percorso_lista_file, "r", encoding="utf8") as mio_file:
# ---------------------------------------------------------------------------------------------- #
# Operazioni sul testo presente nel file, ciclo while True
# ---------------------------------------------------------------------------------------------- #
            while True:
                riga=mio_file.readline()    # Lettura del file
                if riga!="":                # se la riga non è vuota:
# ---------------------------------------------------------------------------------------------- #
# Divide il testo usando il separatore dell'enter
# ---------------------------------------------------------------------------------------------- #
                    riga_corretta=riga.replace("\n","")
                    testo_diviso.append(riga_corretta) # Append in lista
                elif riga=="":
                    break                   # altrimenti se la riga è vuota esce dal ciclo
    except IOError as ex:   # Eccezione IOError per errori nel percorso o nel nome del file
        print(f"{ex}:\nIl file non esiste o il percorso specificato non risulta corretto.\n\
            Controllare l'esistenza del/dei file e/o il percorso del file di testo.\n\
            Il percorso inserito è {percorso_lista_file}")
        sys.exit(1)         # L'algoritmo si interrompe
    return testo_diviso

def lettura_immagine(percorso_immagini, nome_file_immagine):
    """
    Questa funzione permette di caricare l'immagine che si trova nel percorso specificato
    nella costante PERCORSO_IMMAGINI con nome del file corrispondente all'elemento della
    lista lista_nomi_file.
    Parametri in ingresso: PERCORSO_IMMAGINI, nome_file_immagine
    Parametri in uscita: immagine
    """
# ---------------------------------------------------------------------------------------------- #
# Caricamento dell'immagine
# ---------------------------------------------------------------------------------------------- #
# Eccezione nel caso in cui l'immagine è un di tipo None e/o non esiste
# ---------------------------------------------------------------------------------------------- #
    while True:
        immagine=cv.imread(f"{percorso_immagini}{nome_file_immagine}", cv.IMREAD_GRAYSCALE)
# ---------------------------------------------------------------------------------------------- #
# Se l'istanza immagine è di tipo numpy.ndarray, allora prosegue, altrimenti termina
# ---------------------------------------------------------------------------------------------- #
        if isinstance(immagine, np.ndarray):
            break
        else:
            raise IOError(f"Il file non esiste o il percorso specificato non risulta corretto.\n\
            Controllare l'esistenza del/dei file e/o il percorso del file di testo.\n\
            Il percorso inserito è {percorso_immagini} ed il file richiamato è\n\
            {nome_file_immagine}")
    return immagine
