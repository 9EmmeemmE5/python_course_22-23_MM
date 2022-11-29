"""filter"""

#troncare i decimali in base alla posizione dell'indice

circle_area = [2.59897, 5.67895, 4.25687, 98.65472, 0.98542]

result = list(map(round, circle_area, range(1,6))) #funzione round, itera sulla base di 2 oggetti in ingresso, cui primo è in questo caso circle_area, per secondo il numero di cifre decimali
#il round all'interno della map prende:
#[2.59897, 5.67895, 4.25687, 98.65472, 0.98542] ossia l'oggetto
#[1,2,3,4,5] ossia una lista di interi da 1 a 5
#e restituisce: [2.5, 5.67, 4.256, 98.6547, 0.98542]
print(result)
#ottengo la lista che presenta un numero di cifre decimali pari all'indice occupato dall'elemento: il primo ha 1 decimale, il quinto ne ha 5

scores = [60,70,80,90,100,75,15,96,84]
#voglio vedere tutti gli score sopra la sufficienza di minimo 75
result_scores = list(filter(lambda x: x>=75, scores))
#prende in ingresso scorese alla singola variabile della lambda function con soglia di filtraggio di 75
print(result_scores)

#filtraggio parole palindriome
palindromi = ['demigod', 'rewire', 'anna', 'madam','freer','anuforajarofuna', 'radar']

filtered_names = list(filter(lambda word: word==word[::-1], palindromi)) #lambda che prende in ingresso l'elemento word della lista palindromi

print(filtered_names)