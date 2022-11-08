##
# Cicli 2 - esclusione comportamenti input utente
##

#TODO: Chiedere all'utente di inserire un numero positivo float; se negativo richiedere nuovamente all'utente e stampare il numero inserito

while True:
    my_number = float(input("inserisci un numero > 0"))
    if my_number > 0 :
        break
print(my_number)

"""
ci consente di richiedere di far qualcosa fintanto che non si è soddisfatti di una certa condizione, facendoo con un while true, mentre con una variabile
il discorso è differente rispetto al precedente, in quanto si utilizza una variabile sentinella che flagga le incongruenze: in questo caso si imposta la sentinel come True, quindi
per uscire dal while, ossia per andare in break, occorre invalidare la condizione my_flag che è vera e quindi fa girare il while, andando ad impostare un if my_number > 0, allora
my_flag passa da True a False e quindi ho il break del loop
"""
my_flag = True #variabile sentinella
while my_flag:
    my_number = float(input("inserisci un numero > 0"))
    if my_number > 0 :
        my_flag = False #occorre invalidare la condizione che, se rimanesse su True, continuerebbe ad iterare, quindi, invalidandola con il false nella 
print(my_number)        #condizione di break del while, si esce ed il ciclo si conclude