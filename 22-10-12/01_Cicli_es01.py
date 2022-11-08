##
#   CICLI
##

#TODO dalle slides: codifica un ciclo while per il calcolo del bilancio con un tasso di interesse

#balance = 10.0
#target = 100.0
#year = 0
#rate = 0.025

#while balance < target:
#    year += 1
#    interest = balance * (rate/100)
#    balance = balance + interest
#    print(f"il nuovo bilancio all'anno {year} è pari a {balance}")

#TODO: codifica un ciclo while per il calcolo del bilancio con un tasso di interesse
#* Chiedere all'utente il capitale iniziale 
#* Chiedere all'utente il tasso di interesse
#* Chiedere all'utente il capitale target
#* Calcolare per ogni anno il nuovo capitale ed uscire se il target viene raggiunto
#* Uscire dal ciclo se si raggiunge il numero massimo di anni

MAX_YEARS = 12

amount_t0 = float(input("Inserire il capitale iniziale"))
growing_rate = float(input("inserire il tasso di interesse"))
amount_target = float(input("Inserire il capitale target"))
years = 0 #variabile counter che tiene conto ddegli anni che passano
amount_actual = amount_t0 #tiene traccia dell'evoluzione del capitale nel tempo

while amount_actual < amount_target and years < MAX_YEARS:
    years += 1
    amount_actual = amount_actual * (1 + growing_rate)          #possibile editare il breakpoint: ad esempio yrs == 5, il breakpoint si modifica al count 5, divenendo 
print(f"il capitale dopo {years} anni è: {amount_actual:.2f}")  #un conditional bkpointfacendo iterare il ciclo while, a meno di breakpoint standard messi prima, fino al 5° conteggio

#TODO: vedi sopra ma con variabile if ed il breakpoint

while amount_actual < amount_target:
    if(years > MAX_YEARS):      #! attenzione a dove si mettono le istruzioni di break, perche se fosse stato messo sotto dopo amount_actual, allora avrebbe fatto il 13° giro
        break
    years += 1
    amount_actual = amount_actual * (1 + growing_rate)  
print(f"il capitale dopo {years} anni è: {amount_actual:.2f}")