"""Questo modulo implementa le funzioni di plot per mostrare le immagini usando Matplotlib"""

import matplotlib.pyplot as plt

def grafico_immagine(immagine, nome_file_immagine):
    """
    Questa funzione permette di eseguire un grafico di un immagine.
    Parametri in ingresso: immagine (openCV), titolo con casting a stringa
    Parametri in uscita:  grafico che mostra l'immagine con cui si sta lavorando
    """
# ---------------------------------------------------------------------------------------------- #
# Print del messaggio che da istruzioni all'utente per proseguire
# ---------------------------------------------------------------------------------------------- #
    print("Chiudere la finestra contenente il grafico per continuare...")
# ---------------------------------------------------------------------------------------------- #
# Comandi di matplotlib.pyplot importato con alias "plt":
# ---------------------------------------------------------------------------------------------- #
# Si mostra l'immagine con la mappa di colori in scala di grigio
# ---------------------------------------------------------------------------------------------- #
    plt.imshow(immagine, cmap="gray")
# ---------------------------------------------------------------------------------------------- #
# Si stampa il titolo per l'immagine con una f string inserendo il contenuto
# della variabile nome
# ---------------------------------------------------------------------------------------------- #
    plt.title(f"Immagine selezionata: {nome_file_immagine}")
# ---------------------------------------------------------------------------------------------- #
# Si mostra l'immagine nella finestra di matplotlib bloccandone la chiusura automatica
# ---------------------------------------------------------------------------------------------- #
    plt.show(block=True)

def grafico_roi(immagine_roi, nome_file_immagine):
    """
    Questa funzione permette di eseguire un grafico di un immagine ricavata da un'originale
    impostando una bounding box per determinare una regione di interesse utile per successive
    computazioni.
    Parametri in ingresso: immagine_roi, nome_file_immagine
    Parametri in uscita: grafico che mostra la regione di interesse
    """
# ---------------------------------------------------------------------------------------------- #
# Print del messaggio che da istruzioni all'utente per proseguire
# ---------------------------------------------------------------------------------------------- #
    print("Chiudere la finestra contenente il grafico per continuare...")
# ---------------------------------------------------------------------------------------------- #
# Comandi di matplotlib.pyplot importato con alias "plt":
# ---------------------------------------------------------------------------------------------- #
# Si mostra l'immagine con la mappa di colori in scala di grigio
# ---------------------------------------------------------------------------------------------- #
    plt.imshow(immagine_roi, cmap="gray")
# ---------------------------------------------------------------------------------------------- #
# Si stampa il titolo per la regione di interesse con una f string inserendo il contenuto
# della variabile nome
# ---------------------------------------------------------------------------------------------- #
    plt.title(f"Regione di interesse selezionata per l'immagine {nome_file_immagine}")
# ---------------------------------------------------------------------------------------------- #
# Si mostra l'immagine nella finestra di matplotlib bloccandone la chiusura automatica
# ---------------------------------------------------------------------------------------------- #
    plt.show(block=True)

def grafico_cluster(immagine_roi, nome_file_immagine):
    """
    Questa funzione permette di eseguire un grafico di un immagine ricavata da un'originale
    impostando una bounding box per determinare una regione di interesse utile per successive
    computazioni.
    Parametri in ingresso: immagine_roi, nome_file_immagine
    Parametri in uscita: grafico che mostra la regione di interesse
    """
# ---------------------------------------------------------------------------------------------- #
# Print del messaggio che da istruzioni all'utente per proseguire
# ---------------------------------------------------------------------------------------------- #
    print("Chiudere la finestra contenente il grafico per continuare...")
# ---------------------------------------------------------------------------------------------- #
# Comandi di matplotlib.pyplot importato con alias "plt":
# ---------------------------------------------------------------------------------------------- #
# Si mostra l'immagine con la mappa di colori di default per la clusterizzazione
# ---------------------------------------------------------------------------------------------- #
    plt.imshow(immagine_roi)
# ---------------------------------------------------------------------------------------------- #
# Si stampa il titolo per la regione di interesse con una f string inserendo il contenuto
# della variabile nome
# ---------------------------------------------------------------------------------------------- #
    plt.title(f"Regione di interesse selezionata per l'immagine {nome_file_immagine}")
# ---------------------------------------------------------------------------------------------- #
# Si mostra l'immagine nella finestra di matplotlib bloccandone la chiusura automatica
# ---------------------------------------------------------------------------------------------- #
    plt.show(block=True)

def grafico_sottografici(immagine_soglia, immagine_soglia_inversa, titoli):
    """
    Questa funzione permette di eseguire un grafico di più immagini, mostrando all'utente
    due visualizzazioni della regione di interesse da lui richiesta in modo da scegliere quella
    che preferisce per le successive computazioni
    Parametri in ingresso: lista dei titoli, lista delle immagini di sogliatura adattativa
    Parametri in uscita: grafico contenente i sottografici con cui procedere con la computazione
    """
# ---------------------------------------------------------------------------------------------- #
# Creo la tuple di assegnazione delle righe e delle colonne dell'immagine
# ---------------------------------------------------------------------------------------------- #
    (righe,colonne)=immagine_soglia.shape
# ---------------------------------------------------------------------------------------------- #
# Se l'immagine è verticale, allora affianca orizzontalmente i sottografici
# ---------------------------------------------------------------------------------------------- #
    if righe>colonne:
        immagini_sogliatura_adattativa=[immagine_soglia , immagine_soglia_inversa]
# ---------------------------------------------------------------------------------------------- #
# Ciclo for per iterare con le liste dei titoli e delle immagini
# ---------------------------------------------------------------------------------------------- #
        for i in range(len(immagini_sogliatura_adattativa)):
# ---------------------------------------------------------------------------------------------- #
# Struttura di posizionamento dei sotto grafici: 1 riga, 2 colonne, per l'immagine
# ad indice i+1 per via dello start a 0
# ---------------------------------------------------------------------------------------------- #
            plt.subplot(1,2,i+1)
            plt.imshow(immagini_sogliatura_adattativa[i],cmap="gray")
            plt.title(titoli[i])
# ---------------------------------------------------------------------------------------------- #
# Si mostra una barra con il gradiente di colore ad indici estremali 0 e 255
# ---------------------------------------------------------------------------------------------- #
            plt.colorbar(ticks=[0, 255], orientation='horizontal')
        plt.show(block=True)
# ---------------------------------------------------------------------------------------------- #
# Altrimenti, se l'immagine è orizzontale, impila verticalmente i sottografici
# ---------------------------------------------------------------------------------------------- #
    else:
        immagini_sogliatura_adattativa=[immagine_soglia , immagine_soglia_inversa]
# ---------------------------------------------------------------------------------------------- #
# Ciclo for per iterare con le liste dei titoli e delle immagini
# ---------------------------------------------------------------------------------------------- #
        for i in range(len(immagini_sogliatura_adattativa)):
# ---------------------------------------------------------------------------------------------- #
# Struttura di posizionamento dei sotto grafici: 2 righe, 1 colonna, per l'immagine
# ad indice i+1 per via dello start a 0
# ---------------------------------------------------------------------------------------------- #
            plt.subplot(2,1,i+1)
            plt.imshow(immagini_sogliatura_adattativa[i],cmap="gray")
            plt.title(titoli[i])
# ---------------------------------------------------------------------------------------------- #
# Si mostra una barra con il gradiente di colore ad indici estremali 0 e 255
# ---------------------------------------------------------------------------------------------- #
            plt.colorbar(ticks=[0, 255], orientation='horizontal')
        plt.show(block=True)
