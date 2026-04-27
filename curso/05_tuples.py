# TUPLES

# Formas para definir tuplas, la tupla es un conjunto de valores
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (23, 1.84, "Timmy", "Santiago", "Ramirez")
my_other_tuple = (23, 24, 21)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[-6]) # IndexError

print(my_tuple.count("Santiago")) # Cuantas veces se repite este valor dentro de la lista
print(my_tuple.index("Ramirez")) # En que posicion esta el elemento
print(my_tuple.index("Timmy"))

# my_tuple[1] = 1.80 # Error porque las tuplas son inmutables

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple) # Se convierte tupla a lista
print(type(my_tuple))

my_tuple[4] = "Sports Analitics Platform"
my_tuple.insert(2, "Verde")
print(my_tuple)

my_tuple = tuple(my_tuple) # Se vuelve a convertir la lista a tupla
print(type(my_tuple)) # Se muestra el tipo final

del(my_tuple[2])
print(my_tuple) # TypeError: 'tuple' object doesn't support item deletion

del(my_tuple)
# print(my_tuple) # NameError: name 'my_tuple' is not defined