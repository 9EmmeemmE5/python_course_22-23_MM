'''
Questo modulo permette di plottare un'immagine con una sola funzione
'''
import matplotlib.pyplot as plt

def plt_img(img, title):
    '''
    Questa funzione plotta un immagine non bloccante con un titolo.
    @param img: array da plottare
    @param title: stringa da inserire come titolo
    @param block: se block=False non è bloccante
    '''

    plt.imshow(img, cmap="gray") # Con mappa di colori
    plt.title(title)
    plt.show(block=False) # Plot non bloccante False

def plt_img_block(img, title):
    '''
    Questa funzione plotta un immagine bloccante con un titolo.
    @param img: array da plottare
    @param title: stringa da inserire come titolo
    @param block: se block=False non è bloccante
    '''

    plt.imshow(img, cmap="gray") # Con mappa di colori
    plt.title(title)
    print("Chiudere l'immagine per continuare...")
    plt.show(block=True) # Plot bloccante con Ture
