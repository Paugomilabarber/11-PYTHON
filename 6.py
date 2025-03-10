#Crear una funció que donada una llista de valors numèrics, 
# retorni el número d’elements on coincideix el valor i l’índex on és.
# Utilitzar enumerate. Ex: [0, 2, 3, 3, 4], retorni 3.

def comptar_coincidencies():
    entrada = input("Introdueix els números separats per comes: ")
    llista = [int(num.strip()) for num in entrada.split(",")]  # Convertim a enters
    return sum(1 for index, valor in enumerate(llista) if index == valor)

# Exemple d'ús
resultat = comptar_coincidencies()
print(resultat)
