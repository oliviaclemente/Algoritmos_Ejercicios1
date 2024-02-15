import random 

rio= []

for _ in range(10):
    ecosistema= random.choice(["osos", "peces", "none"])
    rio.append(ecosistema)
    
print(f"Primera lista: {rio}")


def mover_none(rio):
    for i in range(len(rio)):
        if rio[i] in [ "osos", "peces" ]:
            mover= random.choice([True, False])
            if mover:
                if i < len(rio) - 1 and rio[i+1]== "none":
                    rio[i], rio[i+1]= rio[i+1], rio[i]


def mover_rio(rio):
    i=0
    for i in range(len(rio)):
        if rio[i] in [ "osos", "peces" ]:
                if i < len(rio)-1 and rio[i+1]== "none":
                    rio[i], rio[i+1]= rio[i+1], rio[i]
                i= i+2
                    

                


#def mover_colision(rio):
    
mover_rio(rio)
print(f"Tercera lista:{rio}")