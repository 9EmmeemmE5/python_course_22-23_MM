##
#   Cicli
##

#TODO: Calcolare lo zero di una funzione: trovare un valore di x, xi, tale per cui f(xi)=0, con il metodo del dicotomico
"""
scegliere due punti A e B tali per cui f(A) ed f(B) siano uno >0 ed uno <0: si puo' dimostrare che se la funzione presenta 
un solo 0, allora e' possibile andare, iterativamente, a cercare la soluzione per approssimazioni successive, partendo ad esempio dal punto mediano,
ossia (B-A)/2 + A, andando a verificare il segno della funzione (positiva o negativa) sul punto mediano; se e' positivo ho un nuovo a, mentre se e' negativa
considero il nuovo a come nuovo b e, per approssimazioni successive, l'intervallo b-a diventa sempre più piccolo e, arrivati ad un valore accettabile,
abbiamo trovato lo 0 di funzione
Si usa un while perche continua fino a che non si e' arrivato al risultato desiderato, piuttosto che un for
"""

#creare la funzione matematica monovariabile...
#x^3 - 4*x^2 + 6*x - 24.5 = y e' la funzione da analizzare

#! NUOVO CONCETTO: FUNZIONE
#Prende in ingresso un qualcosa e restituisce qualcos'altro: python consente di creare delle funzioni ed ampliare, in base alle esigenze dell'utente, le funzioni disponibili

"""Dopo la definizione della funzione occorre sempre inserire la docstring con la tripla " per spiegare che cosa fa, fungendo da vera e propria documentazione"""

def my_poly(x_value = 0):                                                      #definisco la funzione con il def, che e' in blu scuro perche e' riservato per python
    """
    la funzione calcola il valore di un polinomio di 3° grado...
    """
    #return func_value = x_value ** 3 - 4 * x_value ** 2 + 6 * x_value - 24.5   #da errore solo con il return, che e' stato inserito perche non e' stato richiamato l'assegnamento, 
    #return x_value ** 3 - 4 * x_value ** 2 + 6 * x_value - 24.5                #quindi lui non ritorna la funzione di assegnamento, posso quindi cancellare func_value, oppure
    func_value = x_value ** 3 - 4 * x_value ** 2 + 6 * x_value - 24.5
    return func_value                                                           #definisco la func_value e poi faccio un return della func_value senza uguale a...

#! ho inserito un'assegnazione a x_value pari a 0.0 (l'integer non e' ammesso) col doppio "="

my_value = my_poly()                                          #non sto passando nulla alla mia funzione, OK, allora assegna il valore di default ossia lo 0.0 assegnato
print(my_value)                                              #printo con lo 0.0 di default
my_value = my_poly(float(input("inserisci il numero...")))   #qui sto codificando l'input castato dell'utente da assegnare al polinomio
print(my_value)                                              #printo con l'input dell'utente: se il numero e' grande la convergenza e' lenta

def second_degree_poly(x_value=0.0, coeff_0 = 0.0, coeff_1 = 0.0, coeff_2 =0.0):
    """
    return value of a second degree poly
    coeff_0 is the well-known term... coeff_0 + coeff_1 * x + coeff_2 * x ^ 2
    """
    return coeff_0+coeff_1*x_value+coeff_2*x_value**2       #nel caso avessi 100 coefficienti, posso usare un for andando a moltiplicare il coeff_0 ecc

print(second_degree_poly())
print(second_degree_poly(2, coeff_1=0, coeff_2=3))


def print_funny_message(msg = "****______****"):    #ho definito la funzione con la variabile "msg"
    print(msg)

my_value = my_poly()
print(my_value)
my_value = my_poly(float(input("inserisci il numero")))
print(my_value)

print_funny_message()
print_funny_message("pippo")