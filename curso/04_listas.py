# LISTAS

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [23, 35, 62, 52, 30, 30, 18]
print(my_list)
print(f"Tamaño de la lista: {len(my_list)}")

my_other_list = [23, 1.84, "Santiago", "Ramirez"]
print(my_other_list)
print(type(my_list))
print(type(my_other_list))

# Acceder a un elemento por medio de la posicion
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
# print(my_other_list[-5]) # Error: list index out of range

print(my_list.count(30)) # Cuantas veces se repite este valor dentro de la lista

age, height, name, lastname = my_other_list
print(name)

print(list([1, 2, 3, 4]))
print([1, 2, 3, 4])

print(my_list + my_other_list) # Concatenacion de listas
# print(my_list - my_other_list) # Concatenacion de listas

my_other_list.append("Analisis Deportivo") # Inserta valor al final de la lista
print(my_other_list)

my_other_list.insert(1, "Rojo") # Inserta valor en la posicion escrita (1)
print(my_other_list)

my_other_list[1] = "Verde"
print(my_other_list)

my_other_list.remove("Verde") # Elimina por medio de coincidencia escrita
print(my_other_list)

my_list.remove(30) # Elimina la primer coincidencia encontrada
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del(my_list[2])
print(my_list)

my_new_list = my_list.copy() # Realiza una copia de la lista

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse() # Muestra los valores de la lista al reves
print(my_new_list)

my_new_list.sort() # Ordena la lista de menor a mayor
print(my_new_list)

# my_list = "Hola Python" # Se convierte la lista en tipo str
# print(my_list)
# print(type(my_list))
# my_list = ["Hola Python"] # Otra forma de convertir el str en list
# my_list = list("Hola Python") # Otra forma de convertir el str en list
# print(my_list)
# print(type(my_list))