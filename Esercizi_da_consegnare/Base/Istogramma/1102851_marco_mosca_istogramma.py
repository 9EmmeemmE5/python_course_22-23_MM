#
#TODO: Calcolare min, max, media, deviazione standard di una serie di input dati dall'utente usando le liste
#TODO: Opzionale: Diviso l'intervallo di valori dati dall'utente in N classi (input utente), calcolare la frequenza di ognuno di essi e stampare l'istogramma
import sys
import numpy as np
import matplotlib.pyplot as plt

def values(my_list):
    """Function that determines the min, max, avg and std_dev of the user list"""
    min_value = min(my_list)
    max_value = max(my_list)
    mean_value = np.mean(my_list)
    devstd_value = np.std(my_list)
    print(f"Il valore minimo della lista di valori inserita è {min_value:.3f},\n\
            il valore massimo è {max_value:.3f},\nil valor medio è {mean_value:.3f},\n\
            la deviazione standard {devstd_value:.3f}")
    char_values_list = []
    char_values_list.append(min_value)
    char_values_list.append(max_value)
    return char_values_list

def bin_freq(my_list, bin_extr):
    """Prints the frequency of each histogram class"""
    my_list.sort()
    sub_ints_freq = []#lista che contiene le len delle classi in sotto-liste
    bin_extr.pop(0)
    for element in my_list:
        bin_list = []
        for item in bin_extr:
            if element <= item:
                bin_list.append(element)                                             #! appendere sottoliste per poi printarne il len
                my_list.pop(0)
            if element > item:
                bin_list.append(element)                                             #! appendere sottoliste per poi printarne il len
                my_list.pop(0)
                bin_extr.pop(0)
            else:
                sub_ints_freq.append(len(bin_list))
    print(sub_ints_freq)
    print(f"Le frequenze delle classi sono, dalla prima all'ultima, {sub_ints_freq}") #! da correggere e mettere len delle sottoliste

def main():
    """Entry point"""
    my_list =[]
    if len(sys.argv)==17:
        value_to_add = len(sys.argv)
        N_DIV = int(sys.argv[1])
        for i in range (1,value_to_add):
            my_value = input(sys.argv[i])
            if my_value != "exit":
                try:
                    my_list.append(float(my_value))
                except Exception as ex:
                    print("Inserimento non corretto:\nInserire un numero o la parola \"exit\"")
            elif my_value == "exit":
                break
    print(f"I numeri inseriti sono\n{my_list}")
    list_val=values(my_list)
    #* plot dell'istogramma
    sub_ints_largh = (list_val[1]-list_val[0])/N_DIV                                   # larghezza delle classi
    bin_extr = []                                                         # estremi delle classi
    for i in range(N_DIV+1):
        bin_extr.append(list_val[0]+i*sub_ints_largh)                       # append degli estremi
    plt.hist(my_list, bins=bin_extr, edgecolor='black')                   # plot istogramma con .hist, che prende in input i valori della lista e le divisioni in classi
    plt.show
main()
