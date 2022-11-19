##
# Gestione di scelte multiple
##

"""
utente deve inserire la magnitude
"""
magnitude = float(input("Inserire la magnitudo M ")) #casting in float della stringa che inserisce l'utente

if (magnitude < 4.5):
    print("No Damage")
elif magnitude < 6 :
    print("Low Damage")
elif magnitude < 7:
    print("Medium damage")
elif magnitude < 8:
    print("High damage")
else:
    print("Ultra high damage")
"""
# ! l'else if non viene considerato da python in quanto viene modellato dall'interprete come elif, per questo motivo occorre codificare come elif
# ! risultando molto più forte dell'else; se venisse codificato come una serie di if, non riuscirebbe a ricadere nel ramo corretto, in quanto il primo in 
# ! cui entra la decisione prende il controllo, 
# * mentre nell'elif si hanno opzioni alternative con cui la decisione si va ad escludere.
# * Nell'ultima si mette else, perche se tutte le altre sono state escluse: avrei potuto avere sia high damage che ultra high damage se ci fosse stato un elif.

# * Si sta codificando una sorta di Switch-case: una sorta di interruttore che, sulla base di una variabile, considera diverse casistiche basate su un valore,
# * del tipo o caso 1, o caso 2, o caso 3 o caso 4, e, se nessuna delle condizioni e' verificata si va a considerare il caso di default da valutare.

# * switch(var){
# *     case 0
# *     case 5
# *     case 7
# *     default case
# * }

Re/factor: piuttosto che scrivere il codice come appena fatto sopra, fuori dal commento multi/line, e' possibile impostare delle soglie o Threshold, come 
scritto sotto
"""

THRESH_NO_DMG = 4.5
THRESH_LO_DMG = 6
THRESH_MID_DMG = 7
THRESH_HI_DMG = 8

magnitudo = float(input("Inserire la magnitudo ")) #casting in float della stringa che inserisce l'utente

if (magnitudo < THRESH_NO_DMG):
    print(f"No Damage; we are under the {THRESH_NO_DMG} magnitude")
elif magnitudo < THRESH_LO_DMG :
    print(f"Low Damage; we are between the {THRESH_NO_DMG} and {THRESH_LO_DMG} magnitude")
elif magnitudo< THRESH_MID_DMG:
    print(f"Medium Damage; we are between the {THRESH_LO_DMG} and {THRESH_MID_DMG} magnitude")
elif magnitudo < THRESH_HI_DMG:
    print(f"High Damage; we are between the {THRESH_MID_DMG} and {THRESH_HI_DMG} magnitude")
else:
    print(f"Ultra high damage; we are above the {THRESH_HI_DMG} magnitude")
"""
# * A riprova della scelta fatta codificado con l'elif, se si esegue con debug inserendo un breakpoint alla prima riga dell'if-block, inserendo un valore,
# * il debugger chiede di proseguire con le istruzioni finche non si verifica la condizione che si e' scritta, inoltre, se fosse stata codificata come una serie
# * di if e fosse stato inserito un valore di magnitudo pari o maggiore di 8.1, allora sarebbe stato printato ogni messaggio impostato per ogni condizione

# * Nel caso si volesse scrivere un range come in matematica, in questo caso della prima soglia tra 4.5 e 5.99, in python e' possibile scrivere anche
# * 4.5 <= magnitude < 5.99 ; alternativamente posso usare l'AND:
# * magnitude >= THRESH_NO_DMG 
# ! AND
# * magnitude <= THRESH_LO_DMG
"""
