## liste di liste

import numpy as np
import matplotlib.pyplot as plt

my_matrix_np = np.zeros( (100 , 100) , dtype=np.uint8)
my_matrix_np = my_matrix_np + 1
print(my_matrix_np)
my_matrix_np[4][0]
print(my_matrix_np.shape)
print(my_matrix_np[20:3][20:3])        #operazione di slicing della matrice principale in sotto-matrici

#creare una matrice (tabella) di 100 righe e 100 colonne...

#[0,0,0,0,0,0,0,0,0]-> vettore
#[[0,0,0],[0,0,0],[0,0,0]]
#per accedere occorre digitare my_matrix [0][0]
my_matrix= []
my_matrix_rgb = []
for i in range (100):    #se metto da 0 a 101 farebbe da 0 fino a 100
    my_matrix.append([0]*100)
    my_matrix_rgb.append([[0,0,0]]*100)

plt.imshow(my_matrix_np)
plt.show()
print(my_matrix[0][0])
print(my_matrix_rgb[0][0][2])   

#la tabella e' una rappresentazione di dati come str o list, ma nella tabella i dati non devono essere sempre e per forza gli stessi
#una tabella presenta un dato di tipo non omogeneo, come ad esempio la ista, dove posso inserire un int, un bool, una str ecc, quindi non presenta 
#sempre la stessa tipologia di dato, come per una matrice