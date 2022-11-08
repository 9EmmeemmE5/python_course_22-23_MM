##
# Chiedere un numero mediante input
# Effettuare il calcolo di un abs
# stampare il risultato
##

my_string = input("inserisci un numero")
my_num = int(my_string) # casting
my_abs_value = abs(my_num) #calcolo dell'abs
print(my_abs_value) ##

# efactor
print(abs(int(input("inserisci un numero")))) # posso scrivere il codice scritto in precedenza con 4 righe in un unica riga

"""
per testare la funzione abs occorre darle in pasto casi borderline, come un positivo, negativo, zero e qualcosa che non è un 
numero per vedere se si genera un'eccezione
"""