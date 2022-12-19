"""Questo modulo implementa funzioni per l'applicazione di algoritmi di sogliatura e clustering"""

import cv2 as cv
from sklearn.cluster import DBSCAN
from Moduli import operazioni_utente
from Moduli.plot_immagini import grafico_sottografici

def sogliatura_adattativa(immagine_roi):
    """
    Inserire docstring dell'adaptive thresholding
    Parametri in ingresso: immagine_roi
    Paramtei in uscita: tuple che contiene le due immagini sogliate
    """
    print("Applicazione dell'algoritmo di sogliatura adattativa:\n\
    (1) occorre impostare il valore della costante C da sottrarre,\n\
        (2) il valore del blocco di pixel vicini a quello di analisi per la sogliatura,\n\
            (3) infine occorre scegliere l'eventuale metodo di sogliatura adattativa,\n\
                scegliendo tra quello Gaussiano, digitando\"0\" e tra quello con la media,\n\
                digitando \"1\"")
# ---------------------------------------------------------------------------------------------- #
# Inserimento dei parametri della sogliatura
# ---------------------------------------------------------------------------------------------- #
# Ciclo iterativo fino a che l'utente non inserisce valori appropriati
# Inserimento della costante C per l'algoritmo di sogliatura
# ---------------------------------------------------------------------------------------------- #
    costante_c=operazioni_utente.inserimento_valori_numerici("Inserire una costante numerica C>1 \
per l'algoritmo di sogliatura adattativa (ES.:6):\n")
# ---------------------------------------------------------------------------------------------- #
# Blocco di controllo dimensione blocco pixel per l'algoritmo di sogliatura
# ---------------------------------------------------------------------------------------------- #
    while True:
        try:
            dimensione_blocco_px=operazioni_utente.inserimento_valori_numerici("Inserire la\
dimensione del blocco di pixel\nper la sogliatura adattativa (NB: deve essere dispari e >1, per \
ES: 21):\n")
# ---------------------------------------------------------------------------------------------- #
# Per far si che la sogliatura avvenga, il blocco di pixel deve essere maggiore di 1
# e deve essere un numero dispari (divisione per 2 deve dare resto 1)
# ---------------------------------------------------------------------------------------------- #
            if dimensione_blocco_px >1 and dimensione_blocco_px % 2 ==1:
                break
            else:
                print("Il valore della dimensione del blocco di pixel deve essere dispari e \
maggiore di 1,\nossia il resto della divisione per 2 deve essere pari a 1!")
        except ValueError:
            print("Valore inappropriato")
# ---------------------------------------------------------------------------------------------- #
    #Applicazione di entrambi i metodi per la scelta da parte dell'utente su feedback visivo
# ---------------------------------------------------------------------------------------------- #
    immagine_soglia_gauss=cv.adaptiveThreshold(immagine_roi,255,\
        cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,dimensione_blocco_px,costante_c)
    immagine_soglia_media=cv.adaptiveThreshold(immagine_roi,255,cv.ADAPTIVE_THRESH_MEAN_C,\
        cv.THRESH_BINARY,dimensione_blocco_px,costante_c)
    titoli_metodi_sogliatura=["Metodo di sogliatura: Gauss","Metodo di sogliatura: media"]
# ---------------------------------------------------------------------------------------------- #
# Richiamo della funzione per il plot di sottografici
# ---------------------------------------------------------------------------------------------- #
    grafico_sottografici(immagine_soglia_gauss,immagine_soglia_media,titoli_metodi_sogliatura)
# ---------------------------------------------------------------------------------------------- #
# Inserimento del metodo di sogliatura e riassegnazione con stringa in funzione della scelta
# ---------------------------------------------------------------------------------------------- #
    metodo_sogliatura=operazioni_utente.inserimento_valori_numerici("Digitare \"0\" per\n\
il metodo gaussiano oppure \"1\" per\nil metodo con l'uso della media:\n")
    if metodo_sogliatura==0:
        metodo_sogliatura="Gaussiano"
    elif metodo_sogliatura==1:
        metodo_sogliatura="Media"
    print(f"Il metodo scelto per la sogliatura è {metodo_sogliatura}")
# ---------------------------------------------------------------------------------------------- #
# Ciclo iterativo continuo per assegnazione del metodo di sogliatura con creazione delle
# immagini sogliate sia con soglia diretta che inversa
# ---------------------------------------------------------------------------------------------- #
    while metodo_sogliatura!="inizializzato":
# ---------------------------------------------------------------------------------------------- #
# Blocco per la sogliatura con metodo della media
# ---------------------------------------------------------------------------------------------- #
        if metodo_sogliatura=="Media":
            immagine_soglia=cv.adaptiveThreshold(immagine_roi,255,cv.ADAPTIVE_THRESH_MEAN_C,\
                cv.THRESH_BINARY,dimensione_blocco_px,costante_c)
            immagine_soglia_inversa=cv.adaptiveThreshold(immagine_roi,255,\
                cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,dimensione_blocco_px,\
                costante_c)
# ---------------------------------------------------------------------------------------------- #
# Inizializzazione della variabile per l'uscita
# ---------------------------------------------------------------------------------------------- #
            metodo_sogliatura="inizializzato"
# ---------------------------------------------------------------------------------------------- #
#  Blocco per la sogliatura con metodo Gaussiano
# ---------------------------------------------------------------------------------------------- #
        elif metodo_sogliatura=="Gaussiano":
            immagine_soglia=cv.adaptiveThreshold(immagine_roi,255,\
                cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,dimensione_blocco_px,\
                costante_c)
            immagine_soglia_inversa=cv.adaptiveThreshold(immagine_roi,255,\
                cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,dimensione_blocco_px,\
                costante_c)
            metodo_sogliatura="inizializzato"
# ---------------------------------------------------------------------------------------------- #
# Quando la variabile si inizializza, allora esce
# ---------------------------------------------------------------------------------------------- #
        else:
            break
        return immagine_soglia, immagine_soglia_inversa

def riferimento_sogliatura(immagine_soglia, immagine_soglia_inversa):
    """
    Questa funzione implementa l'inserimento del valore di riferimento per la sogliatura ed
    assegna l'immagine sogliata in modo diretto od inverso in funzione del valore scelto
    dall'utente.
    Parametri in ingresso: immagine_soglia, immagine_soglia_inversa
    Parametri in uscita: immagine_soglia_db_scan, valore_di_riferimento
    """
# ---------------------------------------------------------------------------------------------- #
# Inizializzazione valore
# ---------------------------------------------------------------------------------------------- #
    valore_riferimento = None
# ---------------------------------------------------------------------------------------------- #
# Ciclo while di assegnazione valore di riferimento che itera fino all'inserimento corretto
# ---------------------------------------------------------------------------------------------- #
    while valore_riferimento!=0 and valore_riferimento!=255: # v_rif==0 or v_rif==255
# ---------------------------------------------------------------------------------------------- #
# Uso della funzione inserimento_valori_numerici per prendere in input il valore
# ---------------------------------------------------------------------------------------------- #
        valore_riferimento =operazioni_utente.inserimento_valori_numerici("Inserire il \
valore di riferimento di intensità di scala di grigio dei grilli\n\
(0, ossia grillo nero su sfondo bianco o\n\
255, ossia grillo bianco su sfondo nero): \n")
# ---------------------------------------------------------------------------------------------- #
# Assegnazione del valore: assegnazione variabile di uscita in funzione del valore inserito
# ---------------------------------------------------------------------------------------------- #
        if valore_riferimento == 255:
            immagine_soglia_dbscan = immagine_soglia_inversa
        elif valore_riferimento == 0:
            immagine_soglia_dbscan = immagine_soglia
        else:
            print(f"Errore\
            \n{valore_riferimento} != 255\
            \n{valore_riferimento} != 0")
    return immagine_soglia_dbscan, valore_riferimento

def clusterizzazione_db_scan(matrice_p):
    """
    L'algoritmo Density Based Scan Clustering o noto anche come DBSCAN clustering, permette di
    creare cluster di punti vicini tra loro, individuando eventuali punti di rumore, che vengono
    riconosciuti perché distanti dalle zone a densità maggiore ed esclusi dai cluster
    I parametri che vengono utilizzati dall'algoritmo sono:

    -EPS -> distanza entro la quale làalgoritmo ricerca punti vicini in base al numero minimo di
            campioni (punti)
    -MIN_SAMPLES -> numero minimo di punti tali per cui si formi un cluster all'interno di un
                    intorno EPS

    Parametri in ingresso: matrice_p delle coordinate dei px sogliati
    Parametri in uscita: etichette_clusterizzazione prodotte dal DBSCAN
    """
# ---------------------------------------------------------------------------------------------- #
# Inserimento dei parametri della clusterizzazione
# ---------------------------------------------------------------------------------------------- #
    eps_soglia=operazioni_utente.inserimento_valori_float("Inserire il valore di soglia dell'\
algoritmo DBSCAN (Es.:10):\n")
# ---------------------------------------------------------------------------------------------- #
# Ciclo while per l'inserimento da parte dell'utente del numero minimo di campioni per la
# clusterizzazione DBSCAN
# ---------------------------------------------------------------------------------------------- #
    while True:
        n_campioni_minimo=operazioni_utente.inserimento_valori_numerici("Inserire il numero minimo \
di campioni per l'algoritmo DBSCAN (Es.: 20):\n")
        if n_campioni_minimo>=1:
            break
        else:
            print("Non si può inserire un numero minore di 1!")
# ---------------------------------------------------------------------------------------------- #
# Applicazione dell'algoritmo DBSCAN e creazione delle etichette dei gruppi classificati
# ---------------------------------------------------------------------------------------------- #
    db_scan=DBSCAN(eps=eps_soglia,min_samples=n_campioni_minimo).fit(matrice_p)
    etichette_clusterizzazione=db_scan.labels_
# ---------------------------------------------------------------------------------------------- #
# Determinazione del numero di cluster nell'insieme etichette e del rumore:
# ---------------------------------------------------------------------------------------------- #
# Si sottrae alla numerosità dell'insieme etichette 1 se sono presenti valori pari a -1,
# altrimenti no per determinare il numero di cluster
# ---------------------------------------------------------------------------------------------- #
    numero_cluster=len(set(etichette_clusterizzazione)) - \
    (1 if -1 in etichette_clusterizzazione else 0)
# ---------------------------------------------------------------------------------------------- #
# Si conteggiano le occorrenze in etichette_clusterizzazione creando la lista ed
# applicando il metodo .count() inserendo l'argomento -1
# ---------------------------------------------------------------------------------------------- #
    numero_punti_rumore=list(etichette_clusterizzazione).count(-1)
# ---------------------------------------------------------------------------------------------- #
# Stampa del risultato dell'algoritmo
# ---------------------------------------------------------------------------------------------- #
    print(f"Numero stimato di cluster: {numero_cluster}")
    print(f"Numero stimato di punti di rumore: {numero_punti_rumore}")
    return etichette_clusterizzazione
