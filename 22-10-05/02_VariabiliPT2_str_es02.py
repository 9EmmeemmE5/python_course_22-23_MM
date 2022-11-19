###
# Parte 2 della seconda lezione sulle variabili: Stringhe
###

##from math import sin #from math import poi ctrl+space per richiamare i comandi contenuti in math che vengono presentati in un drop-down menu [log2 e' un esempio]
##from math import pi #attraverso hotfix proposta da VSC
import math
my_value = math.sin(math.pi) #importando la libreria math occorre anteporre la dicitura "math." prima della funzione

"""
la differenza tra le due metodologie e' che dalla prima io vado solamente a importare quello che serve, allora non ho bisogno di richamare il namespace;
nel secondo metodo si usa il namespace andando a richiamare tutto l'ambiente math, allora bisogna anteporre il "math."
"""
##
# 3°metodo: ALIAS
##

import math as mathlib # si va a creare un alias dell'ambiente math, ATETNZIONE alla lingua del linguaggio di programmazione, o si fa tutto in ITA o tutto in ENG
my_value = mathlib.sin(mathlib.pi) # invece che richiamare il namespace math., si richiama l'alias mathlib.