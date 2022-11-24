"""Demo of point import"""
from point import Point as pt
from moduloa.suba import prompt_for_point, calculate_distance #esecuzione di import del modulo si inserisce il pathcon cartelle suddivise da punti "." e dopo si scrive il modulename, poi si importa la funzione

print("hello world")
#inserisco bkpoint sul print e debuggo noto che, passando a point.py sul __name__ trovo point e non __main__, quindi trovo il nome del file e perciò lo script è stato importato direttamente
#per riconoscere se qualcosa viene invocata od importata si inserisce il compound statement presente dalla riga 26 del modulo point: se lo lancio direttamente, ossia lo apro da cmd con il cd, path, poi "python nomefile.py", esce il print relativo all'invoke, mentre se lo importo ed eseguo il file python con l'importazione, allora esce il print dell'importazione.
#In questo modo posso discriminare l'importazione sull'invoke, o viceversa, per capire se lo script è partito da solo o lo si è fatto partire e questo è utile per i test: se li voglio fare, allora, inserendoli direttamente dentro al file del modulo e poi lo invoco, allora vengono eseguiti, mentre se si è importato il modulo allora i test sono solo importati

def main():
    my_point1 = prompt_for_point()
    my_point2 = prompt_for_point()
    #così ho codice ripetuto e andrebbe raccolto dentro una funzione e non va bene
    print(f"il mio primo punto è {my_point1}")
    print(f"il mio secondo punto è {my_point2}")
    my_point3 = my_point1+my_point2
    print(f"il mio terzo punto è {my_point3}")
    print(f"la distanza tra i punti 1 e 2 è {calculate_distance(my_point1,my_point2)}")
    print(f"la distanza tra i punti 1 e 3 è {calculate_distance(my_point1,my_point3)}")
    print(f"la distanza tra i punti 2 e 3 è {calculate_distance(my_point2,my_point3)}")

if __name__=="__main__":    #in questo caso creo dall'esterno tutto ciè che si può fare fuori, come dei moduli, quindi poi importo point, lo conosco e lo uso nello script principale
    main() #non ha senso testare main, occorre testare quello che sta fuori, ossia la funzione, non il main; non occorre testare tutte le funzioni, ma esiste un approccio chiamato TDD test driven development simile ad un PDCA, più PDCDA
    #qui il main lo richiamo perche' sto entrando da main, non lo importo, perche non importo una cosa che importa un altra cosa ancora...