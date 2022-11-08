"""scrivere una funzione che ritorna, a partire da una lista di valori, il loro cubo (lista) e salvare il risultato (lista) su un file"""

def calculate_power(list_of_values, power):
    """Returns a new list with values elevated to power"""
    list_out_of_values = []                         #devo creare una unova lista che converte i valori di partenza in una lista in valori al cubo nella nuova lista
    
    #Versione con il range:
    
    # for i in range(len(list_out_of_values)):
        # list_out_of_values.append( list_out_of_values[i]** power )
    
    #for each version
    for item in list_of_values:
        list_out_of_values.append(item**power)      #ad ogni elemento aggiungo un nuovo elemento che è pari alla potenza per l'esponnente power precedentemente definito
    return list_out_of_values

def save_list_to_file(list_of_values, file_name):
    """This function dumps a list to a file"""
    my_file = open(file_name,"w")
    for item in list_of_values:
        my_file.write(str(item)+'\n')                    #il cast a stringaè una misura ridondante di sicurezza #! aggiungere sempre lo +'\n'
        my_file.write(f"{item}\n")                       #molto più pulito il write se si fa con la f.string
    my_file.close()

def main():
    """Entry-point"""
    my_test_list = [0.1, 0.5, 4.5, 3.6, 4.8, 9.7]   #devo creare un lista di test
    my_out_list = calculate_power(my_test_list, 3)
    save_list_to_file(my_out_list, "Mia_Lista.txt")
    for i in range (1,5):
        my_out_list = calculate_power(my_test_list, i)
        save_list_to_file(my_out_list,"Power_iterative")
main()
