##
# TABELLA CON PYTHON
##

def main():
    """ Entry - Point """
    my_file = open ("esempio_open_funct2.txt", "r") #la r dopo la virgola rappresenta l'open in modalita' lettura)
    my_table = [] #all'inizio come una lista vuota
    while True:
        my_line = my_file.readline().rstrip()
        if (my_line ==""):
            break
        my_line_splitted = my_line.split(";") #divisione con il carattere ";"
        my_table.append(my_line_splitted)
    my_table.pop(0)
    my_file.close()
    #alternativa per accedere ad un file senza while true
    my_file = open ("esempio_open_funct2.txt", "r")
    flag = True
    while flag:
        my_line = my_file.readline().rstrip()
    if (my_line ==""):
        flag = False
    else:
        my_line_splitted = my_line.split(";") #divisione con il carattere ";"
        my_table.append(my_line_splitted)
    print(my_table)