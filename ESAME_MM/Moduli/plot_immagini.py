"""Questo modulo implementa le funzioni di plot per mostrare le immagini usando Matplotlib"""
#import unittest
import matplotlib.pyplot as plt

def grafico_immagine(immagine, nome_file_immagine):
    """
    Questa funzione permette di eseguire un grafico di un immagine.
    Parametri in ingresso: immagine (openCV), titolo con casting a stringa
    Parametri in uscita:  grafico che mostra l'immagine con cui si sta lavorando
    """
    print("Chiudere la finestra contenente il grafico per continuare...")
    plt.imshow(immagine, cmap="gray")
    plt.title(f"Immagine selezionata: {nome_file_immagine}")
    plt.show(block=True)

def grafico_roi(immagine_roi, nome_file_immagine):
    """
    Questa funzione permette di eseguire un grafico di un immagine ricavata da un'originale
    impostando una bounding box per determinare una regione di interesse utile per successive
    computazioni.
    Parametri in ingresso: immagine_roi, nome_file_immagine
    Parametri in uscita: grafico che mostra la regione di interesse
    """
    print("Chiudere la finestra contenente il grafico per continuare...")
    plt.imshow(immagine_roi, cmap="gray")
    plt.title(f"Regione di interesse selezionata per l'immagine {nome_file_immagine}")
    plt.show(block=True)

def grafico_roi_auto(immagine):
    """
    Questa funzione implementa un blocco di codice da dare in ingresso alla funzione di
    creazione della roi in modalità automatizzata con 2 click di mouse forzando il plot
    in una figura, in modo da poter usare il matplotlib event handling.
    Parametri in ingresso:
    Parametri in uscita:
    """
    fig,ax=plt.subplots()
    plt.subplot(1,1,1)
    plt.imshow(immagine, cmap="gray")
    return fig,ax

def grafico_sottografici(immagine_soglia, immagine_soglia_inversa, titoli):
    """
    Questa funzione permette di eseguire un grafico di più immagini, mostrando all'utente
    due visualizzazioni della regione di interesse da lui richiesta in modo da scegliere quella
    che preferisce per le successive computazioni
    Parametri in ingresso: lista dei titoli, lista delle immagini di sogliatura adattativa
    Parametri in uscita: grafico contenente i sottografici con cui procedere con la computazione
    """
    immagini_sogliatura_adattativa=[immagine_soglia , immagine_soglia_inversa]
    # Ciclo for per iterare con le liste dei titoli e delle immagini
    for i in range(len(immagini_sogliatura_adattativa)):
        plt.subplot(1,2,i+1)
        plt.imshow(immagini_sogliatura_adattativa[i],"gray")
        plt.title(titoli[i])
        plt.colorbar(ticks=[0, 255], orientation='horizontal')
    plt.show(block=True)
    # inserisci i test dentro ai moduli come best case scenario di lavoro:
    # nel caso di progetti piccoli si può anche creare un modulo esterno di soli test
