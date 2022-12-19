"""Esame di Fondamenti di informatica (Meccanica) Dic 2022 - Marco Mosca mat. 1102851"""
# ---------------------------------------------------------------------------------------------- #
# Image processing: Piccoli Grilli
# ---------------------------------------------------------------------------------------------- #
# Questo script python, sulla base del nome dell'immagine contenuto nel file di testo
# lista_file_immagini, presente nella radice della cartella di lavoro, consente all'utente
# di identificare una regione di interesse (RoI), applicare una soglia di tipo adattativo
# per identificare i grilli della regione di interesse e ricavarne le coordinate a mezzo
# della matrice P delle coordinate.
# Infine lo script applica un algoritmo di suddivisione in cluster per raggruppare campioni
# vicini tra di loro ed eventuali punti di rumore nelle immagini.
# ---------------------------------------------------------------------------------------------- #
# Documentazione web:
# Adaptive Thresholding: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
# DBSCAN: https://bit.ly/demo_DBSCAN_esame
# ---------------------------------------------------------------------------------------------- #
# Richiamo moduli
# ---------------------------------------------------------------------------------------------- #
from Moduli import regioni_di_interesse, sogliatura_clustering,\
    operazioni_matrici, plot_immagini, lettura_input
# ---------------------------------------------------------------------------------------------- #
def main():
    """Punto di ingresso"""
# ---------------------------------------------------------------------------------------------- #
# Definizione del percorso del file contenente la lista di immagini
# ---------------------------------------------------------------------------------------------- #
    percorso_lista_file=".\\ESAME_MM\\lista_file_immagini.txt" #!cambiare prima della consegna
# ---------------------------------------------------------------------------------------------- #
# Creazione lista con nomi dei file
# ---------------------------------------------------------------------------------------------- #
    lista_nomi_file=lettura_input.lettura_input_testo(percorso_lista_file)
    print(f"L'algoritmo verrà eseguito per i file:\n{lista_nomi_file}\n")
# ---------------------------------------------------------------------------------------------- #
# Definizione del percorso contenente i file immagine
# ---------------------------------------------------------------------------------------------- #
    percorso_immagini=".\\ESAME_MM\\Immagini\\" #!cambiare prima della consegna
    for element in lista_nomi_file:
        print(f"Esecuzione algoritmo per l'immagine {element}\n")
        try:    # Tento l'apertura dell'immagine con la funzione lettura_immagine
            immagine=lettura_input.lettura_immagine(percorso_immagini, element)
        except IOError as io_ex:  # Richiamo l'eccezione sollevata nella funzione
            print(f"Eccezione di tipo {io_ex} per {element}\n")
# ---------------------------------------------------------------------------------------------- #
# Grafico immagine di partenza
# ---------------------------------------------------------------------------------------------- #
        print("Apertura immagine in corso...\n\nMuovendo il mouse all'interno dell'immagine,\n\
individuare il punto in alto a sinistra e quello in basso a destra di una regione \n\
rettangolare che rappresenta la regione di interesse in cui verrà eseguita la sogliatura\n\
e la clusterizzazione\n")
        plot_immagini.grafico_immagine(immagine, element)
# ---------------------------------------------------------------------------------------------- #
# Creazione della ROI
# ---------------------------------------------------------------------------------------------- #
        immagine_roi=regioni_di_interesse.creazione_roi_manuale(immagine)
        print("Apertura immagine della regione di interesse selezionata in corso...\n")
        plot_immagini.grafico_roi(immagine_roi, element)
# ---------------------------------------------------------------------------------------------- #
# Applicazione dell'algoritmo di sogliatura adattiva
# ---------------------------------------------------------------------------------------------- #
        immagini_sogliate=sogliatura_clustering.sogliatura_adattativa(immagine_roi)
# ---------------------------------------------------------------------------------------------- #
# Grafico delle immagini sogliate con il quale l'utente sceglie il riferimento
# ---------------------------------------------------------------------------------------------- #
        titoli=["Grilli visualizzati con il valore di \n riferimento di sogliatura v=0","Grilli \
visualizzati con il valore di \nriferimento di sogliatura v=255"]
        plot_immagini.grafico_sottografici(immagini_sogliate[0], immagini_sogliate[1], titoli)
# ---------------------------------------------------------------------------------------------- #
# Creazione matrice P delle coordinate dei punti sogliati:
# scelta dell'utente il valore di riferimento intensità di scala di grigio
# con restituzione all'indice 0 della tuple l'immagine sogliata per il DBSCAN
# e all'indice 1 il valore di riferimento
# ---------------------------------------------------------------------------------------------- #
        (immagine_v_rif_dbscan,valore_riferimento)=\
        sogliatura_clustering.riferimento_sogliatura(immagini_sogliate[0],immagini_sogliate[1])
        matrice_p=operazioni_matrici.matrice_p_coord_px_sogliati(immagine_v_rif_dbscan,\
            valore_riferimento)
# ---------------------------------------------------------------------------------------------- #
# Grafico dell'immagine per entrare nel DBSCAN al valore di riferimento scelto
# ---------------------------------------------------------------------------------------------- #
        plot_immagini.grafico_immagine(immagine_v_rif_dbscan,nome_file_immagine=f"Immagine a cui \
applicare\n l'algoritmo di clusterizzazione DBSCAN:\n\
valore di riferimento scelto {valore_riferimento}")
# ---------------------------------------------------------------------------------------------- #
# Applicazione dell'algoritmo DBSCAN
# ---------------------------------------------------------------------------------------------- #
        etichette_clusters=sogliatura_clustering.clusterizzazione_db_scan(matrice_p)
# ---------------------------------------------------------------------------------------------- #
# Creazione matrice F
# ---------------------------------------------------------------------------------------------- #
        matrice_f=operazioni_matrici.matrice_f_immagine_clusterizzata(immagine_v_rif_dbscan,\
            matrice_p, etichette_clusters)
# ---------------------------------------------------------------------------------------------- #
# Plot di F senza l'esclusione dei cluster di dimensioni maggiori ad un valore N
# ---------------------------------------------------------------------------------------------- #
        plot_immagini.grafico_cluster(matrice_f, nome_file_immagine="\nMatrice F dell'immagine \
clusterizzata")
# ---------------------------------------------------------------------------------------------- #
# Raffinazione della matrice F con esclusione dei cluster di dimensioni maggiori ad un valore N
# ---------------------------------------------------------------------------------------------- #
        matrice_f=operazioni_matrici.matrice_f_immagine_clusterizzata_raffinata(matrice_f,\
            etichette_clusters)
# ---------------------------------------------------------------------------------------------- #
# Plot di F con l'esclusione N
# ---------------------------------------------------------------------------------------------- #
        plot_immagini.grafico_cluster(matrice_f, nome_file_immagine="\nMatrice F dell'immagine\n\
clusterizzata con esclusione dei cluster\n\
di dimensione maggiore al valore inserito")
main()
