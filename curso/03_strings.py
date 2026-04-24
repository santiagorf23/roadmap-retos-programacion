# STRINGS

my_string = "Mi String"
my_other_string = "Mi Otro String"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " +  my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea."
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion."
print(my_tab_string)

my_scape_string = "\\tEste es un string \\n escapado."
print(my_scape_string)

# FORMATEO

name, lastname, age = "Santiago", "Ramirez", 23

print("Mi nombre es {} {} y tengo {} años".format(name, lastname, age)) # Trayendo datos tal cual
print("Mi nombre es %s %s y tengo %d años" %(name, lastname, age)) # Estamos formateando los datos
print("Mi nombre es", name, lastname, "y tengo", age, "años.") # No recomendada

print(f"Mi nombre es {name} {lastname} y tengo {age} años") # Con f-string

# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

# DIVISION
language_slices = language[1:3]
print(language_slices) #yt

language_slices = language[1:]
print(language_slices) # ython

language_slices = language[-2]
print(language_slices) # o

language_slices = language[0:6:2]
print(language_slices) # Pto

# REVERSE
reversed_language = language[::-1]
print(reversed_language) # nohtyP

# FUNCIONES
print(language.capitalize()) # Primera letra en MAYUSCULA
print(language.upper()) # TODAS EN MAYUSCULAS
print(language.count("t")) # Cantidad de veces que se encuentra el caracter "t"
print(language.isnumeric()) # Devuelve bool (False)
print("1".isnumeric()) # Devuelve bool (True)
print(language.lower()) # todas en minusculas
print(language.lower().isupper()) # is es para comprobar devuelve bool (False)