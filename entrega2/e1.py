class TowerOfHanoi:
    def __init__(self, discos, estructura):
        self.discos = discos
        self.estructura= estructura
    
    def torre_inicial(self):
        for i in range(self.discos,0,-1):   #discos en la torre
            palo= ""
            for j in range(3):     #palo
                if len(self.estructura[j])>=i:
                    discos= self.estructura[j][-i]
                    palo += f"{discos:^4}" 
                else:
                    palo += " " * 4
            print(palo)
        print("P1|   P2|   P3|")
    
    def mover_discos(self, n,origen, destino, extra):
        
            
    
            
        
discos=4
estructura= [[1,2,3,4],[],[]]  
torre= TowerOfHanoi(discos,estructura)
torre.torre_inicial()

