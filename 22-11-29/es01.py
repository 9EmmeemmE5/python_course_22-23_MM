"""lambda function"""

# square_func = lambda x : x**2
# square_func(4)
# print(square_func)

# close_enough = lambda x, y : abs(x-y)<3
# close_enough(2, 4)
# print(close_enough)
#printano con l'indirizzo

def add (x, y):
    return x + y
# creo la funzione add
print(add(2,4))
#richiamo la funzione matchando 2 alla x e 4 alla y

#con la lambda function io posso richiamarla anche solamente dentro al print, piuttosto che nel caso scritto sopra dove la funzione è richiamabile in ogni punto del programma

add = lambda x,y: x+y
print(str(add(2,4))) #per evitare che venga stampato a mo di indirizzo, occorre effettuare il cast a str

def get_func(n):
    return lambda x : x * n + x % n

my_func=get_func(13)
my_func(4)

a=[3,4,6,8,7,1,9]
b=[2,3,7,6,-1,2,4]
c=[1,5,6,8,78,-45,-16]
# date due liste voglio una lista che sia formata da elementi dati dalla somma degli elementi delle liste a e b, quindi un append
# se volessi una somma come se fossero due vettori, occorre ciclare con un for

result = []
for i in range (0,len(a)):
    result.append(a[i]+b[i])

add = lambda x,y: x+y
print(add(a,b))
print(result)

#per effettuare il refactor con il map, mappo la funzione, inserisco le varibili necessarie della funzione e non necessito più del ciclo for
print(list(map(lambda x,y,z: 2*x+2.5*y+0.5*z, a,b,c)))
#se volessi aggiungere un altra lista posso ad esempio inserire una lambda function embedded che prende anche la variabile z corrispondente a c

my_dict = [{'name':'Marco', 'points': '27'},{'name':'Giorgio', 'points': 19}]
print(list(map(lambda x: x['name'], my_dict))) #eseguo un map ad una sola entrata (x), a cui viene attribuita la key 'name' dell'elemento singolo ma ITERABILE, che viene passato alla lambda function
print(list(map(lambda x: x['points']*10, my_dict))) #come sopra ma se non tolgo le quotes allora esegue la concatenazione di stringhe quindi 10vv 27 e 10vv 19, se le tolgo esegue 27*10 e 19*10
