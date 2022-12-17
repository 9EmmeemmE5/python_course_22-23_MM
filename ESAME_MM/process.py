"""Esame di Fondamenti di informatica (Meccanica) Dic 2022 - Marco Mosca mat. 1102851"""

"""
Questo script python, sulla base del nome dell'immagine contenuto nel file di testo
lista_file_immagini, presente nella radice della cartella di lavoro, consente all'utente
di identificare una regione di interesse (RoI), applicare una soglia di tipo adattativo
per identificare i grilli della regione di interesse e ricavarne le coordinate a mezzo
della matrice P delle coordinate.
Infine lo script applica un algoritmo di suddivisione in cluster per raggruppare campioni
vicini tra di loro ed eventuali punti di rumore nelle immagini.
"""
# Documentazione web:
# Adaptive Thresholding: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
# DBSCAN: https://bit.ly/demo_DBSCAN_esame

# Importazione librerie
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# Richiamo moduli
from Moduli.lettura_input import lettura_input_testo, lettura_immagine
from Moduli.plot_immagini import grafico_immagine, grafico_roi, grafico_sottografici
from Moduli import operazioni_utente, regioni_di_interesse, sogliatura_clustering

def main():
    """Punto di ingresso"""
    # Definizione del percorso del file contenente la lista di immagini
    PERCORSO_LISTA_FILE=".\\ESAME_MM\\lista_file_immagini.txt"

    # Creazione lista con nomi dei file
    lista_nomi_file=lettura_input_testo(PERCORSO_LISTA_FILE)
    print(lista_nomi_file)
    
    # Definizione del percorso contenente i file immagine
    PERCORSO_IMMAGINI=".\\ESAME_MM\\Immagini\\"
    for element in lista_nomi_file:
        print(f"Esecuzione algoritmo per l'immagine {element}")
        nome_file_immagine=element
        try:    # Tento l'apertura dell'immagine con la funzione lettura_immagine
            immagine=lettura_immagine(PERCORSO_IMMAGINI, nome_file_immagine)
        except IOError as io_ex:  # Richiamo l'eccezione sollevata nella funzione
            print(f"Eccezione di tipo {io_ex} per {nome_file_immagine}")
        
        # Grafico immagine aperta
        print(f"Apertura immagine in corso...\nMuovendo il mouse all'interno dell'immagine,\n\
individuare il punto in alto a sinistra e quello in basso a destra di una regione \n\
rettangolare che rappresenta la regione di interesse in cui verrà eseguita la sogliatura\n\
e la clusterizzazione")
        
        grafico_immagine(immagine, nome_file_immagine) 
        
        # Creazione della ROI mediante scelta tipologia input da parte dell'utente: scelta metodo
        # Ciclo while di scelta del metodo di applicazione della regione di interesse
        immagine_roi=regioni_di_interesse.creazione_roi_manuale(immagine)
        print(f"Apertura immagine della regione di interesse selezionata in corso...")
        grafico_roi(immagine_roi, nome_file_immagine)
        
        # Applicazione dell'algoritmo di sogliatura adattiva #*modulo completato
        immagini_sogliate=sogliatura_clustering.sogliatura_adattativa(immagine_roi)
        immagine_soglia=immagini_sogliate[0]
        immagine_soglia_inv=immagini_sogliate[1]
        
        # Grafico delle immagini sogliate con il quale l'utente sceglie il riferimento
        titoli=["Grilli visualizzati con il valore di \n riferimento di sogliatura v=0","Grilli \
visualizzati con il valore di \nriferimento di sogliatura v=255"]
        grafico_sottografici(immagine_soglia, immagine_soglia_inv, titoli)
        
        # Scelta dell'utente il valore di riferimento intensità di scala di grigio
        # con restituzione all'indice 0 della tuple l'immagine sogliata per il DBSCAN
        # e all'indice 1 il valore di riferimento
        (immagine_v_rif_dbscan,valore_riferimento)=\
        sogliatura_clustering.riferimento_sogliatura(immagine_soglia,immagine_soglia_inv)
        coordinate_px_sogliati=[]
        (righe_immagine_v_rif,colonne_immagine_v_rif)=immagine_v_rif_dbscan.shape
        print(immagine_v_rif_dbscan.shape, immagine_v_rif_dbscan.dtype)
        
        # Iterazione righe/colonne matrice per pescare px con intensità pari al valore di rif.:
        for x_coord_px_v_rif in range(righe_immagine_v_rif):
            for y_coord_px_v_rif in range(colonne_immagine_v_rif):
                if immagine_v_rif_dbscan[x_coord_px_v_rif,y_coord_px_v_rif]==valore_riferimento:
                    coordinate_px_sogliati.append((x_coord_px_v_rif,y_coord_px_v_rif))
                    #todo: spiega perche appendi una lista di tuple
        
        # Assegnazione della lista alla matrice P
        P=np.array(coordinate_px_sogliati) 
        
        # Stampa della matrice P
        print(f"Matrice delle coordinate dei pixel con intensità uguale a \
{valore_riferimento},\n{P}, \navente dimensioni {P.shape}, con elementi di tipo {P.dtype}")
        grafico_immagine(immagine_v_rif_dbscan,nome_file_immagine=f"Immagine a cui applicare\n l'\
algoritmo di clusterizzazione DBSCAN:\n valore di riferimento scelto {valore_riferimento}")
        
        # Applicazione dell'algoritmo DBSCAN
        etichette_clusters=sogliatura_clustering.clusterizzazione_db_scan(P)
        
        # Grafico risultato dell'algoritmo DBSCAN0        
        # Inizializzazione valori della matrice con valori -1
        F=np.full(immagine_v_rif_dbscan.shape, -1)
        print(f"Matrice F inizializzata:\n{F},\ndi dimensioni {F.shape},\n\
con dati di tipo {F.dtype}")
        
        # Associazione ...
        l_contatore_indice_etichetta=0
        for i in range(P.shape[0]):
            # for j in range(len(etichette_clusters)):
            x_clusterizzato_mat_f=P[i][0]
            y_clusterizzato_mat_f=P[i][1]
            punto_clusterizzato=(x_clusterizzato_mat_f,y_clusterizzato_mat_f)
            # F[punto_clusterizzato[0],punto_clusterizzato[1]]=etichette_clusters[j]
            F[punto_clusterizzato[0],punto_clusterizzato[1]]=etichette_clusters[l_contatore_indice_etichetta]
            l_contatore_indice_etichetta+=1
        N=operazioni_utente.inserimento_valori_numerici("Inserire il valore soglia di dimensione \
per l'esclusione di cluster aventi dimensione superiore")
        
        # Plot di F senza l'esclusione N
        grafico_immagine(F, nome_file_immagine=f"Matrice F dell'immagine clusterizzata,  \
senza esclusione dei cluster di dimensioni maggiori del valore {N}")
main()
