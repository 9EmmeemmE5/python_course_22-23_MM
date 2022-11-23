"""class to store a number"""

class Number():
    def __init__(self, number=0.0):
        """method that creates the number"""
        self._number = number
    def getNumber(self):
        """method that returns the number value"""
        return self._number
    def setNumber(self, number):
        """method that sets the numeber"""
        #if( isinstance(number, float) or isinstance(number, int)):
        if isinstance(number, (float,int)):
            self._number = float(number)
        else:
            raise TypeError(f"only float or int: you provided{type(number)}")
    def __repr__(self):
        return f"[{self._number}]"
    def __str__(self):
        return f"[{self._number}]"