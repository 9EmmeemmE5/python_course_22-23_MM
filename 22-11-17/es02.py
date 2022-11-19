"""class and methods 3"""
##HIDE
## 
#  This program tests the CashRegister class.
#
#!deve esistere il metodo, quindi occorre creare sempre il file py del metodo 
#! e va messo nella stessa cartella(?)
from cashregister import CashRegister

register1 = CashRegister()
register1.addItem(1.95)
register1.addItem(0.95)
register1.addItem(2.50)
print(register1.getCount())
print("Expected: 3")
#sono io user che mi aspetto che ci sia 3, se ritorna un valore diverso non va bene
#quindi con la classe "unittest" ossia un tester program
print("%.2f" % register1.getTotal())
print("Expected: 5.40")

#i pattern sono gia' dei codici che sono scritti secondo una determinata struttura