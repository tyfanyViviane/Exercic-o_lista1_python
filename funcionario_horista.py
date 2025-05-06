class FuncionarioHorista:
    def _init_(self, valor_hora: float, horas_trabalhadas: int):
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcularSalario(self):
        return self.valor_hora * self.horas_trabalhadas