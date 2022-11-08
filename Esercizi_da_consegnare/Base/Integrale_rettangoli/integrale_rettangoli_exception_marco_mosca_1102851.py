##
# Calcolo integrale con il metodo dei rettangoli
##

#TODO: calcolare l'integrale di una funzione a piacimento (mediante funzione), con metodo dei rettangoli, dati due valori a, b dell'intervallo ed M suddivisioni definiti dall'utente
#TODO: definire funzione che riceva in input la x e restituisca la f(x) a scelta, richiamata dalla funzione al punto precedente
#TODO (Facoltativo): dare la possibilità di definire i coefficienti del polinomio

#!Polinomio di esempio f(x) = - 6.8 + 8.2x - 4.5x**2 + 2.5x**3 

coeff_0 = float(input("Termine noto..."))                                                       #coefficiente del termine noto          #! test -6.8
coeff_1 = float(input("Coefficiente del primo grado..."))                                       #coefficiente della x del primo grado   #! test  8.2
coeff_2 = float(input("Coefficiente del secondo grado..."))                                     #coefficiente della x del secondo grado #! test -4.5
coeff_3 = float(input("Coefficiente del terzo grado..."))                                       #coefficiente della x del terzo grado   #! test  2.5
x_start = float(input("Inserire il valore iniziale della variabile x..."))

def f_poly (x_start):
    """Funzione polinomio di grado 3 c_3*x^3+c_2*x^2+c_1*x+c_0"""
    y_value = coeff_3*(x_start**3) + coeff_2*(x_start**2) + coeff_1*(x_start) + coeff_0         #variabile di appoggio della f(x)
    return y_value                                                                              #restituisco la f(x)

def calc_integrale_rett (a_int_low, b_int_up, m_div):
    """Funzione per il calcolo dell'integrale con il metodo dei rettangoli"""
    
    h_largh_div = (b_int_up-a_int_low)/m_div                                                    #! da test m_div=5 ->h_larg_int=3
    sub_int_est = []                                                                            #! lista che contiene gli estremi dei sottointervalli
    x_mid_sub_int = []                                                                          #! lista che contiene i punti medi degli estremi dei sottointervalli
    h_rect = []                                                                                 #! lista che contiene le altezze di ogni rettangolo
    sub_areas = []                                                                              #! lista che contiene i valori delle aree degli m rettangoli
    
    for i in range(0,m_div):
        sub_int_est.append([float((a_int_low+i*h_largh_div)), float((a_int_low+(i+1)*h_largh_div))])    #! append degli estremi dei sottointervalli come lista di lista
        x_mid_sub_int.append(sum(sub_int_est[i])/2)                                                     #! append dei punti medi nella relativa lista
        xm_value = x_mid_sub_int[i]
        ym_value = f_poly(xm_value)
        h_rect.append(ym_value)                                                                         #! append delle f(x_mid_i) AKA le altezze dei rett. al punto medio base
        sub_area = h_rect[i]*h_largh_div                                                                #! calcolo dell'area del rettangolo i-esimo
        sub_areas.append(sub_area)                                                                      #! append dei valori delle aree dei rettangoli i-esimi
    area_tot = sum(sub_areas)                                                                           #! calcolo dell'area sottesa per il calcolo integrale con i rett
    return area_tot

def main():
    """Entrypoint"""
    #controllo sui valori dell'intervallo
    while True:
        try:
            a_int_low = float(input("Inserire il valore dell'estremo inferiore dell'intervallo a ...")) #estremo inferiore dell'intervallo in cui cercare lo zero #! test -5
            b_int_up = float(input("Inserire il valore dell'estremo superiore dell'intervallo b ..."))  #estremo superiore dell'intervallo in cui cercare lo zero #! test 10
            if a_int_low >= b_int_up:
                break
        except Exception as ex:
            print(f"Valori dell'intervallo irregolari, cambiare i valori degli estremi (Estremo superiore >= Estremo inferiore) {ex}")
        #controllo sul numero di suddivisioni dell'intervallo
        try:
            m_div = int(input("Inserire il valore di suddivisioni dell'intervallo [a,b] ..."))          #suddivisioni dell'intervallo [a,b]                       #! test 5
            if m_div<= 1:
                break
        except Exception as ex:
            print(f"Suddivisione dell'intervallo irregolare, inserire un valore >1 {ex}")
    
    integrale_def_rett = calc_integrale_rett(a_int_low, b_int_up, m_div)
    
    #uscita dall'algoritmo se ho una soluzione appropriata
    if (integrale_def_rett != None):
            print(f"Algoritmo terminato, l'integrale è pari a {integrale_def_rett:.6f}")
    else:
        print("Argomenti non corretti, integrale non calcolato")                                       #Input dati dall'utente non corretti
main()