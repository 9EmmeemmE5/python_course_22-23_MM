"""Calcolo dello zero di funzione con il metodo di Newton-Raphson"""
EPS_TH = float(input("Inserire un valore di tolleranza dell'algoritmo ..."))
MAX_ITER = float(input("Inserire il numero massimo di iterazioni dell'algoritmo ..."))
coeff_0 = float(input("Termine noto..."))
coeff_1 = float(input("Coefficiente 1° grado..."))
coeff_2 = float(input("Coefficiente 2° grado..."))
coeff_3 = float(input("Coefficiente 3° grado..."))

def f_poly (x_start):
    """Funzione polinomio di analisi con il metodo NR"""
    return coeff_3*x_start**3 + coeff_2*x_start**2 + coeff_1*x_start + coeff_0

def f1_poly (x_start):
    """Derivata prima della funzione di partenza"""
    coeffd_0 = 1*coeff_1
    coeffd_1 = 2*coeff_2
    coeffd_2 = 3*coeff_3
    return coeffd_2*x_start**2 + coeffd_1*x_start + coeffd_0

def find_zero_nr(a_int_low, b_int_up, y_value, y1_value):
    """Funzione che implementa l'algoritmo di Newton Raphson per definire lo zero di funzione"""
    x_start = float(input("Inserire un valore di x di partenza interno all'intervallo ..."))
        #Controllo sugli estremi
    ya_value = f_poly(a_int_low)
    yb_value = f_poly(b_int_up)
    if ya_value * yb_value > 0:
        print("Incoerenza degli estremi. \n Modificare i valori dell'intervallo...")
        return None
    iter = 0
    #Calcolo dello zero con NR
    while True:
        iter+=1
        y_value = f_poly(x_start)
        y1_value = f1_poly(x_start)
        x_new = x_start - y_value/y1_value
        x_delta = abs(x_new - x_start)
        #controllo sul numero di iterazioni
        if iter >= MAX_ITER:
            print(f"x0 = {x_new:.6f} \n non convergente, aumentare n° iterazioni massime")
            return x_new
        #uscita dall'algoritmo per raggiungimento massimo di iterazioni
        if EPS_TH >= x_delta:
            print(f"Algoritmo terminato con {iter} iterazioni")
            return x_new
        x_start = x_new

def main():
    """Entry point"""
    a_int_low = float(input("Inserire il valore dell'estremo inferiore dell'intervallo a ..."))
    b_int_up = float(input("Inserire il valore dell'estremo superiore dell'intervallo b ..."))
    #controllo sui valori dell'intervallo
    if a_int_low >= b_int_up:
        print("Valori dell'intervallo irregolari, cambiare i valori...")
        return None
    x_0 = find_zero_nr(a_int_low, b_int_up, y_value = 0.0, y1_value = 0.0)
    #uscita dall'algoritmo se ho una x_0 appropriata
    if x_0 is not None:
        print(f"Algoritmo terminato, condizione delta<tolleranza verificata,\nLo zero è {x_0:.6f}")
    print("Argomenti non corretti, zero non trovato")
main()
