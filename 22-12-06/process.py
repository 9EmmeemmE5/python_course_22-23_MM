"""Processing opencv2 python script"""
# Si prende un'immagine, se ne ricava una ROI, si creerà un'istogramma per vedere l'intensità di pixel ed andare poi ad eseguire un thresholding binario ed eseguire un algoritmo di clusterizzazione
import cv2 as cv
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt #ricorda sempre il pyplot

def main():
    """Entry point for out application"""
    PATH_IMG="22-12-06\\img\\"
    FILE_NAME="DJI_0035.jpg"
    img_defect_0 = cv.imread(f"{PATH_IMG}{FILE_NAME}")
    print(img_defect_0.shape, img_defect_0.dtype)
    channel_of_interest = img_defect_0[:,:,0] # estrae con gli operatori di broadcast ":" tutte le righe (primo :), tutte le colonne (secondo :) del canale numero 1 con indice 0
    roi_img = channel_of_interest[80:192, 50:205] #creo una roi manuale andando a leggere i valori dei pixel con il plot # attenzione al sistema di riferimento per non far confusione con i valori x ed y dei punti presi sotto
    #point 1 - x=50, y=80
    #point 2 - x=205, y=192
    plt.imshow(channel_of_interest, cmap="gray") #con il cmap la visualizzo correttamente e non palettizzata con un false colouring
    plt.show()
    
    #Creare istogramma
    bins_value = np.zeros((256), dtype=np.uint32) #np.uint8 non va bene perche memorizza valori da 0 a 255 e non va bene perche se sforo la soglia di 255 sto commettendo un errore di troncamento, quindi il dominio va esteso al minimo ad un valore pari al prodotto tra numero di righe e di colonne, considerando il caso monopicco di immagini o tutte nere o tutte bianche
    (rows,cols) = roi_img.shape
    for i in range(rows):
        for j in range(cols):
            value = roi_img[i,j]
            bins_value[value]+=1
    sum_value=np.sum(bins_value)
    print(f"pixel totali: {rows*cols}\n\n somma hist: {sum_value}") #check per la correttezza delle frequenze dell'istogramma
    plt.stairs(bins_value) #mostrato in classe
    plt.show()
    
    #! Dalla doc di opencv con il metodo opencv+matplotlib
    plt.hist(roi_img.ravel(),256,(0,256))
    plt.xlim([0,256])
    plt.show()
    
    #clustering con l'algoritmo k-means
    """
    Dato che non ci interessa l'ordine dei pixel, occorer tradurre una matrice in un vettore e poi anche l'opposto.
    Questo perche l'algoritmo si applica ad una serie di misurazioni e non ad una singola: occorre tradurre la matrice di immagine in un vettore di temperature, per poi andare a clusterizzare i valori di temperatura, per poi andare a ritrasformare il vettore clusterizzato in immagine.
    L'algoreitmo richiede come parametro importante il numero di cluster e poi si esegue il fit; nel nostro caso si hanno n misurazioni monodimensionali.
    Il fatto di aver fatto un fit a monte permette di essere riutilizzato con molte predict sulla base di un solo training iniziale, quindi i dati si usano a monte per addestrare, per poi andare ad essere usati a valle per l'analisi con le prediction
    """
    # si usa il reshape per andare a trasformare una matrice in un vettore:
    temperatures_vector=np.reshape(roi_img, (rows*cols,1)) # se avessi messo (rows, cols) non sarebbe cambiato nulla
    print(temperatures_vector.shape) #ritorna una shape di 17k righe e 1 sola colonna, quindi sio ha un vettore
    my_model=KMeans(n_clusters=3).fit(temperatures_vector) 
    # il metodo fit per essere usato ha bisogno del costruttore, quindi va costruita dando n cluster, che di default sono 8, fittando il vettore di temp
    # ritornando un oggetto KMeans, quindi occorre costruire l'oggetto (my_model)
    #! aggiungi la parte di predict che il prof fa vedere sulla debug console (fatta velocemente e non spiegata bene)
    #! vedi anche se vuoi https://www.datacamp.com/courses/unsupervised-learning-in-python per fare l'unsupervised machine data learning che, in quanto studenti univpm, non si paga, a mezzo di github student pack
    # con il predict si fa una predizione sul cluster di appartenenza
    clustered_img=np.reshape(my_model.labels_, (rows, cols)) # type: ignore #occorre passare la tupla di righe e colonne di px per riottenere una immagine non lineare
    print(my_model.cluster_centers_)    #stampo i centroidi di ogni cluster, ossia il valore della intensita' luminosa del pixel centrale del cluster
    plt.imshow(clustered_img)
    # il reshape ha natura conservativa difatti si ottiene una immagine colorata con colorazione relativa ai cluster
    plt.show()
    print(type(my_model.labels_)) #controllo che il tipo delle labels richiamate come metodo del my_model: qui da un ValueError perche si aspetta un array 2D, quindi correggo con ",1" in vector
    # restituisce come min e max nelle labels digitando "my_model.labels_" nella debug console tutti 0 ed 1 per via dei soli 2 clusters, aumentando a 3 si ottiene come max 2, quindi adeso clusterizzo l'immagine
    th_value = 200
    for i in range(th_value, 255, 5):
        plt.imshow(roi_img > i, cmap="gray") # type: ignore #andando a sogliare con un operatore maggiore di, allora si sta eseguendo una binarizzazione manuale, ossia un thresholding statico
        plt.show()
        # quando arrivo ad immagini completamente nere, allora nessun pixel è a quel valore di intensità
    # creare istogramma di valori presenti nell'immagine, ricordando che all'asse x ho valori di intensità 0... 255, mentre alle y ho l'occorrenza o frequenza o numero di pixel ad una data intensità
"""
Sistema di riferimento delle immagini top left, che sembra una grayscale, ma che in realtà è salvata come BGR: attenzione perché se viene convertita con l'apposito flag
allora rischia di essere alterata, quindi si può escludere una coppia di canali e considerarne uno solo, in modo da risparmiarci un serie di complicazioni data dalla conversione
OT: Per quanto riguarda il versioning di un qualcosa in ambito IT, si usa lo x.y.z versioning, dove la x indica la major release, la y le major changes ed infine la z indica le minor e le bug fixes, a volte si ha una quarta cifra "t" che indica delle modifiche ancora più fini
"""
main()
