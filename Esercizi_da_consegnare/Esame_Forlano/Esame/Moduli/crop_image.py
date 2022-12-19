'''
Questo modulo permette di definire una regione di interesse (ROI) all'interno di un'immagine,
andando a definire le coordinate del punto Top-Left e le coordinate del punto Bottom-Right.
'''
# Importo le librerie
import cv2 as cv
from Moduli.read import read_int

def roi(img):
    '''
    Questa funzione definisce una regione di interesse nell'immagine.
    @param img: array di due dimensioni
    @return roi_img: ritorna un array di due dimensioni più piccolo di img
    '''
    print("Inserisci le coordinate del punto Top Left e del punto Bottom Right per la creazione del bounding box.")

    r,c = img.shape # Ritorna il numero delle righe e delle colonne dell'array di partenza
    '''
    Eseguo il ciclo while fino a quando la condizione non è soddisfatta
    Utilizzo la funzione read_int per prendere in input il valore dei punti
    '''
    str_max_stp = True # Condizione start maggiore di stop
    while str_max_stp: # Fino a quando condizione è vera
        start_x_pt = read_int("inserisci start_x (Es.2000):")
        start_y_pt = read_int("inserisci start_y (Es.800):")
        stop_x_pt = read_int("inserisci stop_x (Es.2400):")
        stop_y_pt = read_int("inserisci stop_y (Es.1000):")
    
        # Verifico che start_x < stop_x e start_y < stop_y e che che i punti siano più piccoli dell'array originale
        if (start_x_pt < stop_x_pt and start_y_pt < stop_y_pt and stop_x_pt < c and stop_y_pt < r):
            str_max_stp = False # Condizione
        else:
            # Faccio il print dell'errore in caso di valori errarti
            print(f'Errore\
                \n start_x deve essere < stop_x\
                \n start_y deve essere < stop_y\
                \n i punti x devono essere < di {c}\
                \n i punti y devono essere < di {r}')

    # Effettuo un operazione di slice
    roi_img = img[start_y_pt:stop_y_pt ,start_x_pt:stop_x_pt] # Prima la y (righe) poi le x (colonne)

    return roi_img


# if (x_alto_sinistra< x_basso_destra and\
#             y_alto_sinistra < y_basso_destra and\
#                 x_basso_destra < colonne and\
#                 y_basso_destra < righe and\
#                     x_alto_sinistra < colonne and\
#                     y_alto_sinistra < righe):
#                 print("Non si sono commessi errori nell'inserimento")
#                 break
#         else:
#             print(f'Errore\
#                 \n x_alto_sinistra deve essere < x_basso_destra\
#                 \n y_alto_sinistra deve essere < y_basso_destra\
#                 \n le x dei punti devono essere < di {colonne}\
#                 \n le y dei punti devono essere < di {righe}')
