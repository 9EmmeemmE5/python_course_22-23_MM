"""Class and methods 4: datetime"""
class Date(object):
    #object puo' essere omesso, ma ci permette di richiamare il self
    def __init__(self):
        self._data = "01-01-1970"
    
    # def __init__(self,date):
        # self._data = date       
        # quando creo oggetto Date vuoto, richiama il 01-01-1970, 
        # mentre se inserisco la data odierna ad esempio, 
        # allora sto facendo override, ossia sovrascrivo 
        # con il vlaore che ho inserito tra le parentese dell'oggetto
        # Date
    def get_date(self):
        self._data = "17-11-2022"
        return self._data

class Time(Date):
    def __init__(self):
        self._time = "00:00:00"

    def get_time(self):
        self._time = "15:30:00"
        return self._time

tm = Time() 
# creo un oggetto di tipo tempo, un'istanza di Time, richiamando il costruttore:
# quindi si va a richiamare l'init di Time, ma Time eredita da Date, quindi 
# viene richiamato anche il costruttore di Date, quindi l'init Date
print(f"{tm.get_date} + {tm.get_time}")