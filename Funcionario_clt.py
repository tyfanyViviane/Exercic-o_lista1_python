class FuncionarioCLT:
    def _init_(self, nome: str, salario_mensal: float):
        self.nome = nome
        self.salario_mensal = salario_mensal

    def calcularSalario(self):
        return self.salario_mensal