# Ejercicio 9: Composición
# Objetivo: entender cómo una clase puede contener otra clase
# Autor: Estudiante Omar Pulido Rojas.


# Clase Motor con sus atributos básicos
class Motor:

    def __init__(self, potencia, tipo):
        self.potencia = potencia  # caballos de fuerza
        self.tipo = tipo          # gasolina, diesel, electrico...

    # Método para describir el motor
    def describir_motor(self):
        return f"Motor {self.tipo} de {self.potencia} CV"


# Clase Coche que contiene un objeto Motor (composición)
class Coche:

    def __init__(self, marca, modelo, anio, motor):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.motor = motor  # aquí se aplica la composición

    # Descripción del coche incluyendo los detalles del motor
    def describir_coche(self):
        return (
            f"Coche: {self.marca} {self.modelo} ({self.anio})\n"
            f"Motor: {self.motor.describir_motor()}"
        )


# Programa principal
if __name__ == "__main__":

    # Creo el motor primero y luego lo paso al coche
    motor1 = Motor(150, "Gasolina")
    coche1 = Coche("Toyota", "Corolla", 2022, motor1)
    print(coche1.describir_coche())

    print()

    motor2 = Motor(204, "Eléctrico")
    coche2 = Coche("Tesla", "Model 3", 2024, motor2)
    print(coche2.describir_coche())

    print()

    motor3 = Motor(122, "Híbrido")
    coche3 = Coche("Honda", "Insight", 2023, motor3)
    print(coche3.describir_coche())
