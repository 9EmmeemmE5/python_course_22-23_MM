"""
Questo modulo implementa la funzione di creazione della lista di coordinate di 2 punti per
generare una regione di interesse all'interno di un grafico contenente un immagine
"""
import matplotlib.pyplot as plt
import cv2 as cv
#! DA RIVEDERE LA DOC DI mplt_connect, pick e click, il prof a copiato ed incollato gli snippet: fai la prova poi modifichi implementazione
def onclick(event,coords,cid,PERCORSO_IMMAGINI,nome_file_immagine):
    global ix, iy, fig, ax
    image=cv.imread(f"{PERCORSO_IMMAGINI}{nome_file_immagine}", cv.IMREAD_GRAYSCALE)
    fig,ax=plt.subplots()
    plt.subplot(1,1,1)
    plt.imshow(image, cmap="gray")
    ix, iy = event.xdata, event.ydata
    x_int=int(ix)
    y_int=int(iy)
    
    coords.append((x_int,y_int))
    
    # Disconnect after 2 clicks
    if len(coords) == 2:
        fig.canvas.mpl_disconnect(cid)
        plt.close(1)
    return



