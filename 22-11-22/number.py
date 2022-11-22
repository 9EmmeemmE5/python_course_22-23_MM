"""Class to store a number (float)"""

class Number(): #eredita da object per assenza contenuto in parentesi
    def __init__(self, number=0.0):
        """method that creates the number"""
        self._number = number
#costruisco un oggetto di tipo number, che per essere inizializzato richiede un parametro di tipo number
    def getNumber(self):
        """methot that returns the number value"""
        return self._number
    def setNumber(self, number):
        """method that sets the number"""
        # self._number = number #!NO QUESTO NON VA ASSOLUTAMENTE FATTO PERCHE STO FACENDO UN PASSTHROUGH DELLA LOGICA BUCANDO LA PROTEZIONE _ E DO ALL'UTENTE LA LIBERTA' DI INSERIRE QUELLO CHE VUOLE
        # if(isinstance(number, float) or isinstance(number, int)): #poco efficiente quando devo fare un controlo dell'istanza su molti tipi
        if isinstance(number, (int, float)):
            self._number = float(number) #secondo la logica un intero viene convertito a float con il cast
        else:
            raise TypeError(f"Only float or int: you provided {type(number)}")
            #se dovessi richiamare un illecito, non posso farlo col try except ma con un Raise
# questa classe così fatta, in realtà, se qualcuno chiama setNumber, cosa si può passare dall'esterno, ma soprattutto c'è quelcosa che dall'esterno controlla che sia un numero?
    def __repr__(self) -> str:
        """"""
        return f"[{self._number}]"
    #con il repr vado a ... ed in debug console entra qui nel repr, restituendo la f.string 
    def __str__(self):
        """"""
        return f"[{self._number}]"
    #qui entro quando sono in terminale