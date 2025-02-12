#Crear una funció que donada una llista de paraules i una lletra, retorni una llista amb les paraules
#que comencen per la lletra donada. Utilitzar filter. Ex: [“maria”, “manta”, “peu”, “mà”] i 
#li deim que ens retorni totes les que comencen per ‘p’, en retorni [‘peu’].

def filtra_paraules():
    paraules = input("Introdueix les paraules de la llista separades per comes: ").split(','' ')
    lletra = input("Introdueix la lletra: ")
    if not lletra:
        print("No s'ha introduït cap lletra valida.")
        return
    primera = lletra[0]
    resultat = list(filter(lambda paraula: paraula.startswith(primera), paraules))
    print("Resultat: ", resultat)

filtra_paraules()
