from motor import Motor

class Carro:
    def _init_(self, marca: str, modelo: str, motor: Motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor