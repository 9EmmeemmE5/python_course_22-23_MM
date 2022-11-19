###
# Decisioni
###

"""
Decisioni: se si verifica una condizione, allora esegui una data scelta, come un vero e proprio bivio, che puo' condurre ad un sotto-bivio e cosi' via, con la
speranza che poi alla fine si ricongiunga tutto in un unico punto finale.
Un determinato percorso, con le relative scelte possibili di livello inferiore e cosi' via, si definisce "Branch" o ramo
La variabile "if" ha solo 2 valori di verita', che possono essere o vero "True" o "False".
Possiamo avere anche delle logiche di altro tipo, codsiddette come "crispy" o spinose, come le logiche "Fuzzy" od offuscate, come nel caso:

if(temp>37.5) restituisce un analisi con assegnazione di decisione parziale, in quanto se avessi 37.6 avrei una data decisione, 
se avessi 37.8 un'altra, 37.7 un'altra ancora e cosi' via.

Lo scopo finale e' che i "decision makers" siano ... [integrare 16:04 (orario)]

Nel corso verranno usati: "if", "else", "elif" che e' una troncatura dell'"else if"

In python le parole chiavi riservate if ed else non possono assumere valori come una normale variaibile, in quanto riservate
"""
#chiedere all'utente di inserire un numero 
#se il numero e' divisibile per due, stampare e' pari
#se il numero e' pari ed e' minore di 10, stampare che il numero e' minore di 10
#altrimenti stampare e' dispari

my_num = float(input("inserisci un numero"))

if my_num % 2 == 0:
    print(f"il numero {my_num} e' pari")
    if my_num <10:
        print(f"il numero {my_num} e' minore di 10")
        if (my_num>100):  #porzione di codice non raggiungibile, ossia errore sintattico e semantico, perche il codice esegue
            print("bravo") #porzione di codice non raggiungibile, ma non raggiunge questa programmazione
else:
    print(f"il numero {my_num} e' dispari")
    