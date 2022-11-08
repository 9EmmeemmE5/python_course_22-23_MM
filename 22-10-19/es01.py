## BASH o BATCH
#TODO: Stampare la somma dei numeri passati in ingresso mediante sys.argv

import sys  #evitiamo variabili globali e definiamo la funzione main

def main():
    """Entry point for our script"""
    print(sys.argv) #stampa il contenuto di sys.argv, dove il primo valore della stringa coincide con il nome del file, del tipo ".\\es01.py"
    #sys.argv[0] --> contiene script name, dove si trovano i numeri all'interno della lista se qualcuno glieli ha dati
    #si necessita un input: numero1 -->sys.argv[1], poi numero2 --> sys.argv[2], quindi a livello di argomenti, la lunghezza di un numero di elementi presente nella lista
    #si definisce con len()
    if len(sys.argv) == 3:
        print(f"La somma di {sys.argv[1]} e {sys.argv[2]} è pari a : \
            {float(sys.argv[1])+float(sys.argv[2])}") #sopra il secondo {} è sys.argv[2] e non di 3 perche genererebbe un'eccezione di index out of range
        """
        {float(sys.argv[1]+sys.argv[2]}") ERRATO per via del fatto che sto facendo una somma di stringhe, quindi và eseguito un casting, facendolo diventare un numero che può essere sommato
        """
    else:
        print("numero di argomenti errato") #se la lunghezza è diversa da 3 allora ...,  la lunghezza diversa da 3 perché ho dimenticato oppure ho sforato coi valori
main()

"""
Per andare ad eseguire lo script dobbiamo richiamare il main con la riga 19, successivamente, nel terminale scriviamo "cd PATH", dove PATH è il percorso che contiene lo script,
poi "python FILENAME + comandi (i.e. 3 4)" così nel terminale viene eseguita la funzione main, restituendo 7.0 ossia la somma
"""
