"""Modulo che implementa le funzioni per la determinazione della regione di interesse"""
#import unittest

from Moduli.operazioni_utente import inserimento_valori_numerici

def creazione_roi_manuale(immagine):
    """
    Questa funzione implementa la creazione della regione di interesse con il metodo manuale
    Parametri in ingresso: immagine
    Parametri in uscita: immagine_roi
    """
# ---------------------------------------------------------------------------------------------- #
# Stampa del messaggio di istruzioni sulla digitazione dei valori per la creazione della bounding
# box
# ---------------------------------------------------------------------------------------------- #
    print("Ingresso nel metodo manuale della creazione della regione di interesse:\n\
ricordando la logica di inserimento Top-Left e Bottom-Right, inserire manualmente\n\
nell'ordine riportato le coordinate x ed y dei due punti della regione di interesse...\n")
# ---------------------------------------------------------------------------------------------- #
# Associazione della tuple di righe e colonne dell'immagine alle dimensioni della matrice
# ---------------------------------------------------------------------------------------------- #
    (righe,colonne)=immagine.shape
# ---------------------------------------------------------------------------------------------- #
# Ciclo while di inserimento dei valori delle coordinate dei punti della bounding box
# ---------------------------------------------------------------------------------------------- #
    while True:
        print(f"ATTENZIONE: valore massimo delle coordinate del pixel per le x è {colonne}\n\
ATTENZIONE: valore massimo delle coordinate del pixel per le y è {righe}\n\
ATTENZIONE: le coordinate del punto in alto a sinistra devono essere minori\n\
            di quelle in basso a destra")
# ---------------------------------------------------------------------------------------------- #
# Inserimento dei valori continuativo ed in blocco fintanto che non viene verificata la logica
# di inserimento della bounding box per la regione di interesse tramite la funzione di inserimento
# dei valori interi
# ---------------------------------------------------------------------------------------------- #
        x_alto_sinistra=inserimento_valori_numerici("Inserire la x del punto in alto a sinistra \
(ES:2000):\n")
        y_alto_sinistra=inserimento_valori_numerici("Inserire la y del punto in alto a sinistra \
(ES:600):\n")
        x_basso_destra=inserimento_valori_numerici("Inserire la x del punto in basso a destra \
(ES:2800):\n")
        y_basso_destra=inserimento_valori_numerici("Inserire la y del punto in basso a destra \
(ES:800):\n")
# ---------------------------------------------------------------------------------------------- #
# Condizione di controllo della logica della bounding box: se si verifica allora esce dal ciclo
# ---------------------------------------------------------------------------------------------- #
        if (x_alto_sinistra < x_basso_destra and\
            y_alto_sinistra < y_basso_destra and\
                x_basso_destra < colonne and\
                y_basso_destra < righe and\
                    x_alto_sinistra < colonne and\
                    y_alto_sinistra < righe):
            print("Non si sono commessi errori nell'inserimento")
            break
# ---------------------------------------------------------------------------------------------- #
# Altrimenti stampa un messaggio di errore ricordando la logica
# ---------------------------------------------------------------------------------------------- #
        else:
            print(f'Errore:\n\
                x_alto_sinistra deve essere < x_basso_destra\n\
                y_alto_sinistra deve essere < y_basso_destra\n\
                le x dei punti devono essere < di {colonne}\n\
                le y dei punti devono essere < di {righe}')
# ---------------------------------------------------------------------------------------------- #
# Slicing della matrice relativa all'immagine di partenza con i valori della regione di interesse
# ---------------------------------------------------------------------------------------------- #
    immagine_roi_manuale=immagine[y_alto_sinistra:y_basso_destra,\
    x_alto_sinistra:x_basso_destra]
    return immagine_roi_manuale
