from ins_val import inserimento_valori_numerici

valore_riferimento = None # Inizializzazione valore
while valore_riferimento!=0 and valore_riferimento!=255: # al posto di diverso da 0 e 255
    # Uso della funzione inserimento_valori_numerici per prendere in input il valore
    valore_riferimento = inserimento_valori_numerici("Inserire il \
valore di riferimento di intensità di scala di grigio dei grilli (0, ossia nero su bianco o 255,\
ossia bianco su nero): \n")
    # Assegnazione il valore
    if valore_riferimento == 255:
        immagine_soglia_dbscan = "immagine_soglia_inversa"
    elif valore_riferimento == 0:
        immagine_soglia_dbscan = "immagine_soglia"
    else:
        print(f"Errore\
        \n{valore_riferimento} != 255\
        \n{valore_riferimento} != 0")
        
print(immagine_soglia_dbscan)