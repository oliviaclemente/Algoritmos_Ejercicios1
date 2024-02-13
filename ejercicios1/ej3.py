class Tarjeta_de_credito:
    def __init__(self, cliente, limite, banco, cuenta, balance=0 ):
        self._cliente = cliente
        self._limite= limite
        self._banco = banco
        self._cuenta = cuenta
        self._balance= balance
        
    def __str__(self):
        return f"El cliente {self._cliente} en el banco {self._banco}, una cuenta {self._cuenta} con un balance de {self._balance} y un limite de {self._limite} "
        
    def get_cliente(self):
        return self._cliente
    
    def get_balance(self):
        return self._balance
    
    def get_banco(self):
        return self._banco
    
    def get_limite(self):
        return self._limite  
    
    def get_cuenta(self):
        return self._cuenta
  
a1= Tarjeta_de_credito("Olivia", 2000, "Santander", 2374382409352, 10)
print(a1)
    
balance= a1.get_balance()
print("Balance:", balance)

limite= a1.get_limite()
print("Limite:", limite)

cargo= int(input("Cargar un precio a la tarjeta de credito:"))
cantidad_cargo= int(input("Cuantos cargos has realizado?:"))

balance1= balance + cargo


class Tarjeta_revolving(Tarjeta_de_credito):
    def __init__  (self, cliente, limite, banco, cuenta, balance=0, cargo_extra=5 ):
        super().__init__(cliente, limite, banco, cuenta, balance)
        self._cargo_extra = cargo_extra
          
    def procesar_mes(self):                                 
        menusal= (1+ self._cargo_extra)**(1/12)-1
        interes= menusal * balance1
        self._balance= interes + balance1
        
        print(f"El interes mensual es de {interes} %")
        print(f"Nuevo balance es {self._balance} %")
        
    def agregar_nueva_llamada(self):
        if cantidad_cargo>10:
            balance2 = balance1 + 1
            print(f"Ha realizado una llamada extra por valor de 1 euro, por lo tanto su cuenta esta a {balance2}.")
        else:
            print("Esta llamada no se cobra.")
        
b1 = Tarjeta_revolving("Olivia", 2000,  "Santander", 10)

b1.procesar_mes()

b1.agregar_nueva_llamada()



  


