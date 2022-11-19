"""Insiemi e dizionari"""
#Gli insiemi non sono del tutto uguali alle liste, cosi' come i dizionari, in quanto rispndono ad una logica del tipo chiave-valore
#Le API permettono di operare in remoto sulla base di chiamate effettuate dallo user che, sulla base del get json, con il formato
#del dizionario, ossia una chiave, che e' il valore di sinistra della struttura dati, la quale presenta un determinato valore univoco,
#di fatti non possono esserci ambiguita' in termini di valori all'interno del dizionario.

#Esistono dei metodi che nelle liste permettono di operare sulle stesse, come l'append o il pop ecc., che possiamo trovare, sotto altre
#diciture, per i dizionari, in modo da poter operare con gli stessi.
#Esiste una forte correlazione con la struttura json ed il python e non a caso, proprio per l'utilizzo con il suddetto codice.
#Esiste anche la possibilita' di concatenare i valori e le chiavi, andando a creare delle sottostrutture di chiavi e valori che possono
#trovarsi a livelli inferiori, come se fossero degli indent e dei de-indent per ogni discesa/salita di livello delle chiavi.

#Si ha la possibilita' di concatenare dentro una chiave di primo livello una lista di chiavi di secondo livello, impostando come valore
#della chiave di primo livello una lista di chiavi

#Non esiste una relazione d'ordine all'interno di un insieme, inoltre non possono esistere duplicati all'interno dello stesso insieme
#pposso pero' effetturare le operazioni classiche sugli insiemi, come nella matematica, ma la differenza con il dizionario e' l'assenza
#della chiave, ma la sola presenza del valore

#! START ESERCIZIO QUI

def main():
    my_set = {"Adriano", "Marco", "zero"}
    print(my_set)
    print(len(my_set))
    # print(my_set[0])    #non esiste una relazione d'ordine non posso richaimare un dato valore, quindi non posso richiamarlo con l'indice
    my_empty_set = set() #sto chiamando il costruttore che costrusice una collezione non ordinata di elementi unici.
    my_set_from_list = set(["one", "one", "two", "hello"]) #sto costruendo un insieme dalla lista scritta
    print(my_set_from_list) #ogni qualvolta che si deve rimuovere duplicati da un insieme, si usa il costruttore con la lista
    for item in my_set_from_list:
        print(item) #iterando un print degli elementi per l'insieme, si denota che per ogni F5 l'ordine varia per quanto scritto in #L26
    my_list_from_set = list(my_set_from_list) #operazione di trasformazione in lista
    my_list_from_set.sort() #sorting della lista
    print(my_list_from_set) #print della lista
    print(my_list_from_set[0]) #print del primo elemento della lista
    print(set("hello")) #print di un insieme formato dagli elementi della stringa "hello", ossia h,l,o,e senza la seconda l
    print(sorted(set("hello"), reverse=True)) #il sorted trasforma in lista un insieme richiamato con il set, il reverse True ... chiedi al prof

main()
