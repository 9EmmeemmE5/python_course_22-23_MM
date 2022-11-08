"""Esercizio dizionari ed insiemi"""
#creare una lista con tutte le parole
#creare un insieme per ogni lista
#fare intersezione...

def load_file_into_string(path_of_file):
    """Returns a string from a file"""
    my_line = ""
    with open(path_of_file) as my_file:
        my_line += my_file.readline()
    return my_line

def extract_list_from_string(my_str:str, sep = " ", items_to_be_removed = [".",",",";",":","!","?"]):
    """returns a list of words"""
    tmp_value = my_str.lower()
    for item in items_to_be_removed:
        tmp_value = tmp_value.replace(item, "")
    #tmp_value = tmp_value.split(sep)   #non serve assegnare per poi ritornare, ritorno direttamente il risultato
    return tmp_value.split(sep)

def main():
    my_list1 = extract_list_from_string(load_file_into_string())
main()
