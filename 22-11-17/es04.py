"""Animal"""
class Animal(object):
    # costruttore che istanzia un nuovo oggetto di default con il tab filling di VSC
    # def __init__(self) -> None:
    #     pass
    # costruttore che istanzia un nuovo oggetto animale
    # sulla base dell'inserimento del nome dello stesso
    def __init__(self, name):
        self._name = name
    
    def eat(self, food):
        print("{0} eats {1}".format(self._name, food))
        #print("%s eats %s")

class Dog(Animal):
    def fetch(self, thing):
        print("{0} goes after the {1}".format(self._name, thing))
    
    def show_affection(self):
        print("{0} wags tail".format(self._name))

class Cat(Animal):
    def swatstring(self):
        print("{0} shreds more string".format(self._name))

    def show_affection(self):
        print("{0} purrs".format(self._name))

d = Dog("Roger")
c = Cat("Fluffy")
#creo un istanza Dog che eredita dalla classe Animal l'attributo name con il
# self name; se digito d. e apro lo snippet a tendina delle possibili scelte
# ritrovo l'eat della classe Animal che trasferisce per eredita a d perche
# facente parte della classe Dog che eredita dalla classe Animal

d.fetch("paper") #richiama il fetch di dog ma attribuisce un nome dato tra parentesi
d.eat("dog food") #richiama il eat di animal ma attribuisce un nome dato tra parentesi
print("----------")
c.eat("cat food") #richiama il eat di animal ma attribuisce un nome dato tra parentesi
c.swatstring() #richiama la self di swatstring di cat

for a in (Dog("Rover"), Cat("Fluffy"), Cat("Lucky"), Dog("Scout")):
    # se una delle 2 show affection fosse stata assente
    # o la commentassimo ora, sarebbe andat in errore
    # perche uno dei 2 tra dog e cat non avrebbe una show_affection.
    # Inoltre qui stiamo creando un'istanza che non rimane in memoria
    # perche e' strettamente circoscritta al for, nasce, si sviluppa e muore li'
    a.show_affection()