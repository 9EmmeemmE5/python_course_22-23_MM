##
#   CICLI: square root Babilonia method
##

import sys

#TODO: chiedere all'utente il numero alpha>0

while True:
    alpha = float(input("inserisci un numero > 0"))
    if alpha > 0 :
        break
print(alpha)

x_new = None               #Xn+1
x_prev = alpha/2           #Xn che può essere arbitraria
delta = sys.float_info.max #occorre importare una libreria detta sys, per far in modo da poter richiamare il float positivo massimo rappresentabile dal calcolatore
reqired_precision = 0.001  #occorre impostare una req precision per andare ad impostare la condizione del while per non avere ==0 perche impossibile e non avere <0 perche ho gli abs()
iter_count = 0             #codifica del counter iterazioni

while delta > reqired_precision:
    x_new = 0.5*(x_prev + alpha/x_prev) #formula del metodo babilonese (ref:wiki radice quadrata): si genera un errore dato dalla divisione per un None, difatti tanto più tende alla radice, migliore sarà il risultato
    delta = abs(x_new-x_prev)
    x_prev = x_new #al giro successivo vado ad usare l' x_prev aggiornato
    iter_count+=1

print(f"La radice quadrata di {alpha} è {x_new:.3f}")
print(f"Test:{x_new**2}")