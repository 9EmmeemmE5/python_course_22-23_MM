"""example of with statement"""
# l'opzione di encoding serve per rimuovere il descoring di pylint,
# ma in primo luogo per definire un encoding del file che si sta
# operando tramite la linea dello script
def main():
    """entrypoint for our application"""
    with open("./22-11-03/myfile2.txt","w", encoding="utf-8") as my_file:
        my_file.write("ciao mondo\n")
    # my_file.write("hello") qui si genera un IOError perche ho aperto il file,
    # operato e poi chiuso con il with
    with open("./22-11-03/myfile2.txt", encoding="utf-8") as my_file:
        while True:
            my_line = my_file.readline()
            if my_line=="":
                break
            print(f"{my_line}")
    print("hello")
main()
