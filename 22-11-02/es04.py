
#TODO chiedere all'utenete il nome del file
#TODO stampare l'insieme delle linee
#TODO se il file non esiste... richiedere nuovamente il nome...

def main():
    
    while True: #posso mettere un while per permettere il successivo inserimento
        file_name = input("inserisci il nome del file")
        my_list_of_values = [] #creo una lista vuota
        try:
            #qui metto le operazioni che possono dare errore...
            my_file = open(file_name)   #prova ad aprire il codice
            while True:
                my_line = my_file.readline()
                if (my_line == ""):
                    break
                # my_list_of_values.append(float(my_file.readline().rstrip())) #genera un type error
                my_list_of_values.append(float(my_line.readline().rstrip()))
            my_file.close()
            break #ha senso mettere il break qui perche se lo mettessi sotto al print dell'eccezine non permetto il successivo inserimento, dato che spengo il while true prima
        except Exception as ex: #Exception e' l'eccezione più generale possiblie, quindi ha una forte elasticita' di utilizzo, ma allo stesso tempo e' tutto e niente(vedi diagramma gerarchico delle eccezioni sulle slide)
            print(f"Ahi Ahi....{ex}")   #se esiste fa qualcosa, se non esiste ci restituisce un errore
main() 