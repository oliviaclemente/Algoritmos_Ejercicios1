import random 

rio= []

for _ in range(10):
    ecosistema= random.choice(["osos", "peces", "none"])
    rio.append(ecosistema)
    


def mover_animales(rio):
    for i in range(len(rio)):
        if rio[i] in [ "osos", "peces" ]:
            mover= random.choice([True, False])
            if mover:
                if i < len(rio) - 1 and rio[i+1]== "none":
                    rio[i], rio[i+1]= rio[i+1], rio[i]
                    
                if i < len(rio) - 1 and rio[i] == rio[i + 1]:
                    rio.append("none")
                
                    
                    
                    
print(f"Primera lista: {rio}")

mover_animales(rio)

print(f"Segunda lista: {rio}")

