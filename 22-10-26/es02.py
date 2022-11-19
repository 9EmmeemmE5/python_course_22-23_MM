###

"""modulo che gestisce lista delle parole"""

def create_list_of_words(my_text: str, uniform_case = False):       #definisco la funzione di creazione della lista "lista di parole", my_text viene forzato ad essere una stringa, definendo che non ho un case uniforme, aka ho sia lower che uppercase, piu punteggiatura
    """This funct returns a list of words from a text"""
    my_copy_text = str(my_text)
    my_list_of_words = []
    if uniform_case:                                                #CS if dove dico che 
        my_copy_text = my_text.lower()                                   #trasformo il my_text in lowercase
    #rimuovere la punteggiatura
    my_text.replace(",","").replace(".","")                         #replacing#1: definisco l'elemento "," e lo sostituisco con lo spazio " "? no, va modellato come assente senno' viene doppio spazio,a cui aggiungo un altro replace dove tolgo il punto
    #alternativa a quello sopra: rimpiazzo
    my_items_tobe_replaced = [",",".",";","-","!"]
    for item in my_items_tobe_replaced:
        my_copy_text = my_copy_text.replace(item, "")
    print(my_copy_text)
    # my_list_of_words = my_copy_text.split(" ")
    my_tmp_string=""    #stringa temporanea per estrazione parole: se non ho uno spazio va avanti finche non arrivo allo spazio, dove chiudo la parola e la aggiungo 
    for single_char in my_copy_text:
        if single_char != " ":
            my_tmp_string+= single_char
        else:
            my_list_of_words.append(my_tmp_string)
            my_tmp_string = ""

def main():
    """Entry Point"""
    my_text = "Vivamus vehicula leo a justo. Quisque nec augue. Morbi mauris wisi, aliquet vitae, dignissim eget, sollicitudin molestie, ligula. In dictum enim sit ametrisus. Curabitur vitae velit eu diam rhoncus hendrerit. Vivamus ut elit. Praesent mattis ipsum quis turpis. Curabitur rhoncus neque eu dui. Etiam vitae magna. Nam ullamcorper. Praesent interdum bibendum magna. Quisque auctor aliquam dolor. Morbi eu lorem et est porttitor fermentum. Nunc egestasarcu at tortor varius viverra. Fusce eu nulla ut nulla interdum consectetuer.Vestibulum gravida. Morbi mattis libero sed est."
    my_list = create_list_of_words(my_text, True)
    my_list.sort()
    print(my_list)
main()