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
    def __add__(self, other_num):
        if isinstance(other_num, (int, float)):
            return Number(self._number + other_num) #controllo isinstance per
        elif isinstance(other_num,Number): #non ci mette al sicuro da un'eccezione solo l'else
            return Number(self._number + other_num.getNumber()) #se faccio la somma di due oggetti occorre ritornare un oggetto dello stesso tipo (other num deve esserre compatibile con _number, che è un float, quindi deve essere float o int, quindi posso fare un isinstance oppure forzare con ._number ("other_number._number()"), oscurando il getter, altrimenti faccio other_num.getNumber(), quindi se esiste, apparterrà alla classe number e sarà soggetto al controllo di istance)
        else:
            raise TypeError (f"invalid type: you provided {type(other_num)}")
        # attenzione perche ritorno un float e non un Number, quindi occorre creare un nuovo numero agigungendo Number(...) con .. al posto del return, facendo ritornare un oggetto di tipo Number
        #come verifico la correttezza? vedi codice numero_test.py
    def __sub__(self, other_num):
        if isinstance(other_num, (int, float)):
            return Number(self._number - other_num) #controllo isinstance per
        elif isinstance(other_num,Number): #non ci mette al sicuro da un'eccezione solo l'else
            return Number(self._number - other_num.getNumber()) #se faccio la somma di due oggetti occorre ritornare un oggetto dello stesso tipo (other num deve esserre compatibile con _number, che è un float, quindi deve essere float o int, quindi posso fare un isinstance oppure forzare con ._number ("other_number._number()"), oscurando il getter, altrimenti faccio other_num.getNumber(), quindi se esiste, apparterrà alla classe number e sarà soggetto al controllo di istance)
        else:
            raise TypeError (f"invalid type: you provided {type(other_num)}")
    def __eq__(self, other_num):
        if isinstance(other_num, (int, float)):
            return Number(self._number - other_num) #controllo isinstance per
        elif isinstance(other_num,Number): #non ci mette al sicuro da un'eccezione solo l'else
            return Number(self._number - other_num.getNumber()) #se faccio la somma di due oggetti occorre ritornare un oggetto dello stesso tipo (other num deve esserre compatibile con _number, che è un float, quindi deve essere float o int, quindi posso fare un isinstance oppure forzare con ._number ("other_number._number()"), oscurando il getter, altrimenti faccio other_num.getNumber(), quindi se esiste, apparterrà alla classe number e sarà soggetto al controllo di istance)
        else:
            raise TypeError (f"invalid type: you provided {type(other_num)}")
    """...si può aggiungere tutti quelli che sono gli operatori logici come la moltiplicazione, la divisione ecc.."""
    def __repr__(self) -> str:
        """representation in debug environment definition"""
        return f"[{self._number}]"
    #con il repr vado a convertire l'oggetto in stringa in debug console: entra qui nel repr, restituendo la f.string 
    def __str__(self):
        """representation in terminal environment definition"""
        return f"[{self._number}]"
    #qui entro quando sono in terminale
"""Nuova lezione del 23-11-22 da qui"""

class ComplexNumber(Number): #estensione della classe genitore Number con la sub-class dei numeri complessi
    def __init__(self, realPart=0.0, imgPart=0.0): #aggiungo la parte reale e quella complessa come obbligatorie
        #per sfruttare quello che ho già fatto cosa posso fare per aggiungere? se inserisco il super invoco il costruttore della super class, ma se estendo number già ho una parte del numero compresa, ossia la parte reale
        super().__init__(realPart) #ho scelto di richiamare la parte reale, inizializzando il costruttore della superclass, cui sottoclasse necessita della parte complessa da aggiungere
        self._imgPart = imgPart #ho aggiunto la parte complessa ed ora manca la parte di getters e setters
    def getRealPart(self): #costruisco il metodo della parte reale
        """method that returns the real part of the commplex number"""
        return self.getNumber() #posso fare sia questo, ossia richiamo il metodo get della parte reale oppure posso fare anche il self._number, quello messo qui fa rif a quello che sta nel genitore e li richiama per eredità
    def getImgPart(self):
        """method that returns the img part of the commplex number"""
        return self._imgPart
    # def getValue(self):#non relazionata al complelsso ma per scopi didattici va bene
    #     return self._number
    def getValue(self, part): #può capitare di richiamare 2 metodi con lo stesso nome ma che richiedono argomenti diversi, quindi occorre prendere quella più completa di definizione, altrimenti si ha un errore di non unicità
        if part=="real":
            return self._number
        elif part=="img":
            return self._imgPart
        else:
            raise ValueError ("invalid input: only real or img")

    def getSignSymbol(self):
        if(self._imgPart<0):
            return "-" #compare il -- quindi in maniera meno elegante posso eliminarlo qui
        else:
            return "+"

    def __add__(self, other_num):
        """method that returns the complex number as a + b"""
        if isinstance(other_num, ComplexNumber): #se othernum è verificato come complesso, allora
            return ComplexNumber( self._number + other_num, self._imgPart + other_num.imgPart )# devo passare la parte reale e quella img
        else:
            raise TypeError ("a complex number should be added with another complex number...")
    def __str__(self):
        return f"{self._number}{self.getSignSymbol()}{self._imgPart}i"
    def __repr__(self):
        return f"{self._number}{self.getSignSymbol()}{abs(self._imgPart)}i"#compare il -- quindi in maniera elegante posso eliminarlo qui con l'abs()