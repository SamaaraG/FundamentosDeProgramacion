from abc import ABC, abstractmethod

# Clase abstracta
class Vehiculo(ABC):
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def __str__(self):
        return f"Vehículo genérico: {self.marca} {self.modelo} ({self.año}) - Color: {self.color}"


# Subclases que heredan solo los atributos
class Auto(Vehiculo):
    pass


class Moto(Vehiculo):
    pass


class Camion(Vehiculo):
    pass

class Barco(Vehiculo):
    pass


# Crear objetos de las clases hijas
auto1 = Auto("Toyota", "Corolla", 2022, "Rojo")
moto1 = Moto("Yamaha", "FZ", 2021, "Negra")
camion1 = Camion("Volvo", "FH", 2020, "Blanco")
barco1 = Barco("Sunseeker","Predator 55 EVO", 2021, "Amarillo")

auto2 = Auto("Chevrolet", "Corvette", 2006, "Rojo")
moto2 = Moto("Yamaha", "MT-07", 2006, "Rosa")
camion2 = Camion("Kenworth", "T680", 2017, "Verde")
barco2 = Barco("Harland and Wolff", "RMS Titanic", 1912, "Blanco")

# Visualización
print(auto1)
print(moto1)
print(camion1)
print(barco1)

print(auto2)
print(moto2)
print(camion2)
print(barco2)