##
#       Analisi del sistema massa-molla-smorzatore forzato ad intervallo classico di campionamento per l'analisi della funzione
##

#TODO:
#TODO:
#TODO: Plottare il risultato in matplotlib

#! codificare pensando alla possibilità di variare la funzione e non usare la sola funzione di base presente all' interno della consegna
#! creare una seconda funzione che restituisca i valori da impostare in ingresso alla prima funzione

import numpy as np
import matplotlib.pyplot as plt

def y_travel_funct():
    y_mass_travel =
    return y_mass_travel

T_SIM =10 #float(input("Inserire il valore temporale totale del tempo simulazione"))
tC = 0.01 #float(input("Inserire il valore temporale del singolo campione"))
n_samples = int(T_SIM/tC)

my_sim_data = np.zeros((n_samples,2))      #sono delle matrici perche si necessita di visualizzare l'andamento nel tempo,
# quindi la matrice deve essere grande n_samples x n°colonne dei valori da memorizzare, quindi la il tempo e la y della molla

print(my_sim_data)

my_sim_data[0][0] = 0.0
my_sim_data[0][1] = 0.2343  #nel for si cambia l'indice di sinistra perche indica il tempo ciclo
#come alternativa è possibile scrivere i valori della simulazione su 2 liste; se si riesce

time_list = []
travel_list = []

# #! plot
# fig, ax = plt.subplots()
# ax.plot(time_list, travel_list)     
# ax.set(xlabel='time (s)', ylabel='y(t) - Mass travel',
#        title='Mass-Spring-Damper simulation')
# ax.grid()
# plt.show()