#Crear un directori dins /home/cicles/AO que es digui Prova, canviar-nos a aquest directori, 
#a dins, crear el fitxer Ex12.txt i posar a dins el nom de tots els companys de classe. 
#Tancar el fitxer. Obrir-lo per afegir el nom dels professors. Tancar-lo. 
#Finalment, l’obrirem i posarem tot el seu contingut dins una llista de noms.

# Obrir el fitxer en mode d'escriptura per afegir noms
with open('professors.txt', 'a') as file:
    file.write("Professor 1\n")
    file.write("Professor 2\n")
    file.write("Professor 3\n")

# Obrir el fitxer en mode de lectura per obtenir tots els noms
with open('professors.txt', 'r') as file:
    professors = file.readlines()

# Convertir les línies a una llista de noms, eliminant salt de línia
professors = [professor.strip() for professor in professors]

# Mostrar la llista de noms
print(professors)
