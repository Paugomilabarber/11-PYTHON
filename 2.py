"""Crear una funció que donada una llista de dígits ordenats, retorni el número corresponent. 
Utilitzar reduce. Ex: [3, 4, 1, 5] correspòn al número 3415. Ex: def Passar_a_Numero(llista):
 -- retorni el número que corresponen els dígits."""

from functools import reduce

def convertir_a_llista():
    entrada = input("Introdueix una llista de dígits separats per espais o comes: ")
    return [int(x) for x in entrada.replace(",", " ").split()]

def passar_a_numero(llista):
    return reduce(lambda acc, digit: acc * 10 + digit, llista)

# Programa principal
llista_digits = convertir_a_llista()
numero = passar_a_numero(llista_digits)
print("El número corresponent és:", numero)
