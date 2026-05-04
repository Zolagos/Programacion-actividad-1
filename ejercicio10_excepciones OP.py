# Ejercicio 10: Manejo de Excepciones y Clases Personalizadas
# Objetivo: crear una excepción personalizada y manejarla correctamente
# Autor: Estudiante Omar Pulido Rojas.


# Excepción personalizada para cuando se pasa el límite de velocidad
class ExcesoVelocidadException(Exception):

    def __init__(self, velocidad_actual, velocidad_maxima):
        self.velocidad_actual = velocidad_actual
        self.velocidad_maxima = velocidad_maxima
        mensaje = (
            f"Velocidad {velocidad_actual} km/h supera el límite de "
            f"{velocidad_maxima} km/h"
        )
        super().__init__(mensaje)


# Clase Motor
class Motor:

    def __init__(self, potencia, tipo):
        self.potencia = potencia
        self.tipo = tipo

    def describir_motor(self):
        return f"Motor {self.tipo} de {self.potencia} CV"


# Clase Coche con control de velocidad
class Coche:

    def __init__(self, marca, modelo, anio, motor):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.motor = motor
        self.velocidad_actual = 0      # empieza en 0
        self.velocidad_maxima = 200    # límite permitido en km/h

    # Aumenta la velocidad, lanza excepción si se pasa del límite
    def incrementarVelocidad(self, velocidad):
        nueva_velocidad = self.velocidad_actual + velocidad

        if nueva_velocidad > self.velocidad_maxima:
            raise ExcesoVelocidadException(nueva_velocidad, self.velocidad_maxima)

        self.velocidad_actual = nueva_velocidad
        print(f"Velocidad actual: {self.velocidad_actual} km/h")

    def describir_coche(self):
        return (
            f"Coche: {self.marca} {self.modelo} ({self.anio})\n"
            f"Motor: {self.motor.describir_motor()}\n"
            f"Velocidad: {self.velocidad_actual} km/h"
        )


# Programa principal
if __name__ == "__main__":

    motor1 = Motor(310, "Gasolina")
    mi_coche = Coche("BMW", "M3", 2023, motor1)

    print("--- Estado inicial ---")
    print(mi_coche.describir_coche())

    # Caso 1: velocidad dentro del límite
    print("\n--- Incrementos válidos ---")
    try:
        mi_coche.incrementarVelocidad(80)
        mi_coche.incrementarVelocidad(70)
        mi_coche.incrementarVelocidad(40)
    except ExcesoVelocidadException as e:
        print(f"Error: {e}")

    # Caso 2: velocidad que supera el límite
    print("\n--- Intentando superar 200 km/h ---")
    try:
        mi_coche.incrementarVelocidad(50)  # 190 + 50 = 240, supera el límite
    except ExcesoVelocidadException as e:
        print(f"Excepción capturada: {e}")
        print(f"El coche sigue a {mi_coche.velocidad_actual} km/h")

    print("\n--- Estado final ---")
    print(mi_coche.describir_coche())
