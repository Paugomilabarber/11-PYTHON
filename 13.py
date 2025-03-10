

from abc import ABC, abstractmethod

# Classe Animal abstracta
class Animal(ABC):
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat

    @abstractmethod
    def xerrar(self):
        pass

    @abstractmethod
    def mourem(self):
        pass

    def quisoc(self):
        print(f"{self.especie} fa un crit!")

# Classe Cavall
class Cavall(Animal):
    def __init__(self, edat):
        super().__init__("Cavall", edat)

    def xerrar(self):
        print("El cavall fa un nexe!")

    def mourem(self):
        print("El cavall corre!")

# Classe Dofí
class Dofí(Animal):
    def __init__(self, edat):
        super().__init__("Dofí", edat)

    def xerrar(self):
        print("El dofí fa un crit estrident!")

    def mourem(self):
        print("El dofí nedant per l'oceà!")

# Classe Abella
class Abella(Animal):
    def __init__(self, edat):
        super().__init__("Abella", edat)

    def xerrar(self):
        print("L'abelleta fa un zumbido!")

    def mourem(self):
        print("L'abelleta vola!")

    def picar(self):
        print("L'abelleta pica!")

# Classe Humà
class Humà(Animal):
    def __init__(self, edat, nom):
        super().__init__("Humà", edat)
        self.nom = nom

    def xerrar(self):
        print(f"{self.nom} diu hola!")

    def mourem(self):
        print(f"{self.nom} camina!")

# Subclasse Fiet
class Fiet(Humà):
    def __init__(self, edat, nom, pares):
        super().__init__(edat, nom)
        self.pares = pares

    def nompares(self):
        print(f"Els pares de {self.nom} són: {', '.join(self.pares)}")

# Subclasse Centaure que hereta de Cavall i Humà
class Centaure(Cavall, Humà):
    def __init__(self, edat, nom):
        Cavall.__init__(self, edat)
        Humà.__init__(self, edat, nom)

    def xerrar(self):
        print(f"El centaure {self.nom} diu un crit fort!")

    def mourem(self):
        print(f"El centaure {self.nom} corre amb velocitat!")

# Classe Xou (sense relació amb Animal)
class Xou:
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat

    def xerrar(self):
        print(f"{self.especie} fa un soroll estrany!")

    def mourem(self):
        print(f"{self.especie} es mou de manera inusual!")

    def quisoc(self):
        print(f"{self.especie} fa un crit!")

# Creant una llista amb objectes de cada classe
animals = [
    Cavall(5),
    Dofí(3),
    Abella(1),
    Humà(30, "Joan"),
    Fiet(25, "Maria", ["Pere", "Anna"]),
    Centaure(35, "Hèctor"),
    Xou("Alienígena", 100)
]

# Iterant per la llista d'animals i cridant els mètodes
for animal in animals:
    animal.xerrar()
    animal.mourem()
    animal.quisoc()

# Proves específiques per a les subclases
for animal in animals:
    if isinstance(animal, Fiet):
        animal.nompares()
    if isinstance(animal, Abella):
        animal.picar()
