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


class Tarjeta_revolving(Tarjeta_de_credito):
    def __init__  (self, cliente, limite, banco, cuenta, balance=0, cargo_extra=5 ):
        super().__init__(cliente, limite, banco, cuenta, balance)
        self._cargo_extra = cargo_extra
        
 
          
    def procesar_mes(self):                                 
        menusal= (1+ self._cargo_extra)**(1/12)-1
        interes= menusal * balance
        self._balance +=interes
        
        print(f"El interes mensual es de {interes} %")
        print(f"Nuevo balance es {self._balance} %")
        

  
b1 = Tarjeta_revolving("Olivia", 2000,  "Santander", 10)

b1.procesar_mes()

if __name__ == '__main__':

    cargo= int(input("Cargar un precio a la tarjeta de credito:"))

    balance1= balance + cargo

    if balance1 > limite:
        cargo= balance + 5
        print(f"Se ha excedido el limite por lo tanto tendrá un cargo adicional de 5 euros, en este momento su tarjeta es de {cargo}")
    else:
        print(f"Se ha cargado con exito, ahora el balance es de {balance1}.")
        
