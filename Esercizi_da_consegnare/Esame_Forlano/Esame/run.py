##
'''
Questo codice per ogni immagine con nome all'intenro del file image.txt premette
di identificare una regione di interesse (RoI), applicare una soglia adattiva sulle 
immagini con i grilli, realizzare la matrice delle coordinate dei pixel dei grilli
e infine applicare un algoritmo che clusterizza i campioni vicini tra loro e 
individuare eventuali punti di rumore.
'''
# URL Adaptive Thresholding: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
# URL DBSCAN: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN

# Importo le librerie
import sys
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

from Moduli import read, crop_image
from Moduli.plt import plt_img, plt_img_block

def main():
    # Definisco il path del file di testo e leggo i nomi delle immagini con la funzione read_txt
    PATH_FILE = ".\\Esercizi_da_consegnare\\Esame_Forlano\\Esame\\image.txt"
    name_splitted = read.read_txt(PATH_FILE)

    # Definisco il path delle immagini
    PATH_IMG = ".\\Esercizi_da_consegnare\\Esame_Forlano\\Esame\\Immagini\\"
    # Ripeto il codice per tutte le immagini in name_splitted
    for item in name_splitted:
        print(f'Codice eseguito per: {item}')
        try:
            img = read.read_img(PATH_IMG, item)
        except ValueError as err: # Catturo l'eccezione sollevata nella funzione read_img
            print(f'Eccezione di tipo value error per {item}\n{err}')
            sys.exit(1) # Printo l'errore e esco

        # Plot immagine utilizzando la funzione plt_img
        # Parametri (Array, Titolo)
        plt_img(img, "Immagine Originale")

        # Estrazione ROI (Region Of Interest) con la funzione roi
        print("Con il cursore sull'immaigne scegliere i valori da inserire...")
        roi_img = crop_image.roi(img)

        # Plot ROI utilizzando la funzione plt_img_block
        # Parametri (Array, Titolo)
        plt_img_block(roi_img, "Region of Interest inserita")

        # Eseguo l'adaptive thresholding sulla roi
        BLOCK_SIZE = 21 # Dimensione di pixel vicini utilizzati per calcolare la soglia
        C = 6 # Costante sottratta dalla media
        '''
        L'algoritmo determina la soglia per un pixel in base a una regione attorno ad esso (BLOCK_SIZE).
        Otteniamo soglie diverse per diverse regioni della stessa immagine,
        Otteniamo risultati migliori per immagini con illuminazione variabile.
        '''
        # Realizzo due threshold con funzioni che trasformano l'immagine in scala di grigi
        # in un immagine binaria e binaria inversa
        th_adp = cv.adaptiveThreshold(roi_img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
                    cv.THRESH_BINARY, BLOCK_SIZE, C)
        th_adp_inv = cv.adaptiveThreshold(roi_img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
                    cv.THRESH_BINARY_INV, BLOCK_SIZE, C)

        # Erosione e dilatazione
        '''
        # Codice di prova non implementato
        kernel_1 = np.ones((3,3))
        kernel_2 = np.copy(kernel_1)
        kernel_2 [1,1] = 2
        th_filter = cv.dilate(th_adp, kernel_1)
        th_filter = cv.erode(th_adp, kernel_2)
        '''

        # Plot ROI con 2 valori
        titles = ["Valore grilli v=0", "Valore grilli v=255"]
        images = [th_adp, th_adp_inv]

        # Ciclo utilizzato per plottare le due immagini vicine
        for i in range(2):
            plt.subplot(1,2,i+1),
            plt.imshow(images[i],'gray') # Color map gray
            plt.title(titles[i]) # Titoli delle immagini
            plt.xticks([]),plt.yticks([])
            plt.colorbar(ticks=[0, 255], orientation='horizontal') # Barre dei colori
        plt.show()

        # Faccio scegliere all'utente il valore dei grilli 0 o 255
        v = -1 # Inizializzo il valore
        while (v != 255 and v != 0):
            # Utilizzo la funzione red_int per prendere in input il valore
            v = read.read_int("Inserisci valori grilli (0 o 255): ")
            # Con l'if assegno il valore 
            if v == 255:
                th = th_adp_inv
            elif v == 0:
                th = th_adp
            else:
                print(f'Errore\
                \n{v} != 255\
                \n{v} != 0')

        # Faccio la matrice P con le coordinate dei pixel che hanno valori pari a v
        coordinate = []  # Lista delle coordinate

        rows, cols = th.shape  # Calcoliamo righe e colonne dell'array th

        # Itero su righe e colonne con due for per prendere le coordinate dei pixel uguali a v
        for x in range(rows):
            for y in range(cols): 
                if th[x, y] == v: # Se il pixel x,y è uguale al valore di v lo metto nella lista
                    coordinate.append((y, x))

        P = np.array(coordinate) # Faccio la matrice

        # Faccio il print della matrice delle coordinate
        print(f'MATRICE DELLE COORDINATE \n{P}')
        plt_img_block(th,f'Immagine v = {v}')
        # Algoritmo DBSCAN
        '''
        Density-Based Spatial Clustering of Applications with Noise è un algoritmo di clustering
        Il DBSCAN clusterizza campioni vicini tra loro e individua eventuali punti di rumore,
        I punti molto distanti dalle zone a maggiore densità vengono esclusi dai cluster e riconosciuti come rumore.
        
        EPS -> distanza all'interno della quale ricercare i punti vicini
        MIN_SAMPLES -> numero minimo di punti affinché si formi un cluster
        '''
        
        # Leggo i valori di EPS e MIN_SAMPLES con la funzione read_int
        print("Applico l'algoritmo DBSCAN...")
        EPS = read.read_int("Inserisci EPS (Es.10):")
        MIN_SAMPLES = read.read_int("Inserisci MIN_SAMPLES (Es.20):")

        db = DBSCAN(EPS, min_samples = MIN_SAMPLES).fit(P)
        labels = db.labels_ # Indici o identificatori presi dal cluster

        # Numero di cluster nelle etichette, ignorando il rumore se presente.
        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
        n_noise = list(labels).count(-1)
        # Stampo i cluster stimati e eventuali punti di disturbo
        print(f'Numero di cluster stimati: {n_clusters}')
        print(f'Numero stimato di punti di disturbo: {n_noise}')

        # Matrice F con dimenisone uguale alla roi_img inizilizzata con valore -1
        F = np.full((rows, cols), -1)

        # Associo alla nuova immagine F l’identificatore del cluster DBSCAN
        i = 0 # Contatore
        for item in P:
            y = item[0]
            x = item[1]
            F[x,y] = labels[i]
            i += 1
        print(f'Matrice F con gli indici del cluter\n {F}')
        # Plot di F
        plt_img_block(F, "Matrice F")
        
main()