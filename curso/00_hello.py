# INTRODUCCION A PYTHON

# Esto es un comentario

print("Hola Python")
print('Hola Python')

'''
Comentario
de varias
lineas
'''

"""
Este tambien 
es un comentario
de varias lineas
"""

# Consultar el tipo de dato
print(type("Hola Python")) # str
print(type(23)) # int
print(type(1.80)) # float
print(type(True)) # bool
print(type(1j + 23)) # complex number
print(type([1, 2, 3])) # list
print(type({"name": "Santiago"})) # dict
print(type({1.1, 2.2, 3.3})) # set
print(type((1.1, 2.2, 3.3))) # tuple

# NoneType
print(type(print("Cadena de texto")))