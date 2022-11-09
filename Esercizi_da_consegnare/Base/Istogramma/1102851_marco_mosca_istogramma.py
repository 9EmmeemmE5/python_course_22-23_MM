#
#TODO: Calcolare min, max, media, deviazione standard di una serie di input dati dall'utente usando le liste
#TODO: Opzionale: Diviso l'intervallo di valori dati dall'utente in N classi (input utente), calcolare la frequenza di ognuno di essi e stampare l'istogramma

import numpy as np
import matplotlib.pyplot as plt

N_DIV = int(input("Definire il numero di classi in cui dividere l'intervallo di numeri inserito..."))
value_to_add = int(input("Definire quanti valori inserire..."))     #TODO prova ad eliminare inserendo il while true sotto a #L12
my_list =[]

while len(my_list) != value_to_add:                                 #TODO Prova true
    my_value = input("Inserire un numero o la parola \"exit\" per uscire dall'inserimento: \n")
    if my_value != "exit":
        try:
            my_list.append(float(my_value))
        except Exception as ex:
            print("Inserimento non corretto:\nInserire un numero o la parola \"exit\"")
    elif my_value == "exit":
        break

print(f"I numeri inseriti sono\n{my_list}")

min_value = min(my_list)
max_value = max(my_list)
mean_value = np.mean(my_list)
devstd_value = np.std(my_list)
print(f"Il valore minimo della lista di valori inserita è {min_value:.3f},\nil valore massimo è {max_value:.3f},\nil valor medio è {mean_value:.3f},\nla deviazione standard {devstd_value:.3f}")

#* plot dell'istogramma
sub_ints_largh = (max_value-min_value)/N_DIV                                    # larghezza delle classi
sub_ints_bin_range = []                                                         # estremi delle classi

for i in range(N_DIV+1):
    sub_ints_bin_range.append(min_value+i*sub_ints_largh)                       # append degli estremi
plt.hist(my_list, bins=sub_ints_bin_range, edgecolor='black')                   # plot istogramma con .hist, che prende in input i valori della lista e le divisioni in classi
plt.show

#! print della frequenza di ogni classe
my_list.sort()
sub_ints_freq = []#lista che contiene le len delle classi in sotto-liste
sub_ints_bin_range.pop(0)
for element in my_list:
    bin_list = []
    if element <= sub_ints_bin_range[0]:
        bin_list.append(element)                                             #! appendere sottoliste per poi printarne il len
        my_list.pop(0)
    if element > sub_ints_bin_range[0]:
        sub_ints_bin_range.pop(0)
        bin_list.append(element)                                             #! appendere sottoliste per poi printarne il len
        my_list.pop(0)
    else:
        sub_ints_freq.append(len(bin_list))
print(sub_ints_freq)
print(f"Le frequenze delle classi sono, dalla prima all'ultima, {sub_ints_freq}") #! da correggere e mettere len delle sottoliste