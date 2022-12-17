"""Questo modulo implementa funzioni per l'applicazione di algoritmi di sogliatura e clustering"""

import cv2 as cv
from sklearn.cluster import DBSCAN
from Moduli.operazioni_utente import inserimento_valori_numerici

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
    # Inserimento dei parametri della sogliatura
    # Ciclo iterativo fino a che l'utente non inserisce valori appropriati
    # Blocco di controllo costante C
    costante_c=inserimento_valori_numerici("Inserire una costante numerica >1 C per l'algoritmo\
di sogliatura adattativa: ")
    # Blocco di controllo dimensione blocco pixel per la sogliatura
    while True:
        try:
            dimensione_blocco_px=inserimento_valori_numerici("Inserire la dimensione del blocco \
di pixel per la sogliatura adattativa (NB: deve essere dispari e >1): ")
            if dimensione_blocco_px >1 and dimensione_blocco_px % 2 ==1:
                break
            print("Il valore della dimensione del blocco di pixel deve essere dispari e \
maggiore di 1, ossia il resto della divisione per 2 deve essere pari a 1")
        except ValueError:
            print("Valore inappropriato")
    # Inserimento del metodo di sogliatura
    metodo_sogliatura=inserimento_valori_numerici("Digitare \"0\" per il metodo gaussiano o \n\
\"1\" per il metodo con l'uso della media: ")
    if metodo_sogliatura==0:
        metodo_sogliatura="Gaussiano"
    elif metodo_sogliatura==1:
        metodo_sogliatura="Media"
    print(f"Il metodo scelto per la sogliatura è {metodo_sogliatura}")
    # Ciclo iterativo continuo fino a che l'utente non inserisce uno dei due comandi di sogliatura
    while metodo_sogliatura!="inizializzato":
        #!gestire la typeerror se si inserisce un tipo diverso, value error volendo anche
        if metodo_sogliatura=="Media":
            immagine_soglia=cv.adaptiveThreshold(immagine_roi,255,cv.ADAPTIVE_THRESH_MEAN_C,\
                cv.THRESH_BINARY,dimensione_blocco_px,costante_c)
            immagine_soglia_inversa=cv.adaptiveThreshold(immagine_roi,255,\
                cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,dimensione_blocco_px,\
                costante_c)
            metodo_sogliatura="inizializzato"
        elif metodo_sogliatura=="Gaussiano":
            immagine_soglia=cv.adaptiveThreshold(immagine_roi,255,\
                cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,dimensione_blocco_px,\
                costante_c)
            immagine_soglia_inversa=cv.adaptiveThreshold(immagine_roi,255,\
                cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,dimensione_blocco_px,\
                costante_c)
            metodo_sogliatura="inizializzato"
        else:
            break
        # Risultato:
        return immagine_soglia, immagine_soglia_inversa

def riferimento_sogliatura(immagine_soglia, immagine_soglia_inversa):
    """
    Questa funzione implementa l'inserimento del valore di riferimento per la sogliatura ed
    assegna l'immagine sogliata in modo diretto od inverso in funzione del valore scelto
    dall'utente.
    Parametri in ingresso: immagine_soglia, immagine_soglia_inversa
    Parametri in uscita: immagine_soglia_db_scan, valore_di_riferimento
    """
    valore_riferimento = None # Inizializzazione valore
    while valore_riferimento!=0 and valore_riferimento!=255: # al posto di diverso da 0 e 255
        # Uso della funzione inserimento_valori_numerici per prendere in input il valore
        valore_riferimento = inserimento_valori_numerici("Inserire il \
valore di riferimento di intensità di scala di grigio dei grilli\n\
(0, ossia grillo nero su sfondo bianco o\n\
255, ossia grillo bianco su sfondo nero): \n")
        # Assegnazione il valore
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
    Inserire documentaizone del DBSCAN clustering
    Parametri in ingresso:
    Parametri in uscita:
    """
    # Inserimento dei parametri della clusterizzazione
    eps_soglia=inserimento_valori_numerici("Inserire il valore di soglia dell'algoritmo \
DBSCAN (Es.:10)")
    n_campioni_minimo=inserimento_valori_numerici("Inserire il numero minimo di campioni \
per l'algoritmo DBSCAN (Es.: 20)")
    # Applicazione dell'algoritmo DBSCAN e creazione delle etichette dei gruppi classificati
    db_scan=DBSCAN(eps=eps_soglia,min_samples=n_campioni_minimo).fit(matrice_p)
    etichette_clusterizzazione=db_scan.labels_
    # Determinazione del numero di cluster nell'insieme etichette e del rumore:
    # Si sottrae alla numerosità dell'insieme etichette 1 se sono presenti valori pari a -1,
    # altrimenti no per determinare il numero di cluster
    numero_cluster=len(set(etichette_clusterizzazione)) - \
    (1 if -1 in etichette_clusterizzazione else 0)
    # Si conteggiano le occorrenze in etichette_clusterizzazione creando la lista ed
    # applicando il metodo .count() inserendo l'argomento -1
    numero_punti_rumore=list(etichette_clusterizzazione).count(-1)
    # Stampa del risultato dell'algoritmo
    print(f"Numero stimato di cluster: {numero_cluster}")
    print(f"Numero stimato di punti di rumore: {numero_punti_rumore}")
    return etichette_clusterizzazione
