
#TODO: calcolare lo zero di una funzione a piacimento, con metodo Newton-Raphson, dati due valori a e b definiti dall'utente andando a 
#TODO: definire la soglia di arresto e numero iterazioni massime

#! Polinomio di esempio f(x) = 2.5x**3 - 4.5x**2 + 8.2x - 6.8;
#*                      f'(x)= 7.5x**2 - 9x + 8.2

a_int_low = float(input("Inserire il valore dell'estremo inferiore dell'intervallo a ..."))
b_int_up = float(input("Inserire il valore dell'estremo superiore dell'intervallo b ..."))
x_start = float(input("Inserire un valore di x di partenza interno all'intervallo ..."))
tolleranza = float(input("Inserire un valore di tolleranza dell'algoritmo ..."))
max_iter = float(input("Inserire il numero massimo di iterazioni dell'algoritmo ..."))
iter = 0
controller = 1       #sentinel: se 1 continua, se 0 non continua

while a_int_low < b_int_up and iter < max_iter and controller !=0 : 
    iter+=1
    x_new = x_start - ((2.5*x_start**3 - 4.5*x_start**2 + 8.2*x_start - 6.8)/(7.5*x_start**2 - 9*x_start + 8.2))
    delta = abs(x_new - x_start)
    if delta < tolleranza:
        controller=0
        print("Programma terminato: delta < Tolleranza")
    x_start = x_new

print(f"lo zero della funzione è pari a {x_new:.6f} con {iter} iterazioni")