#Crear una llista amb les lletres d’una paraula qualsevol. 
# Utilitzar list comprehensions. Ex: “institut”, retorni [‘i’,’n’,’s’,’t’,’i’,’t’,’u’,’t’].

def paraula_a_llista():
    paraula = input("Introdueix una paraula: ")
    return [lletra for lletra in paraula]

# Exemple d'ús
resultat = paraula_a_llista()
print(resultat)
