"""Variabili"""

a1="pippo" 
# assegno ad una variabile di nome "a1" la str "pippo"
# 1a="pippo" è un errore perché non posso iniziare una variabile con un numero
# -var1="pippo" è un errore perché non posso iniziare una variabile con un operatore

EARTH_RADIUS = 6300
# in maiuscolo si scrivono variabili legate a valori che sono costanti

Speed_rpm = 3000
speed_rpm = 3000

# è buona norma iniziare la digitazione di una variabile con una lettera minuscola
# e non con una maiuscola
# è buona cosa digitare in snake case typing con l'underscore

my_number = 1
type(my_number)
# imposto la variabile my number# come un int o float o una str;
# se nasce come float al massimo conterrà un int
# e non una str e ciò non ha alcun senso logico;
# inoltre, grazie al runtime di python non devo definire ad esempio la variabile
# a come intero prima di farle assumere valore come nel linguaggio C

my_number = 4.4 
# reimposto il valore della variabila come float

my_number = 4.4 + 1 
# eseguo l'addizione di un int 1 alla variabile e riottengo il float perché vince il float sull'int

my_number +=1 
# la funzione type restituisce la classe relativa a cosa è
# memorizzato in memoria in termini di variabile, 
# operazione analoga a quella della riga superiore:
# occorre applicare prima dell'uguale l'operatore che deve agire sulla
# variabile alla quale viene aggiunto/sottratto/moltiplicato...
# il valore che viene digitato dopo

power_of = 5 ** 2 
# l'elevazione a potenza con esponente "n" si esegue con
# un doppio operatore di moltiplicazione; per la radice quadrata basta elevare a 0.5

div_int = 5 // 2
# con un doppio operatore "//" si riesce ad eseguire una divisione intera,
# andando a forzare il tipo di destinazione come intero e non come float
# se si dividono interi, altrimenti, dividendo float il type sarà float

resto_div = 5 % 2
# con il simbolo "%" si esegue l'operatore modulo per andare a restituire
# il resto della divisione, per individuare numeri pari e dispari

div_std = 5 / 2
# restituisce un float ed è la divisione normale

r_shifting = 8 >> 2 
# operazione di shift right di 2 ossia 8/(2**2)=4

l_shifting = 8 << 2 
#operazione di shift left di 2 ossia 8*(2**2)=32

# lo shift è più efficiente della moltiplicazione/divisione per 2 perché
# basta un colpo di clock mentre invece con gli operatori normali si va 
# a perdere molto più tempo, aumentando notevolemnte le inefficienze

my_condition = 5 > 3 
# operazione logica che restituisce True o False

type(my_condition) 
# restituisce una nuova classe di python, che è il "bool" ossia è un booleano

my_condition 
# restituisce True -> ATTENZIONE: non bisogna usare come nome di variabile una parola
# come True o False, dato che viene utilizzata dall'interprete 
