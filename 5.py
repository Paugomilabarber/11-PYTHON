#Crear una funció que donada una llista, retorni un diccionari que tingui com a clau: 
#els valors de la llista i com a valor el seu índex dins la llista. Utilitzar enumerate.
#Ex: (‘casa’,’cotxe’,’cadira’,’taula’) retorni {‘casa’:0, ‘cotxe’:1, ‘cadira’:2, ‘taula’:3}.

def llista_a_diccionari():
    entrada = input("Introdueix els elements separats per comes: ")
    llista = entrada.split(",")  # Separem els elements per comes
    llista = [element.strip() for element in llista]  # Eliminem espais innecessaris
    return {valor: index for index, valor in enumerate(llista)}

# Exemple d'ús
resultat = llista_a_diccionari()
print(resultat)
