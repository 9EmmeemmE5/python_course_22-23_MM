"""Class to model 2D point"""
import unittest

class Point():
    def __init__(self, x=0.0, y=0.0):
        self._x=x
        self._y=y
    def setX(self, x):
        self._x=x
    def setY(self, y):
        self._y=y
    def getX(self):
        return self._x
    def getY(self):
        return self._y
    def __add__(self, other_point): #metodo addizione tra punti
        if isinstance(other_point, Point):
            return Point(self._x+other_point._x, self._y+other_point._y)
        else:
            raise TypeError()
    def __sub__(self, other_point): #metodo sottrazione tra punti
        if isinstance(other_point, Point):
            return Point(self._x-other_point._x, self._y-other_point._y)
        else:
            raise TypeError()
    def __str__(self):
        """representation of object in terminal environment method definition"""
        return f"[{self._x};{self._y}]" #ritorna la rappresentazione in ogni richiamo del punto per i print
    def __repr__(self):
        """representation of object in debug console environment method definitio"""
        return f"[{self._x};{self._y}]"

class PointTest(unittest.TestCase):
    def test_x_y_value(self):
        print("testing x and y values...")
        my_point= Point(3.0,4.0)
        self.assertEqual(my_point.getX(),3.0)
        self.assertEqual(my_point.getY(),4.0)
    def test_add_points(self):
        print("testing x and y values...")
        my_point_a= Point(3.0,4.0)
        my_point_b= Point(3.0,4.0)
        my_point_c=my_point_a+my_point_b
        self.assertIsInstance(my_point_c, Point)
        self.assertEqual(my_point_c.getX(),6.0)
        self.assertEqual(my_point_c.getY(),8.0)
        # self.assertTupleEqual((my_point_c.getX,my_point_c.getY),(6.0,8.0)) #meno leggibile
    #essendoci un raise devo testarlo, quindi occorre stimolare l'errore del raise, il caso deve mandare il codice in errore
    def test_add_exception(self):
        my_point_a = Point(3.0,4.0)
        with self.assertRaises(TypeError):
            my_point_b = my_point_a + 4.0 #codice che sollecita la TypeError

if __name__=="__main__": #variabile che python inizializza per noi, di cui noi non abbiamo controllo; se inserisco un bkpoint ed eseguo con debug noto che la variabile __name__ è main: ciò significa che viene impostata a main se e solo se viene messo in esecuzione questo script in maniera diretta, quindi significa che ho lanciato direttamente point.py
    print("Sono stato invocato direttamente")
    #TEST CON APPROCCIO ESTERNO AL FRAMEWORK
    unittest.main()
    #TEST NON OTTIMIZZATO - CASERECCIO
    #test..
    p1=Point(2.0,3.0)
    p2=Point(4.0,5.0)
    p3=p1+p2
    if isinstance(p3, Point) and p3.getX()==(p2.getX()+p1.getX()) and \
        p3.getY()==(p2.getY()+p1.getY()): #per testare che p3 sia un punto occorre verificare l'appartenenza all'oggetto Point e che la x e la y di p3 siano, come attributi dell'oggetto, derivanti da operazioni sugli stessi attributi degli oggeti usati per il test
        print("Test OK")
    else:
        print("Test KO")
else:
    print("Sono stato importato da qualcuno")