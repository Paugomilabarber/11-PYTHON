"""Crear una funció que donada una llista de dígits ordenats, retorni el número corresponent. 
Utilitzar reduce. Ex: [3, 4, 1, 5] correspòn al número 3415. Ex: def Passar_a_Numero(llista):
 -- retorni el número que corresponen els dígits."""

from functools import reduce

def convertir_a_llista(cadena):
    cadena = cadena.strip('[]')
    elements = cadena.replace(",", " ").split()
    return [int(x) for x in elements]


def combinar_digits_base10(llista):
    numero = reduce(lambda acc, x: acc * 10 + x, llista, 0)
    return numero

entrada_usuari = input("Introdueix una llista de dígits en base 10 : ")
llista = convertir_a_llista(entrada_usuari)
resultat = combinar_digits_base10(llista)
print("Número en base 10:", resultat)
llista_digitos = list(map(int, entrada.split()))

numero = passar_a_numero(llista_digitos)

print("El número formado es:", numero)
