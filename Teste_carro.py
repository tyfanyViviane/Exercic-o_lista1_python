from motor import Motor
from carro import Carro

motor1 = Motor("X12345", 150, 300.0)
carro1 = Carro("Toyota", "Corolla", motor1)

print(f"Marca: {carro1.marca}")
print(f"Modelo: {carro1.modelo}")
print(f"Motor - Nº de série: {carro1.motor.numero_serie}, Cavalos: {carro1.motor.cavalos}, Torque: {carro1.motor.torque}")