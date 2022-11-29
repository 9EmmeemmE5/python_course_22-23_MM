"""map and lambda"""

my_pets = ['alfred','tabitha','william','aria']

uppered_my_pets = []

for pet in my_pets:
    pet = pet.upper()
    uppered_my_pets.append(pet)

print(uppered_my_pets)
#base ciclata col for
uppered_my_pets2 = list(map(lambda x: x.upper(), my_pets))
#con la map ed una labda ad una entry
uppered_my_pets3 = list(map(str.upper, my_pets))
#con la map ed una labda ad una entry, ma con il metodo della libreria primitiva della classe str, andando a rimuovere le ()
print(uppered_my_pets2)
