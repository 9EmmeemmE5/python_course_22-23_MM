"""Dizionari 3"""

def main():
    """Entrypoint"""
    my_dict = dict()
    my_dict = {}
    my_dict["nome"]="Adriano"
    my_dict["cognome"]="Mancini"
    my_dict["tags"]=["python","C","C++","java","JS"] 
    #più compelsso del semplice valore perché il valore della chiave ora è una lista
    my_dict["data"]=[
        {"name":"Mario", "surname":"Rossi"},
        {"name":"Maria", "surname":"Montessori"}
        ]
    my_dict["metadata"]={"matricola":"S1234567","id_interno":"xxxxxxx"}
    print(my_dict) #non printa "Adriano" "Mancini", ma 'chiave':"valore"
    print(type(my_dict["tags"])) #printa "list" perche è una lista e non una str
    print(my_dict["tags"][2]) #printa "java" perche ho inserito l'index della lista
    #stampare name degli amici
    print(type(my_dict["friends"])) #printa la lista contenente il dizionario
    #posso scrivere in una sola riga il comando per accedere la lista dei nomi amici
    if "friends" in my_dict:
        for item in my_dict["friends"]:
            print(f"{item['name']}{item['surname'].upper()}")
            #NB: se uso la double quote nel recall della chiave va in errore la f string
            #quindi risolvo con la single quote, perché se avessi usato il "\" sarebbe
            #andato nuovamente in errore pinco pallino cacca rosa
main()
