"""Questa e' la docstring del titolo (causa linting)"""
#Questo e' un commento
"""
doc string: ci dice come utilizzare qualcosa, funge da documentazione e si formatta
con 3x double quote
"""
print("ciao", sep="|",end=".")
# print(""): di default si ha lo spazio come separatore delle variabili e come end 
# si ha il frontslashN "\n"

print("ciao", "pippo",sep="|",\
    end=".")
# per andare a capo mentre si sta scrivendo un argomento tra parentesi si usa il \
    
print("ciao","5",5) 
# 5 sotto forma di stringa e' tale, mentre se non viene scritto con le double quote
# e' un numero e viene gestito in maniera dirfferente dalla stringa, ossia come numero

print("ciao"+" Emme") 
# sommare una stringa implica concatenare le stringhe che vengono sommate,
# andando a creare una nuova stringa che concatena le stringhe addendo

# print("la somma di 3+2 e' "+5)
# la riga presenta un errore dato dal fatto che si possono concatenare
# solamente stringhe e non stringhe e numeri, difatti il terminale presenta
# il seguente errore

# TypeError: can only concatenate str (not "int") to str,
# in quanto tale e' un'eccezione che va a stoppare l'interruzione del nostro programma,
# indicando la localizzazione dell'errore "line 12, in <module>";
# per questo motivo non si possono concatenare numeri e stringhe

# In merito alle eccezioni, esiste un costrutto che e' presente in molti linguaggi
# di programmazione, chiamato "try except" che va a non considerare l'eccezione del runtime
# print("la somma di 3+2 e' "+str(5)) dalla documentazione, usando il costruttore str()
# si va a convertire l'argomento, che in questo caso e' un numero, in stringa
# OT: a sx si e' inserito un punto di interruzione o "Breakpoint",
# i.e. un punto in cui si spera che il programma si fermi.
# le operazioni che sono ammesse sono S(stringa)+S, S+str(I(intero))

print("3"+"2")
#il risultato e' una stringa che restituisce "32"# quindi occorre convertirlo in int o float

print(int("3")+int(2)) 
# nel caso si vada ad inserire la [] allora implica che l'argomento risulta essere
# di tipo opzionale, inoltre esiste una seconda modalita' con cui posso portare la x
# in un'altra base

print(int("3")+int(2)) 
#CASTING: passaggio da un intero ad una stringa o da un tipo ad un altro,
# come da un intero ad un float, o da un float ad una stringa