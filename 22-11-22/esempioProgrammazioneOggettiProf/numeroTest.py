from numero import Number

my_number = Number()
my_value = str(my_number)
my_number.setNumber(4.0)
print(my_number)
try:
    my_number.setNumber("nono...")
except TypeError as ex:
    print(f"numero sbagliato {ex}")

print(my_number)
my_number.setNumber(8)
print(my_number)