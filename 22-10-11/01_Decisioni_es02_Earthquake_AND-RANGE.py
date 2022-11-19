##
# Gestione di scelte multiple con AND
##

#* Utente deve inserire la magnitude

#  TODO: inserire le soglie

THRESH_NO_DMG = 4.5
THRESH_LO_DMG = 6
THRESH_MID_DMG = 7
THRESH_HI_DMG = 8

magnitude = float(input("Inserire la magnitudo M ")) #casting in float della stringa che inserisce l'utente

if magnitude < THRESH_NO_DMG:
    print("No damage")
elif magnitude >= THRESH_NO_DMG and magnitude < THRESH_LO_DMG:
    print("Low damage")
elif magnitude >= THRESH_LO_DMG and magnitude <= THRESH_MID_DMG:
    print("Medium damage")
elif magnitude >= THRESH_MID_DMG and magnitude <= THRESH_HI_DMG:
    print("High damage")
else: 
    print("Ultra high damage")
"""
#! il codice comincia a divenire complesso, quindi occorre orre particolare attenzione al codice e alle relative soglie, in quanto, per quanto intuitivo
#! puo' indurre in errore

#* non esistono limiti agli AND: A and B and C, che e' vera se sono tutte e 3 vere, mentre nel caso in cui ci sia anche solo 1 falso, allora risulta essere 
#* falsa, cosi' come se lo sono tutti e 3

#* L'operatore NOT inverte tra vero e falso, mentre il =! e' l'operatore di diseguaglianza, inoltre fare attenzione alla priorita' con le parentesi ()
#* L'operatore OR
# TODO: aggiungere la parte teorica dell'operatore OR

Le condizioni vengono prese in considerazione da sinistra a destra e, nel caso dell'and, se anche una soltanto non e' verificata, il circuito di valutazione
si stoppa, quindi si va ad effettuare una valutazione in corto-circuito laddove possivile, ossia si impone come condizione di valutazione, ad esempio un
falso e, nel caso sia verificato all'inizio, allora stoppo gia' sul nascere il circuito di valutazione.
"""
