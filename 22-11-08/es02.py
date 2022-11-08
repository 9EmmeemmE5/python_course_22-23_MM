"""Esercizio dizionari ed insiemi"""
#creare una lista con tutte le parole
#creare un insieme per ogni lista
#fare intersezione...

def load_file_into_string(path_of_file):
    """Returns a string from a file"""
    my_line = ""
    with open(path_of_file) as my_file:
        while True:                         #CS per ciclare la lettura di più righe e terminare alla linea vuota post-ultima riga 
            my_tmp_line = my_file.readline()    #uso la temporanea per ciclare il controllo
            if my_tmp_line == "":               #condizione linea vuota per il ciclo di controllo
                break
            my_line = my_tmp_line               #uguaglianza a my_line della temp dal controllo
    return my_line

def extract_list_from_string(my_str:str, sep = " ", items_to_be_removed = [".",",",";",":","!","?"]):
    """returns a list of words"""
    tmp_value = my_str.lower()
    for item in items_to_be_removed:
        tmp_value = tmp_value.replace(item, "")
    #tmp_value = tmp_value.split(sep)   #non serve assegnare per poi ritornare, ritorno direttamente il risultato
    return tmp_value.split(sep)

def main():
    my_list1 = extract_list_from_string(load_file_into_string("./22-11-08/word1.txt"))
    print(my_list1)
    my_set1 = set(extract_list_from_string(load_file_into_string("./22-11-08/word1.txt")))
    my_set2 = set(extract_list_from_string(load_file_into_string("./22-11-08/word2.txt")))
    print(len(my_set1), len(my_set2))
    my_common_words = my_set1.intersection(my_set2)
    print(f"numero di parole comuni {len(my_common_words)}")
    print(f"le parole in comune sono:\n {(my_common_words)}")
main()
