import random

class Osos:
    def __init__(self):
        self.nombre = "osos"

class Peces:
    def __init__(self):
        self.nombre = "peces"

class NoneObjecto:
    def __init__(self):
        self.nombre = "none"
                                        
def mover_rio(rio):
    for i in reversed(range(len(rio))):
        if isinstance(rio[i], (Osos, Peces)):
            mover = random.choice([True, False])
            if mover:
                if i < len(rio) - 1:
                    if isinstance(rio[i+1], NoneObjecto):
                        rio[i], rio[i+1] = rio[i+1], rio[i]
                    elif isinstance(rio[i], Peces) and isinstance(rio[i+1], Osos):   
                        rio[i] = NoneObjecto()
                    elif isinstance(rio[i], Osos) and isinstance(rio[i+1], Peces):
                        rio[i+1] = Osos()
                        rio[i] = NoneObjecto()
                    elif isinstance(rio[i], Peces) and isinstance(rio[i+1], Peces):  
                        for i in range(len(rio)):
                            if isinstance(rio[i], NoneObjecto):
                                rio[i] = Peces()
                                break
                    elif isinstance(rio[i], Osos) and isinstance(rio[i+1], Osos):      
                             for i in range(len(rio)):
                                if isinstance(rio[i], NoneObjecto):
                                    rio[i] = Osos()
                                    break
                    

rio = []

for _ in range(10):
    ecosistema = random.choice([Osos,Peces, NoneObjecto()])
    rio.append(ecosistema)

print("Primera lista:")
for elemento in rio:
    print(elemento.nombre, end=' ')
print()

mover_rio(rio)

print("Segunda lista:")
for elemento in rio:
    print(elemento.nombre, end=' ')
print()
