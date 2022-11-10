# MATRICI

n_row = 100
n_cols = 50
#per ogni riga
#per ogni colonna
#stampa indice di riga e colonna

for i in range(0, n_row):
    for j in range(0, n_cols):
        print(f"A[{i}][{j}]")

#il ciclo for interno è molto più veloce di quello esterno; quest'ultimo avanza solo quando quello interno è stato completato
#con due cicli for devo per forza usare indici diversi, in questo caso i, j 