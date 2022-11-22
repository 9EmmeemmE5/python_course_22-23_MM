"""Ereditarietà"""
# l=list([1,2,3,4])
#ho richiamato il costruttore, infatti con il type viene restituito "class"
# print(type(l))
#i metodi si dividono in 2 categorie: i getters, ossia quelli per reperire un metodo che ritorna un valore, in modo da proteggere l'accesso ai contributi in modo incontrollato
# i secondi sono i setters, ossia quelli che vanno a settare i valori dei vari metodi

#perche si usano? perche può capitare che esiste una logica di assegnamento che, se non richiamata con il metodo, può essere distrutta
#l'ereditarietà sarà molto usata con il modulo di testing "Unit Test"
#UML: la freccia del diagramma è diretta verso la superclasse, ossia al genitore.
# Il bello dell'ereditarietà è quello di andare a prendere i metodi delle classi superiori, andando anche a re-implementare dei metodi specifici
# se istanzio qulcosa creando un oggetto da una classe, se vado a controllare il tipo, quello di alto livello permettere di individuare il tipo da cui discerne il tipo di cui si sta eseguendo il comando tipo
# def__init__(self) è il costruttore ed ha lo scopo di inizializzare le variabili di istanza, inoltre la semantica "_" è di tipo privato, ossia non permette un accesso diretto
#se esistono n variabili di istanza, allora devono esistere n setter
#un metodo ha un contesto, che è la classe, mentre la funzione no; self fa riferimento all'oggetto stesso: se uso 2 oggetti come capisco cosa sto usando?
# lo faccio con il self, in modo da accedere a tutto ciò che è nostro, ossia a tutti gli attributi ed i metodi ad essi collegati

#tutta la logica del controllo non è esterno, ma bensi' interno alla classe

#in python ogni classe non dichiarata senza superclass estende una classe object, ossia la superclass built-in di python, in modo che tutto sia figlio di object, come list, dict, set ecc
# s=set([1,2,1,1,1])
# print(s)
#come fa python a stampare i contenuti di una lista? eredita una serie di metodi dalla classe object
#come è possibilie che una somma di liste è una list? quando ereditiamo da object, si eredita una serie di metodi dalla classe object che permettono di effettuare conversioni che ci permettono di operare con operazioni basilari
#eventuali nuove classi, specificate le varie relazionidi ereditarietà, object viene esteso con la classe, che a sua volta viene estesa con una sotto-classe
# l'override è simile alla sovrascrittura, andando quindi a cambiare il comportamento della classe a cui è applicato, andando anche ad aggiungere: una sub-class permette di andare ad eseguire un override del comportamento della classe genitore
#fare attenzione alla logica con cui si scrive il codice delle classi in python: si usa il CamelCase per le classi, mentre invece i metodi con la minuscola:
# class ChoiceQuestion(Question):
#     #The subclass has its own constructor.
#     def _ _init_ _(self) :
#         . . .
#     #This instance variable is added to the subclass.
#         self._choices = []
# #This method is added to the subclass
# def addChoice(self, choice, correct) :
# . . .
# #This method overrides a method from the superclass
# def void display(self) :
# . . .
#quando si ha un costruttore che ha una clase che eredita da un'altra, implicitamente accade che nel costruttore della sotto classe si ha un meccanismo diverso:
#si parte dal genitore, che al suo interno answer e question, inizializza il costruttore, quindi il costruttore della superclasse si richiama con il "super().__init__()", facendo riferimento alla costruzione della classe question, ossia la porzione di codice:
#CODICE SLIDE 8
#prima si esegue la chiamata, poi si procede (vedi syntax 10.2)
#!... manca parte di teoria
