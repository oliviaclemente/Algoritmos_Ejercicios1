class TowerOfHanoi:
    def __init__(self, discos, estructura):
        self.discos = discos
        self.estructura = estructura
    
    def torre_inicial(self):
        for i in range(self.discos, 0, -1):
            palo = ""
            for j in range(3):
                if len(self.estructura[j]) >= i:
                    disco = self.estructura[j][i - 1]  
                    palo += f"{disco:^4}" 
                else:
                    palo += " " * 4
            print(palo)
        print("P1|   P2|   P3|")    #Siendo P1, P2 y P3 los palos
    
    def resolver(self, n, origen, auxiliar, destino):  
        if n == 1:   #primer caso
            disco = self.estructura[origen].pop()
            self.estructura[destino].append(disco)     
            self.torre_inicial()
        else:    #resto de casos
            self.resolver(n - 1, origen, destino, auxiliar)
            disco = self.estructura[origen].pop()
            self.estructura[destino].append(disco)
            self.torre_inicial()
            self.resolver(n - 1, auxiliar, origen, destino)

discos = 4
estructura = [[4, 3, 2, 1], [], []]  # Siendo el 1 el disco más pequeño
torre = TowerOfHanoi(discos, estructura)
torre.torre_inicial()
torre.resolver(discos, 0, 1, 2)