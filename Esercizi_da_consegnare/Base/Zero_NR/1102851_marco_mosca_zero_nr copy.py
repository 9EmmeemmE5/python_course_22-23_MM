##
# Calcolo dello zero di funzione con il metodo di Newton-Raphson
##

#TODO: calcolare lo zero di una funzione a piacimento, con metodo Newton-Raphson, dati due valori a e b definiti dall'utente
#TODO: definire la soglia di arresto e numero iterazioni massime
#TODO (Facoltativo): dare la possibilità di definire i coefficienti del polinomio

#! Considero un polinomio di terzo grado                                                        Polinomio di esempio f(x) = - 6.8 + 8.2x - 4.5x**2 + 2.5x**3 ;
#*                                                                                              ->                   f'(x)= 8.2 -9*x + 7.5x**2
#*                                                                                              ->                   x0 = 1.086003 come check

EPS_TH = float(input("Inserire un valore di tolleranza dell'algoritmo ..."))                    #intervallo di tolleranza dato dall'utente
MAX_ITER = float(input("Inserire il numero massimo di iterazioni dell'algoritmo ..."))          #numero massimo di iterazioni dell'algoritmo, dato dall'utente
coeff_0 = float(input("Termine noto..."))                                                       #coefficiente del termine noto
coeff_1 = float(input("Coefficiente del primo grado..."))                                       #coefficiente della x del primo grado
coeff_2 = float(input("Coefficiente del secondo grado..."))                                     #coefficiente della x del secondo grado
coeff_3 = float(input("Coefficiente del terzo grado..."))                                       #coefficiente della x del terzo grado

def f_poly (x_start):
    """Funzione polinomio di analisi con il metodo NR"""
    return coeff_3*x_start**3 + coeff_2*x_start**2 + coeff_1*x_start + coeff_0                  #c_3*x^3+c_2*x^2+c_1*x+c_0

def f1_poly (x_start):
    """Derivata prima della funzione di partenza"""
    coeffd_0 = 1*coeff_1                                                                        #coefficiente della x del primo grado derivata
    coeffd_1 = 2*coeff_2                                                                        #coefficiente della x del secondo grado derivata
    coeffd_2 = 3*coeff_3                                                                        #coefficiente della x del terzo grado derivata
    return coeffd_2*x_start**2 + coeffd_1*x_start + coeffd_0                                    # cd_2*x^2+cd_1*x+cd_0

def find_zero_nr(a_int_low, b_int_up, y_value, y1_value):
    """Funzione che implementa l'algoritmo di Newton Raphson per il calcolo dello zero di funzione"""                                                                           
    x_start = float(input("Inserire un valore di x di partenza interno all'intervallo ..."))    #valore di partenza della x, dato dall'utente
    
    #Controllo sugli estremi
    ya_value = f_poly(a_int_low)                                                                #variabile di appoggio della f(x=a)
    yb_value = f_poly(b_int_up)                                                                 #variabile di appoggio della f(x=b)
    if ya_value * yb_value > 0:
        print("Incoerenza degli estremi dell'intervallo in cui ricercare lo zero. \n Modificare i valori dell'intervallo...")
        return None
    iter = 0
    
    #Calcolo dello zero con NR
    while True:
        iter+=1                                                                                 #crescita di un'iterazione
        y_value = f_poly(x_start)                                                               #variabile di appoggio della f(x)
        y1_value = f1_poly(x_start)                                                             #variabile di appoggio della f'(x)
        x_new = x_start - y_value/y1_value                                                      #formula dell'algoritmo NR
        x_delta = abs(x_new - x_start)                                                          #delta tra la x calcolata e quella in ingresso
        
        #controllo sul numero di iterazioni
        if iter >= MAX_ITER:
            print(f"Numero massimo di iterazioni dell'algoritmo raggiunte, il risultato x0 = {x_new:.6f} \n non è convergente, aumentare il numero di iterazioni massime...")
            return x_new
        
        #uscita dall'algoritmo per raggiungimento massimo di iterazioni
        elif EPS_TH >= x_delta:
            print(f"Algoritmo terminato con {iter} iterazioni")
            return x_new
        x_start = x_new

def main():
    """Entry point"""
    a_int_low = float(input("Inserire il valore dell'estremo inferiore dell'intervallo a ...")) #estremo inferiore dell'intervallo in cui cercare lo zero
    b_int_up = float(input("Inserire il valore dell'estremo superiore dell'intervallo b ..."))  #estremo superiore dell'intervallo in cui cercare lo zero
    
    #controllo sui valori dell'intervallo
    if a_int_low >= b_int_up:
        print("Valori dell'intervallo irregolari, cambiare i valori...")
        return None
    
    x_0 = find_zero_nr(a_int_low, b_int_up, y_value = 0.0, y1_value = 0.0)
    
    #uscita dall'algoritmo se ho una x_0 appropriata
    if (x_0 != None):
            print(f"Algoritmo terminato per via della condizione delta < tolleranza, \nLo zero è {x_0:.6f}")
    else:
        print("Argomenti non corretti, zero non trovato")                                       #Input dati dall'utente non corretti
main()