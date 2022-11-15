"""Esercizio dizionari 1"""

my_dict1= { 'n1': 2, 'n2': 3, 'n3':5 , 'n4':7, 'n5':11, 'n6':13, 'n7':17, 'n8':23}
#sto sommando i valori del mio dizionario
print(sum(my_dict1.values()))

#* script che stampa la lista dell chiavi e il quadrato del valore relativo alla chiave

my_dict2={} #oppure con dict()
for i in range(1,11):
    my_dict2[i] = i**2
    print("%i ----- %d " % (i, my_dict2[i]))
#%i e %d sono dei placeholder ed implica che il valore è un int ed un decimale(?)

#* script che rimuove la tuple con chiave "c" da un dizinario, per poi stampare
#* in ordine le chiavi del dizionario con apposito sort, stampando poi anche il type

my_dict3={'b':2, 'a':1, 'c':3, 'd':4}

if 'c' in my_dict3:     #CS di verifica dell'esistenza della chiave 'c' all'interno del dict
    del my_dict3['c']   #cancellazione della chiave 'c' dal dizionario

print(sorted(my_dict3))
#se si vuole invertire l'ordine, aggiungere ", reverse=True" dopo my_dict3;
#se volessi printare i valori (default richiama le chiavi),
#allora occorre aggingere il ".values()" dopo il nome del dizionario

print(type(my_dict3))
#print del tipo delle chiavi del dizionario

# Cancellare i doppioni e printare la lista
list_1=[12,24,35,24,88,120,155,88,120,155]

set_1=set(list_1)
#trasformo in set per eliminare in automatico i doppioni per la definizione di set,
#dove gli elementi sono definiti in modo univoco

print(list(set_1))
#eseguo il print del cast del set

#TODO: Fill the file with codeshare.io/K8q1eY and complete assignments
# 1
# A prime number (or a prime) is a natural number that has exactly 
# two distinct divisors among the natural numbers: 1 and itself
# Create a dictionary in which the first 10 prime numbers are present 
# and then outputs their sum
# OUTPUT:129

myDict1 = {'n1': 2, 'n2': 3, 'n3': 5, 'n4': 7, 'n5': 11, 'n6': 13, 'n7': 17, 'n8': 19, 'n9': 23, 'n10': 29}
print(sum(myDict1.values()))


# 2
# Write a script that prints the list of all keys associated 
# with the values of a dictionary, where the keys are numbers 
# between 1 and 10 (both inclusive) and the values are the 
# square of the keys
# OUTPUT:
# 1          1
# 2          4
# 3          9
# 4          16
# 5          25
# 6          36
# 7          49
# 8          64
# 9          81
# 10         100

myDict2 = dict()

for i in range(1,11):
    myDict2[i] = i*i
    print("%d ---- %d" % (i,myDict2[i]))

# 3
# Write a Python program to remove key='c' from a dictionary, 
# then print only the keys in sorted order. 
# Please, print also the type of output.
# Dizionario(key/value)=b/2;a/1;c/3;d/4
# OUTPUT: ['a', 'b', 'd']

myDict3 = {'b':2, 'a': 1, 'c':3, 'd':4}

if 'c' in myDict3:
    del myDict3['c']

print(sorted(myDict3.values(), reverse=True))
x = 3.28088

print("%.10f"%(x))

# 4
# With a given list [12,24,35,24,88,120,155,88,120,155],
# write a program to print this list after removing all duplicate 
# values.

list1 = [12,24,35,24,88,120,155,88,120,155]

set1 = set(list1)
print(list(set1))


# 5
# Write a Python program to create a new dictionary, 
# named newDict, by extracting the mentioned 
# keys= ["name", "salary"] from the following dictionary:

sampleDict = {"name": "Kelly","age": 25,"salary": 8000,"city": "New york"}
keys = ["name", "salary"]

# 6 
# Delete using the following list of keys ["name", "salary"] 
# from the previous sampleDict dictionary
# OUTPUT: {'city': 'New york', 'age': 25}


# 7
# Given the following dictionary:
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']}


#Try to do the followings:

# a) Add a key to inventory called 'pocket'and set the value 
# of 'pocket' to be a list consisting of the strings 'seashell', 
# 'strange berry', and 'lint'.


# b) .sort() the items in the list stored under the 'backpack' key.


# c) Then .remove('dagger') from the list of items stored under the 'backpack' key.


# d) Add 50 to the number stored under the 'gold' key.


# e) print(inventory)


#f) Print in reverse order all values of dictionary with 'backpack' keys
