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

if __name__ == '__main__':

    print("Cliente:", a1.get_cliente())

    print("Banco:", a1.get_banco())

    balance= a1.get_balance()
    print("Balance:", balance)

    limite= a1.get_limite()
    print("Limite:", limite)

    print("Cuenta:",  a1.get_cuenta())

    cargo= int(input("Cargar un precio a la tarjeta de credito:"))

    balance1= balance + cargo

    if balance1 < limite:
        print(f"Se ha cargado con exito, ahora el balance es de {balance1}.") 
    else: 
        print("No se ha podido realizar el cargo")

    realizar_pago= int(input("Cuanto dinero desea ingresar al banco:"))

    balance_nuevo= realizar_pago - balance1
    print(f"El nuevo balance del banco es {balance_nuevo}")
