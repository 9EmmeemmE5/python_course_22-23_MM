"""Calcolo integrale con il metodo dei rettangoli"""
#!Polinomio di esempio f(x) = - 6.8 + 8.2x - 4.5x**2 + 2.5x**3

coeff_0 = float(input("Termine noto..."))
coeff_1 = float(input("Coefficiente del 1° grado..."))
coeff_2 = float(input("Coefficiente del 2° grado..."))
coeff_3 = float(input("Coefficiente del 3° grado..."))
x_start = float(input("Valore iniziale della variabile x..."))

def f_poly (x_start):
    """Funzione polinomio di grado 3 c_3*x^3+c_2*x^2+c_1*x+c_0"""
    y_value = coeff_3*(x_start**3) + coeff_2*(x_start**2) + coeff_1*(x_start) + coeff_0
    return y_value

def calc_integrale_rett (a_int_low, b_int_up, m_div):
    """Funzione per il calcolo dell'integrale con il metodo dei rettangoli"""
    h_largh_div = (b_int_up-a_int_low)/m_div
    sub_int_est = []
    x_mid_sub_int = []
    h_rect = []
    sub_areas = []
    for i in range(0,m_div):
        sub_int_est.append([float((a_int_low+i*h_largh_div)), float((a_int_low+(i+1)*h_largh_div))])
        x_mid_sub_int.append(sum(sub_int_est[i])/2)
        xm_value = x_mid_sub_int[i]
        ym_value = f_poly(xm_value)
        h_rect.append(ym_value)
        sub_area = h_rect[i]*h_largh_div
        sub_areas.append(sub_area)
    area_tot = sum(sub_areas)
    return area_tot

def main():
    """Entrypoint"""
    a_int_low = float(input("Inserire il valore dell'estremo inferiore dell'intervallo a ..."))
    b_int_up = float(input("Inserire il valore dell'estremo superiore dell'intervallo b ..."))
    m_div = int(input("Inserire il valore di suddivisioni dell'intervallo [a,b] ..."))
    #controllo sui valori dell'intervallo
    if a_int_low >= b_int_up:
        print("Valori dell'intervallo irregolari, cambiare i valori degli estremi dell'intervallo.")
        return None
    #controllo sul numero di suddivisioni dell'intervallo
    if m_div<= 1:
        print("Suddivisione dell'intervallo irregolare, cambiare il valore delle suddivisioni.")
        return None
    integrale_def_rett = calc_integrale_rett(a_int_low, b_int_up, m_div)
    #uscita dall'algoritmo se ho una soluzione appropriata
    if integrale_def_rett is not None:
        print(f"Algoritmo terminato, l'integrale è pari a {integrale_def_rett:.6f}")
    else:
        print("Argomenti non corretti, integrale non calcolato")
main()
