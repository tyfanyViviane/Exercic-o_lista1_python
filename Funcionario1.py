class Funcionario:
    def __init__(self, nome, cpf, valorPorHora):
        self.nome = nome
        self.cpf = cpf
        self.valorPorHora = valorPorHora
        self.horasTrabalhadas = 0

    def calcularSalario(self):
        return self.horasTrabalhadas * self.valorPorHora

    def incrementarHoras(self, quantidade):
        self.horasTrabalhadas += quantidade
