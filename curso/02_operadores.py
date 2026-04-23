# OPERADORES

print(3 + 4) # Suma
print(3 - 4) # Resta
print(3 * 4) # Multiplicacion
print(3 / 4) # Division
print(3 % 4) # Modulo
print(10 // 3) # Division parte entera
print(10 ** 3) # Exponente
print(2 ** 3 + 3 - 7 / 1 // 4)

print("Hola " + "Python " + "¿Que tal?") # Concatenacion
print("Hola " + str(5)) # Concatenacion y se debe convertir para poder que imprima el numero
print("Hola " + "5")
print("Hola " * 3)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

# OPERADORES COMPARATIVOS
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

# Valida por orden alfabetico
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa") # Orden alfabetico por ASCII
print(len("Hola") <= len("Python")) # Cuenta caracteres
print("Hola" == "Python")
print("Hola" != "Python")

print(len("Hola"))
print(len("Python"))

# OPERADORES LOGICOS

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not(3 > 4))