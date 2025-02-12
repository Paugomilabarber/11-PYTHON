#Crear una funció que donades dues llistes, les concateni amb un connector. 
#Utilitzar zip. Ex: [‘sub’,’supra’] i [‘campió’ ‘campiona’] i el connector ‘-’, retorni [‘sub-campió’][‘supra-campiona’].

def llista():
    l = input("Introdueix les paraules de la primera llista separades per comes: ").split(',')
    k = input("Introdueix les paraules de la segona llista separades per comes: ").split(',')
    e = zip(l, k)
    j = zip(l, k)

    for e,j in zip(l,k):
        print("Resultat: {}-{}".format(e,j))

llista()
