class Animal:
    def __init__(self, especie):
        self.especie = especie
        
class Osos(Animal):
    def __init__(self):
        super().__init__("Osos")
    
class Peces(Animal):
    def __init__(self):
        super().__init__("Peces")
        
from random import random

