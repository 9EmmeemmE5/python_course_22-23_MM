"""Processing opencv2 python script"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt #ricorda sempre il pyplot

def main():
    """Entry point for out application"""
    img_defect_0 = cv.imread("22-12-06\\img\\DJI_0035.jpg")
    print(img_defect_0.shape, img_defect_0.dtype)
    channel_of_interest = img_defect_0[:,:,0] # estrae con gli operatori di broadcast ":" tutte le righe (primo :), tutte le colonne (secondo :) del canale numero 1 con indice 0
    roi_img = channel_of_interest[80:192, 50:205] #creo una roi manuale andando a leggere i valori dei pixel con il plot #! attenzione al sistema di riferimento per non far confuzine con i valori x ed y dei punti presi sotto
    #point 1 - x=50, y=80
    #point 2 - x=205, y=192
    plt.imshow(channel_of_interest, cmap="gray") #con il cmap la visualizzo correttamente e non palettizzata con un false colouring
    plt.show()
    #Creare istogramma
    bins_value = np.zeros((256,1), dtype=np.uint32) #np.uint8 non va bene perche memorizza valori da 0 a 255 e non va bene perche se sforo la soglia di 255 sto commettendo un errore di troncamento, quindi il dominio va esteso al minimo ad un valore pari al prodotto tra numero di righe e di colonne, considerando il caso monopicco di immagini o tutte nere o tutte bianche
    (rows,cols) = roi_img.shape
    for i in range(rows):
        for j in (cols):
            value = roi_img[i,j]
            bins_value[value]+=1
    th_value = 200
    for i in range(th_value, 255, 5):
        plt.imshow(roi_img > i, cmap="gray") #andando a sogliare con un operatore maggiore di, allora si sta eseguendo una binarizzazione manuale, ossia un thresholding statico
        plt.show()
        #quando arrivo ad immagini completamente nere, allora nessun pixel è a quel valore di intensità
    #creare istogramma di valori presenti nell'immagine, ricordando che all'asse x ho valori di intensità 0... 255, mentre alle y ho l'occorrenza o frequenza o numero di pixel ad una data intensità
    
"""sistema di riferimento delle immagini top left, che sembra una grayscale, ma che in realtà è salvata come BGR: attenzione perché se viene convertita con l'apposito flag
allora rischia di essere alterata, quindi si può escludere una coppia di canali e considerarne uno solo, in modo da risparmiarci un serie di complicazioni data dalla conversione
"""
main()