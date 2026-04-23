# VARIABLES

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 23
print(my_int_variable)

# Se convierte de int a str
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print(f"Este es el valor de: {my_bool_variable}")

# Funciones del sistema

# len()
print(len(my_string_variable))
print(len(my_int_to_str_variable))

# Variables en una sola linea (No es recomendable)
name, surname, alias, age = "Santiago", "Ramirez", "Timmy", 23
print("Me llamo:", name, surname, "Mi edad es:", age, " Y mi apodo es:", alias)

# ¿Forzamos el tipo?
address: str = "Casa"
address = 32 # int
address = True # bool
address = 32.2 # float
print(type(address))

firtname = "Santiago"
lastname = "Ramirez Florez"
age = 23
height = 1.80
dates = {
    "firtname": "Santiago",
    "lastname": "Ramirez Florez",
    "age" : 23,
    "height" : 1.80
}