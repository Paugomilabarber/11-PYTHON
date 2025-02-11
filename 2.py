"""Crear una funció que donada una llista de dígits ordenats, retorni el número corresponent. 
Utilitzar reduce. Ex: [3, 4, 1, 5] correspòn al número 3415. Ex: def Passar_a_Numero(llista):
 -- retorni el número que corresponen els dígits."""

from functools import reduce

def convertir_a_llista(cadena):
    l = []
    a = input("Dime una llista de numeros: ")
    l.append(a)
    lista = a.split(",")
    