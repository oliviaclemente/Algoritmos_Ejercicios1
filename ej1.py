
class Tarjeta_de_credito:
    def __init__(self, cliente, balance, limite, banco, cuenta):
        self._cliente = cliente
        self._balance= balance
        self._limite= limite
        self._banco = banco
        self._cuenta = cuenta
        
    def descripcion(self):
        return "El cliente {self._cliente} en el banco {self._banco}, una cuenta {self._cuenta} con un balance de {self._balance} y un limite de {self._limite} "
    
a1= Tarjeta_de_credito("Olivia", 10, 2000, "Santander", 2374382409352)

a1.descripcion()