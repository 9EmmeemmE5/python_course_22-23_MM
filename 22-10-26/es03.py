""" 
creare due liste
my_list1 contiene valori da 0 a 10
my_list2 contiene valori che sono il quadrato degli item di my_list1
"""

# from matplotlib import pyplot           #importazione del modulo pyplot dalla libreria matplotlib: esso e' il modulo che ci permette di plottare in python
import matplotlib.pyplot as plt           #alternativa con rinominazione "as" e' l'alias per creare un nuovo nome per facilitare il richiamo dentro l'IDE

def main():
    """entrypoint"""
    my_list1 = []
    my_list2 = []
    for i in range(11):
        my_list1.append(i)
        my_list2.append(i**2)
    print(my_list1)
    print(my_list2)
    plt.plot(my_list1, my_list2, 'r-*')    #sequenza di operazioni per creare il mio plot
    plt.title("Titolo del mio grafico")
    plt.xlabel("Il nome dell'asse x del mio grafico")
    plt.ylabel("Il nome dell'asse y del mio grafico")
    plt.savefig("mioplot.png",)
    plt.savefig("mioplot.jpg",)
    plt.savefig("mioplot.pdf",)
    plt.show()  # mostro il plot: chiamata di tipo bloccante AKA il programma rimane bloccato fintanto che lo showplot non viene chiuso
main()