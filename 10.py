#Crear una funció que controli la divisió per zero i ens avisi que volem fer-ho.

def dividir(x, y):
    if y == 0:
        return "Error: No es pot dividir per zero."
    else:
        return x / y

# Sol·licitar els números a l'usuari
x = float(input("Introdueix el numerador: "))
y = float(input("Introdueix el divisor: "))

# Realitzar la divisió i mostrar el resultat
resultat = dividir(x, y)
print(resultat)

