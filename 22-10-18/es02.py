##
# sys.argv
##
# adder(a) --> return a + bias
import sys
BIAS=0

def adder(my_value):
    """function that add bias to input"""
    return my_value + BIAS
def dummy():
    """dummy funct - increment bias"""
    global BIAS
    BIAS+=1.0
def main():
    print(sys.argv)
    print(adder(4.0))
    print(adder(4.0))
    dummy()
    print(adder(4.0))
    x = 3
    print(adder(x))
main()
"""
il sys.argv e' la lista di comandi mandati al nostro script, dove in sys.argv[0], 0 e' il nome del nostro script; questo implica che si possono mandare dei comandi in ingrersso
al nostro script come se fosse una vera e propria lista di comandi
"""