"""Questo modulo implementa funzioni per operare sulle matrici P ed F"""

import numpy as np
from Moduli.operazioni_utente import inserimento_valori_numerici

def matrice_p_coord_px_sogliati(immagine_v_rif_dbscan,valore_riferimento):
    """
    Questa funzione crea, partendo dall'immagine della regione di interesse, la matrice delle
    coordinate dei pixel sogliati tramite sogliatura adattativa con il metodo scelto dall'utente
    Parametri in ingresso: immagine_v_rif_dbscan, valore_riferimento
    Parametri in uscita: matrice_p
    """
# ---------------------------------------------------------------------------------------------- #
# Creazione della tuple di associazione delle dimensioni della matrice
# ---------------------------------------------------------------------------------------------- #
    (righe_immagine_v_rif,colonne_immagine_v_rif)=immagine_v_rif_dbscan.shape
# ---------------------------------------------------------------------------------------------- #
# Creazione della lista vuota che contiene i pixel sogliati
# ---------------------------------------------------------------------------------------------- #
    coordinate_px_sogliati=[]
# ---------------------------------------------------------------------------------------------- #
# Iterazione righe/colonne matrice per pescare px con intensità pari al valore di rif.:
# ---------------------------------------------------------------------------------------------- #
    for x_coord_px_v_rif in range(righe_immagine_v_rif):        # per ogni pixel delle righe
        for y_coord_px_v_rif in range(colonne_immagine_v_rif):  # per ogni pixel delle colonne
# ---------------------------------------------------------------------------------------------- #
# se il pixel presenta valore pari a quello di riferimento, allora esegue l'append
# ---------------------------------------------------------------------------------------------- #
            if immagine_v_rif_dbscan[x_coord_px_v_rif,y_coord_px_v_rif]==valore_riferimento:
# ---------------------------------------------------------------------------------------------- #
# append delle coordinate sotto forma di tuple
# ---------------------------------------------------------------------------------------------- #
                coordinate_px_sogliati.append((x_coord_px_v_rif,y_coord_px_v_rif))
# ---------------------------------------------------------------------------------------------- #
# Assegnazione della lista di tuple delle coordinate alla matrice P
# ---------------------------------------------------------------------------------------------- #
    matrice_p=np.array(coordinate_px_sogliati)
# ---------------------------------------------------------------------------------------------- #
# Stampa della matrice P, delle dimensioni e del tipo di dato
# ---------------------------------------------------------------------------------------------- #
    print(f"Matrice delle coordinate dei pixel con intensità uguale a \
{valore_riferimento},\n{matrice_p}, \navente dimensioni {matrice_p.shape}, \
con elementi di tipo {matrice_p.dtype}")
    return matrice_p

def matrice_f_immagine_clusterizzata(immagine_v_rif_dbscan, matrice_p, etichette_clusters):
    """
    Questa funzione crea una matrice F contenente l'immagine della regione di interesse contenente
    i pixel sogliati e clusterizzati a seguito dell'applicazione dell'algoritmo di clustering
    DBSCAN associando l'etichetta del cluster ai pixel di coordinate (x,y) sogliati, sulla base
    del dato ricavato dalla creazione della matrice P
    """
# ---------------------------------------------------------------------------------------------- #
# Creazione della matrice F a partire dalle dimensioni dell'immagine output della sogliatura
# ---------------------------------------------------------------------------------------------- #
    matrice_f=np.full(immagine_v_rif_dbscan.shape, -1)
# ---------------------------------------------------------------------------------------------- #
# Stampa della matrice F, delle dimensioni e del tipo di dato
# ---------------------------------------------------------------------------------------------- #
    print(f"Matrice F inizializzata:\n{matrice_f},\ndi dimensioni {matrice_f.shape},\n\
con dati di tipo {matrice_f.dtype}")
# ---------------------------------------------------------------------------------------------- #
# Associazione delle etichette dei cluster alla matrice f sulla base dell'informazione di
# posizione contenuta nella matrice P delle coordinate dei pixel sogliati:
# Inizializzazione contatore per l'etichetta del cluster
# ---------------------------------------------------------------------------------------------- #
    l_contatore_indice_etichetta=0
# ---------------------------------------------------------------------------------------------- #
# Ciclo for per scorrere tutti gli elementi della matrice p: il contatore arriva correttamente
# alla fine senza andare fuori intervallo perché la len(etichette)=range(matrice_i.shape[0])
# ---------------------------------------------------------------------------------------------- #
    for i in range(matrice_p.shape[0]):
# ---------------------------------------------------------------------------------------------- #
# Associazione per la x del pixel nella matrice F con la coordinata x del pixel sogliato
# ---------------------------------------------------------------------------------------------- #
        x_clusterizzato_mat_f=matrice_p[i][0]
# ---------------------------------------------------------------------------------------------- #
# Associazione per la y del pixel nella matrice F con la coordinata y del pixel sogliato
# ---------------------------------------------------------------------------------------------- #
        y_clusterizzato_mat_f=matrice_p[i][1]
# ---------------------------------------------------------------------------------------------- #
# Creazione della tuple contenente le informazioni di posizione x ed y del pixel clusterizzato
# ---------------------------------------------------------------------------------------------- #
        punto_clusterizzato=(x_clusterizzato_mat_f,y_clusterizzato_mat_f)
# ---------------------------------------------------------------------------------------------- #
# Il pixel della matrice F è uguale all'etichetta del cluster 0, poi 1, 2,... fino a n°cluster
# ---------------------------------------------------------------------------------------------- #
        matrice_f[punto_clusterizzato[0],punto_clusterizzato[1]]=\
        etichette_clusters[l_contatore_indice_etichetta]
# ---------------------------------------------------------------------------------------------- #
# Incremento di 1 il contatore etichetta per il cluster successivo
# ---------------------------------------------------------------------------------------------- #
        l_contatore_indice_etichetta+=1
    return matrice_f

def matrice_f_immagine_clusterizzata_raffinata(matrice_f, etichette_clusters):
    """
    Questa funzione permette di raffinare la matrice associata all'immagine della regione di
    interesse sogliata e clusterizzata F andando ad escludere i cluster di dimensione maggiore
    ad un parametro N inserito dall'utente
    Parametri in ingresso: matrice_f, etichette_clusters
    Parametri in uscita: matrice_f (raffinata togliendo i cluster più grandi di N)
    """
# ---------------------------------------------------------------------------------------------- #
# Inserimento da parte dell'utente del valore di soglia per l'esclusione dei cluster di dimensione
# maggiore
# ---------------------------------------------------------------------------------------------- #
    n_soglia_dimensione=inserimento_valori_numerici("Inserire il valore N di soglia di dimensione\
\nper l'esclusione di cluster aventi dimensione superiore (ES.:N>100):\n")
# ---------------------------------------------------------------------------------------------- #
# Applicazione del comando numpy: np.unique, che ritorna, inserendo il parametro return_counts
# uguale a True una tuple di 2 array, con il primo contenente le istanze dell'array etichette
# in maniera univoca, senza ripetizioni, come un cast a set, mentre il secondo array ritorna
# il conteggio delle istanze di ogni singola istanza di etichetta cluster
# ---------------------------------------------------------------------------------------------- #
    (id_clusters, conteggio_singolo_cluster)=np.unique(etichette_clusters, return_counts=True)
    matrice_dimensione_clusters=np.array((id_clusters,conteggio_singolo_cluster))
# ---------------------------------------------------------------------------------------------- #
# Esecuzione del cast a lista dei 2 array:
# ---------------------------------------------------------------------------------------------- #
    id_clusters=list(matrice_dimensione_clusters[0])
    conteggio_singolo_cluster=list(matrice_dimensione_clusters[1])
# ---------------------------------------------------------------------------------------------- #
# Creazione della lista contenente i cluster da eliminare
# ---------------------------------------------------------------------------------------------- #
    cluster_da_eliminare=[]
# ---------------------------------------------------------------------------------------------- #
# Ciclo for che scorre tra il conteggio delle istanze di ogni cluster ed elimina quelle maggiori
# di N inserito dall'utente
# ---------------------------------------------------------------------------------------------- #
    for i in range(len(id_clusters)):
        if n_soglia_dimensione<=conteggio_singolo_cluster[i]:
            cluster_da_eliminare.append(id_clusters[i])
# ---------------------------------------------------------------------------------------------- #
# Applicazione del comando numpy: np.delete, che cancella da un array (1° parametro), gli elementi
# di una maschera, in questo caso la lista precedentemente creata che contiene l'id del cluster da
# eliminare (2° parametro), eliminando tutti gli elementi in una direzione (3° parametro)
# ---------------------------------------------------------------------------------------------- #
    matrice_dim_cluster_new=np.delete(matrice_dimensione_clusters, cluster_da_eliminare, axis=1)
# ---------------------------------------------------------------------------------------------- #
# Rimuove la colonna dell'id cluster con l'area maggiore di N
# ---------------------------------------------------------------------------------------------- #
    print(f"{cluster_da_eliminare}\n\
sono i cluster che sono stati eliminati a fronte dell'inserimento di {n_soglia_dimensione}.\n\
Sono rimasti i cluster\n\
{matrice_dim_cluster_new[0]},\n\
aventi dimensione, in pixel,\n\
{matrice_dim_cluster_new[1]}.")
# ---------------------------------------------------------------------------------------------- #
# Iterazione righe colonne con controllo del valore del cluster:
# Inizializzazione la tuple delle dimensioni della matrice F
# ---------------------------------------------------------------------------------------------- #
    (righe_f,colonne_f)=matrice_f.shape
# ---------------------------------------------------------------------------------------------- #
    # Esecuzione del cast a lista degli identificativi dei cluster raffinati a fronte dell'input
    # utente con il numero N
# ---------------------------------------------------------------------------------------------- #
    id_clusters_raffinati=list(matrice_dim_cluster_new[0])
# ---------------------------------------------------------------------------------------------- #
# Per ogni riga dell'immagine F, per ogni colonna, se il pixel a quel determinato indice di
# riga e colonna ha un valore (ossia un id cluster) che non è presente nella lista degli id
# raffinati, allora quel pixel avrà un valore azzerato di -1
# ---------------------------------------------------------------------------------------------- #
    for i in range(righe_f):
        for j in range(colonne_f):
            if matrice_f[i][j] not in (id_clusters_raffinati):
                matrice_f[i][j]=-1
    return matrice_f
