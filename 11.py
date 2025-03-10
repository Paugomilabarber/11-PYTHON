#Crear una funció que permeti llegir la informació d’un fitxer, 
#però que controli que el fitxer existeix i que la seva obertura no doni cap problema.
#Fes-ho també utilitzant with. Si voleu podeu practicar el try, except afegint-ho a les funcions anteriors.

def llegir_fitxer(nom_fitxer):
    try:
        # Intentem obrir el fitxer amb 'with' per garantir que es tanqui correctament
        with open(nom_fitxer, 'r') as fitxer:
            contingut = fitxer.read()
            return contingut
    except FileNotFoundError:
        return f"Error: El fitxer '{nom_fitxer}' no existeix."
    except IOError:
        return "Error: Hi ha hagut un problema a l'obrir el fitxer."
        
# Exemple d'ús
nom_fitxer = input("Introdueix el nom del fitxer: ")
resultat = llegir_fitxer(nom_fitxer)
print(resultat)
    