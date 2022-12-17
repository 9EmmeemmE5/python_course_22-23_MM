"""Modulo che implementa le funzioni per la determinazione della regione di interesse"""
#import unittest e rivedi pylint
import matplotlib.pyplot as plt
import cv2 as cv

from Moduli.operazioni_utente import inserimento_valori_numerici
from Moduli.lettura_input import lettura_immagine
from Moduli.plot_immagini import grafico_roi_auto

def creazione_roi_manuale(immagine):
    """
    Questa funzione implementa la creazione della regione di interesse con il metodo manuale
    Parametri in ingresso: immagine
    Parametri in uscita: immagine_roi
    """
    print("Ingresso nel metodo manuale della creazione della regione di interesse:\n\
ricordando la logica di inserimento Top-Left e Bottom-Right, inserire manualmente\n\
nell'ordine riportato le coordinate x ed y dei due punti della regione di interesse...\n")
    (righe,colonne)=immagine.shape
    while True:
        print(f"ATTENZIONE: valore massimo delle coordinate del pixel per le x è {colonne}\n\
ATTENZIONE: valore massimo delle coordinate del pixel per le y è {righe}")
        x_alto_sinistra=inserimento_valori_numerici("Inserire la x del punto in alto a sinistra\
(ES:2000):\n")
        y_alto_sinistra=inserimento_valori_numerici("Inserire la y del punto in alto a sinistra\
(ES:600):\n")
        x_basso_destra=inserimento_valori_numerici("Inserire la x del punto in basso a destra\
(ES:2800):\n")
        y_basso_destra=inserimento_valori_numerici("Inserire la y del punto in basso a destra\
(ES:800):\n")
        coerenza_coordinata_x=x_alto_sinistra < x_basso_destra #type:ignore
        coerenza_coordinata_y=y_alto_sinistra < y_basso_destra #type:ignore
        coerenza_limite_colonne=x_basso_destra < colonne
        coerenza_limite_righe=y_basso_destra < righe
        condizioni=(coerenza_coordinata_x,coerenza_coordinata_y,\
            coerenza_limite_colonne,coerenza_limite_righe)
        errore_coord_x="Errore: x_alto_sinistra deve essere < x_basso_destra"
        errore_coord_y="Errore: y_alto sinistra deve essere < y_basso destra"
        errore_lim_righe=f"Errore: i punti x devono avere valore < di {colonne}"
        errore_lim_colonne=f"Errore: i punti y devono avere valore < di {righe}"
        condizioni_errate=(errore_coord_x,errore_coord_y,errore_lim_righe,errore_lim_colonne)
        for element in condizioni:
            for item in condizioni_errate:
                if element is False:
                    print(item)
                elif element is True:
                    print("Non si sono commessi errori nell'inserimento")
                    break
        immagine_roi_manuale=immagine[y_alto_sinistra:y_basso_destra,\
        x_alto_sinistra:x_basso_destra]
        return immagine_roi_manuale
