import random

class Animal:
    def __init__(self, genero, fuerza):
        self.genero = genero
        self.fuerza = fuerza
        
class Osos(Animal):
    def __init__(self, genero, fuerza):
        super().__init__(genero, fuerza)
        self.nombre = "Osos"
    
class Peces(Animal):
    def __init__(self, genero, fuerza):
        super().__init__(genero, fuerza)
        self.nombre= "Peces"
        
class NoneObjecto:
    def __init__(self):
        self.nombre = "none"
        
def mover_rio(rio):
    for i in reversed(range(len(rio))):
        if isinstance(rio[i], (Osos, Peces)):
            mover = random.choice([True, False])
            if mover:
                if i < len(rio) - 1 and isinstance(rio[i+1], NoneObjecto):
                    rio[i], rio[i+1] = rio[i+1], rio[i]
                elif i< len(rio) -1 and isinstance(rio[i+1], (Osos, Peces)):
                    if rio[i].__class__ == rio[i+1].__class__ and rio[i].genero == rio[i+1].genero:
                        if rio[i].fuerza > rio[i+1].fuerza:
                            rio[i+1] = NoneObjecto()
                        else:
                            if rio[i].fuerza > rio[i+1].fuerza:
                                rio[i+1] = NoneObjecto()
                            else:
                                rio[i] = NoneObjecto()
                            
rio= []

for _ in range(10):
    genero = random.choice(["chico", "chica"])
    fuerza = random.randint(1 ,100)
    ecosistema = random.choice([Osos(genero, fuerza), Peces(genero, fuerza), NoneObjecto()])
    rio.append(ecosistema)


print("Primera lista:")
for elemento in rio:
    if isinstance(elemento, (Osos, Peces)):
        print(f"/{elemento.nombre}, {elemento.genero}, {elemento.fuerza}/", end=' ')
    else:
        print(elemento.nombre, end=' ')
print()

mover_rio(rio)

print("Segunda lista:")
for elemento in rio:
    if isinstance(elemento, (Osos, Peces)):
        print(f"{elemento.nombre}, {elemento.genero}, {elemento.fuerza}", end=' ')
    else:
        print(elemento.nombre, end=' ')
print()
