from ejercicios_4_5 import *

vehiculos = [
    car("Ford", "F150", 2022),
    car("Ferrari", "F80", 2026),
    bicicle("Montaña", "GW"),
    bicicle("Ruta", "Trek")
]

for v in vehiculos:
    print("\nTipo:", type(v).__name__)
    v.accelerate()
    print("Velocidad actual:", v.velocity)





from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def hacerSonido(self):
        pass

class Perro(Animal):
    def hacerSonido(self):
        print("El perro hace: Guau")


class Gato(Animal):
    def hacerSonido(self):
        print("El gato hace: Miau")

animales = [Perro(), Gato()]

# Recorrer lista
for animal in animales:
    animal.hacerSonido()



class Volador:

    def volar(self):
        pass

class Pajaro(Volador):
    def volar(self):
        print("El pájaro vuela usando alas")

class Avion(Volador):
    def volar(self):
        print("El avión vuela usando motores")


voladores = [Pajaro(), Avion()]

for v in voladores:
    v.volar()



