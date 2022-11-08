##
#   METODO DI BISEZIONE PER LA RICERCA DELLO ZERO DI UNA FUNZIONE
##

#TODO:  far definire all'utente 6 ingressi (estremi dell'intervallo e coefficienti del polinomio di terzo grado) per calcolare lo zero di funzione col dicotomico
import sys
MAX_ITER = 20
EPS_TH = 1e-5
#quelli sotto sono valori di default, difatti, se non sono definiti si potrebbe inserire una dummy_value con tutti zero, impostando dei valori di default
def third_deg_poly(x_value = 0.0, coeff_0 = 0.0, coeff_1 = 0.0, coeff_2 = 0.0, coeff_3 = 0.0):  
    """This function calculate the value of a third degree poly..."""
    return coeff_0 + coeff_1*x_value + coeff_2*x_value**2 + coeff_3*x_value**3

def find_zero(a_value, b_value, coeff_0, coeff_1, coeff_2, coeff_3):
    """
    Function that implements the dicotomic algorithm
    """
    iter_count = 0
    #verificare 1. segno concorde => errore 2. a_value < b_value
    if ( a_value >= b_value ):
        print("a_value deve essere inferiore a b_value")
        return None  #primo controllo eseguito, andando ad inserire il none nel caso in cui ci siano problemi
    
    while True:
        c_value = (a_value+b_value)*0.5
        y_c_value = third_deg_poly(c_value, coeff_0, coeff_1 , coeff_2, coeff_3) #variabile di appoggio per non entrare diretti nel CS if c_value = 0, detta anche BUFFER; i.e. f(x)
        y_a_value = third_deg_poly(a_value, coeff_0, coeff_1 , coeff_2, coeff_3) #variabile di appoggio per a
        y_b_value = third_deg_poly(b_value, coeff_0, coeff_1 , coeff_2, coeff_3) #variabile di appoggio per b
        #verifico se il segno sia concorde; in caso positivo allora esco...
        if( y_a_value * y_b_value > 0 ):
            return None #l'else risulta implicito perche' se si verifica bene, altrimenti esce; se inserico il break, occorre definire cosa succede, altrimenti esito indeterminato
        iter_count +=1
        if ( y_c_value <= abs(EPS_TH) ):    #lo == 0 non risulta di facile raggiungimento, quindi si avanza con l'ottica del circa uguale
            return c_value  #zero della nostra funzione
        elif y_a_value * y_c_value < 0 :
            b_value = c_value
        else:
            a_value = c_value
        if iter_count >= MAX_ITER:
            print("Max iterations reached... No result given...")
            return None #non conviene mettere l'else break, ma piuttosto il none, con il print

def main():
    """
    input: estremo sx, estremo dx, c0, c1, c2, c3
    output: zero
    """
    if len(sys.argv) == 7:           #qui abbiamo il primo punto di ingresso della funzione main, detto "Entry point"; se il debugger non viene istruito con un json (solo x debug)
        a_value = float(sys.argv[1]) #allora ho solamente il nome dello script e non gli altri valori: se non istruito esegue da riga di comando l'istruzione 
        b_value = float(sys.argv[2]) #"python dicotomico.py" che nel mio caso presenta il nome "es02.py"; per dare qualcosa in ingresso, va istruito il debugger
        coeff_0 = float(sys.argv[3]) #andando a creare un file json, andando a customizzare il run, andando a scegliere la configurazione di debug di python
        coeff_1 = float(sys.argv[4]) #presentando una struttura di codice simile ad un "dizionario", formata da coppie, ossia l'elemento e la relativa attribuzione,
        coeff_2 = float(sys.argv[5]) #separate da una virgola.  In aggiunta a questo, si possono creare molteplici configurazioni all'interno del json, come ad esempio
        coeff_3 = float(sys.argv[6]) #quella nominale, quella dell'errore intervallo ecc., andando a ad aggiungere con copia+incolla della sezione nelle {} cambiando il nome
        x_value = find_zero(a_value, b_value, coeff_0, coeff_1, coeff_2, coeff_3)   #se passiamo i controlli iniziali, allora ricaviamo lo zero della funzione
        if (x_value != None):
            print(f"Lo zero è {x_value}")
        else:
            print("Zero non trovato")   #se non ricava lo zero forse siamo troppo stringenti con la soglia
    else:
        print("Numero di argomenti non corretto")
main() #come sempre occorre richiamare il main, ossia un caller che richiama la funzione, altrimenti entra in memoria senza che venga eseguita